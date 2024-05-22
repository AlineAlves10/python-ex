import random
nome = []
for i in range(4):
    alunos = input()
    nome.append(alunos)

random.shuffle(nome)
print('a ordem de apresentacao é {}'.format(nome))
