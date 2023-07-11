import mysql.connector

class Banco(object):
    def conectar(self):
        self.db = mysql.connector.connect(db='vendas', host='localhost', port=3306,
                                  user='edilberto', password='beto1996')
        self.cur = self.db.cursor()

    def desconectar(self):
        self.cur.close()
        self.db.close()

class Venda(object):
    def __init__(self, id = 0, produto = "", vendedor = "", valUnitario = "", 
                 quantidade = "", unidade = ""):
        self.info = {}
        self.id = id
        self.produto = produto
        self.vendedor = vendedor
        self.valUnitario = valUnitario
        self.quantidade = quantidade
        self.unidade = unidade

    def inserirVenda(self):
        banco = Banco()
        banco.conectar()
        banco.cur.execute(
            "INSERT INTO venda (produto, vendedor, valUnitario, quantidade, " +
            "unidade, createdAt, updatedAt) values ('" +
            self.produto + "','" + self.vendedor + "', " +
            self.valUnitario + ", " + self.quantidade + ", '" + 
            self.unidade + "', NOW(), NOW())"
        )
        banco.commit()
        banco.desconectar()

    def selecionarvenda(self):
        banco = Banco()
        banco.conectar()
        banco.cur.execute(
            "SELECT produto, vendedor, valUnitario, quantidade, unidade " +
            "FROM venda WHERE id = " + str(self.id)
        )
        for linha in banco.cur:
            self.produto = linha[0]
            self.vendedor = linha[1]
            self.valUnitario = linha[2]
            self.quantidade = linha[3]
            self.unidade = linha[4]
        banco.desconectar        