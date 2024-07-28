#Quiz Python

#Perguntas


def sintaxe_hello_word():
    print('----------------------------------------------------------')
    print('----------------------------------------------------------')
    print('Sejam bem vindos a Quiz de Python')
    print('Esse Quiz tem o objetivo de testar o seu conhecimento, é uma serie de perguntas \n'
        'acada resposta que for acertada você ganhará 1 ponto e ao final saberá o seu nível de conhecimento')
    print('Boa Sorte!')
    print('----------------------------------------------------------')
    print('----------------------------------------------------------')
    pontuacao = 0
    print('Qual é a sintaxe correta para exibir "Hello Word" em Python')
    print('  \n'
    'A) print("Hello Word") \n'
    'B) p("Hello Word"); \n'
    'C) echo ("Hello Word"); \n'
    'D) print "Hello word" \n'
    'E) print ("Hello Word"); \n')
    #Código

    opcoes = ['A', 'B', 'C', 'D', 'E']
    resposta = input('Diga a sua resposta: ').upper()

    if resposta not in opcoes:
            print('Escolha invalidade, tente novamente')
            return
    print('')
    if resposta == opcoes[0]:
        pontuacao += 1
        print('Parabéns Você acertou')
    else:
         print('Infelizmente você errou, a resposta correta é A) print("Hello Word")')
    #quiz 2
    print('')
    print ('Como você insere comentários no código em python?')
    print(' \n'
        'A) //Isso é um comentário \n'
        'B) #Isso é um comentário \n'
        'C) /* Isso é um comentário \n')
    opcoes = ['A', 'B', 'C', 'D', 'E']
    resposta = input('Diga a sua resposta: ').upper()

    if resposta not in opcoes:
        print('Escolha invalidade, tente novamente')
        return
    print('')
    if resposta == opcoes[1]:
        pontuacao += 1
        print('Parabéns Você acertou')
    else:
        print('Infelizmente você errou, a resposta correta é B) #Isso é um comentário')
    #Quiz 3
    print('')
    print ('Qual deles NÃO é um nome de variável válido')
    print(' \n'
        'A) _minhavar\n'
        'B) Minhavar\n'
        'C) minha_var\n'
        'D) my-var\n')
    opcoes = ['A', 'B', 'C', 'D', 'E']
    resposta = input('Diga a sua resposta: ').upper()

    if resposta not in opcoes:
        print('Escolha invalidade, tente novamente') 
        return
    print('')
    if resposta == opcoes[3]:
        pontuacao += 1
        print('Parabéns Você acertou')
    else:
         print('Infelizmente você errou, a resposta correta é D) my-var')
    #Quiz 4 
    print('')
    print('Como você cria uma variável  com o  valor numérico 5? ')
    print(' \n'
          'A) X=int(5)\n'
          'B) x = 5\n'
          'C) Ambas as outras respostas estão corretas\n')
    opcoes = ['A', 'B', 'C', 'D', 'E']
    resposta = input('Diga a sua resposta: ').upper()

    if resposta not in opcoes:
        print('Escolha invalidade, tente novamente') 
        return
    print('')
    if resposta == opcoes[2]:
        pontuacao += 1
        print('Parabén você acertou')
    else:
         print('Infelizmente você errou, a resposta correta é C) Ambas as outras respostas estão corretas')
    #Quiz 5
    print('Qual é a extensão de arquivo correta para arquivos Python? ')
    print(' \n'
          'A) .pyt \n'
          'B) .pt \n'
          'C) .pyth \n'
          'D) .py')
    opcoes = ['A', 'B', 'C', 'D', 'E']
    resposta = input('Diga a sua resposta: ').upper()

    if resposta not in opcoes:
        print('Escolha invalidade, tente novamente') 
        return
    print('')
    if resposta == opcoes[3]:
        pontuacao += 1
        print('Parabéns ocê acertou')
    else:
         print('Infelizmente você errou, a resposta correta é D) .py ')
    #Quiz 6
    print('Como você cria uma variável com número flutuante 2,8? ')
    print(' \n'
          'A) X=float(2.8)\n'
          'B) x = 2.8\n'
          'C) Ambas as outras respostas estão corretas\n')
    opcoes = ['A', 'B', 'C', 'D', 'E']
    resposta = input('Diga a sua resposta: ').upper()

    if resposta not in opcoes:
        print('Escolha invalidade, tente novamente') 
        return
    print('')
    if resposta == opcoes[2]:
        pontuacao += 1
        print('Parabéns você acertou')
    else:
         print('Infelizmente você errou, a resposta correta é C) Ambas as outras respostas estão corretas')
    #Quiz 7
    print('Qual é a sintaxe correta para gerar o tipo de uma variável  ou objeto em Python?')
    print(' \n'
          'A) print(typeof(x))\n'
          'B) print(typeOf(x))\n'
          'C) print(type(x))\n'
          'D) print(typeof x)')
    opcoes = ['A', 'B', 'C', 'D', 'E']
    resposta = input('Diga a sua resposta: ').upper()

    if resposta not in opcoes:
        print('Escolha invalidade, tente novamente') 
        return
    print('')
    if resposta == opcoes[2]:
        pontuacao += 1
        print('Parabéns você acertou')
    else:
         print('Infelizmente você errou, a resposta correta é C) print(type(x))')
    #Quiz 8
    print('Qual é a maneira correta de criar uma função em Python? ')
    print(' \n'
          'A) criar minhafuncao()\n'
          'B) funcao minhafuncao()\n'
          'C) def minhafuncao()\n')
    opcoes = ['A', 'B', 'C', 'D', 'E']
    resposta = input('Diga a sua resposta: ').upper()

    if resposta not in opcoes:
        print('Escolha invalidade, tente novamente') 
        return
    print('')
    if resposta == opcoes[2]:
        pontuacao += 1
        print('Parabéns você acertou')
    else:
         print('Infelizmente você errou, a resposta correta é C) def minhafuncao()')
    #Quiz 9
    print('Em Python, Aspas duplas é o mesmo que Aspas simples? ')
    print(' \n'
          'A) True(Verdadeiro) \n'
          'B) False(falso)\n')
    opcoes = ['A', 'B', 'C', 'D', 'E']
    resposta = input('Diga a sua resposta: ').upper()

    if resposta not in opcoes:
        print('Escolha invalidade, tente novamente') 
        return
    print('')
    if resposta == opcoes[0]:
        pontuacao += 1
        print('Parabéns você acertou')
    else:
         print('Infelizmente você errou, a resposta correta é  A) True(verdadeiro)')
    #Quiz 10
    print('')
    print('Em lista qual é a sixtaxe correta para retornar o primeiro caractere em uma string? ')
    print(' \n'
          'A) X= "Hello"[0]\n'
          'B) x= sub("Hello",0,1) \n'
          'C) x= "Hello".sub(0,1) \n')
    opcoes = ['A', 'B', 'C', 'D', 'E']
    resposta = input('Diga a sua resposta: ').upper()

    if resposta not in opcoes:
        print('Escolha invalidade, tente novamente') 
        return
    print('')
    if resposta == opcoes[0]:
        pontuacao += 1
        print('Parabéns você acertou')
    else:
         print('Infelizmente você errou, a resposta correta é A) X="Hello"[0]')
    print('')
    if pontuacao == 10:
        print(f'Você acertou {pontuacao} de  10 questões')
        print('Parabéns, tenha orgulho de você')
    elif pontuacao <=9 and pontuacao >=6:
        print(f'Você acertou {pontuacao} de  10 questões')
        print('Parabéns, você tem um ótimo conhecimento de Python')
    else:
        print(f'Você acertou {pontuacao} de  10 questões')
        print('Não fique triste com o seu resultado, continue tentando que logo você estará fera em Python')
sintaxe_hello_word()

