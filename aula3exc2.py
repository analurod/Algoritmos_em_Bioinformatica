# 1) Em um script, o usuário deve responder à pergunta
# “Continuar (s/n)?”. Se o
# usuário digitar ‘s’ ou ‘S’, o script deve retornar a mensagem
# “OK, continuando...”. Se o usuário digitar ‘n’ ou ‘N’, o script
# deve retornar a mensagem “OK, parando...”. Por fim, se o
# usuário digitar qualquer outra coisa,
# o script deve retornar uma mensagem de erro.

escolha = input('Continuar (s/n)? ')

if escolha == 's' or escolha == 'S':
    print('OK, continuando...')
elif escolha == 'n' or escolha == 'N':
    print('OK, parando...')
else:
    print('ERRO!')
