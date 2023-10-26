# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'matplot.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *

from .AGraphicsView import AGraphicsView
from .TreeView import TreeView
from .AListView import AListView

import res_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1462, 967)
        icon = QIcon()
        icon.addFile(u"./Res/logo.ico", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.actionOpen_CSV = QAction(MainWindow)
        self.actionOpen_CSV.setObjectName(u"actionOpen_CSV")
        icon1 = QIcon()
        icon1.addFile(u"./Res/OpenCSV.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.actionOpen_CSV.setIcon(icon1)
        self.actionExit = QAction(MainWindow)
        self.actionExit.setObjectName(u"actionExit")
        self.actionAxes = QAction(MainWindow)
        self.actionAxes.setObjectName(u"actionAxes")
        self.actionAxes.setEnabled(False)
        icon2 = QIcon()
        icon2.addFile(u"./Res/Axes.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.actionAxes.setIcon(icon2)
        self.actionSearch = QAction(MainWindow)
        self.actionSearch.setObjectName(u"actionSearch")
        self.actionSearch.setEnabled(False)
        icon3 = QIcon()
        icon3.addFile(u"./Res/Search.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.actionSearch.setIcon(icon3)
        self.actionTools = QAction(MainWindow)
        self.actionTools.setObjectName(u"actionTools")
        self.actionSettings = QAction(MainWindow)
        self.actionSettings.setObjectName(u"actionSettings")
        self.actionHelp = QAction(MainWindow)
        self.actionHelp.setObjectName(u"actionHelp")
        self.actionAdd_Edit_Item = QAction(MainWindow)
        self.actionAdd_Edit_Item.setObjectName(u"actionAdd_Edit_Item")
        self.actionDelete_Item = QAction(MainWindow)
        self.actionDelete_Item.setObjectName(u"actionDelete_Item")
        self.actionGroup_Family = QAction(MainWindow)
        self.actionGroup_Family.setObjectName(u"actionGroup_Family")
        self.actionUngroup_Family = QAction(MainWindow)
        self.actionUngroup_Family.setObjectName(u"actionUngroup_Family")
        self.actionHotReload = QAction(MainWindow)
        self.actionHotReload.setObjectName(u"actionHotReload")
        self.actionConvexHull = QAction(MainWindow)
        self.actionConvexHull.setObjectName(u"actionConvexHull")
        icon4 = QIcon()
        icon4.addFile(u"./Res/FamBubb.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.actionConvexHull.setIcon(icon4)
        self.actionFamily = QAction(MainWindow)
        self.actionFamily.setObjectName(u"actionFamily")
        self.actionFamily.setEnabled(False)
        icon5 = QIcon()
        icon5.addFile(u"./Res/Family.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.actionFamily.setIcon(icon5)
        self.actionGenerateChart = QAction(MainWindow)
        self.actionGenerateChart.setObjectName(u"actionGenerateChart")
        icon6 = QIcon()
        icon6.addFile(u"./Res/MatBubb.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.actionGenerateChart.setIcon(icon6)
        self.actionSelection = QAction(MainWindow)
        self.actionSelection.setObjectName(u"actionSelection")
        self.actionSelection.setEnabled(False)
        icon7 = QIcon()
        icon7.addFile(u"./Res/Select.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.actionSelection.setIcon(icon7)
        self.actionPlotSelLn = QAction(MainWindow)
        self.actionPlotSelLn.setObjectName(u"actionPlotSelLn")
        self.actionPlotSelLn.setEnabled(False)
        icon8 = QIcon()
        icon8.addFile(u"./Res/SelectionLine.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.actionPlotSelLn.setIcon(icon8)
        self.actionFamilyBubble = QAction(MainWindow)
        self.actionFamilyBubble.setObjectName(u"actionFamilyBubble")
        self.actionFamilyBubble.setIcon(icon4)
        self.actionResetView = QAction(MainWindow)
        self.actionResetView.setObjectName(u"actionResetView")
        self.actionFitView = QAction(MainWindow)
        self.actionFitView.setObjectName(u"actionFitView")
        self.actionManageItem = QAction(MainWindow)
        self.actionManageItem.setObjectName(u"actionManageItem")
        icon9 = QIcon()
        icon9.addFile(u"./Res/ManageItem.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.actionManageItem.setIcon(icon9)
        self.actionCapture = QAction(MainWindow)
        self.actionCapture.setObjectName(u"actionCapture")
        icon10 = QIcon()
        icon10.addFile(u"./Res/Capture.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.actionCapture.setIcon(icon10)
        self.actionAbout = QAction(MainWindow)
        self.actionAbout.setObjectName(u"actionAbout")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setHorizontalSpacing(6)
        self.gridLayout.setContentsMargins(0, 0, -1, -1)
        self.label_16 = QLabel(self.centralwidget)
        self.label_16.setObjectName(u"label_16")

        self.gridLayout.addWidget(self.label_16, 15, 3, 1, 1)

        self.label_14 = QLabel(self.centralwidget)
        self.label_14.setObjectName(u"label_14")

        self.gridLayout.addWidget(self.label_14, 6, 3, 1, 1)

        self.familyColumn = QComboBox(self.centralwidget)
        self.familyColumn.setObjectName(u"familyColumn")

        self.gridLayout.addWidget(self.familyColumn, 0, 2, 1, 3)

        self.Refresh_List = QPushButton(self.centralwidget)
        self.Refresh_List.setObjectName(u"Refresh_List")

        self.gridLayout.addWidget(self.Refresh_List, 0, 5, 1, 1)

        self.label_5 = QLabel(self.centralwidget)
        self.label_5.setObjectName(u"label_5")
        font = QFont()
        font.setPointSize(10)
        self.label_5.setFont(font)

        self.gridLayout.addWidget(self.label_5, 10, 0, 1, 2)

        self.delete_mat_label = QPushButton(self.centralwidget)
        self.delete_mat_label.setObjectName(u"delete_mat_label")

        self.gridLayout.addWidget(self.delete_mat_label, 5, 5, 1, 1)

        self.treeView = TreeView(self.centralwidget)
        self.treeView.setObjectName(u"treeView")
        self.treeView.header().setVisible(False)

        self.gridLayout.addWidget(self.treeView, 4, 0, 1, 6)

        self.add_selection = QPushButton(self.centralwidget)
        self.add_selection.setObjectName(u"add_selection")

        self.gridLayout.addWidget(self.add_selection, 10, 4, 1, 1)

        self.listView = AListView(self.centralwidget)
        self.listView.setObjectName(u"listView")

        self.gridLayout.addWidget(self.listView, 11, 0, 1, 6)

        self.Plot_sel_ln = QPushButton(self.centralwidget)
        self.Plot_sel_ln.setObjectName(u"Plot_sel_ln")

        self.gridLayout.addWidget(self.Plot_sel_ln, 14, 4, 1, 1)

        self.label_13 = QLabel(self.centralwidget)
        self.label_13.setObjectName(u"label_13")

        self.gridLayout.addWidget(self.label_13, 5, 3, 1, 1)

        self.clear_sel_ln = QPushButton(self.centralwidget)
        self.clear_sel_ln.setObjectName(u"clear_sel_ln")

        self.gridLayout.addWidget(self.clear_sel_ln, 14, 5, 1, 1)

        self.label_11 = QLabel(self.centralwidget)
        self.label_11.setObjectName(u"label_11")

        self.gridLayout.addWidget(self.label_11, 5, 0, 1, 1)

        self.delete_selection = QPushButton(self.centralwidget)
        self.delete_selection.setObjectName(u"delete_selection")

        self.gridLayout.addWidget(self.delete_selection, 10, 5, 1, 1)

        self.clear_mat_bubble = QPushButton(self.centralwidget)
        self.clear_mat_bubble.setObjectName(u"clear_mat_bubble")

        self.gridLayout.addWidget(self.clear_mat_bubble, 5, 2, 1, 1)

        self.Plot_Prop_Chrt = QPushButton(self.centralwidget)
        self.Plot_Prop_Chrt.setObjectName(u"Plot_Prop_Chrt")

        self.gridLayout.addWidget(self.Plot_Prop_Chrt, 5, 1, 1, 1)

        self.Plot_hulls = QPushButton(self.centralwidget)
        self.Plot_hulls.setObjectName(u"Plot_hulls")

        self.gridLayout.addWidget(self.Plot_hulls, 6, 1, 1, 1)

        self.delete_fam_label = QPushButton(self.centralwidget)
        self.delete_fam_label.setObjectName(u"delete_fam_label")

        self.gridLayout.addWidget(self.delete_fam_label, 6, 5, 1, 1)

        self.clear_hulls = QPushButton(self.centralwidget)
        self.clear_hulls.setObjectName(u"clear_hulls")

        self.gridLayout.addWidget(self.clear_hulls, 6, 2, 1, 1)

        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFont(font)

        self.gridLayout.addWidget(self.label_4, 0, 0, 3, 2)

        self.show_fam_label = QPushButton(self.centralwidget)
        self.show_fam_label.setObjectName(u"show_fam_label")

        self.gridLayout.addWidget(self.show_fam_label, 6, 4, 1, 1)

        self.Plot_clear = QPushButton(self.centralwidget)
        self.Plot_clear.setObjectName(u"Plot_clear")

        self.gridLayout.addWidget(self.Plot_clear, 15, 4, 2, 2)

        self.label_15 = QLabel(self.centralwidget)
        self.label_15.setObjectName(u"label_15")

        self.gridLayout.addWidget(self.label_15, 14, 3, 1, 1)

        self.show_mat_label = QPushButton(self.centralwidget)
        self.show_mat_label.setObjectName(u"show_mat_label")

        self.gridLayout.addWidget(self.show_mat_label, 5, 4, 1, 1)

        self.label_12 = QLabel(self.centralwidget)
        self.label_12.setObjectName(u"label_12")

        self.gridLayout.addWidget(self.label_12, 6, 0, 1, 1)

        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tabWidget.sizePolicy().hasHeightForWidth())
        self.tabWidget.setSizePolicy(sizePolicy)
        self.tabWidget.setFocusPolicy(Qt.TabFocus)
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.horizontalLayout_4 = QHBoxLayout(self.tab)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.gridLayout_4 = QGridLayout()
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.label_18 = QLabel(self.tab)
        self.label_18.setObjectName(u"label_18")

        self.gridLayout_4.addWidget(self.label_18, 0, 0, 1, 1)

        self.label_17 = QLabel(self.tab)
        self.label_17.setObjectName(u"label_17")

        self.gridLayout_4.addWidget(self.label_17, 1, 0, 1, 1)

        self.lineEdit_xaxis = QLineEdit(self.tab)
        self.lineEdit_xaxis.setObjectName(u"lineEdit_xaxis")
        sizePolicy1 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.lineEdit_xaxis.sizePolicy().hasHeightForWidth())
        self.lineEdit_xaxis.setSizePolicy(sizePolicy1)

        self.gridLayout_4.addWidget(self.lineEdit_xaxis, 0, 1, 1, 1)

        self.lineEdit_yaxis = QLineEdit(self.tab)
        self.lineEdit_yaxis.setObjectName(u"lineEdit_yaxis")
        sizePolicy1.setHeightForWidth(self.lineEdit_yaxis.sizePolicy().hasHeightForWidth())
        self.lineEdit_yaxis.setSizePolicy(sizePolicy1)

        self.gridLayout_4.addWidget(self.lineEdit_yaxis, 1, 1, 1, 1)

        self.axis_refresh_graphics = QPushButton(self.tab)
        self.axis_refresh_graphics.setObjectName(u"axis_refresh_graphics")

        self.gridLayout_4.addWidget(self.axis_refresh_graphics, 2, 1, 1, 1)


        self.horizontalLayout_4.addLayout(self.gridLayout_4)

        self.tabWidget.addTab(self.tab, "")
        self.plot_prop = QWidget()
        self.plot_prop.setObjectName(u"plot_prop")
        sizePolicy2 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.plot_prop.sizePolicy().hasHeightForWidth())
        self.plot_prop.setSizePolicy(sizePolicy2)
        self.horizontalLayout_2 = QHBoxLayout(self.plot_prop)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.Plot_refresh_graphics = QPushButton(self.plot_prop)
        self.Plot_refresh_graphics.setObjectName(u"Plot_refresh_graphics")

        self.gridLayout_2.addWidget(self.Plot_refresh_graphics, 2, 2, 1, 2)

        self.label = QLabel(self.plot_prop)
        self.label.setObjectName(u"label")

        self.gridLayout_2.addWidget(self.label, 0, 0, 1, 1)

        self.linearRadio = QRadioButton(self.plot_prop)
        self.buttonGroup = QButtonGroup(MainWindow)
        self.buttonGroup.setObjectName(u"buttonGroup")
        self.buttonGroup.addButton(self.linearRadio)
        self.linearRadio.setObjectName(u"linearRadio")

        self.gridLayout_2.addWidget(self.linearRadio, 3, 3, 2, 1)

        self.checkBox_cursor = QCheckBox(self.plot_prop)
        self.checkBox_cursor.setObjectName(u"checkBox_cursor")
        self.checkBox_cursor.setChecked(True)

        self.gridLayout_2.addWidget(self.checkBox_cursor, 3, 0, 2, 1)

        self.x_range_h = QLineEdit(self.plot_prop)
        self.x_range_h.setObjectName(u"x_range_h")
        sizePolicy3 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.x_range_h.sizePolicy().hasHeightForWidth())
        self.x_range_h.setSizePolicy(sizePolicy3)
        self.x_range_h.setMaximumSize(QSize(100, 16777215))

        self.gridLayout_2.addWidget(self.x_range_h, 0, 3, 1, 1)

        self.logRadio = QRadioButton(self.plot_prop)
        self.buttonGroup.addButton(self.logRadio)
        self.logRadio.setObjectName(u"logRadio")
        self.logRadio.setChecked(True)

        self.gridLayout_2.addWidget(self.logRadio, 3, 2, 2, 1)

        self.x_range_l = QLineEdit(self.plot_prop)
        self.x_range_l.setObjectName(u"x_range_l")
        sizePolicy3.setHeightForWidth(self.x_range_l.sizePolicy().hasHeightForWidth())
        self.x_range_l.setSizePolicy(sizePolicy3)
        self.x_range_l.setMaximumSize(QSize(100, 16777215))

        self.gridLayout_2.addWidget(self.x_range_l, 0, 2, 1, 1)

        self.label_2 = QLabel(self.plot_prop)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout_2.addWidget(self.label_2, 1, 0, 1, 1)

        self.y_range_h = QLineEdit(self.plot_prop)
        self.y_range_h.setObjectName(u"y_range_h")
        sizePolicy3.setHeightForWidth(self.y_range_h.sizePolicy().hasHeightForWidth())
        self.y_range_h.setSizePolicy(sizePolicy3)
        self.y_range_h.setMaximumSize(QSize(100, 16777215))

        self.gridLayout_2.addWidget(self.y_range_h, 1, 3, 1, 1)

        self.y_range_l = QLineEdit(self.plot_prop)
        self.y_range_l.setObjectName(u"y_range_l")
        sizePolicy3.setHeightForWidth(self.y_range_l.sizePolicy().hasHeightForWidth())
        self.y_range_l.setSizePolicy(sizePolicy3)
        self.y_range_l.setMaximumSize(QSize(100, 16777215))

        self.gridLayout_2.addWidget(self.y_range_l, 1, 2, 1, 1)


        self.horizontalLayout_2.addLayout(self.gridLayout_2)

        self.tabWidget.addTab(self.plot_prop, "")
        self.label_property = QWidget()
        self.label_property.setObjectName(u"label_property")
        sizePolicy2.setHeightForWidth(self.label_property.sizePolicy().hasHeightForWidth())
        self.label_property.setSizePolicy(sizePolicy2)
        self.horizontalLayout_3 = QHBoxLayout(self.label_property)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.gridLayout_3 = QGridLayout()
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.label_10 = QLabel(self.label_property)
        self.label_10.setObjectName(u"label_10")

        self.gridLayout_3.addWidget(self.label_10, 0, 3, 1, 1)

        self.FontColor_Mat = QLineEdit(self.label_property)
        self.FontColor_Mat.setObjectName(u"FontColor_Mat")
        sizePolicy3.setHeightForWidth(self.FontColor_Mat.sizePolicy().hasHeightForWidth())
        self.FontColor_Mat.setSizePolicy(sizePolicy3)

        self.gridLayout_3.addWidget(self.FontColor_Mat, 3, 2, 1, 1)

        self.FontColor_Fam = QLineEdit(self.label_property)
        self.FontColor_Fam.setObjectName(u"FontColor_Fam")
        sizePolicy3.setHeightForWidth(self.FontColor_Fam.sizePolicy().hasHeightForWidth())
        self.FontColor_Fam.setSizePolicy(sizePolicy3)

        self.gridLayout_3.addWidget(self.FontColor_Fam, 3, 3, 1, 1)

        self.Fontsize_Mat = QLineEdit(self.label_property)
        self.Fontsize_Mat.setObjectName(u"Fontsize_Mat")
        sizePolicy3.setHeightForWidth(self.Fontsize_Mat.sizePolicy().hasHeightForWidth())
        self.Fontsize_Mat.setSizePolicy(sizePolicy3)
        self.Fontsize_Mat.setMaximumSize(QSize(100, 16777215))

        self.gridLayout_3.addWidget(self.Fontsize_Mat, 2, 2, 1, 1)

        self.FontComboBox_Mat = QFontComboBox(self.label_property)
        self.FontComboBox_Mat.setObjectName(u"FontComboBox_Mat")
        self.FontComboBox_Mat.setEnabled(True)
        self.FontComboBox_Mat.setMaximumSize(QSize(100, 16777215))

        self.gridLayout_3.addWidget(self.FontComboBox_Mat, 1, 2, 1, 1)

        self.label_7 = QLabel(self.label_property)
        self.label_7.setObjectName(u"label_7")

        self.gridLayout_3.addWidget(self.label_7, 2, 0, 1, 2)

        self.FontComboBox_Fam = QFontComboBox(self.label_property)
        self.FontComboBox_Fam.setObjectName(u"FontComboBox_Fam")
        self.FontComboBox_Fam.setMaximumSize(QSize(100, 16777215))

        self.gridLayout_3.addWidget(self.FontComboBox_Fam, 1, 3, 1, 1)

        self.label_6 = QLabel(self.label_property)
        self.label_6.setObjectName(u"label_6")

        self.gridLayout_3.addWidget(self.label_6, 1, 0, 1, 2)

        self.Fontsize_Fam = QLineEdit(self.label_property)
        self.Fontsize_Fam.setObjectName(u"Fontsize_Fam")
        sizePolicy3.setHeightForWidth(self.Fontsize_Fam.sizePolicy().hasHeightForWidth())
        self.Fontsize_Fam.setSizePolicy(sizePolicy3)
        self.Fontsize_Fam.setMaximumSize(QSize(100, 16777215))

        self.gridLayout_3.addWidget(self.Fontsize_Fam, 2, 3, 1, 1)

        self.label_8 = QLabel(self.label_property)
        self.label_8.setObjectName(u"label_8")

        self.gridLayout_3.addWidget(self.label_8, 3, 0, 1, 2)

        self.label_9 = QLabel(self.label_property)
        self.label_9.setObjectName(u"label_9")

        self.gridLayout_3.addWidget(self.label_9, 0, 2, 1, 1)

        self.Plot_refresh_label = QPushButton(self.label_property)
        self.Plot_refresh_label.setObjectName(u"Plot_refresh_label")

        self.gridLayout_3.addWidget(self.Plot_refresh_label, 4, 3, 1, 1)


        self.horizontalLayout_3.addLayout(self.gridLayout_3)

        self.tabWidget.addTab(self.label_property, "")

        self.gridLayout.addWidget(self.tabWidget, 8, 0, 1, 6)

        self.manage_item = QPushButton(self.centralwidget)
        self.manage_item.setObjectName(u"manage_item")

        self.gridLayout.addWidget(self.manage_item, 1, 4, 2, 2)


        self.horizontalLayout.addLayout(self.gridLayout)

        self.graphicsView = AGraphicsView(self.centralwidget)
        self.graphicsView.setObjectName(u"graphicsView")
        sizePolicy4 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.graphicsView.sizePolicy().hasHeightForWidth())
        self.graphicsView.setSizePolicy(sizePolicy4)
        self.graphicsView.setMinimumSize(QSize(800, 800))
        self.graphicsView.setMaximumSize(QSize(800, 800))

        self.horizontalLayout.addWidget(self.graphicsView)

        self.horizontalLayout.setStretch(0, 1)
        self.horizontalLayout.setStretch(1, 10)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1462, 23))
        self.menuFile = QMenu(self.menubar)
        self.menuFile.setObjectName(u"menuFile")
        self.menuEdit = QMenu(self.menubar)
        self.menuEdit.setObjectName(u"menuEdit")
        self.menuView = QMenu(self.menubar)
        self.menuView.setObjectName(u"menuView")
        self.menuSelect = QMenu(self.menubar)
        self.menuSelect.setObjectName(u"menuSelect")
        self.menuTools = QMenu(self.menubar)
        self.menuTools.setObjectName(u"menuTools")
        self.menuWindow = QMenu(self.menubar)
        self.menuWindow.setObjectName(u"menuWindow")
        self.menuFeature_Request = QMenu(self.menubar)
        self.menuFeature_Request.setObjectName(u"menuFeature_Request")
        self.menuHelp = QMenu(self.menubar)
        self.menuHelp.setObjectName(u"menuHelp")
        self.menuSettings = QMenu(self.menubar)
        self.menuSettings.setObjectName(u"menuSettings")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.toolBar = QToolBar(MainWindow)
        self.toolBar.setObjectName(u"toolBar")
        self.toolBar.setMaximumSize(QSize(16777215, 100))
        font1 = QFont()
        font1.setPointSize(8)
        self.toolBar.setFont(font1)
        self.toolBar.setIconSize(QSize(64, 64))
        self.toolBar.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
        MainWindow.addToolBar(Qt.TopToolBarArea, self.toolBar)

        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuEdit.menuAction())
        self.menubar.addAction(self.menuView.menuAction())
        self.menubar.addAction(self.menuSelect.menuAction())
        self.menubar.addAction(self.menuTools.menuAction())
        self.menubar.addAction(self.menuWindow.menuAction())
        self.menubar.addAction(self.menuFeature_Request.menuAction())
        self.menubar.addAction(self.menuSettings.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())
        self.menuFile.addAction(self.actionOpen_CSV)
        self.menuFile.addAction(self.actionCapture)
        self.menuFile.addAction(self.actionExit)
        self.menuEdit.addAction(self.actionManageItem)
        self.menuEdit.addAction(self.actionDelete_Item)
        self.menuEdit.addSeparator()
        self.menuView.addAction(self.actionFitView)
        self.menuView.addAction(self.actionResetView)
        self.menuTools.addAction(self.actionHotReload)
        self.menuHelp.addAction(self.actionAbout)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionOpen_CSV)
        self.toolBar.addAction(self.actionManageItem)
        self.toolBar.addAction(self.actionFamily)
        self.toolBar.addAction(self.actionGenerateChart)
        self.toolBar.addAction(self.actionFamilyBubble)
        self.toolBar.addAction(self.actionSelection)
        self.toolBar.addAction(self.actionPlotSelLn)
        self.toolBar.addAction(self.actionCapture)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionConvexHull)
        self.toolBar.addAction(self.actionAxes)
        self.toolBar.addAction(self.actionSearch)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Beans", None))
        self.actionOpen_CSV.setText(QCoreApplication.translate("MainWindow", u"Open CSV...", None))
        self.actionExit.setText(QCoreApplication.translate("MainWindow", u"Exit", None))
        self.actionAxes.setText(QCoreApplication.translate("MainWindow", u"Axes", None))
#if QT_CONFIG(tooltip)
        self.actionAxes.setToolTip(QCoreApplication.translate("MainWindow", u"Axes", None))
#endif // QT_CONFIG(tooltip)
        self.actionSearch.setText(QCoreApplication.translate("MainWindow", u"Search", None))
        self.actionTools.setText(QCoreApplication.translate("MainWindow", u"Tools", None))
        self.actionSettings.setText(QCoreApplication.translate("MainWindow", u"Settings", None))
        self.actionHelp.setText(QCoreApplication.translate("MainWindow", u"Help", None))
        self.actionAdd_Edit_Item.setText(QCoreApplication.translate("MainWindow", u"Add/Edit Item", None))
        self.actionDelete_Item.setText(QCoreApplication.translate("MainWindow", u"Delete Item", None))
        self.actionGroup_Family.setText(QCoreApplication.translate("MainWindow", u"Group Family", None))
        self.actionUngroup_Family.setText(QCoreApplication.translate("MainWindow", u"Ungroup Family", None))
        self.actionHotReload.setText(QCoreApplication.translate("MainWindow", u"Hot Reload", None))
#if QT_CONFIG(tooltip)
        self.actionHotReload.setToolTip(QCoreApplication.translate("MainWindow", u"Hot reload your code", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(shortcut)
        self.actionHotReload.setShortcut(QCoreApplication.translate("MainWindow", u"F5", None))
#endif // QT_CONFIG(shortcut)
        self.actionConvexHull.setText(QCoreApplication.translate("MainWindow", u"ConvexHull", None))
        self.actionFamily.setText(QCoreApplication.translate("MainWindow", u"Family", None))
        self.actionGenerateChart.setText(QCoreApplication.translate("MainWindow", u"Generate Chart", None))
        self.actionSelection.setText(QCoreApplication.translate("MainWindow", u"Selection", None))
        self.actionPlotSelLn.setText(QCoreApplication.translate("MainWindow", u"Plot Selection Lines", None))
        self.actionFamilyBubble.setText(QCoreApplication.translate("MainWindow", u"Family Bubble", None))
        self.actionResetView.setText(QCoreApplication.translate("MainWindow", u"Reset View", None))
#if QT_CONFIG(tooltip)
        self.actionResetView.setToolTip(QCoreApplication.translate("MainWindow", u"ResetView", None))
#endif // QT_CONFIG(tooltip)
        self.actionFitView.setText(QCoreApplication.translate("MainWindow", u"Fit View", None))
        self.actionManageItem.setText(QCoreApplication.translate("MainWindow", u"Manage Item", None))
        self.actionCapture.setText(QCoreApplication.translate("MainWindow", u"Capture", None))
        self.actionAbout.setText(QCoreApplication.translate("MainWindow", u"About Qt...", None))
        self.label_16.setText("")
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"Family label", None))
        self.Refresh_List.setText(QCoreApplication.translate("MainWindow", u"Refresh List", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Selections Lines", None))
        self.delete_mat_label.setText(QCoreApplication.translate("MainWindow", u"Delete all", None))
        self.add_selection.setText(QCoreApplication.translate("MainWindow", u"Add Selection", None))
        self.Plot_sel_ln.setText(QCoreApplication.translate("MainWindow", u"Generate", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"Materials label", None))
        self.clear_sel_ln.setText(QCoreApplication.translate("MainWindow", u"Clear", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"Materials bubble", None))
        self.delete_selection.setText(QCoreApplication.translate("MainWindow", u"Delete Selection", None))
        self.clear_mat_bubble.setText(QCoreApplication.translate("MainWindow", u"Clear", None))
        self.Plot_Prop_Chrt.setText(QCoreApplication.translate("MainWindow", u"Generate", None))
        self.Plot_hulls.setText(QCoreApplication.translate("MainWindow", u"Generate", None))
        self.delete_fam_label.setText(QCoreApplication.translate("MainWindow", u"Delete all", None))
        self.clear_hulls.setText(QCoreApplication.translate("MainWindow", u"Clear", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"List of Materials", None))
        self.show_fam_label.setText(QCoreApplication.translate("MainWindow", u"Show", None))
        self.Plot_clear.setText(QCoreApplication.translate("MainWindow", u"Clear all", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"Selection line", None))
        self.show_mat_label.setText(QCoreApplication.translate("MainWindow", u"Show", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"Family bubble", None))
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"X-axis Feature", None))
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"Y-axis Feature", None))
        self.lineEdit_xaxis.setText(QCoreApplication.translate("MainWindow", u"Modulus", None))
        self.lineEdit_yaxis.setText(QCoreApplication.translate("MainWindow", u"Strength", None))
        self.axis_refresh_graphics.setText(QCoreApplication.translate("MainWindow", u"Refresh Plot", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("MainWindow", u"Axis select", None))
        self.Plot_refresh_graphics.setText(QCoreApplication.translate("MainWindow", u"Refresh Plot", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"X-axis Range", None))
        self.linearRadio.setText(QCoreApplication.translate("MainWindow", u"Linear", None))
        self.checkBox_cursor.setText(QCoreApplication.translate("MainWindow", u"Cursor lines", None))
        self.logRadio.setText(QCoreApplication.translate("MainWindow", u"LogScale", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Y-axis Range", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.plot_prop), QCoreApplication.translate("MainWindow", u"Plot Property", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"Family", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Font size (pt)", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Font", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Color (Hex code: #RRGGBB)", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Material", None))
        self.Plot_refresh_label.setText(QCoreApplication.translate("MainWindow", u"Refresh Labels", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.label_property), QCoreApplication.translate("MainWindow", u"Label Property", None))
        self.manage_item.setText(QCoreApplication.translate("MainWindow", u"Manage Item", None))
        self.menuFile.setTitle(QCoreApplication.translate("MainWindow", u"File", None))
        self.menuEdit.setTitle(QCoreApplication.translate("MainWindow", u"Edit", None))
        self.menuView.setTitle(QCoreApplication.translate("MainWindow", u"View", None))
        self.menuSelect.setTitle(QCoreApplication.translate("MainWindow", u"Select", None))
        self.menuTools.setTitle(QCoreApplication.translate("MainWindow", u"Tools", None))
        self.menuWindow.setTitle(QCoreApplication.translate("MainWindow", u"Window", None))
        self.menuFeature_Request.setTitle(QCoreApplication.translate("MainWindow", u"Feature Request", None))
        self.menuHelp.setTitle(QCoreApplication.translate("MainWindow", u"Help", None))
        self.menuSettings.setTitle(QCoreApplication.translate("MainWindow", u"Settings", None))
        self.toolBar.setWindowTitle(QCoreApplication.translate("MainWindow", u"toolBar", None))
    # retranslateUi

