# -*- coding:utf-8 -*-
import sys
from typing import List

from PySide2.QtCore import QFile, QRectF, QPointF
from PySide2.QtUiTools import QUiLoader
from PySide2.QtWidgets import QApplication, QMainWindow, QGraphicsScene, QFileDialog, QTreeView, QDialog, QMessageBox
from PySide2.QtGui import QBrush, QPen, QColor, QFont, QIcon
import res_rc # noqa

from GraphicsModule import MatPlotController
from View.AGraphicsView import AGraphicsView
from View.AxesSelectionPopUp import setAxesPopUp
from View.TreeView import TreeView
from View.TableWidget import ManageItem
from View.AListView import AListView

app = None


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        if QFile.exists("matplot.ui"):
            file = QFile("matplot.ui")
            file.open(QFile.ReadOnly)
            file.close()
            loader = QUiLoader()
            loader.registerCustomWidget(AGraphicsView)
            loader.registerCustomWidget(TreeView)
            loader.registerCustomWidget(AListView)
            self.ui = loader.load(file)
            self.ui.show()
        else:
            from View.matplot import Ui_MainWindow
            self.ui = Ui_MainWindow()
            self.ui.setupUi(self)
            self.show()
        self.connectSignals()
        self.csv_fpath = None
        self.myScene = QGraphicsScene()
        self.ui.graphicsView.setScene(self.myScene)
        self.controller = MatPlotController(self, self.csv_fpath)

        self.pen = QPen(QColor(0, 0, 0))
        self.ui.graphicsView.resetView()
        self.ui.graphicsView.initHelperItems()
        self.onTextEdited()


    def connectSignals(self):
        ## Tool bar buttons
        # TODO(ky): update the ui nameing style in the menu to be consistent with the buttons.
        self.ui.actionOpen_CSV.triggered.connect(self.onActionOpenCSV)
        self.ui.actionHotReload.triggered.connect(self.onActionHotReload)
        self.ui.actionConvexHull.triggered.connect(self.onActionConvexHull)
        self.ui.actionGenerateChart.triggered.connect(self.onClickGenPropChrt)
        self.ui.actionFamilyBubble.triggered.connect(self.onActionFamilyHull)
        self.ui.actionPlotSelLn.triggered.connect(self.onClickPlotSelLn)
        self.ui.actionResetView.triggered.connect(self.onResetView)
        self.ui.actionFitView.triggered.connect(self.onFitView)
        self.ui.actionAxes.triggered.connect(self.onDefineAxes)
        self.ui.actionManageItem.triggered.connect(self.onManageItem)
        self.ui.actionCapture.triggered.connect(self.onActionCapture)
        self.ui.actionAbout.triggered.connect(self.onAbout)

        ## top layer of buttons ##
        self.ui.Refresh_List.clicked.connect(self.onRefreshTreeList)
        self.ui.manage_item.clicked.connect(self.onManageItem)

        ## middle layer of buttons ##
        self.ui.Plot_Prop_Chrt.clicked.connect(self.onClickGenPropChrt)
        self.ui.Plot_hulls.clicked.connect(self.onActionFamilyHull)
        self.ui.clear_mat_bubble.clicked.connect(self.onClickClearMat)
        self.ui.clear_hulls.clicked.connect(self.onClickClearHull)
        self.ui.show_mat_label.clicked.connect(self.onClickShowMatLabel)
        self.ui.show_fam_label.clicked.connect(self.onClickShowFamLabel)
        self.ui.delete_mat_label.clicked.connect(self.onClickDeleteMatLabel)
        self.ui.delete_fam_label.clicked.connect(self.onClickDeleteFamLabel)
        
        ## Plot property tab ##
        self.ui.buttonGroup.buttonToggled.connect(self.onAxisStyleChanged)
        self.ui.checkBox_cursor.stateChanged.connect(self.onCursorChecked)

        self.ui.lineEdit_xaxis.textEdited.connect(self.onTextEdited)
        self.ui.lineEdit_yaxis.textEdited.connect(self.onTextEdited)

        ## Label property tab ##
    ## TODO need to implement this
        #self.ui.Plot_refresh_label.clicked.connect(self.onClickRefreshLabel)

        ## lower layer of buttons ##
        self.ui.Plot_sel_ln.clicked.connect(self.onClickPlotSelLn)
        self.ui.Plot_clear.clicked.connect(self.onActionClear)
        self.ui.add_selection.clicked.connect(self.onAddSelection)
        self.ui.delete_selection.clicked.connect(self.onDelSelection)
    ## TODO need to implement this
        #self.ui.clear_sel_ln.clicked.connect(self.onClickClearSelLn)

    #
    # Button and menu functions, called upon UI interactions.
    #

    def onAbout(self):
        QMessageBox.aboutQt(None, "About")

    def onAddSelection(self):
        self.ui.listView.addItem()

    def onDelSelection(self):
        self.ui.listView.popItem()

    def onTextEdited(self, *args):
        self.ui.graphicsView.setAxisLabel( self.ui.lineEdit_xaxis.text(),  self.ui.lineEdit_yaxis.text())

    def onActionCapture(self):
        filename, _ = QFileDialog.getSaveFileName(self, "save Capture", filter="Bitmap (*.bmp)")
        if filename:
            pix = self.ui.graphicsView.grab()
            pix.save(filename)

    def onClickClearMat(self):
        self.ui.graphicsView.clearItemByType(self.ui.graphicsView.ITEM_TYPE_ELLIPSE)

    def onClickClearHull(self):
        self.ui.graphicsView.clearItemByType(self.ui.graphicsView.ITEM_TYPE_HULL)

    def onClickShowMatLabel(self):
        self.ui.graphicsView.setItemVisibleByType(self.ui.graphicsView.ITEM_TYPE_ELLIPSELABEL, True)

    def onClickShowFamLabel(self):
        self.ui.graphicsView.setItemVisibleByType(self.ui.graphicsView.ITEM_TYPE_HULLLABEL, True)

    def onClickDeleteMatLabel(self):
        # to huizhang: delete? or hide? implemented as show/hide now
        self.ui.graphicsView.setItemVisibleByType(self.ui.graphicsView.ITEM_TYPE_ELLIPSELABEL, False)

    def onClickDeleteFamLabel(self):
        self.ui.graphicsView.setItemVisibleByType(self.ui.graphicsView.ITEM_TYPE_HULLLABEL, False)

    def onDefineAxes(self):
        pop_up = setAxesPopUp(self.controller.model.getNumericColumns())
        pop_up.exec_()
        if pop_up.returnNewXY():
            self.controller.updateObjectsByAxis(pop_up.returnNewXY())

    def onCursorChecked(self, state):
        self.ui.graphicsView.setIndicatorVisible(self.ui.checkBox_cursor.isChecked())

    def onAxisStyleChanged(self, _):
        self.controller.updateConfig()
        if self.ui.linearRadio.isChecked():
            self.ui.graphicsView.changeAxisMode(0)
        else:
            self.ui.graphicsView.changeAxisMode(1)
        self.onFitView()

    def onResetView(self):
        self.ui.graphicsView.resetView()
        app.processEvents()

    def onFitView(self):
        self.ui.graphicsView.fitView()
        app.processEvents()

    def onActionHotReload(self):
        '''
        Hot reloads the code modules. For debug purpose.
        '''
        from HotReloadModule import reloadModules
        reloadModules()
        from GraphicsModule import MatPlotController
        from DataModel import MatPlotModel
        self.controller = MatPlotController(self, self.csv_fpath)

    def onClickGenPropChrt(self):
        '''
        Draws all existing materials onto the plot.
        '''
        self.onActionClear()
        self.controller.drawAllMaterialEclipses()
        self.onFitView()

    def onActionOpenCSV(self):
        '''
        Loads data, updates both the model and controller.
        '''
        print("Ready to input data.")
        filename, _ = QFileDialog.getOpenFileName(self, "Open CSV", filter="CSV Files (*.csv)", dir="./Data")
        if filename:
            self.csv_fpath = filename
        self.controller = MatPlotController(self, self.csv_fpath)
        self.ui.familyColumn.addItems(self.controller.model.getStringColumns())

    def onClickPlotSelLn(self):
        self.controller.drawLine()

    def onActionClear(self):
        self.controller.clearScene()
        self.ui.graphicsView.resetView()

    def onActionConvexHull(self):
        self.controller.drawAllHull()

    def onActionFamilyHull(self):
        self.controller.clearHull()
        self.controller.drawFamilyHull(self.ui.familyColumn.currentText())

    def onRefreshTreeList(self):
        self.controller.initTreeView(self.ui.familyColumn.currentText())
        
    def onManageItem(self):
        self.manager = ManageItem(self.controller.model)
        self.manager.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec_())
