from PySide6.QtWidgets import QWidget, QMessageBox
from PySide6.QtGui import QCloseEvent


class BasicWindow(QWidget):

    def quitEvent(self, event: QCloseEvent):
        reply = QMessageBox.question(self, 'Message', 'Etes-vous sur de vouloir quitter ?',
                                     QMessageBox.Yes | QMessageBox.No, QMessageBox.No)

        if reply == QMessageBox.Yes:
            self.close()
        else:
            event.ignore()

    def refresh(self):
        pass
