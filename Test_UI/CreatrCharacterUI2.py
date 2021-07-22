# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'CreatrCharacterUI2.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_root(object):
    def setupUi(self, root):
        if not root.objectName():
            root.setObjectName(u"root")
        root.resize(720, 480)
        self.widget = QWidget(root)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(0, 0, 720, 480))
        self.verticalLayout = QVBoxLayout(self.widget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_2 = QLabel(self.widget)
        self.label_2.setObjectName(u"label_2")
        font = QFont()
        font.setFamily(u"Noto Sans CJK TC")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)

        self.verticalLayout.addWidget(self.label_2)

        self.horizontalLayout_13 = QHBoxLayout()
        self.horizontalLayout_13.setSpacing(4)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.horizontalLayout_14 = QHBoxLayout()
        self.horizontalLayout_14.setSpacing(6)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.horizontalLayout_14.setContentsMargins(-1, 10, 10, 10)
        self.label_4 = QLabel(self.widget)
        self.label_4.setObjectName(u"label_4")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy)
        self.label_4.setFont(font)

        self.horizontalLayout_14.addWidget(self.label_4)

        self.nameVal_2 = QLineEdit(self.widget)
        self.nameVal_2.setObjectName(u"nameVal_2")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.nameVal_2.sizePolicy().hasHeightForWidth())
        self.nameVal_2.setSizePolicy(sizePolicy1)

        self.horizontalLayout_14.addWidget(self.nameVal_2)


        self.verticalLayout_5.addLayout(self.horizontalLayout_14)

        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setSpacing(6)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(-1, 0, -1, 100)
        self.horizontalLayout_15 = QHBoxLayout()
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.horizontalLayout_15.setContentsMargins(17, -1, 20, -1)
        self.label_15 = QLabel(self.widget)
        self.label_15.setObjectName(u"label_15")
        sizePolicy2 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.label_15.sizePolicy().hasHeightForWidth())
        self.label_15.setSizePolicy(sizePolicy2)
        self.label_15.setFont(font)

        self.horizontalLayout_15.addWidget(self.label_15)

        self.APLa_2 = QLabel(self.widget)
        self.APLa_2.setObjectName(u"APLa_2")
        sizePolicy3 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.APLa_2.sizePolicy().hasHeightForWidth())
        self.APLa_2.setSizePolicy(sizePolicy3)
        self.APLa_2.setFont(font)

        self.horizontalLayout_15.addWidget(self.APLa_2)

        self.label_16 = QLabel(self.widget)
        self.label_16.setObjectName(u"label_16")
        sizePolicy.setHeightForWidth(self.label_16.sizePolicy().hasHeightForWidth())
        self.label_16.setSizePolicy(sizePolicy)
        self.label_16.setFont(font)

        self.horizontalLayout_15.addWidget(self.label_16)


        self.verticalLayout_6.addLayout(self.horizontalLayout_15)

        self.horizontalLayout_16 = QHBoxLayout()
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.horizontalLayout_16.setContentsMargins(-1, -1, 30, -1)
        self.horizontalLayout_17 = QHBoxLayout()
        self.horizontalLayout_17.setSpacing(4)
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.horizontalLayout_17.setContentsMargins(70, -1, 40, -1)
        self.label_7 = QLabel(self.widget)
        self.label_7.setObjectName(u"label_7")
        sizePolicy4 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy4.setHorizontalStretch(60)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.label_7.sizePolicy().hasHeightForWidth())
        self.label_7.setSizePolicy(sizePolicy4)
        self.label_7.setFont(font)

        self.horizontalLayout_17.addWidget(self.label_7)


        self.horizontalLayout_16.addLayout(self.horizontalLayout_17)

        self.strelowerBu_2 = QPushButton(self.widget)
        self.strelowerBu_2.setObjectName(u"strelowerBu_2")
        sizePolicy5 = QSizePolicy(QSizePolicy.Ignored, QSizePolicy.Fixed)
        sizePolicy5.setHorizontalStretch(10)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.strelowerBu_2.sizePolicy().hasHeightForWidth())
        self.strelowerBu_2.setSizePolicy(sizePolicy5)

        self.horizontalLayout_16.addWidget(self.strelowerBu_2)

        self.horizontalLayout_25 = QHBoxLayout()
        self.horizontalLayout_25.setObjectName(u"horizontalLayout_25")
        self.horizontalLayout_25.setContentsMargins(10, -1, 10, -1)
        self.streVal_2 = QLabel(self.widget)
        self.streVal_2.setObjectName(u"streVal_2")
        sizePolicy6 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        sizePolicy6.setHorizontalStretch(10)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(self.streVal_2.sizePolicy().hasHeightForWidth())
        self.streVal_2.setSizePolicy(sizePolicy6)
        self.streVal_2.setFont(font)

        self.horizontalLayout_25.addWidget(self.streVal_2)


        self.horizontalLayout_16.addLayout(self.horizontalLayout_25)

        self.streHoistBu_2 = QPushButton(self.widget)
        self.streHoistBu_2.setObjectName(u"streHoistBu_2")
        sizePolicy5.setHeightForWidth(self.streHoistBu_2.sizePolicy().hasHeightForWidth())
        self.streHoistBu_2.setSizePolicy(sizePolicy5)

        self.horizontalLayout_16.addWidget(self.streHoistBu_2)


        self.verticalLayout_6.addLayout(self.horizontalLayout_16)

        self.horizontalLayout_18 = QHBoxLayout()
