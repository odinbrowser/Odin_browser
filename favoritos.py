import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
import sys
import sqlite3

from PyQt5.QtWidgets import *

from PyQt5 import uic

class favoritos(QWidget):
    def __init__(self):
        QMainWindow.__init__(self)
        uic.loadUi("layout/favoritos.ui", self)
        self.configTblFavoritos = self.tblFavoritos

        self.btnFavInserir.clicked.connect(self.inserirFavoritos)
        self.btnFavDeletarTodos.clicked.connect(self.deletarFavoritos)
        self.btnFavDeletar.clicked.connect(self.deletarItemFavoritos)
        self.btnFavAlterar.clicked.connect(self.alterarFavoritos)

    def men_erro(self, titulo, men1, men2):
        msg = QMessageBox()
        msg.setStyleSheet('''
            background-color: rgb(40,40,40);
            color: rgb(255,255,255);
            ''')
        msg.setIcon(QMessageBox.Critical)
        msg.setText(men1)
        msg.setWindowTitle(titulo)
        msg.setDetailedText(men2)
        msg.exec_()


    def alterarFavoritos(self):
        try:
            aux = self.tblFavoritos.currentItem().row()
            url = self.tblFavoritos.item(aux, 0).text()
            if self.txtFavUrl.text() != "":
                try:
                    conn = sqlite3.connect('bd.s3db')
                    cur = conn.cursor()
                    cur.execute(
                        "UPDATE tbFavoritos SET favUrl = '" + self.txtFavUrl.text() + "' WHERE favUrl = '" + url + "';")
                    conn.commit()
                except:
                    self.men_erro("ERRO", "Erro 016",
                                  "Erro ao alterar uma informação de favoritos, veja se arquivo bd.s3db se encontra no mesmo local do arquivo ODIN.exe, caso ele tenha sido alterado ou não estaja lá tente baixar outro software e copiar o arquivo dele ou então baixar outra versão do software, caso o problema persista tente contatar o administrador do produto.")
                conn.close()
                try:
                    self.tblFavoritos.setColumnCount(1)
                    self.tblFavoritos.setHorizontalHeaderLabels(['Url'])

                    self.conn_2 = sqlite3.connect('bd.s3db')
                    self.cur_2 = self.conn_2.cursor()
                    self.cur_2.execute("SELECT favUrl FROM tbFavoritos ORDER BY favUrl")
                    rows_2 = self.cur_2.fetchall()

                    while (self.tblFavoritos.rowCount() > 0):
                        self.tblFavoritos.removeRow(0)

                    for row in rows_2:
                        inx_2 = rows_2.index(row)
                        self.tblFavoritos.insertRow(inx_2)
                        self.tblFavoritos.setItem(inx_2, 0, QTableWidgetItem(row[0]))
                except:
                    self.men_erro("ERRO", "Erro 012",
                                  "Erro na seleção dos favoritos no banco de dados, veja se arquivo bd.s3db se encontra no mesmo local do arquivo ODIN.exe, caso ele tenha sido alterado ou não estaja lá tente baixar outro software e copiar o arquivo dele ou então baixar outra versão do software, caso o problema persista tente contatar o administrador do produto.")
                self.conn_2.close()
            else:
                self.men_erro("ERRO", "Erro", "Preencha o campo da Url.")
        except:
            self.men_erro("ERRO", "Erro", "Selecione um item da tabela")


    def deletarItemFavoritos(self):
        try:
            aux = self.tblFavoritos.currentItem().row()
            delet = self.tblFavoritos.item(aux, 0).text()
            try:
                conn = sqlite3.connect('bd.s3db')
                cur = conn.cursor()
                cur.execute("DELETE FROM tbFavoritos WHERE favUrl = '" + delet + "';")
                conn.commit()
            except:
                self.men_erro("ERRO", "Erro 014",
                              "Erro ao deletar uma informação de favoritos, veja se arquivo bd.s3db se encontra no mesmo local do arquivo ODIN.exe, caso ele tenha sido alterado ou não estaja lá tente baixar outro software e copiar o arquivo dele ou então baixar outra versão do software, caso o problema persista tente contatar o administrador do produto.")
            conn.close()

            try:
                self.tblFavoritos.setColumnCount(1)
                self.tblFavoritos.setHorizontalHeaderLabels(['Url'])

                self.conn_2 = sqlite3.connect('bd.s3db')
                self.cur_2 = self.conn_2.cursor()
                self.cur_2.execute("SELECT favUrl FROM tbFavoritos ORDER BY favUrl")
                rows_2 = self.cur_2.fetchall()

                while (self.tblFavoritos.rowCount() > 0):
                    self.tblFavoritos.removeRow(0)

                for row in rows_2:
                    inx_2 = rows_2.index(row)
                    self.tblFavoritos.insertRow(inx_2)
                    self.tblFavoritos.setItem(inx_2, 0, QTableWidgetItem(row[0]))
            except:
                self.men_erro("ERRO", "Erro 012",
                              "Erro na seleção dos favoritos no banco de dados, veja se arquivo bd.s3db se encontra no mesmo local do arquivo ODIN.exe, caso ele tenha sido alterado ou não estaja lá tente baixar outro software e copiar o arquivo dele ou então baixar outra versão do software, caso o problema persista tente contatar o administrador do produto.")
            self.conn_2.close()
        except:
            self.men_erro("ERRO", "Erro", "Selecione um item da tabela")


    def deletarFavoritos(self):
        try:
            conn = sqlite3.connect('bd.s3db')
            cur = conn.cursor()
            cur.execute("DELETE FROM tbFavoritos;")
            conn.commit()
        except:
            self.men_erro("ERRO", "Erro 013",
                          "Erro ao deletar as informações dos favoritos, veja se arquivo bd.s3db se encontra no mesmo local do arquivo ODIN.exe, caso ele tenha sido alterado ou não estaja lá tente baixar outro software e copiar o arquivo dele ou então baixar outra versão do software, caso o problema persista tente contatar o administrador do produto.")
        conn.close()

        try:
            self.tblFavoritos.setColumnCount(1)
            self.tblFavoritos.setHorizontalHeaderLabels(['Url'])

            self.conn_2 = sqlite3.connect('bd.s3db')
            self.cur_2 = self.conn_2.cursor()
            self.cur_2.execute("SELECT favUrl FROM tbFavoritos ORDER BY favUrl")
            rows_2 = self.cur_2.fetchall()

            while (self.tblFavoritos.rowCount() > 0):
                self.tblFavoritos.removeRow(0)

            for row in rows_2:
                inx_2 = rows_2.index(row)
                self.tblFavoritos.insertRow(inx_2)
                self.tblFavoritos.setItem(inx_2, 0, QTableWidgetItem(row[0]))
        except:
            self.men_erro("ERRO", "Erro 012",
                          "Erro na seleção dos favoritos no banco de dados, veja se arquivo bd.s3db se encontra no mesmo local do arquivo ODIN.exe, caso ele tenha sido alterado ou não estaja lá tente baixar outro software e copiar o arquivo dele ou então baixar outra versão do software, caso o problema persista tente contatar o administrador do produto.")
        self.conn_2.close()


    def inserirFavoritos(self):
        if self.txtFavUrl.text() != "":
            try:
                conn = sqlite3.connect('bd.s3db')
                cur = conn.cursor()
                cur.execute("INSERT INTO tbFavoritos VALUES(null, '" + self.txtFavUrl.text() + "')")
                conn.commit()
            except:
                self.men_erro("ERRO", "Erro 011",
                              "Erro ao inserir a informação em favoritos, veja se a url digitada já existe, veja se arquivo bd.s3db se encontra no mesmo local do arquivo ODIN.exe, caso ele tenha sido alterado ou não estaja lá tente baixar outro software e copiar o arquivo dele ou então baixar outra versão do software, caso o problema persista tente contatar o administrador do produto.")
            conn.close()

            try:
                self.tblFavoritos.setColumnCount(1)
                self.tblFavoritos.setHorizontalHeaderLabels(['Url'])

                self.conn_2 = sqlite3.connect('bd.s3db')
                self.cur_2 = self.conn_2.cursor()
                self.cur_2.execute("SELECT favUrl FROM tbFavoritos ORDER BY favUrl")
                rows_2 = self.cur_2.fetchall()

                while (self.tblFavoritos.rowCount() > 0):
                    self.tblFavoritos.removeRow(0)

                for row in rows_2:
                    inx_2 = rows_2.index(row)
                    self.tblFavoritos.insertRow(inx_2)
                    self.tblFavoritos.setItem(inx_2, 0, QTableWidgetItem(row[0]))
            except:
                self.men_erro("ERRO", "Erro 012",
                              "Erro na seleção dos favoritos no banco de dados, veja se arquivo bd.s3db se encontra no mesmo local do arquivo ODIN.exe, caso ele tenha sido alterado ou não estaja lá tente baixar outro software e copiar o arquivo dele ou então baixar outra versão do software, caso o problema persista tente contatar o administrador do produto.")
            self.conn_2.close()
        else:
            self.men_erro("ERRO", "Erro", "Preencha o campo da Url.")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    main = browser()
    main.show()
    sys.exit(app.exec_())