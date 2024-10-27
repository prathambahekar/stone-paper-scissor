# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainCrnkUQ.ui'
##
## Created by: Qt User Interface Compiler version 6.8.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLabel,
    QMainWindow, QPushButton, QSizePolicy, QSpacerItem,
    QStackedWidget, QVBoxLayout, QWidget)
import files.assest_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(757, 624)
        MainWindow.setMinimumSize(QSize(550, 500))
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"/* Dark Theme */\n"
"\n"
"* {\n"
"    background-color: #1b1b1b;\n"
"    font: 600 20pt \"Consolas\";\n"
"    color: #e0e0e0;\n"
"}\n"
"\n"
"#leftMenu .QPushButton {\n"
"    background-color: transparent;\n"
"    border-radius: 7px;\n"
"}\n"
"\n"
"#leftMenu .QPushButton:hover {\n"
"    background-color: #3a3a3a;\n"
"}\n"
"\n"
"#leftMenu .QPushButton:pressed {\n"
"    background-color: #2b2b2b;\n"
"}\n"
"\n"
"#mainFrame {\n"
"    border: 2px solid #202326;	\n"
"	border-radius: 7px;\n"
"}\n"
"\n"
"#mainFrame .QFrame {\n"
"\n"
"	background-color: #1e1e1e;\n"
"	\n"
"}\n"
"\n"
"#mainFrame .QLabel {\n"
"\n"
"	background-color: #1e1e1e;\n"
"	\n"
"}\n"
"\n"
"#leftMenu .QPushButton {\n"
"	\n"
"    padding: 7px;\n"
"    image-position: left center;\n"
"    font:  13pt \"Consolas\";\n"
"    color: #ffffff;\n"
"}\n"
"\n"
"#settings_btn {\n"
"    \n"
"	image: url(:/dark/dark/settings_48_regular.svg);\n"
"}\n"
"\n"
"#home_btn {\n"
"    \n"
"	\n"
"	image: url(:/dark/dark/home_48_regular.svg);\n"
"}\n"
"\n"
"#theme_btn {\n"
""
                        "    \n"
"	image: url(:/dark/dark/weather_sunny_48_regular.svg);\n"
"}\n"
"\n"
"#menu_btn {\n"
"    \n"
"	image: url(:/dark/dark/panel_left_text_48_regular.svg);\n"
"}\n"
"\n"
"#stg_lbl_main {\n"
"    padding-left: 4px;\n"
"    font: 700 24pt \"Consolas\";\n"
"}\n"
"\n"
"#stack_stg .QWidget {\n"
"    border-radius: 8px;\n"
"    background-color: #4a4a4a;\n"
"}\n"
"\n"
"#stg_home_app_bt_lbl {\n"
"    font: 600 13pt \"Consolas Semib\";\n"
"    padding-left: 16px;\n"
"}\n"
"\n"
"#stg_home_app_img_lbl {\n"
"    padding: 17px;\n"
"}\n"
"\n"
"#stg_home_app_hd_lbl {\n"
"    font: 900 16pt \"Consolas\";\n"
"    padding-left: 2px;\n"
"}\n"
"\n"
"#stg_home_app_img_btn {\n"
"    font: 600 14pt \"Consolas\";\n"
"    padding-left: 4px;\n"
"	border: 0px;\n"
"}\n"
"\n"
"#stg_home_info_bt_lbl {\n"
"    font: 600 13pt \"Consolas\";\n"
"    padding-left: 16px;\n"
"}\n"
"\n"
"#stg_home_info_img_lbl {\n"
"    padding: 17px;\n"
"}\n"
"\n"
"#stg_home_info_hd_lbl {\n"
"    font: 900 16pt \"Consolas\";\n"
"    padding-left: 2px;\n"
"}"
                        "\n"
