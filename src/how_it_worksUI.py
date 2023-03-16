# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'how_it_works.ui'
##
## Created by: Qt User Interface Compiler version 6.3.1
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
from PySide6.QtWidgets import (QApplication, QFrame, QMainWindow, QMenuBar,
    QPushButton, QSizePolicy, QStatusBar, QTextEdit,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(661, 508)
        MainWindow.setMinimumSize(QSize(661, 508))
        MainWindow.setMaximumSize(QSize(661, 508))
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.textEdit = QTextEdit(self.centralwidget)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setGeometry(QRect(30, 20, 601, 381))
        self.textEdit.setFrameShape(QFrame.Box)
        self.textEdit.setFrameShadow(QFrame.Sunken)
        self.textEdit.setReadOnly(True)
        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(560, 430, 75, 31))
        self.pushButton_2 = QPushButton(self.centralwidget)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(30, 430, 181, 31))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 661, 21))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.textEdit.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"justify\" style=\" margin-top:18px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">LEACHABILITY</span></p>\n"
"<p align=\"justify\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">The leachability concept which is implemented in this tool represents an advanced way to estimate mobility. Leachability is defined as the predicted potential of a chemical to leach through an unsaturated soil profile of 1 m thickness under worst-case pedo-climatic boundary conditions [1]. Adsorption to soil (Koc) combined with degrada"
                        "tion in the soil matrix (DegT50 according to [2]) were considered as the main drivers for the transport of substances through soil. Based on the percentage of the substance leached to a soil depth of 1 m as a f unction of the substance amount at the soil surface the following metric for mobility is proposed</p>\n"
"<p align=\"justify\" style=\"-qt-paragraph-type:empty; margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:8pt;\"><br /></p>\n"
"<table border=\"0\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px;\" cellspacing=\"2\" cellpadding=\"0\"><thead>\n"
"<tr>\n"
"<td>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">Percentage   </span></p></td>\n"
"<td>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-inde"
                        "nt:0px;\"><span style=\" font-weight:600;\">Mobility</span></p></td>\n"
"<td></td></tr></thead>\n"
"<tr>\n"
"<td>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">&lt; 1 %</p></td>\n"
"<td>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">not mobile</p></td>\n"
"<td></td></tr>\n"
"<tr>\n"
"<td>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">1 % - 10 %</p></td>\n"
"<td>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">mobile</p></td>\n"
"<td></td></tr>\n"
"<tr>\n"
"<td>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\""
                        ">&gt; 10 %</span></p></td>\n"
"<td>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">very mobile</p></td>\n"
"<td></td></tr></table>\n"
"<p align=\"justify\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:8pt;\"><br /></p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">The leaching is calculated with the freely available FOCUS-PELMO 6.6.4 [3] for a set of 41 DT50 by 21 KOC combinations (861 combinations). This is done for the 9 locations defined in the FOCUS framework [1,4] for a simulated time of 120 years. For each location the 80th percentile of annual percentage leached mass at a depth of 100 cm is calculated and the average over all locations is taken. The table containing the resultin"
                        "g leaching percentages is stored in lookup_table.txt and can be obtained via pressing the button &quot;Copy Lookup Table to Clipboard&quot;.</span></p>\n"
"<p align=\"justify\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">If a combination of input parameters is not represented in the lookup table an interpolation is performed. This is done with the RectBivariateSpline function from the python3 module scipy.interpolate [5].</span></p>\n"
"<p align=\"justify\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">[1] FOCUS (2000) \u201cFOCUS groundwater scenarios in the EU review of active substances\u201d Report of the FOCUS Groundwater  cenarios Workgroup, EC Document Reference Sanco/321/2000 rev.2, 202pp.</span></p>\n"
"<p align=\"justify\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margi"
                        "n-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">[2] European Food Safety Authority, 2014. EFSA Guidance Document for evaluating laboratory and field dissipation studies to obtain DegT50 values of active substances of plant protection products and transformation products of these active substances in soil. EFSA Journal 2014;12(5):3662, 37 pp., doi:10.2903/j.efsa.2014.3662</span></p>\n"
"<p align=\"justify\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">[3] Klein M., </span><span style=\" font-family:'sans-serif'; font-size:8pt;\">Thomas K., Trapp M., Guerniche D.</span><span style=\" font-size:8pt;\"> (2016), publication: </span><a href=\"http://www.umweltbundesamt.de/publikationen\"><span style=\" font-size:8pt; text-decoration: underline; color:#0000ff;\">http://www.umweltbundesamt.de/publikationen</span></a><a href=\"http://www.umweltbundesamt.de/publikationen\"><span "
                        "style=\" font-size:8pt; text-decoration: underline; color:#000000;\">, Download: </span></a><a href=\"https://esdac.jrc.ec.europa.eu/projects/pelmo\"><span style=\" font-size:8pt; text-decoration: underline; color:#0000ff;\">https://esdac.jrc.ec.europa.eu/projects/pelmo</span></a></p>\n"
