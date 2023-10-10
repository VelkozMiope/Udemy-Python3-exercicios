perguntas = [
    {
        'Pergunta': 'Quanto é 2 + 2?',
        'Opções': ['1', '2', '3', '4'],
        'Resposta': '4'
    },
    {
        'Pergunta': 'Quanto é 5 x 5?',
        'Opções': ['10', '25', '50', '75'],
        'Resposta': '25'
    },
    {
        'Pergunta': 'Quanto é 10/2?',
        'Opções': ['1', '2', '4', '5'],
        'Resposta': '5'
    }
]

acertos = 0

print('Bem vindo ao jogo de perguntas!')

for pergunta in perguntas:
    print(pergunta['Pergunta'])
    print('Opções: ', pergunta['Opções'])
    resposta_Usuario = input('Insira sua resposta: ')

    if resposta_Usuario == pergunta['Resposta']:
        acertos +=1
        print('Resposta correta!')
    else:
        print('Resposta errada! A resposta correta era ', pergunta['Resposta'])

if acertos == len(perguntas):
    print('Parabéns! Você acertou todas as perguntas!')
elif acertos <= (len(perguntas)-1) and not acertos == 0:
    print('Você acertou algumas perguntas!')
else:
    print('Que pena, você errou todas as perguntas!')