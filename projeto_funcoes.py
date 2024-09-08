todas_as_tarefas = []

def criar_tarefa():
    tarefa = {}
    nome = input('Digite o nome da tarefa: ')
    descricao = input('Descreva a tarefa: ')
    prioridade = input('Qual o nivel de prioridade(1 para o mais urgente e 5 para o menos urgente)')
    categoria = input('Realizado ou não: ')    
    tarefa[nome] = {'nome':nome,'descricao':descricao,'prioridade':prioridade,'categoria':categoria}
    todas_as_tarefas.append(tarefa)
    
    print(f'Tarefa {descricao} adicionada com sucesso')
    
    
    
def listar_tarefa(todas_as_tarefas): 
     for tarefa in todas_as_tarefas:
          status = "Concluída" if tarefa["concluída"] else "Pendente"
          print(f"Nome: {tarefa['nome']}\nDescrição: {tarefa['descrição']}\nPrioridade: {tarefa['prioridade']}\nCategoria: {tarefa['categoria']}\nStatus: {status}\n")

     return
def concluido_ou_nao(todas_as_tarefas,nome):
     for tarefa in todas_as_tarefas:
        if tarefa["nome"] == nome:
            tarefa["concluída"] = True
            print(f"Tarefa '{nome}' marcada como concluída.")
            return
       
def editar_tarefa(todas_as_tarefas, prioridade):
     tarefas_filtradas = [tarefa for tarefa in todas_as_tarefas if tarefa["prioridade"] == prioridade]
     if not tarefas_filtradas:
        print(f"Nenhuma tarefa com prioridade '{prioridade}'.")
     else:
        for tarefa in tarefas_filtradas:
            status = "Concluída" if tarefa["concluída"] else "Pendente"
            print(f"Nome: {tarefa['nome']}\nDescrição: {tarefa['descrição']}\nPrioridade: {tarefa['prioridade']}\nCategoria: {tarefa['categoria']}\nStatus: {status}\n")

def excluir_tarefa(todas_as_tarefas, nome):
     for tarefa in todas_as_tarefas:
        if tarefa["nome"] == nome:
            todas_as_tarefas.remove(tarefa)
            print(f"Tarefa '{nome}' removida com sucesso.")
            return
     print(f"Tarefa '{nome}' não encontrada.")
     
     

while True:
    print('Boas Vindas ao CarlosTask')
    print('1 - Criar tarefas')
    print('2 - Listar taferas') 
    print('3 - Alterar par aconcluido ou não')
    print('4 - Editar tarefa')
    print('5 - Excluir tarefa')
    print('6 - Para sair ')
    op = int(input())
    if op == 1:
        criar_tarefa()
    elif op == 2:
          listar_tarefa()
    elif op == 3:
         concluido_ou_nao()
    elif op == 4:   
         editar_tarefa()
    elif op == 5:
         excluir_tarefa()
    elif op == 6:
        print('Sair do programa')
        break
    else:
        print()
    
        