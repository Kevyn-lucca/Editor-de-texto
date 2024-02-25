from PyQt5.QtWidgets import *
from PyQt5.QtGui import QFont
from PyQt5 import uic


class MyGUI(QMainWindow):
    
    def __init__(self):
        super(MyGUI,self).__init__()
        uic.loadUi('Editor.ui',self)
        self.show()

        self.setWindowTitle("Editor de texto")
        self.action12x.triggered.connect(lambda: self.mudar_tamanho(12))
        self.action24x.triggered.connect(lambda: self.mudar_tamanho(24))
        self.action32x.triggered.connect(lambda: self.mudar_tamanho(32))

        self.actionOpen.triggered.connect(self.abrir_arquivo)
        self.actionSave.triggered.connect(self.salvar_arquivo)
        self.actionClose.triggered.connect(exit)
        
    def mudar_tamanho(self,size):
        self.plainTextEdit.setFont(QFont("Arial", size))
    
    def abrir_arquivo(self):
        options = QFileDialog.Options()
        filename, _ = QFileDialog.getOpenFileName(self, "Open File", "", "Text Files (*.txt);;Python File (*.py)", options=options)
        if filename != "":
            with open(filename, "r") as f:
                self.plainTextEdit.setPlainText(f.read())

    def salvar_arquivo(self):
        options = QFileDialog.Options()
        filename, _= QFileDialog.getSaveFileName(self, "save file", "", "Text Files (*.txt);;ALL FILES(*)", options=options)
        if filename != "":
            with open(filename, "w") as f:
                f.write(self.plainTextEdit.toPlainText())

    def closeEvent(self,event):
        dialog = QMessageBox()
        dialog.setText("Deseja salvar o arquivo?")
        dialog.addButton(QPushButton("Sim"), QMessageBox.YesRole)
        dialog.addButton(QPushButton("Não"), QMessageBox.NoRole)
        dialog.addButton(QPushButton("Cancelar"), QMessageBox.RejectRole)

        answer = dialog.exec_()

        if answer == 0:
            self.salvar_arquivo()
            event.accept()
        elif answer == 2:
            event.ignore()




def main():
    app =  QApplication([])
    window = MyGUI()
    app.exec_()

if __name__ == '__main__':
    main()