# -*- coding:utf-8 -*-
from typing import List

import numpy as np
from PySide2.QtCore import QPointF, QRectF, Qt
from PySide2.QtWidgets import QGraphicsItem
from PySide2.QtGui import QBrush, QPen, QColor, QFont, QPolygonF

from AlgorithmUtils import selectionLine, lineExtrapolation
from DataModel import MatPlotModel, MaterialItem
from GraphicTransformer import GraphicConfig, GraphicTransformer

class MatPlotController(object):
    def __init__(self, window, filename: str):
        self.window = window
        self.view = window.ui.graphicsView
        self.scene = window.myScene
        self.tree = window.ui.treeView
        self.pen = QPen(QColor(0, 0, 0))
        self.pen.setWidth(0)
        self.dash_pen = QPen(QColor(0, 0, 0))
        self.dash_pen.setWidth(0)
        self.dash_pen.setStyle(Qt.DashLine)
        self.model = MatPlotModel(filename)
        self.config = GraphicConfig()
        self.transformer = GraphicTransformer(self.config)
        # Store the semantic items which have been drawn on the plot, used when the config is updated.
        self.semantic_items = []

        self.initTreeView()
        self.connectSignals()
        self.initConfigs()

    def initConfigs(self):
        ui = self.window.ui
        # append your configs here
        configMap = {
            "x_axis": ui.lineEdit_xaxis.text,
            "y_axis": ui.lineEdit_yaxis.text,
            "log_scale": lambda: not ui.linearRadio.isChecked(),
            "mat_selections": lambda: self.tree.getSelections()["Items"],
            "selection_lines": ui.listView.getData
        }
        for key, getter in configMap.items():
            self.config.registerConfigGetter(key, getter)

    #
    # Public
    #
    def updateConfig(self):
        self.config.updateFromUI()
        self.transformer = GraphicTransformer(self.config)
        self.updateGraphicItems()

    def clearScene(self):
        self.semantic_items.clear()
        self.view.clearAllItems()

    def drawAllMaterialEclipses(self):
        self.config.updateFromUI()
        for name, info in self.model.getSelectedItems(self.config.mat_selections).items():
            self.drawEllipse(info)

    def drawFamilyHull(self, family_key="Type"):
        family_candidates = self.model.provideFamilyCandidateByColumn(family_key)
        for family in family_candidates:
            items = self.model.getItemsByFamilyAndSelected(family_key, family, self.config.mat_selections).values()
            self.drawHull((family, list(items)))

    def drawAllHull(self):
        items = self.model.getSelectedItems(self.config.mat_selections).values()
        self.drawHull((None, list(items)))

    def updateObjectsByAxis(self, new_column_info: List[str]):
        x_column = new_column_info[0]
        y_column = new_column_info[1]
        # FIXME!(tienan) this is for test.
        y_column = "Modulus"
        x_column = "Strength"
        self.updateConfig()

    def clearHull(self):
        remaining_items = []
        for item in self.semantic_items:
            # Only keep the item that is not hull (i.e. not an item list).
            if not isinstance(item, list):
                remaining_items.append(item)
        self.semantic_items = remaining_items
        self.updateGraphicItems()

    #
    # Private
    #
    def connectSignals(self):
        self.tree.OnSelectionChanged.connect(self.OnTreeSelectionChanged)
        self.window.ui.listView.EditFinished.connect(self.onListDataChanged)

    def onListDataChanged(self):
        self.updateConfig()
        print(self.config.selection_lines)

    def OnTreeSelectionChanged(self, selections):
        # todo: make it do someing!
        self.config.updateFromUI()
        print(selections)
        # # anotherway to get
        # selections = self.tree.getSelections()

    def initTreeView(self, family_key="Type"):
        self.tree.clearModel()
        mattypes = self.model.getMaterialFamily(family_key)
        items = self.model.getAllItems()
        self.tree.addFamilies(mattypes)  # not necessary at all
        for item in items.values():
            self.tree.addItem(item, item.family_info[family_key])

    def drawEllipse(self, mat_item: MaterialItem):
        brush = QBrush(QColor(mat_item.color_r, mat_item.color_g, mat_item.color_b, a=255))
        ret = self.transformer.matToSquare(mat_item)
        if ret is None:
            return
        ul_x, ul_y, w, h = ret
        elps = self.scene.addEllipse(QRectF(ul_x, ul_y, w, h), self.pen, brush)
        elps.setRotation(self.transformer.matRotation(mat_item))
        elps.name = mat_item.label

        text = self.scene.addText(mat_item.label, QFont("Arial", 12, 2))
        c_x, c_y = self.transformer.matCenterPoint(mat_item)
        text.setPos(QPointF(c_x, c_y))
        text.setRotation(self.transformer.matRotation(mat_item))
        text.setFlag(QGraphicsItem.ItemIgnoresTransformations)
        text.name = mat_item.label + "_Label"

        text.setFlag(QGraphicsItem.ItemIsMovable)
        # Append semantic item info for re-draw.
        self.semantic_items.append(mat_item)
        self.view.addItemByType(self.view.ITEM_TYPE_ELLIPSE, elps)
        self.view.addItemByType(self.view.ITEM_TYPE_ELLIPSELABEL, text)

    def drawHull(self, items_info: tuple):
        family_name = items_info[0]
        items = items_info[1]
        if len(items) > 0:
            r, g, b = self.model.getMeanColor(items)
            self.pen = QPen(QColor(125, 125, 125, 50), 0)
            self.brush = QBrush(QColor(r, g, b, 100))
            hull = self.transformer.getEllipseHull(items)
            poly = self.scene.addPolygon(QPolygonF(list(map(QPointF, *hull.T))), self.pen, self.brush)
            poly.setZValue(-1)
            self.semantic_items.append(items_info)
            self.view.addItemByType(self.view.ITEM_TYPE_HULL, poly)
            if family_name:
                text = self.scene.addText(family_name, QFont("Arial", 14, QFont.Bold))
                # Hull's label is put at the center of all its boundary point.
                c_x, c_y = np.mean(hull, axis=0)
                text.setPos(QPointF(c_x, c_y))
                text.setFlag(QGraphicsItem.ItemIgnoresTransformations)
                text.name = family_name + "_Hull_Label"
                text.setFlag(QGraphicsItem.ItemIsMovable)
                self.view.addItemByType(self.view.ITEM_TYPE_ELLIPSELABEL, text)

    def drawSelectionLine(self, item: selectionLine):
        # Will not draw selection line if not in log scale.
        if not self.transformer.config.log_scale:
            return

        # Sample two points from the line.
        # (a1 * (x ^ a2)) / (b1 * (y ^ b2)) = c
        def sampling(item: selectionLine, x: float):
            rhs = item.c / item.a1 * item.b1
            lhs_upper = x ** item.a2
            lhs_lower = lhs_upper / rhs
            y = lhs_lower ** (1 / item.b2)
            return y
        POINT1_X = 10.
        POINT2_X = 100.
        POINT1_Y = sampling(item, POINT1_X)
        POINT2_Y = sampling(item, POINT2_X)

        x1, y1 = self.transformer.pointTransform(POINT1_X, POINT1_Y)
        x2, y2 = self.transformer.pointTransform(POINT2_X, POINT2_Y)
        # Extrapolate to mock a "near" infinite-length line.
        X_END_L, X_END_R = -1e9, 1e9
        Y_END = lineExtrapolation([x1, x2], [y1, y2], [X_END_L, X_END_R])
        line = self.scene.addLine(X_END_L, Y_END[0], X_END_R, Y_END[1], self.dash_pen)
        self.view.addItemByType(self.view.ITEM_TYPE_SELECTION_LINE, line)

    def updateGraphicItems(self):
        '''
        Iterates over the existing items and re-draw them with the latest config.
        '''
        prev_items = self.semantic_items.copy()
        self.clearScene()
        for p_item in prev_items:
            # If it is one item, draw the corresponding ellipse.
            if isinstance(p_item, MaterialItem):
                self.drawEllipse(p_item)
            # If it is a tuple (family_name, item_list), draw their convex hull.
            if isinstance(p_item, tuple):
                self.drawHull(p_item)
