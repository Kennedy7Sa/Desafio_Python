import random


def buscar_regisro(termo, lista):
    if termo == 'todos':
        return lista
    else:
        return [
            pessoa for pessoa in lista
            if any(str(valor).lower()== termo for valor in pessoa.values())
        ]
    
if __name__ == '__main__':

    nomes = [
        {'id':1,'nome':'Kennedy','idade':32},
        {'id':2,'nome':'Sara','idade':31},
        {'id':3,'nome':'Laura','idade':3},    
    ]

    print('*'*40)
    print("Escolha sua opção")
    print("1 para listar todos os registros")
    print("2 para pesquisar")
    print("3 para cadastrar um novo registro")
    print("4 para atualizar um registro")
    print("5 excluir")
    print("0 para sair")
    print('*'*40)
    
    opcao = 30
    
    
    while opcao != 0:
        opcao = int(input('Digite sua opção '))
               
        if opcao == 1:
           termo = 'todos'
           resultado = buscar_regisro(termo,nomes)
           for item in resultado:
            print(item)
        
        elif( opcao == 2 ):
            termo = input('Digite o termo para pesquisa: ').strip().lower()
            resultado = buscar_regisro(termo,nomes)
            for pessoa in resultado:
                for c,v in pessoa.items():
                    print(f'{c}:{v}')  
        
        elif(opcao == 3):
            print('********* Novo Cadastro ************')
            id = random.randint(1,20)
            nome = input('Digite o nome: ')
            idade = input('Digite o idade: ')
            novo_registro = {'id':id,'nome':nome,'idade':idade}
            nomes.append(novo_registro)
            
            for item in nomes:
                print(item)
            
        elif(opcao == 4):
            termo = int(input('Digite o id do registro a ser atualizado: '))                   
                       
            nome = input('Digite o nome ')
            idade = int(input('Digite o idade '))
            
            for pessoa in nomes:
                if pessoa['id']==termo:
                    pessoa['nome'] = nome
                    pessoa['idade']=idade
        
        elif(opcao==5):
            termo = int(input('Digite o id a ser excluido')) 
            
            for pessoa in nomes:
                if pessoa['id']==termo:
                    nomes.remove(pessoa)
            
            for item in nomes:
                print(item) 
        else:
            opcao = 0 
            print('Programa encerrado')         
    