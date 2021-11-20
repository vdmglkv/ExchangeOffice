from PyQt5 import QtWidgets
from UI import MainWindow, Cheque, Client, Statistic, Settings, Courses
import sys


class mywindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(mywindow, self).__init__()
        self.ui = MainWindow.Ui_MainWindow()
        # self.ui = Settings.Ui_Settings()
        # self.ui = Client.Ui_Client()
        # self.ui = Cheque.Ui_Cheque()
        # self.ui = Statistic.Ui_Statistic()
        # self.ui = Courses.Ui_Courses()

        self.ui.setupUi(self)
        # self.ui.Password.setEchoMode(QtWidgets.QLineEdit.Password)


app = QtWidgets.QApplication([])
application = mywindow()
application.show()

sys.exit(app.exec())