"\n"
"#stg_home_info_img_btn {\n"
"    font: 600 14pt \"Consolas\";\n"
"    padding-left: 4px;\n"
"	border: 0px;\n"
"}\n"
"\n"
"#home_page {\n"
"	background-color: #1e1e1e;\n"
"}\n"
"#setting_page {\n"
"	background-color: #1e1e1e;\n"
"}\n"
"#info_page {\n"
"	background-color: #1e1e1e;\n"
"}\n"
"\n"
"#stg_abt_pg{\n"
"	background-color: #1e1e1e;\n"
"}\n"
"\n"
"#stg_home_pg{\n"
"	background-color: #1e1e1e;\n"
"}\n"
"\n"
"#stg_app_pg{\n"
"	background-color: #1e1e1e;\n"
"}\n"
"\n"
"#topbar_frame .QPushButton {\n"
"	background-color: #202326;\n"
"}\n"
"\n"
"#gamebar_nav .QPushButton {\n"
"	background-color: #202326;	\n"
"}\n"
"\n"
"#stone_btn {\n"
"\n"
"	image: url(:/dark img/dark/img/stone.png);\n"
"\n"
"}\n"
"#paper_btn {\n"
"	\n"
"	\n"
"	image: url(:/dark img/dark/img/paper.png);\n"
"}\n"
"\n"
"#scissor_btn {\n"
"	\n"
"image: url(:/dark img/dark/img/scissor.png);\n"
"	\n"
"\n"
"}\n"
"\n"
"#result_lbl {\n"
"	font: 700 20pt \"Segoe Script\";\n"
"}\n"
"\n"
"#display_bar .QLabel{\n"
"	background-color: #202326;\n"
""
                        "}")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 7, 7, 7)
        self.leftMenu = QFrame(self.centralwidget)
        self.leftMenu.setObjectName(u"leftMenu")
        self.leftMenu.setMinimumSize(QSize(60, 0))
        self.leftMenu.setMaximumSize(QSize(50, 16777215))
        self.leftMenu.setStyleSheet(u"")
        self.verticalLayout = QVBoxLayout(self.leftMenu)
        self.verticalLayout.setSpacing(5)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(5, 5, 5, 5)
        self.menu_btn = QPushButton(self.leftMenu)
        self.menu_btn.setObjectName(u"menu_btn")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.menu_btn.sizePolicy().hasHeightForWidth())
        self.menu_btn.setSizePolicy(sizePolicy)
        self.menu_btn.setMaximumSize(QSize(16777215, 40))
        self.menu_btn.setStyleSheet(u"image-position : center")

        self.verticalLayout.addWidget(self.menu_btn)

        self.home_btn = QPushButton(self.leftMenu)
        self.home_btn.setObjectName(u"home_btn")
        sizePolicy.setHeightForWidth(self.home_btn.sizePolicy().hasHeightForWidth())
        self.home_btn.setSizePolicy(sizePolicy)
        self.home_btn.setMaximumSize(QSize(16777215, 40))
        self.home_btn.setStyleSheet(u"")

        self.verticalLayout.addWidget(self.home_btn)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.theme_btn = QPushButton(self.leftMenu)
        self.theme_btn.setObjectName(u"theme_btn")
        sizePolicy.setHeightForWidth(self.theme_btn.sizePolicy().hasHeightForWidth())
        self.theme_btn.setSizePolicy(sizePolicy)
        self.theme_btn.setMaximumSize(QSize(16777215, 40))
        self.theme_btn.setStyleSheet(u"")

        self.verticalLayout.addWidget(self.theme_btn)

        self.settings_btn = QPushButton(self.leftMenu)
        self.settings_btn.setObjectName(u"settings_btn")
        sizePolicy.setHeightForWidth(self.settings_btn.sizePolicy().hasHeightForWidth())
        self.settings_btn.setSizePolicy(sizePolicy)
        self.settings_btn.setMaximumSize(QSize(16777215, 40))
        self.settings_btn.setStyleSheet(u"")

        self.verticalLayout.addWidget(self.settings_btn)


        self.horizontalLayout.addWidget(self.leftMenu)

        self.mainFrame = QFrame(self.centralwidget)
        self.mainFrame.setObjectName(u"mainFrame")
        self.mainFrame.setStyleSheet(u"border-radius: 7px;")
        self.mainFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.mainFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.mainFrame)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.switchPage = QStackedWidget(self.mainFrame)
        self.switchPage.setObjectName(u"switchPage")
        self.switchPage.setStyleSheet(u"")
        self.home_page = QWidget()
        self.home_page.setObjectName(u"home_page")
        self.home_page.setStyleSheet(u"")
        self.verticalLayout_5 = QVBoxLayout(self.home_page)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.topbar_frame = QFrame(self.home_page)
        self.topbar_frame.setObjectName(u"topbar_frame")
        self.topbar_frame.setMinimumSize(QSize(0, 91))
        self.topbar_frame.setMaximumSize(QSize(16777215, 91))
        self.topbar_frame.setStyleSheet(u"")
        self.horizontalLayout_2 = QHBoxLayout(self.topbar_frame)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label = QLabel(self.topbar_frame)
        self.label.setObjectName(u"label")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy1)
        self.label.setStyleSheet(u"font: 600 30pt \"Segoe UI Variable Display Semib\";")

        self.horizontalLayout_2.addWidget(self.label)

        self.replay_btn = QPushButton(self.topbar_frame)
        self.replay_btn.setObjectName(u"replay_btn")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.MinimumExpanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.replay_btn.sizePolicy().hasHeightForWidth())
        self.replay_btn.setSizePolicy(sizePolicy2)
        self.replay_btn.setMinimumSize(QSize(150, 0))
        self.replay_btn.setStyleSheet(u"")

        self.horizontalLayout_2.addWidget(self.replay_btn)

        self.exit_btn = QPushButton(self.topbar_frame)
        self.exit_btn.setObjectName(u"exit_btn")
        sizePolicy2.setHeightForWidth(self.exit_btn.sizePolicy().hasHeightForWidth())
        self.exit_btn.setSizePolicy(sizePolicy2)
        self.exit_btn.setMinimumSize(QSize(150, 0))
        self.exit_btn.setStyleSheet(u"")

        self.horizontalLayout_2.addWidget(self.exit_btn)


        self.verticalLayout_5.addWidget(self.topbar_frame)

        self.mainbar_frame = QFrame(self.home_page)
        self.mainbar_frame.setObjectName(u"mainbar_frame")
        self.mainbar_frame.setStyleSheet(u"")
        self.verticalLayout_7 = QVBoxLayout(self.mainbar_frame)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.display_bar = QFrame(self.mainbar_frame)
        self.display_bar.setObjectName(u"display_bar")
        self.display_bar.setMinimumSize(QSize(650, 234))
        self.display_bar.setStyleSheet(u"")
        self.verticalLayout_8 = QVBoxLayout(self.display_bar)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.result_lbl = QLabel(self.display_bar)
        self.result_lbl.setObjectName(u"result_lbl")
        self.result_lbl.setMinimumSize(QSize(0, 35))
        self.result_lbl.setMaximumSize(QSize(16777215, 105))
        self.result_lbl.setStyleSheet(u"")
        self.result_lbl.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_8.addWidget(self.result_lbl)

        self.choices_bar = QFrame(self.display_bar)
        self.choices_bar.setObjectName(u"choices_bar")
        self.choices_bar.setMinimumSize(QSize(0, 200))
        self.choices_bar.setStyleSheet(u"\n"
"margin: 4px;")
        self.horizontalLayout_7 = QHBoxLayout(self.choices_bar)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.player_choice_lbl = QLabel(self.choices_bar)
        self.player_choice_lbl.setObjectName(u"player_choice_lbl")
        sizePolicy1.setHeightForWidth(self.player_choice_lbl.sizePolicy().hasHeightForWidth())
        self.player_choice_lbl.setSizePolicy(sizePolicy1)
        self.player_choice_lbl.setStyleSheet(u"")
        self.player_choice_lbl.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_7.addWidget(self.player_choice_lbl)

        self.vs_lbl = QLabel(self.choices_bar)
        self.vs_lbl.setObjectName(u"vs_lbl")
        self.vs_lbl.setMaximumSize(QSize(50, 16777215))
        self.vs_lbl.setStyleSheet(u"background-color: transparent;")
        self.vs_lbl.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_7.addWidget(self.vs_lbl)

        self.ai_choice_lbl = QLabel(self.choices_bar)
        self.ai_choice_lbl.setObjectName(u"ai_choice_lbl")
        sizePolicy1.setHeightForWidth(self.ai_choice_lbl.sizePolicy().hasHeightForWidth())
        self.ai_choice_lbl.setSizePolicy(sizePolicy1)
        self.ai_choice_lbl.setStyleSheet(u"")
        self.ai_choice_lbl.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_7.addWidget(self.ai_choice_lbl)


        self.verticalLayout_8.addWidget(self.choices_bar)


        self.verticalLayout_7.addWidget(self.display_bar)

        self.gamebar_nav = QFrame(self.mainbar_frame)
        self.gamebar_nav.setObjectName(u"gamebar_nav")
        self.gamebar_nav.setMaximumSize(QSize(16777215, 233))
        self.gamebar_nav.setStyleSheet(u"padding: 5px;")
        self.horizontalLayout_3 = QHBoxLayout(self.gamebar_nav)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.stone_btn = QPushButton(self.gamebar_nav)
        self.stone_btn.setObjectName(u"stone_btn")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.stone_btn.sizePolicy().hasHeightForWidth())
        self.stone_btn.setSizePolicy(sizePolicy3)
        self.stone_btn.setMaximumSize(QSize(209, 16777215))
        self.stone_btn.setStyleSheet(u"")

        self.horizontalLayout_3.addWidget(self.stone_btn)

        self.paper_btn = QPushButton(self.gamebar_nav)
        self.paper_btn.setObjectName(u"paper_btn")
        sizePolicy3.setHeightForWidth(self.paper_btn.sizePolicy().hasHeightForWidth())
        self.paper_btn.setSizePolicy(sizePolicy3)
        self.paper_btn.setMaximumSize(QSize(208, 16777215))
        self.paper_btn.setStyleSheet(u"")

        self.horizontalLayout_3.addWidget(self.paper_btn)

        self.scissor_btn = QPushButton(self.gamebar_nav)
        self.scissor_btn.setObjectName(u"scissor_btn")
        sizePolicy3.setHeightForWidth(self.scissor_btn.sizePolicy().hasHeightForWidth())
        self.scissor_btn.setSizePolicy(sizePolicy3)
        self.scissor_btn.setMaximumSize(QSize(209, 16777215))
        self.scissor_btn.setStyleSheet(u"")

        self.horizontalLayout_3.addWidget(self.scissor_btn)


        self.verticalLayout_7.addWidget(self.gamebar_nav)


        self.verticalLayout_5.addWidget(self.mainbar_frame)

        self.switchPage.addWidget(self.home_page)
        self.settings_page = QWidget()
        self.settings_page.setObjectName(u"settings_page")
        self.verticalLayout_4 = QVBoxLayout(self.settings_page)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.stg_lbl_v_frame_2 = QFrame(self.settings_page)
        self.stg_lbl_v_frame_2.setObjectName(u"stg_lbl_v_frame_2")
        self.stg_lbl_v_frame = QVBoxLayout(self.stg_lbl_v_frame_2)
        self.stg_lbl_v_frame.setSpacing(0)
        self.stg_lbl_v_frame.setObjectName(u"stg_lbl_v_frame")
        self.stg_lbl_v_frame.setContentsMargins(0, 0, 0, 0)
        self.stg_lbl_main = QLabel(self.stg_lbl_v_frame_2)
        self.stg_lbl_main.setObjectName(u"stg_lbl_main")
        self.stg_lbl_main.setMinimumSize(QSize(746, 43))
        self.stg_lbl_main.setMaximumSize(QSize(16777215, 43))

        self.stg_lbl_v_frame.addWidget(self.stg_lbl_main)

        self.setting_stackfrm = QStackedWidget(self.stg_lbl_v_frame_2)
        self.setting_stackfrm.setObjectName(u"setting_stackfrm")
        self.setting_stackfrm.setStyleSheet(u"")
        self.stg_home_pg = QWidget()
        self.stg_home_pg.setObjectName(u"stg_home_pg")
        self.setting_stackfrm.addWidget(self.stg_home_pg)
        self.stg_abt_pg = QWidget()
        self.stg_abt_pg.setObjectName(u"stg_abt_pg")
        self.verticalLayout_6 = QVBoxLayout(self.stg_abt_pg)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.setting_stackfrm.addWidget(self.stg_abt_pg)
        self.stg_app_pg = QWidget()
        self.stg_app_pg.setObjectName(u"stg_app_pg")
        self.setting_stackfrm.addWidget(self.stg_app_pg)

        self.stg_lbl_v_frame.addWidget(self.setting_stackfrm)


        self.verticalLayout_4.addWidget(self.stg_lbl_v_frame_2)

        self.switchPage.addWidget(self.settings_page)
        self.info_page = QWidget()
        self.info_page.setObjectName(u"info_page")
        self.verticalLayout_3 = QVBoxLayout(self.info_page)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.switchPage.addWidget(self.info_page)

        self.verticalLayout_2.addWidget(self.switchPage)


        self.horizontalLayout.addWidget(self.mainFrame)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.switchPage.setCurrentIndex(0)
        self.setting_stackfrm.setCurrentIndex(2)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
