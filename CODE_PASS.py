import random
import string

print("Gerador de Senha Aleatória")

# solicita ao usuário o tamanho da senha
tamanho_senha = int(input("Digite o tamanho da senha que você deseja (mínimo 8 caracteres): "))

# verifica se o tamanho da senha é válido
while tamanho_senha < 8:
    print("Tamanho de senha inválido! O tamanho mínimo é 8.")
    tamanho_senha = int(input("Digite novamente o tamanho da senha: "))

# define os caracteres que podem ser usados na senha
caracteres = string.ascii_letters + string.digits + string.punctuation

# gera a senha aleatória
senha = ''.join(random.choice(caracteres) for i in range(tamanho_senha))

# exibe a senha gerada
print("A senha gerada é:", senha)