"<p align=\"justify\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">[4] European Commission (2014) \u201cAssessing Potential for Movement of Active Substances and their Metabolites to Ground Water in the EU\u201d Report of the FOCUS Ground Water Work Group, EC Document Reference Sanco/13144/2010 version 3, 613 pp.</p>\n"
"<p align=\"justify\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">[5] Pauli Virtanen, Ralf Gommers, Travis E. Oliphant, Matt Haberland, Tyler Reddy, David Cournapeau, Evgeni Burovski, Pearu Peterson, Warren Weckesser, Jonathan Brig"
                        "ht, St\u00e9fan J. van der Walt, Matthew Brett, Joshua Wilson, K. Jarrod Millman, Nikolay Mayorov, Andrew R. J. Nelson, Eric Jones, Robert Kern, Eric Larson, CJ Carey, \u0130lhan Polat, Yu Feng, Eric W. Moore, Jake VanderPlas, Denis Laxalde, Josef Perktold, Robert Cimrman, Ian Henriksen, E.A. Quintero, Charles R Harris, Anne M. Archibald, Ant\u00f4nio H. Ribeiro, Fabian Pedregosa, Paul van Mulbregt, and SciPy 1.0 Contributors. (2020) SciPy 1.0: Fundamental Algorithms for Scientific Computing in Python. </span><span style=\" font-size:8pt; font-style:italic;\">Nature Methods</span><span style=\" font-size:8pt;\">, 17(3), 261-272. </span></p>\n"
"<p align=\"justify\" style=\" margin-top:18px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt; font-weight:600;\">USAGE</span></p>\n"
"<p align=\"justify\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">The substance name a"
                        "nd the corresponding set of values for Koc and DegT50 need to be entered into the appropriate input fields. Alternatively, the up- and down arrows can be used. A condensed<span style=\" font-size:8pt;\"> result is output in the text field box which is updated whenever the input parameters are changed. The result can be copied with the &quot;Copy to Clipboard&quot;-button and pasted into any text editor of choice. </span></p>\n"
"<p align=\"justify\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">Based on the lookup-table and the interpolation method a contour plot is created representing the three mobility classes as function of Koc and DT50. The mobility class of the respective substance is maked with a cross which is updated whenever the input changes.The figure can be saved as a PNG, JPG or PDF file with the &quot;Save Figure&quot;-button.</span></p>\n"
"<p align=\"justify\" style=\" margin-top:18px; mar"
                        "gin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt; font-weight:600;\">BUG REPORTS</span></p>\n"
"<p align=\"justify\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">For reporting bugs, asking questions, giving remarks and suggestions, we welcome you to use the issue tracker: https://github.com/IMEDiman/LeachCalc/issues</span></p>\n"
"<p align=\"justify\" style=\" margin-top:18px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt; font-weight:600;\">CONTACT</span></p>\n"
"<p align=\"justify\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">Dimitrios Skodras - dimitrios.skodras@ime.fraunhofer.de</span></p>\n"
"<p align=\"justify\" style=\" margin-top:12px; margin-bot"
                        "tom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">Project link: https://github.com/IMEDiman/LeachCalc</span></p>\n"
"<p align=\"justify\" style=\" margin-top:18px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt; font-weight:600;\">CREDITS</span></p>\n"
"<p align=\"justify\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">The author thanks Michael Klein, Judith Klein and Bernhard Jene for support and fruitful discussions. This project was financed by CropLife Europe in B-1040 Brussels, BELGIUM</span></p>\n"
"<p align=\"justify\" style=\" margin-top:18px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt; font-weight:600;\">LICENCE</span></p>\n"
"<p align=\"justify\" style=\" margin-top:12px; margin"
                        "-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">This project is licensed under GNU General Public License. A version of it should be shipped with this file. If not, you can find the text here:</span><a href=\" https://www.gnu.org/licenses/gpl-3.0.en.html\"><span style=\" font-size:8pt; text-decoration: underline; color:#0000ff;\">https://www.gnu.org/licenses/gpl-3.0.en.html</span></a></p></body></html>", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Close", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"Copy Lookup Table to Clipboard", None))
    # retranslateUi

