#Sistema Policial
#Autor: Matheus Ruivo
#Inicio - 21/10/25 Fim - 

email = input("Digite seu número do cracha (ra):")
senha = input("Digite sua senha:")
nome = input("Seu nome:")
n = 'Arthur'
senha1 = 222
email1 = 'policia@gmail.com' #Aos poucos vou add mais coisas!

print(F"Verificando,  {nome}!")

if (email == email1 and senha == senha1) or nome == n:
    print(f"Bem-vindo ao sistema policial {nome}")
else:
    print(f"Erro. {nome}")