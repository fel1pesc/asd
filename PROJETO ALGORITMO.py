SALA = 'sala'
TIPO = 'tipo'
FILME = 'filme'
CADEIRAS = 'cadeiras'
OCUPADAS =  'ocupadas'

salas = [
    {SALA : 1, TIPO : '3D', FILME : 'Vingadores', CADEIRAS : 50, OCUPADAS : 0},
    {SALA : 2, TIPO : '2D', FILME : 'Capitao America', CADEIRAS : 50, OCUPADAS : 0},
    {SALA : 3, TIPO : '2D', FILME : 'Deadpool', CADEIRAS : 50, OCUPADAS : 0},
    {SALA : 4, TIPO : '3D', FILME : 'Guerra Civil', CADEIRAS : 50, OCUPADAS : 0},
    {SALA : 5, TIPO : '3D', FILME : 'Rio', CADEIRAS : 50, OCUPADAS : 0},
    {SALA : 6, TIPO : '2D', FILME : 'Intocaveis', CADEIRAS : 50, OCUPADAS : 0}
    ]

def imprimir_filmes(s):
    print(' %-3d   %-20s %s' %(s[SALA] , s[FILME] , s[TIPO]))

def imprimir(salas):
    for s in salas:
        imprimir_filmes(s)

def menu():
    print('************* COMANDOS ***************')
    print('(1) - Imprimir salas e filmes.')
    print('(2) - Adicionar filme ao cartaz.')
    print('(3) - Editar filme do cartaz.')
    print('(4) - Remover um filme do cartaz.')
    print('(5) - Fechar o programa.')
    print('**************************************')
def cabecario():
    print('SALA   FILME               TIPO')

def existe_filme(nome):
    for s in salas :
        if s[FILME] == nome :    
            return True
    return False

def busca_pos(nome):
    for i in range(len(salas)):
        if salas[i][FILME] == nome:
            return i
    return -1

def cmd_print():
    cabecario()
    for s in salas:
        imprimir_filmes(s)

def cmd_add():
    nome = input('Digite um filme:\n')
    if existe_filme(nome) :
        print('Filme já existente.')
    else:
        novo = { }
        novo[FILME] = nome
        novo[TIPO] = input('3D ou 2D ?\n')
        novo[SALA] = int(input('Qual sera a sala do filme?\n'))
        novo[CADEIRAS] = int(input('Quantas cadeiras havera na sala?\n'))
        novo[OCUPADAS] = 0
        salas.append(novo)
        print('Filme adicionado com sucesso!')

def cmd_update():
    busca = input('Digite o filme para atualizar:\n')
    if existe_filme(busca):
        pos = busca_pos(busca)
        sala = salas[pos]

        print('Filme encontrado:')
        imprimir_filmes(salas[pos])

        sala[FILME] = input('Novo filme:\n:')
        sala[TIPO] = input('Novo tipo: (3D ou 2D)\n')
        sala[SALA] = int(input('Novo numero da sala\n'))
        sala[CADEIRAS] = int(input('Novo numero de cadeiras na sala\n'))
        sala[OCUPADAS] = 0

def cmd_del():
    busca = input('Digite nome para apagar:\n')
    if existe_filme(busca):
        pos = busca_pos(busca)
        del salas[pos]
        print('Filme removido')
    else:
        print('Filme nao encontrado')

def cmd_find():
    busca = input('Digite sua busca:\n')
    encontrados = []
    for s in salas:
        if busca in s[FILME]:
            encontrados.append(s)
    cabecario()
    imprimir(encontrados)

menu()
while True:

    cmd = input(":")

    if cmd == '1':
        cmd_print()
    elif cmd == '5':
        break
    elif cmd == '2':
        cmd_add()
    elif cmd == '3':
        cmd_update()
    elif cmd == '4':
        cmd_del()
    elif cmd == 'find':
        cmd_find()
        
    
    else:
        menu
