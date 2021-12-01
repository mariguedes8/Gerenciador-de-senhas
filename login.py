from PyQt5 import uic, QtWidgets
import sqlite3


def chama_segunda_tela():
    primeira_tela.label_4.setText("")
    nome_usuario = primeira_tela.lineEdit.text()
    senha = primeira_tela.lineEdit_2.text()
    if nome_usuario == "Mari" and senha == "123456":
        primeira_tela.close()
        segunda_tela.show()
    else:
        primeira_tela.label_4.setText("Dados de login incorretos!")


def logout():
    segunda_tela.close()
    primeira_tela.show()


def abre_tela_cadastro():
    tela_cadastro.show()

def abre_tela_senhas():
    tela_mostraSenhas.show()

    cursor3 = banco2.cursor()
    comando_SQL = "SELECT * FROM cadastroSenha"
    cursor3.execute(comando_SQL)
    dados_lidos = cursor3.fatchall()


    tela_mostraSenhas.tableWidget.setRowCount(len(dados_lidos))
    tela_mostraSenhas.tableWidget.setcolunmCount(3)


def cadastrar():
    nome = tela_cadastro.lineEdit.text()
    login = tela_cadastro.lineEdit_2.text()
    senha = tela_cadastro.lineEdit_3.text()
    c_senha = tela_cadastro.lineEdit_4.text()

    if (senha == c_senha):
        try:
            banco = sqlite3.connect('banco_cadastro.db')
            cursor = banco.cursor()
            cursor.execute("CREATE TABLE IF NOT EXISTS cadastro (nome text,login text,senha text)")
            cursor.execute("INSERT INTO cadastro VALUES ('" + nome + "','" + login + "','" + senha + "')")

            banco.commit()
            banco.close()
            tela_cadastro.label.setText("Usuario cadastrado com sucesso")

        except sqlite3.Error as erro:
            print("Erro ao inserir os dados: ", erro)
    else:
        tela_cadastro.label.setText("As senhas digitadas estão diferentes")

def cadastrarSenha():
    aplicacao = segunda_tela.lineEdit.text()
    senha = segunda_tela.lineEdit_3.text()
    categoria = ""

    if segunda_tela.radioButton.isChecked():
        categoria = "Pessoal"
    else:
        categoria = "Profissional"

    banco2 = sqlite3.connect('banco_cadastro.db')
    cursor2 = banco2.cursor()
    cursor2.execute("CREATE TABLE IF NOT EXISTS cadastroSenha (aplicacao text,senha text,categoria text)")
    cursor2.execute("INSERT INTO cadastroSenha VALUES ('" + aplicacao + "','" + senha + "','" + categoria + "')")

    banco.commit()
    banco.close()
    segunda_tela.label_5.setText("Senha cadastrada com sucesso!")





app=QtWidgets.QApplication([])
primeira_tela = uic.loadUi("primeira_tela.ui")
segunda_tela = uic.loadUi("segunda_tela.ui")
tela_cadastro = uic.loadUi("tela_cadastro.ui")
tela_mostraSenhas = uic.loadUi("tela_mostraSenhas.ui")

primeira_tela.pushButton.clicked.connect(chama_segunda_tela)

segunda_tela.pushButton.clicked.connect(logout)
segunda_tela.pushButton_4.clicked.connect(cadastrarSenha)
segunda_tela.pushButton_3.clicked.connect(abre_tela_senhas)

primeira_tela.lineEdit_2.setEchoMode(QtWidgets.QLineEdit.Password)
primeira_tela.pushButton_2.clicked.connect(abre_tela_cadastro)

tela_cadastro.pushButton_2.clicked.connect(cadastrar)


primeira_tela.show()
app.exec()
