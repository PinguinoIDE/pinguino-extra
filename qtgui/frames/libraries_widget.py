# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/yeison/.virtualenvs/pinguino_env/pinguino/pinguino-ide/qtgui/frames/libraries_widget.ui'
#
# Created: Thu Jan 30 18:04:39 2014
#      by: pyside-uic 0.2.15 running on PySide 1.2.1
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_LibraryManager(object):
    def setupUi(self, LibraryManager):
        LibraryManager.setObjectName("LibraryManager")
        LibraryManager.resize(839, 382)
        self.centralwidget = QtGui.QWidget(LibraryManager)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.pushButton_close = QtGui.QPushButton(self.centralwidget)
        self.pushButton_close.setMinimumSize(QtCore.QSize(165, 0))
        self.pushButton_close.setMaximumSize(QtCore.QSize(165, 16777215))
        self.pushButton_close.setObjectName("pushButton_close")
        self.gridLayout.addWidget(self.pushButton_close, 1, 2, 1, 1)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 1, 1, 1, 1)
        self.commandLinkButton_how = QtGui.QCommandLinkButton(self.centralwidget)
        self.commandLinkButton_how.setCursor(QtCore.Qt.WhatsThisCursor)
        self.commandLinkButton_how.setObjectName("commandLinkButton_how")
        self.gridLayout.addWidget(self.commandLinkButton_how, 1, 0, 1, 1)
        self.tabWidget = QtGui.QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName("tabWidget")
        self.tab_2 = QtGui.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.gridLayout_3 = QtGui.QGridLayout(self.tab_2)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.lineEdit_source = QtGui.QLineEdit(self.tab_2)
        self.lineEdit_source.setObjectName("lineEdit_source")
        self.gridLayout_3.addWidget(self.lineEdit_source, 0, 0, 1, 1)
        self.pushButton_add = QtGui.QPushButton(self.tab_2)
        self.pushButton_add.setObjectName("pushButton_add")
        self.gridLayout_3.addWidget(self.pushButton_add, 0, 1, 1, 1)
        self.pushButton_from_zip = QtGui.QPushButton(self.tab_2)
        self.pushButton_from_zip.setObjectName("pushButton_from_zip")
        self.gridLayout_3.addWidget(self.pushButton_from_zip, 0, 2, 1, 1)
        self.tableWidget_sources = QtGui.QTableWidget(self.tab_2)
        self.tableWidget_sources.setAutoFillBackground(True)
        self.tableWidget_sources.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.tableWidget_sources.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.tableWidget_sources.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        self.tableWidget_sources.setAlternatingRowColors(True)
        self.tableWidget_sources.setVerticalScrollMode(QtGui.QAbstractItemView.ScrollPerPixel)
        self.tableWidget_sources.setHorizontalScrollMode(QtGui.QAbstractItemView.ScrollPerPixel)
        self.tableWidget_sources.setGridStyle(QtCore.Qt.NoPen)
        self.tableWidget_sources.setObjectName("tableWidget_sources")
        self.tableWidget_sources.setColumnCount(2)
        self.tableWidget_sources.setRowCount(6)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_sources.setVerticalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_sources.setVerticalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_sources.setVerticalHeaderItem(2, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_sources.setVerticalHeaderItem(3, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_sources.setVerticalHeaderItem(4, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_sources.setVerticalHeaderItem(5, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_sources.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_sources.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        item.setFlags(QtCore.Qt.ItemIsDragEnabled|QtCore.Qt.ItemIsUserCheckable|QtCore.Qt.ItemIsEnabled)
        self.tableWidget_sources.setItem(1, 0, item)
        self.tableWidget_sources.horizontalHeader().setHighlightSections(False)
        self.tableWidget_sources.horizontalHeader().setStretchLastSection(True)
        self.tableWidget_sources.verticalHeader().setVisible(False)
        self.tableWidget_sources.verticalHeader().setHighlightSections(True)
        self.tableWidget_sources.verticalHeader().setStretchLastSection(False)
        self.gridLayout_3.addWidget(self.tableWidget_sources, 1, 0, 1, 3)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton_update = QtGui.QPushButton(self.tab_2)
        self.pushButton_update.setEnabled(False)
        self.pushButton_update.setObjectName("pushButton_update")
        self.horizontalLayout.addWidget(self.pushButton_update)
        self.pushButton_remove = QtGui.QPushButton(self.tab_2)
        self.pushButton_remove.setEnabled(False)
        self.pushButton_remove.setObjectName("pushButton_remove")
        self.horizontalLayout.addWidget(self.pushButton_remove)
        self.gridLayout_3.addLayout(self.horizontalLayout, 3, 0, 1, 3)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.checkBox_sources = QtGui.QCheckBox(self.tab_2)
        self.checkBox_sources.setObjectName("checkBox_sources")
        self.horizontalLayout_3.addWidget(self.checkBox_sources)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem1)
        self.gridLayout_3.addLayout(self.horizontalLayout_3, 2, 0, 1, 3)
        self.tabWidget.addTab(self.tab_2, "")
        self.tab = QtGui.QWidget()
        self.tab.setObjectName("tab")
        self.gridLayout_2 = QtGui.QGridLayout(self.tab)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.tableWidget_libs = QtGui.QTableWidget(self.tab)
        self.tableWidget_libs.setAlternatingRowColors(True)
        self.tableWidget_libs.setVerticalScrollMode(QtGui.QAbstractItemView.ScrollPerPixel)
        self.tableWidget_libs.setHorizontalScrollMode(QtGui.QAbstractItemView.ScrollPerPixel)
        self.tableWidget_libs.setGridStyle(QtCore.Qt.NoPen)
        self.tableWidget_libs.setWordWrap(False)
        self.tableWidget_libs.setCornerButtonEnabled(False)
        self.tableWidget_libs.setObjectName("tableWidget_libs")
        self.tableWidget_libs.setColumnCount(4)
        self.tableWidget_libs.setRowCount(6)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_libs.setVerticalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_libs.setVerticalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_libs.setVerticalHeaderItem(2, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_libs.setVerticalHeaderItem(3, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_libs.setVerticalHeaderItem(4, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_libs.setVerticalHeaderItem(5, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_libs.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_libs.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_libs.setHorizontalHeaderItem(2, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_libs.setHorizontalHeaderItem(3, item)
        self.tableWidget_libs.horizontalHeader().setHighlightSections(False)
        self.tableWidget_libs.horizontalHeader().setStretchLastSection(True)
        self.tableWidget_libs.verticalHeader().setVisible(False)
        self.gridLayout_2.addWidget(self.tableWidget_libs, 0, 0, 1, 1)
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.checkBox_libs = QtGui.QCheckBox(self.tab)
        self.checkBox_libs.setObjectName("checkBox_libs")
        self.horizontalLayout_4.addWidget(self.checkBox_libs)
        spacerItem2 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem2)
        self.gridLayout_2.addLayout(self.horizontalLayout_4, 1, 0, 1, 1)
        self.pushButton_apply = QtGui.QPushButton(self.tab)
        self.pushButton_apply.setEnabled(False)
        self.pushButton_apply.setMinimumSize(QtCore.QSize(265, 0))
        self.pushButton_apply.setMaximumSize(QtCore.QSize(265, 16777215))
        self.pushButton_apply.setObjectName("pushButton_apply")
        self.gridLayout_2.addWidget(self.pushButton_apply, 2, 0, 1, 1)
        self.tabWidget.addTab(self.tab, "")
        self.gridLayout.addWidget(self.tabWidget, 0, 0, 1, 4)
        LibraryManager.setCentralWidget(self.centralwidget)

        self.retranslateUi(LibraryManager)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(LibraryManager)
        LibraryManager.setTabOrder(self.lineEdit_source, self.pushButton_add)
        LibraryManager.setTabOrder(self.pushButton_add, self.pushButton_from_zip)
        LibraryManager.setTabOrder(self.pushButton_from_zip, self.tableWidget_sources)
        LibraryManager.setTabOrder(self.tableWidget_sources, self.pushButton_update)
        LibraryManager.setTabOrder(self.pushButton_update, self.pushButton_remove)
        LibraryManager.setTabOrder(self.pushButton_remove, self.tabWidget)
        LibraryManager.setTabOrder(self.tabWidget, self.tableWidget_libs)
        LibraryManager.setTabOrder(self.tableWidget_libs, self.pushButton_apply)
        LibraryManager.setTabOrder(self.pushButton_apply, self.commandLinkButton_how)
        LibraryManager.setTabOrder(self.commandLinkButton_how, self.pushButton_close)

    def retranslateUi(self, LibraryManager):
        LibraryManager.setWindowTitle(QtGui.QApplication.translate("LibraryManager", "Library Manager", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_close.setText(QtGui.QApplication.translate("LibraryManager", "Close", None, QtGui.QApplication.UnicodeUTF8))
        self.commandLinkButton_how.setText(QtGui.QApplication.translate("LibraryManager", "How develop libraries", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_add.setText(QtGui.QApplication.translate("LibraryManager", "Add", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_from_zip.setText(QtGui.QApplication.translate("LibraryManager", "Install from .zip", None, QtGui.QApplication.UnicodeUTF8))
        self.tableWidget_sources.verticalHeaderItem(0).setText(QtGui.QApplication.translate("LibraryManager", "New Row", None, QtGui.QApplication.UnicodeUTF8))
        self.tableWidget_sources.verticalHeaderItem(1).setText(QtGui.QApplication.translate("LibraryManager", "New Row", None, QtGui.QApplication.UnicodeUTF8))
        self.tableWidget_sources.verticalHeaderItem(2).setText(QtGui.QApplication.translate("LibraryManager", "New Row", None, QtGui.QApplication.UnicodeUTF8))
        self.tableWidget_sources.verticalHeaderItem(3).setText(QtGui.QApplication.translate("LibraryManager", "New Row", None, QtGui.QApplication.UnicodeUTF8))
        self.tableWidget_sources.verticalHeaderItem(4).setText(QtGui.QApplication.translate("LibraryManager", "New Row", None, QtGui.QApplication.UnicodeUTF8))
        self.tableWidget_sources.verticalHeaderItem(5).setText(QtGui.QApplication.translate("LibraryManager", "New Row", None, QtGui.QApplication.UnicodeUTF8))
        self.tableWidget_sources.horizontalHeaderItem(0).setText(QtGui.QApplication.translate("LibraryManager", "Name", None, QtGui.QApplication.UnicodeUTF8))
        self.tableWidget_sources.horizontalHeaderItem(1).setText(QtGui.QApplication.translate("LibraryManager", "Repository", None, QtGui.QApplication.UnicodeUTF8))
        __sortingEnabled = self.tableWidget_sources.isSortingEnabled()
        self.tableWidget_sources.setSortingEnabled(False)
        self.tableWidget_sources.setSortingEnabled(__sortingEnabled)
        self.pushButton_update.setText(QtGui.QApplication.translate("LibraryManager", "Update selected", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_remove.setText(QtGui.QApplication.translate("LibraryManager", "Remove selected", None, QtGui.QApplication.UnicodeUTF8))
        self.checkBox_sources.setText(QtGui.QApplication.translate("LibraryManager", "Check/Uncheck all", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QtGui.QApplication.translate("LibraryManager", "Sources", None, QtGui.QApplication.UnicodeUTF8))
        self.tableWidget_libs.verticalHeaderItem(0).setText(QtGui.QApplication.translate("LibraryManager", "New Row", None, QtGui.QApplication.UnicodeUTF8))
        self.tableWidget_libs.verticalHeaderItem(1).setText(QtGui.QApplication.translate("LibraryManager", "New Row", None, QtGui.QApplication.UnicodeUTF8))
        self.tableWidget_libs.verticalHeaderItem(2).setText(QtGui.QApplication.translate("LibraryManager", "New Row", None, QtGui.QApplication.UnicodeUTF8))
        self.tableWidget_libs.verticalHeaderItem(3).setText(QtGui.QApplication.translate("LibraryManager", "New Row", None, QtGui.QApplication.UnicodeUTF8))
        self.tableWidget_libs.verticalHeaderItem(4).setText(QtGui.QApplication.translate("LibraryManager", "New Row", None, QtGui.QApplication.UnicodeUTF8))
        self.tableWidget_libs.verticalHeaderItem(5).setText(QtGui.QApplication.translate("LibraryManager", "New Row", None, QtGui.QApplication.UnicodeUTF8))
        self.tableWidget_libs.horizontalHeaderItem(0).setText(QtGui.QApplication.translate("LibraryManager", "Library", None, QtGui.QApplication.UnicodeUTF8))
        self.tableWidget_libs.horizontalHeaderItem(1).setText(QtGui.QApplication.translate("LibraryManager", "Architecture", None, QtGui.QApplication.UnicodeUTF8))
        self.tableWidget_libs.horizontalHeaderItem(2).setText(QtGui.QApplication.translate("LibraryManager", "Author", None, QtGui.QApplication.UnicodeUTF8))
        self.tableWidget_libs.horizontalHeaderItem(3).setText(QtGui.QApplication.translate("LibraryManager", "Description", None, QtGui.QApplication.UnicodeUTF8))
        self.checkBox_libs.setText(QtGui.QApplication.translate("LibraryManager", "Check/Uncheck all", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_apply.setText(QtGui.QApplication.translate("LibraryManager", "Apply", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QtGui.QApplication.translate("LibraryManager", "Libraries", None, QtGui.QApplication.UnicodeUTF8))

