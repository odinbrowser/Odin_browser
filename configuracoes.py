'''
Favoritos: Ir
Historico: Ir
'''

# -*- coding: utf-8 -*-

import sys
import os.path
import sqlite3

from PyQt5.QtWidgets import *

from PyQt5 import uic

from download import Dialogo

class configuracoes(QWidget):

    def __init__(self):
        QWidget.__init__(self)
        uic.loadUi("layout/configuracoes.ui",self)
        self.configTblHistorico = self.tblHistorico
        
        self.btnGerPadrao.clicked.connect(self.paginaPadrao)
        self.btnGerAlterar.clicked.connect(self.alterarHomePage)
        self.btnGerDownload.clicked.connect(self.chamar_download)
        self.btnGerLeiame.clicked.connect(self.ajuda_download)
        self.btnHisDeletar.clicked.connect(self.deletarItemHistorico)
        self.btnHisDeletarTodos.clicked.connect(self.deletarHistorico)

        self.down = Dialogo()

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

    def chamar_download(self):
        self.down.show()

    def ajuda_download(self):
        os.startfile("Download.txt")

    def deletarItemHistorico(self):
        try:
            aux = self.tblHistorico.currentItem().row()
            delet = self.tblHistorico.item(aux, 0).text()
            try:
                conn = sqlite3.connect('bd.s3db')
                cur = conn.cursor()
                cur.execute("DELETE FROM tbHistorico WHERE hisUrl = '" + delet + "';")
                conn.commit()
            except:
                self.men_erro("ERRO", "Erro 015", "Erro ao deletar uma informação de historico, veja se arquivo bd.s3db se encontra no mesmo local do arquivo ODIN.exe, caso ele tenha sido alterado ou não estaja lá tente baixar outro software e copiar o arquivo dele ou então baixar outra versão do software, caso o problema persista tente contatar o administrador do produto.")
            conn.close()

            try:
                self.tblHistorico.setColumnCount(2)
                self.tblHistorico.setHorizontalHeaderLabels(['Url', 'Data'])

                self.conn_1 = sqlite3.connect('bd.s3db')
                self.cur_1 = self.conn_1.cursor()
                self.cur_1.execute("SELECT hisUrl, hisData FROM tbHistorico ORDER BY hisID DESC")
                rows_1 = self.cur_1.fetchall()

                while (self.tblHistorico.rowCount() > 0):
                    self.tblHistorico.removeRow(0)

                for row in rows_1:
                    inx_1 = rows_1.index(row)
                    self.tblHistorico.insertRow(inx_1)

                    self.tblHistorico.setItem(inx_1, 0, QTableWidgetItem(row[0]))
                    self.tblHistorico.setItem(inx_1, 1, QTableWidgetItem(row[1]))
            except:
                self.men_erro("ERRO", "Erro 002", "Erro na seleção do histórico no banco de dados, veja se arquivo bd.s3db se encontra no mesmo local do arquivo ODIN.exe, caso ele tenha sido alterado ou não estaja lá tente baixar outro software e copiar o arquivo dele ou então baixar outra versão do software, caso o problema persista tente contatar o administrador do produto.")
            self.conn_1.close()
        except:
            self.men_erro("ERRO", "Erro", "Selecione um item da tabela.")

    def deletarHistorico(self):
        try:
            conn = sqlite3.connect('bd.s3db')
            cur = conn.cursor()
            cur.execute("DELETE FROM tbHistorico;")
            conn.commit()
        except:
            self.men_erro("ERRO", "Erro 010", "Erro ao deletar as informações do histórico, veja se arquivo bd.s3db se encontra no mesmo local do arquivo ODIN.exe, caso ele tenha sido alterado ou não estaja lá tente baixar outro software e copiar o arquivo dele ou então baixar outra versão do software, caso o problema persista tente contatar o administrador do produto.")
        conn.close()

        try:
            self.tblHistorico.setColumnCount(2)
            self.tblHistorico.setHorizontalHeaderLabels(['Url', 'Data'])

            self.conn_1 = sqlite3.connect('bd.s3db')
            self.cur_1 = self.conn_1.cursor()
            self.cur_1.execute("SELECT hisUrl, hisData FROM tbHistorico ORDER BY hisID DESC")
            rows_1 = self.cur_1.fetchall()

            while (self.tblHistorico.rowCount() > 0):
                self.tblHistorico.removeRow(0)

            for row in rows_1:
                inx_1 = rows_1.index(row)
                self.tblHistorico.insertRow(inx_1)

                self.tblHistorico.setItem(inx_1, 0, QTableWidgetItem(row[0]))
                self.tblHistorico.setItem(inx_1, 1, QTableWidgetItem(row[1]))
        except:
            self.men_erro("ERRO", "Erro 002", "Erro na seleção do histórico no banco de dados, veja se arquivo bd.s3db se encontra no mesmo local do arquivo ODIN.exe, caso ele tenha sido alterado ou não estaja lá tente baixar outro software e copiar o arquivo dele ou então baixar outra versão do software, caso o problema persista tente contatar o administrador do produto.")
        self.conn_1.close()
    
    def paginaPadrao(self):
        try:
            conn = sqlite3.connect("bd.s3db")
            cur = conn.cursor()
            cur.execute("UPDATE tbHomePage SET hpgUrl = 'paginaInicialRequisitada' WHERE hpgID = 1")
            conn.commit()
            msg = QMessageBox()
            msg.setStyleSheet('''
                background-color: rgb(40,40,40);
                color: rgb(255,255,255);
                ''')
            msg.setText("Sucesso ao alterar para a página padrão")
            msg.setWindowTitle("SUCESSO")
            msg.exec_()
        except:
            self.men_erro("ERRO", "Erro 008", "Erro ao atualizar a página inicial para a padrão, tente utilizar outra versão do software, caso o problema persista tente contatar o administrador do produto.")
        conn.close()
        
    def alterarHomePage(self):
        if self.txtGerHomePage.text() == "":
            self.men_erro("ERRO", "Erro", "Digite uma URL na caixa de texto.")
        else:
            homePage = str(self.txtGerHomePage.text())
            try:
                conn = sqlite3.connect("bd.s3db")
                cur = conn.cursor()
                cur.execute("UPDATE tbHomePage SET hpgUrl = '" + homePage + "' WHERE hpgID = 1")
                conn.commit()
                msg = QMessageBox()
                msg.setStyleSheet('''
                        background-color: rgb(40,40,40);
                        color: rgb(255,255,255);
                        ''')
                msg.setText("Sucesso ao alterar a página inicial")
                msg.setWindowTitle("SUCESSO")
                msg.exec_()
            except:
                self.men_erro("ERRO", "Erro 009", "Erro ao atualizar a página inicial para a solicitada pelo usuário, verifique se a url está correta, caso o problema persista tente utilizar outra versão do software ou contatar o administrador do produto.")
            conn.close()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main = configuracoes()
    main.show()
    sys.exit(app.exec_())
