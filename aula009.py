frase = 'curso em video python'
#frase[9:13] frase[9:21:2] frase[:5] frase [15:] frase[9::3]

#ANALISE
len(frase) #qual o comprimento da frase
frase.count('o') #contar quantas vezes aparece a letra o na frase
frase.count('o', 0, 13) #contar com fatiamento
frase.find('deo') #vai me dizer quantas vezes ele encontrou o deo
frase.find('Android') #vai retornar -1 essa string nn foi encontrada
'curso' in frase #dentro da frase tem a palavra curso? True

#TRANSFORMAÇÃO
frase.replace('python', 'android') #substituir a palavra
frase.upper() #ele vai trocar tudo por MAIUSCULO
frase.lower() #trocar tudo para minusculo
frase.capitalize() #vai trocar tudo para minusculo e so colocar a primeira para maiusculo
frase.title() #vai analisar quantas palavras tem(4) e vai trocar a primeira para maiusculo em TODAS as palavras
frase.strip() #vai remover os espacos inuteis do começo e final
frase.rstrip() #vai remover os espacos somente do lado direito(final)
frase.lstrip() #vai remover os espacos da esquerda(comeco)

#DIVISAO
frase.split() #vai criar uma divisao das palavras na frase, vai criar uma lista com todos as cadeias da frase

#JUNCAO
'-'.join(frase) #vai juntar os elementos usando - (curso-em-video-python)