#ifndef Q_OS_MAC
        self.horizontalLayout_18.setSpacing(-1)
#endif
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.horizontalLayout_18.setContentsMargins(0, -1, 30, -1)
        self.horizontalLayout_19 = QHBoxLayout()
        self.horizontalLayout_19.setSpacing(4)
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.horizontalLayout_19.setContentsMargins(70, -1, 40, -1)
        self.label_8 = QLabel(self.widget)
        self.label_8.setObjectName(u"label_8")
        sizePolicy4.setHeightForWidth(self.label_8.sizePolicy().hasHeightForWidth())
        self.label_8.setSizePolicy(sizePolicy4)
        self.label_8.setFont(font)

        self.horizontalLayout_19.addWidget(self.label_8)


        self.horizontalLayout_18.addLayout(self.horizontalLayout_19)

        self.agilowerBu_2 = QPushButton(self.widget)
        self.agilowerBu_2.setObjectName(u"agilowerBu_2")
        sizePolicy5.setHeightForWidth(self.agilowerBu_2.sizePolicy().hasHeightForWidth())
        self.agilowerBu_2.setSizePolicy(sizePolicy5)

        self.horizontalLayout_18.addWidget(self.agilowerBu_2)

        self.horizontalLayout_27 = QHBoxLayout()
        self.horizontalLayout_27.setObjectName(u"horizontalLayout_27")
        self.horizontalLayout_27.setContentsMargins(10, -1, 10, -1)
        self.agiVal_2 = QLabel(self.widget)
        self.agiVal_2.setObjectName(u"agiVal_2")
        sizePolicy6.setHeightForWidth(self.agiVal_2.sizePolicy().hasHeightForWidth())
        self.agiVal_2.setSizePolicy(sizePolicy6)
        self.agiVal_2.setFont(font)

        self.horizontalLayout_27.addWidget(self.agiVal_2)


        self.horizontalLayout_18.addLayout(self.horizontalLayout_27)

        self.agiHoistBu_2 = QPushButton(self.widget)
        self.agiHoistBu_2.setObjectName(u"agiHoistBu_2")
        sizePolicy5.setHeightForWidth(self.agiHoistBu_2.sizePolicy().hasHeightForWidth())
        self.agiHoistBu_2.setSizePolicy(sizePolicy5)

        self.horizontalLayout_18.addWidget(self.agiHoistBu_2)


        self.verticalLayout_6.addLayout(self.horizontalLayout_18)

        self.horizontalLayout_20 = QHBoxLayout()
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
        self.horizontalLayout_20.setContentsMargins(-1, -1, 30, -1)
        self.horizontalLayout_21 = QHBoxLayout()
        self.horizontalLayout_21.setObjectName(u"horizontalLayout_21")
        self.horizontalLayout_21.setContentsMargins(70, -1, 40, -1)
        self.label_10 = QLabel(self.widget)
        self.label_10.setObjectName(u"label_10")
        sizePolicy4.setHeightForWidth(self.label_10.sizePolicy().hasHeightForWidth())
        self.label_10.setSizePolicy(sizePolicy4)
        self.label_10.setFont(font)

        self.horizontalLayout_21.addWidget(self.label_10)


        self.horizontalLayout_20.addLayout(self.horizontalLayout_21)

        self.intelowerBu_2 = QPushButton(self.widget)
        self.intelowerBu_2.setObjectName(u"intelowerBu_2")
        sizePolicy5.setHeightForWidth(self.intelowerBu_2.sizePolicy().hasHeightForWidth())
        self.intelowerBu_2.setSizePolicy(sizePolicy5)

        self.horizontalLayout_20.addWidget(self.intelowerBu_2)

        self.horizontalLayout_28 = QHBoxLayout()
        self.horizontalLayout_28.setObjectName(u"horizontalLayout_28")
        self.horizontalLayout_28.setContentsMargins(10, -1, 10, -1)
        self.inteVal_2 = QLabel(self.widget)
        self.inteVal_2.setObjectName(u"inteVal_2")
        sizePolicy6.setHeightForWidth(self.inteVal_2.sizePolicy().hasHeightForWidth())
        self.inteVal_2.setSizePolicy(sizePolicy6)
        self.inteVal_2.setFont(font)

        self.horizontalLayout_28.addWidget(self.inteVal_2)


        self.horizontalLayout_20.addLayout(self.horizontalLayout_28)

        self.inteHoistBu_2 = QPushButton(self.widget)
        self.inteHoistBu_2.setObjectName(u"inteHoistBu_2")
        sizePolicy5.setHeightForWidth(self.inteHoistBu_2.sizePolicy().hasHeightForWidth())
        self.inteHoistBu_2.setSizePolicy(sizePolicy5)

        self.horizontalLayout_20.addWidget(self.inteHoistBu_2)


        self.verticalLayout_6.addLayout(self.horizontalLayout_20)

        self.horizontalLayout_22 = QHBoxLayout()
        self.horizontalLayout_22.setObjectName(u"horizontalLayout_22")
        self.horizontalLayout_22.setContentsMargins(-1, -1, 30, -1)
        self.verticalLayout_7 = QVBoxLayout()
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(70, -1, 40, -1)
        self.label_12 = QLabel(self.widget)
        self.label_12.setObjectName(u"label_12")
        sizePolicy4.setHeightForWidth(self.label_12.sizePolicy().hasHeightForWidth())
        self.label_12.setSizePolicy(sizePolicy4)
        self.label_12.setFont(font)

        self.verticalLayout_7.addWidget(self.label_12)


        self.horizontalLayout_22.addLayout(self.verticalLayout_7)

        self.conlowerBu_2 = QPushButton(self.widget)
        self.conlowerBu_2.setObjectName(u"conlowerBu_2")
        sizePolicy5.setHeightForWidth(self.conlowerBu_2.sizePolicy().hasHeightForWidth())
        self.conlowerBu_2.setSizePolicy(sizePolicy5)

        self.horizontalLayout_22.addWidget(self.conlowerBu_2)

        self.horizontalLayout_29 = QHBoxLayout()
        self.horizontalLayout_29.setObjectName(u"horizontalLayout_29")
        self.horizontalLayout_29.setContentsMargins(10, -1, 10, -1)
        self.conVal_2 = QLabel(self.widget)
        self.conVal_2.setObjectName(u"conVal_2")
        sizePolicy7 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy7.setHorizontalStretch(10)
        sizePolicy7.setVerticalStretch(0)
        sizePolicy7.setHeightForWidth(self.conVal_2.sizePolicy().hasHeightForWidth())
        self.conVal_2.setSizePolicy(sizePolicy7)
        self.conVal_2.setFont(font)

        self.horizontalLayout_29.addWidget(self.conVal_2)


        self.horizontalLayout_22.addLayout(self.horizontalLayout_29)

        self.conHoistBu_2 = QPushButton(self.widget)
        self.conHoistBu_2.setObjectName(u"conHoistBu_2")
        sizePolicy5.setHeightForWidth(self.conHoistBu_2.sizePolicy().hasHeightForWidth())
        self.conHoistBu_2.setSizePolicy(sizePolicy5)

        self.horizontalLayout_22.addWidget(self.conHoistBu_2)


        self.verticalLayout_6.addLayout(self.horizontalLayout_22)

        self.horizontalLayout_23 = QHBoxLayout()
        self.horizontalLayout_23.setObjectName(u"horizontalLayout_23")
        self.horizontalLayout_23.setContentsMargins(-1, -1, 30, -1)
        self.horizontalLayout_24 = QHBoxLayout()
        self.horizontalLayout_24.setObjectName(u"horizontalLayout_24")
        self.horizontalLayout_24.setContentsMargins(70, -1, 40, -1)
        self.label_17 = QLabel(self.widget)
        self.label_17.setObjectName(u"label_17")
        sizePolicy4.setHeightForWidth(self.label_17.sizePolicy().hasHeightForWidth())
        self.label_17.setSizePolicy(sizePolicy4)
        self.label_17.setFont(font)

        self.horizontalLayout_24.addWidget(self.label_17)


        self.horizontalLayout_23.addLayout(self.horizontalLayout_24)

        self.wislowerBu_2 = QPushButton(self.widget)
        self.wislowerBu_2.setObjectName(u"wislowerBu_2")
        sizePolicy5.setHeightForWidth(self.wislowerBu_2.sizePolicy().hasHeightForWidth())
        self.wislowerBu_2.setSizePolicy(sizePolicy5)

        self.horizontalLayout_23.addWidget(self.wislowerBu_2)

        self.horizontalLayout_30 = QHBoxLayout()
        self.horizontalLayout_30.setObjectName(u"horizontalLayout_30")
        self.horizontalLayout_30.setContentsMargins(10, -1, 10, -1)
        self.wisVal_2 = QLabel(self.widget)
        self.wisVal_2.setObjectName(u"wisVal_2")
        sizePolicy6.setHeightForWidth(self.wisVal_2.sizePolicy().hasHeightForWidth())
        self.wisVal_2.setSizePolicy(sizePolicy6)
        self.wisVal_2.setFont(font)

        self.horizontalLayout_30.addWidget(self.wisVal_2)


        self.horizontalLayout_23.addLayout(self.horizontalLayout_30)

        self.wisHoistBu_2 = QPushButton(self.widget)
        self.wisHoistBu_2.setObjectName(u"wisHoistBu_2")
        sizePolicy5.setHeightForWidth(self.wisHoistBu_2.sizePolicy().hasHeightForWidth())
        self.wisHoistBu_2.setSizePolicy(sizePolicy5)

        self.horizontalLayout_23.addWidget(self.wisHoistBu_2)


        self.verticalLayout_6.addLayout(self.horizontalLayout_23)

        self.nextpage = QPushButton(self.widget)
        self.nextpage.setObjectName(u"nextpage")

        self.verticalLayout_6.addWidget(self.nextpage)


        self.verticalLayout_5.addLayout(self.verticalLayout_6)

        self.verticalLayout_5.setStretch(1, 20)

        self.horizontalLayout_13.addLayout(self.verticalLayout_5)

        self.textBrowser_2 = QTextBrowser(self.widget)
        self.textBrowser_2.setObjectName(u"textBrowser_2")
        sizePolicy8 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Minimum)
        sizePolicy8.setHorizontalStretch(0)
        sizePolicy8.setVerticalStretch(0)
        sizePolicy8.setHeightForWidth(self.textBrowser_2.sizePolicy().hasHeightForWidth())
        self.textBrowser_2.setSizePolicy(sizePolicy8)

        self.horizontalLayout_13.addWidget(self.textBrowser_2)

        self.horizontalLayout_13.setStretch(0, 1)
        self.horizontalLayout_13.setStretch(1, 2)

        self.verticalLayout.addLayout(self.horizontalLayout_13)


        self.retranslateUi(root)

        QMetaObject.connectSlotsByName(root)
    # setupUi

    def retranslateUi(self, root):
        root.setWindowTitle(QCoreApplication.translate("root", u"Form", None))
        self.label_2.setText(QCoreApplication.translate("root", u"\u5275\u9020\u4f60\u5fc3\u76ee\u4e2d\u7684\u5049\u5927\u82f1\u96c4", None))
        self.label_4.setText(QCoreApplication.translate("root", u"\u82f1\u96c4\u540d\u7a31\uff1a", None))
        self.label_15.setText(QCoreApplication.translate("root", u"\u4f60\u7684\u82f1\u96c4\u9084\u6709", None))
        self.APLa_2.setText(QCoreApplication.translate("root", u"3", None))
        self.label_16.setText(QCoreApplication.translate("root", u"\u9ede\u53ef\u4ee5\u52a0\u9ede", None))
        self.label_7.setText(QCoreApplication.translate("root", u"\u529b\u91cf", None))
        self.strelowerBu_2.setText(QCoreApplication.translate("root", u"<", None))
        self.streVal_2.setText(QCoreApplication.translate("root", u"6", None))
        self.streHoistBu_2.setText(QCoreApplication.translate("root", u">", None))
        self.label_8.setText(QCoreApplication.translate("root", u"\u654f\u6377", None))
        self.agilowerBu_2.setText(QCoreApplication.translate("root", u"<", None))
        self.agiVal_2.setText(QCoreApplication.translate("root", u"6", None))
        self.agiHoistBu_2.setText(QCoreApplication.translate("root", u">", None))
        self.label_10.setText(QCoreApplication.translate("root", u"\u667a\u6167", None))
        self.intelowerBu_2.setText(QCoreApplication.translate("root", u"<", None))
        self.inteVal_2.setText(QCoreApplication.translate("root", u"6", None))
        self.inteHoistBu_2.setText(QCoreApplication.translate("root", u">", None))
        self.label_12.setText(QCoreApplication.translate("root", u"\u9ad4\u8cea", None))
        self.conlowerBu_2.setText(QCoreApplication.translate("root", u"<", None))
        self.conVal_2.setText(QCoreApplication.translate("root", u"6", None))
        self.conHoistBu_2.setText(QCoreApplication.translate("root", u">", None))
        self.label_17.setText(QCoreApplication.translate("root", u"\u777f\u667a", None))
        self.wislowerBu_2.setText(QCoreApplication.translate("root", u"<", None))
        self.wisVal_2.setText(QCoreApplication.translate("root", u"6", None))
        self.wisHoistBu_2.setText(QCoreApplication.translate("root", u">", None))
        self.nextpage.setText(QCoreApplication.translate("root", u"\u4e0b\u4e00\u9801", None))
    # retranslateUi

