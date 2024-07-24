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
