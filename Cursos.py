#========menu========#
import mysql.connector
def cadastrar_assuntos(): 
    nome = input('digite o nome do assunto: ')
    mydb = mysql.connector.connect(
      host="localhost",
      user="root",
      password="",
      database="cursos"
    )

    mycursor = mydb.cursor()

    sql = "INSERT INTO assuntos (nome) VALUES (%s)"
    val = (nome,) 
      
    mycursor.execute(sql,val) 
    mydb.commit() 
      
    print(mycursor.rowcount, "details inserted") 
    mydb.close() 



def listar_assuntos():
    mydb = mysql.connector.connect(
      host="localhost",
      user="root",
      password="",
      database="cursos"
    )

    mycursor = mydb.cursor()

    mycursor.execute("SELECT * FROM assuntos")

    myresult = mycursor.fetchall()
    
    print('{:^10} | {:^10}'.format('ID', 'Nome'))
    for id, nome in myresult:
        print('{:^10} | {:^10}'.format(id, nome))
    





def alterar_assuntos():
    nome = input('digite o nome do assuntos: ')
    update = int(input('Qual o id que você deseja atualizar os dados? '))

    mydb = mysql.connector.connect(
      host="localhost",
      user="root",
      password="",
      database="cursos"
    )

    mycursor = mydb.cursor()

    sql = "UPDATE assuntos SET nome = %s WHERE id = %s"
    val = (nome, update)
      
    mycursor.execute(sql, val) 
    mydb.commit() 
      
    print(mycursor.rowcount, "details inserted") 
    mydb.close() 

     
def apagar_assuntos():
    print('Os dados disponiveis para serem deletados são:\n')
    listar_assuntos()
    id = int(input('\nQuais dados você deseja apagar? selecione um ID: '))
    print("\nInformações com ID {} foram deletadas com sucesso!\nTabela atualizada com sucesso!\n".format(id))
    mydb = mysql.connector.connect(
      host="localhost",
      user="root",
      password="",
      database="cursos"
    )

    mycursor = mydb.cursor()

    sql = "DELETE FROM assuntos WHERE id = %s"
    val = (id,)

    mycursor.execute(sql,val)

    mydb.commit()

    print(mycursor.rowcount, "record(s) deleted")
    
    
def sair():
    print("Saindo...")

#####################################
#############menuu_cursos############
#####################################
def cadastrar_cursos(): 
    nome = input('digite o nome do curso: ')
    link = input('cadastre o novo link: ')
    print('Os assuntos disponiveis são:\n')
    listar_assuntos()
    id_assunto = int(input('\nSelecione um ID: '))
    mydb = mysql.connector.connect(
      host="localhost",
      user="root",
      password="",
      database="cursos"
    )

    mycursor = mydb.cursor()

    sql = "INSERT INTO cursos (nome, link, id_assunto) VALUES (%s, %s, %s)"
    val = (nome, link, id_assunto) 
      
    mycursor.execute(sql, val) 
    mydb.commit() 
      
    print(mycursor.rowcount, "details inserted") 
    mydb.close() 

def listar_cursos():
    mydb = mysql.connector.connect(
      host="localhost",
      user="root",
      password="",
      database="cursos"
    )

    mycursor = mydb.cursor()

    mycursor.execute("select cursos.id, cursos.nome, assuntos.nome, cursos.link from cursos left join assuntos on id_assunto = assuntos.id;")

    myresult = mycursor.fetchall()

    #for x in myresult:
        #print(x)
    print('{:^10} | {:^30} | {:^30} | {:^30}'.format('ID', 'Nome','Assunto','LINK'))
    for id, nome, id_assunto, link in myresult:
        print('{:^10} | {:^30} | {:^30} | {:^30}'.format(str(id), nome, str(id_assunto), link))
    
        
   
    
def alterar_cursos():
    nome = input('Digite o novo nome do curso: ')
    link = input("Registre um novo link para '{}': ".format(nome))
    update = int(input('Qual id que você deseja atualizar os dados? '))
    mydb = mysql.connector.connect(
      host="localhost",
      user="root",
      password="",
      database="cursos"
    )

    mycursor = mydb.cursor()

    sql = "UPDATE cursos SET nome = %s, link = %s WHERE id = %s"
    val = (nome, link, update)
      
    mycursor.execute(sql, val) 
    mydb.commit() 
      
    print(mycursor.rowcount, "details inserted") 
    mydb.close() 
    
    
    
    
def apagar_cursos():
        
        print('Os dados disponiveis para serem deletados são:\n')
        listar_cursos()
        id = int(input('\nQuais dados você deseja apagar? selecione um ID: '))
        print("\nInformações com ID {} foram deletadas com sucesso!\nTabela atualizada com sucesso!\n".format(id))
        mydb = mysql.connector.connect(
          host="localhost",
          user="root",
          password="",
          database="cursos"
        )

        mycursor = mydb.cursor()

        sql = "DELETE FROM cursos WHERE id = %s"
        val = (id,)

        mycursor.execute(sql,val)

        mydb.commit()

        print(mycursor.rowcount, "record(s) deleted")
    
def sair():
    print("Saindo...")


#######################################
########### def do segundo menu########
#######################################



def menuu_cursos():
    enter = input("\n===============================================\nTabela selecionada com sucesso!!\nPress Enter..\n===============================================\n")
    while True:
        menu = input("\n================\nTabela Cursos\n================\n1-Cadastrar\n2-Listar\n3-Alterar\n4-Apagar\n5-Sair\n")

        if menu =='1':
            cadastrar_cursos()
   
        elif menu =='2':
            listar_cursos()
     
        elif menu =='3':
            alterar_cursos()
        
        elif menu =='4':
             apagar_cursos()
         
        elif menu =='5':
            sair()
            break      
         
        else:
            print("\nerror")




def menuu():
    enter = input("\n===============================================\nTabela selecionada com sucesso!!\nPress Enter..\n===============================================\n")
    while True:
        
        menu = input("\n================\nTabela Assuntos\n================\n1-Cadastrar\n2-Listar\n3-Alterar\n4-Apagar\n5-Sair\n")

        if menu =='1':
            cadastrar_assuntos()
         
        elif menu =='2':
            listar_assuntos()
             
        elif menu =='3':
            alterar_assuntos()
                
        elif menu =='4':
            apagar_assuntos()
                 
        elif menu =='5':
            sair()
            break      
                 
        else:
            print("\nerror")
        
#primeiro menu#
            
while True:
    menu2 = input("Qual tabela você deseja acessar?\nDigite....\n1- Assuntos\n2- Cursos\n3- Sair\n")
    if menu2 =='1':
        menuu()
   
    elif menu2 =='2':
        menuu_cursos()

    elif menu2 =='3':
        print("Saindo.....\n==========================================\nObrigado por utilizar o nosso Programa :)\n==========================================\n")
        break
    else:
        print('\n\nERRO, OPÇÃO INVÁLIDA....\n\n')






############################################

