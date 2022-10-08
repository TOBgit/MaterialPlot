# -*- coding:utf-8 -*-
from typing import List

from PySide2.QtCore import QPointF, QRectF
from PySide2.QtWidgets import QGraphicsItem
from PySide2.QtGui import QBrush, QPen, QColor, QFont, QPolygonF

from DataModel import AshbyModel, MaterialItem
from GraphicTransformer import GraphicConfig, GraphicTransformer


class AshbyGraphicsController(object):
    def __init__(self, window, filename: str):
        self.window = window
        self.view = window.ui.graphicsView
        self.scene = window.myScene
        self.tree = window.ui.treeView
        self.pen = QPen(QColor(0, 0, 0))
        self.pen.setWidth(0)
        self.model = AshbyModel(filename)
        self.config = GraphicConfig()
        self.transformer = GraphicTransformer(self.config)
        # Store the semantic items which have been drawn on the plot, used when the config is updated.
        self.semantic_items = []

        self.initTreeView()
        self.connectSignals()

    #
    # Public
    #
    def updateConfig(self, expend_ratio: float=None,
                           hull_sampling_step: int=None,
                           log_scale: bool=None,
                           x_axis: str=None,
                           y_axis: str=None):
        self.config.updateConfig(expend_ratio, hull_sampling_step, log_scale, x_axis, y_axis)
        self.transformer = GraphicTransformer(self.config)
        self.updateGraphicItems()

    def clearScene(self):
        self.semantic_items.clear()
        self.view.clearAllItems()

    def drawAllMaterialEclipses(self):
        for name, info in self.model.getAllItems().items():
            self.drawEllipse(info)

    def drawFamilyHull(self, family_key = "Type"):
        family_candidates = self.model.provideFamilyCandidateByColumn(family_key)
        for family in family_candidates:
            items = self.model.getItemsByFamily(family_key, family).values()
            self.drawHull(list(items))

    def drawAllHull(self):
        items = self.model.getAllItems().values()
        self.drawHull(list(items))

    def updateObjectsByAxis(self, new_column_info: List[str]):
        x_column = new_column_info[0]
        y_column = new_column_info[1]
        #FIXME!(tienan) this is for test.
        y_column = "Modulus"
        x_column = "Strength"
        self.updateConfig(x_axis = x_column, y_axis = y_column)

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

    def OnTreeSelectionChanged(self, selections):
        # todo: make it do someing!
        print(selections)
        # anotherway to get
        selections = self.tree.getSelections()
        print(selections)

    def initTreeView(self, family_key = "Type"):
        self.tree.clearModel()
        mattypes = self.model.getMaterialFamily(family_key)
        items = self.model.getAllItems()
        self.tree.addFamilies(mattypes)  # not necessary at all
        for item in items.values():
            self.tree.addItem(item, item.family_info[family_key])

    def drawEllipse(self, mat_item: MaterialItem):
        brush = QBrush(QColor(mat_item.color_r, mat_item.color_g, mat_item.color_b, a=255))
        ul_x, ul_y, w, h = self.transformer.matToSquare(mat_item)
        elps = self.scene.addEllipse(QRectF(ul_x, ul_y, w, h), self.pen, brush)
        elps.setRotation(self.transformer.matRotation(mat_item))

        text = self.scene.addText(mat_item.label, QFont("Arial", 12, 2))
        c_x, c_y = self.transformer.matCenterPoint(mat_item)
        text.setPos(QPointF(c_x, c_y))
        text.setRotation(self.transformer.matRotation(mat_item))
        text.setFlag(QGraphicsItem.ItemIgnoresTransformations)

        text.setFlag(QGraphicsItem.ItemIsMovable)
        # Append semantic item info for re-draw.
        self.semantic_items.append(mat_item)
        self.view.addItemByType(self.view.ITEM_TYPE_ELLIPSE, elps)
        self.view.addItemByType(self.view.ITEM_TYPE_ELLIPSELABEL, text)

    def drawHull(self, items: List[MaterialItem]):
        if len(items) > 0:
            r, g, b = self.model.getMeanColor(items)
            self.pen = QPen(QColor(125, 125, 125, 50), 0)
            self.brush = QBrush(QColor(r, g, b, 100))
            hull = self.transformer.getEllipseHull(items)
            poly = self.scene.addPolygon(QPolygonF(list(map(QPointF, *hull.T))), self.pen, self.brush)
            poly.setZValue(-1)
            self.semantic_items.append(items)
            self.view.addItemByType(self.view.ITEM_TYPE_HULL, poly)

    def drawLine(self):
        # fake example, make your draw with your data
        self.scene.addLine(0, 0, 100, 400, self.pen)
        for i in range(self.model.getCount()):
            matitem = self.model.getItem(i)
            mean = matitem.getMean("Param3")
            std = matitem.getStd("Param3")
            # draw a cross
            graphicitem = self.scene.addLine(mean - 10, std - 10, mean + 10, std + 10, self.pen)
            graphicitem2 = self.scene.addLine(mean - 10, std + 10, mean + 10, std - 10, self.pen)


    def updateGraphicItems(self):
        '''
        Iterates over the existing items and re-draw them with the latest config.
        '''
        prev_items = self.semantic_items.copy()
        self.clearScene()
        for item in prev_items:
            # If it is one item, draw the corresponding ellipse.
            if isinstance(item, MaterialItem):
                self.drawEllipse(item)
            # If it is a list of items, draw their convex hull.
            if isinstance(item, list):
                self.drawHull(item)