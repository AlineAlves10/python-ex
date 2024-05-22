import random
nome = []
for i in range(4):
    alunos = input()
    nome.append(alunos)

escolhido = random.choice(nome)
print('o aluno para vim no quadro é {}'.format(escolhido))