#if QT_CONFIG(tooltip)
        self.menu_btn.setToolTip(QCoreApplication.translate("MainWindow", u"Menu", None))
#endif // QT_CONFIG(tooltip)
        self.menu_btn.setText("")
#if QT_CONFIG(tooltip)
        self.home_btn.setToolTip(QCoreApplication.translate("MainWindow", u"Home", None))
#endif // QT_CONFIG(tooltip)
        self.home_btn.setText("")
#if QT_CONFIG(tooltip)
        self.theme_btn.setToolTip(QCoreApplication.translate("MainWindow", u"Theme", None))
#endif // QT_CONFIG(tooltip)
        self.theme_btn.setText("")
#if QT_CONFIG(tooltip)
        self.settings_btn.setToolTip(QCoreApplication.translate("MainWindow", u"Settings", None))
#endif // QT_CONFIG(tooltip)
        self.settings_btn.setText("")
        self.label.setText(QCoreApplication.translate("MainWindow", u"Score : 0", None))
        self.replay_btn.setText(QCoreApplication.translate("MainWindow", u"Replay", None))
        self.exit_btn.setText(QCoreApplication.translate("MainWindow", u"Exit", None))
        self.result_lbl.setText(QCoreApplication.translate("MainWindow", u"Yet to Begin", None))
        self.player_choice_lbl.setText("")
        self.vs_lbl.setText(QCoreApplication.translate("MainWindow", u"Vs", None))
        self.ai_choice_lbl.setText("")
        self.stone_btn.setText("")
        self.paper_btn.setText("")
        self.scissor_btn.setText("")
        self.stg_lbl_main.setText(QCoreApplication.translate("MainWindow", u"Settings", None))
    # retranslateUi

