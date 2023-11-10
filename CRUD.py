import os
import mysql.connector

def conectarBD(host, usuario, senha, DB):
    cnx = mysql.connector.connect(user=usuario, 
                                  password=senha,
                                  host=host,
                                  database=DB
                                )
    return cnx

def insertBD(nomeCliente, rgCliente, cpfCliente, endereçoCliente, cidadeCliente, ufCliente, conn):
    connection = conn
    cursor = connection.cursor()

    sql = "INSERT INTO Cliente (nomeCliente, rgCliente, cpfCliente, endereçoCliente, cidadeCliente, ufCliente)" + "VALUES(%s, %s, %s, %s, %s, %s)"
    data = (
        nomeCliente,
        rgCliente,
        cpfCliente,
        endereçoCliente,
        cidadeCliente,
        ufCliente,
    )
    cursor.execute(sql, data)
    connection.commit()

    cliente_id = cursor.lastrowid
    cursor.close()
    connection.close()
    print(f'Foi cadastrado o novo cliente de ID: {cliente_id}')

def readBD(conn):
    connection = conn
    cursor = connection.cursor()


    sql = "SELECT * FROM Cliente"
    cursor.execute(sql)
    results = cursor.fetchall()
    cursor.close()
    connection.close()
    
    for result in results:
        print(result)

def updateBD(nomeCliente, endereçoCliente, cidadeCliente, ufCliente, id, conn):
    connection = conn
    cursor = connection.cursor()

    sql = "UPDATE Cliente SET nomeCliente=%s, endereçoCliente=%s, cidadeCliente=%s, ufCliente=%s" + "WHERE id=%s"
    data = (
        nomeCliente,
        endereçoCliente,
        cidadeCliente,
        ufCliente,
        id
    )
    cursor.execute(sql, data)
    connection.commit()
    recordsAffected = cursor.rowcount
    cursor.close()
    connection.close()
    print(recordsAffected, " Registros afetados.")

def deleteBD(id, conn):
    connection = conn
    cursor = connection.cursor()

    sql = "DELETE FROM Cliente WHERE id=%s"

    data = (id,)
    cursor.execute(sql, data)
    connection.commit()
    recordsAffected = cursor.rowcount
    cursor.close()
    connection.close()
    print(recordsAffected, " Registros deletados.")

while True:
    print("GERENCIADOR DE CADASTRO DE CLIENTES".center(60, ":"))
    print('''
    1 - Cadastrar Cliente
    2 - Exibir Cadastros
    3 - Alterar Cadastros
    4 - Deletar Cadastros
    5 - Sair
''')
    opcao = input('Insira a opção desejada: ')
    if opcao == '1':
        nomeCliente = input('Insira o nome completo do cliente: ')
        rgCliente = input('Insira o rg do cliente: ')
        cpfCliente = input('Insira o cpf do cliente: ')
        endereçoCliente = input('Insira o endereço do cliente: ')
        cidadeCliente = input('Insira a cidade do cliente: ')
        ufCliente = input('Insira o estado do cliente: ')

        connection = conectarBD('localhost', 'root', 'admin', 'projeto')
        insertBD(nomeCliente, rgCliente, cpfCliente, endereçoCliente, cidadeCliente, ufCliente, connection)
    
    elif opcao == '2':
        connection = conectarBD('localhost', 'root', 'admin', 'projeto')
        readBD(connection)

    elif opcao == '3':
        id = input('Insira o ID do cliente que deseja alterar os dados: ')
        nomeCliente = input('Insira o nome do cliente: ')
        endereçoCliente = input('Insira o endereço do cliente: ')
        cidadeCliente = input('Insira a cidade do cliente: ')
        ufCliente = input('Insira o estado do cliente: ')
        connection = conectarBD('localhost', 'root', 'admin', 'projeto')
        updateBD(nomeCliente, endereçoCliente, cidadeCliente, ufCliente, id, connection)

    elif opcao == '4':
        idCliente = input('Insira o ID do cliente que deseja deletar os dados: ')
        connection = conectarBD('localhost', 'root', 'admin', 'projeto')
        deleteBD(idCliente, connection)

    elif opcao == '5':
        print('\n\nFechando.')
        quit()
    break
