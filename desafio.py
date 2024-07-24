71 996414225

#a lógica que vou desenvolver é diferente da do professor, preciso pensar na solução, ela precisa ser rápida e prática
#preciso pensar no futuro e na manutenção do código
#Acabei de comprar um celular, ele está liso, ao ligar ele pede o pin e depois ele da o boot, em seguida senha, é preciso confirmar senha, confirmou senha "Bem vindo ao sistema"
#string - inteiro - float

print('---Nokia tijolão---')
print('Vamos nessa')
#so vou conferir o que foi informado, então não precisa colocar int
pin = input('Cadastre seu PIN: ')
confpin = input('Confirme o PIN para cadastro: ')

while confpin != pin:
    pin = input('Incorreto, tente novamente: ')
    confpin = input('Confirme o PIN para cadastro: ')

print('PIN Cadastrado com sucesso')

cont = 3
for tentativa in range(4):
    senha = input('Cadastre sua senha: ')
    confsenha = input('Confirme sua senha: ')
    if confsenha != senha:
        cont -= 1
        print(f'Você tem mais {cont} tentativas')
    else: #3 tentativas para bloqueio, precisa de break

==================================================

Objetivo do projeto:
Realizar cadastro de pin e apos o pin a senha.
3 tentativas de senha pra bloqueio.
Pin no looping infinito.
print('---Nokia tijolao---')
print('$$$Vamo nessa$$$')
pin = input('Digite o pin para cadastro: ')
confpin = input('Confirme o pin para cadastro: ')

while confpin != pin:
    pin = input('Errado. Tente novamente: ')
    confpin = input('Confirme o pin para cadastro: ')

print('pin cadastrado com sucesso.')

cont = 3
for tentativa in range(4):
    senha = input('Cadastre senha usuario: PALAVRA: ')
    confsenha = input('Confirme senha usuario: PALAVRA: ')
    if confsenha != senha:
        cont -= 1
        print(f'Voce tem mais {cont} tentativas')
    else:
        print('Correto')
        break
# 3 tentativas para bloqueio
# dica = precisa de break
# mensagem saindo do sistema
