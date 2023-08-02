import time 
import pandas as pd 
import pyautogui as pa

# Desabilitar a funcionalidade fail-safe
pa.FAILSAFE = False

pa.PAUSE = 1
#Importar a tabela de produtos
tabela = pd.read_csv('produtos.csv')
# print(tabela)

# Abrir o navegador 
pa.press('win')
pa.write('brave')
pa.press('enter')
time.sleep(6)

#Abrir o sistema
pa.write(r'https://dlp.hashtagtreinamentos.com/python/intensivao/login')
pa.press('enter')
time.sleep(5)

#Preencher as informações de login e entrar no sistema
pa.press('tab')
pa.write('teste@hashtagtreinamentos.com')
pa.press('tab')
pa.write('senha1234')
pa.press('tab')
pa.press('enter')

#Cadastrar as informações dos produtos e enviar
pa.press('tab')

for i in range(len(tabela)):
    for coluna in tabela.columns:
        if not pd.isna(tabela[coluna][0]):
            pa.write(str(tabela[coluna][i]))
            pa.press('tab')

    pa.press('enter')
    pa.click(x=282, y=221)
    pa.press('pgup')
    pa.press('tab')
    
pa.click(x=282, y=221)

# Definir uma variável para armazenar a posição inicial do cursor
posicao_inicial = pa.position()

# Loop para descer até o fim da página
while True:
    # Pressionar a tecla 'pgdn'
    pa.press('pgdn')
    
    # Aguardar um pequeno intervalo de tempo para a página rolar
    time.sleep(1)

    # Obter a posição atual do cursor
    posicao_atual = pa.position()

    # Verificar se a posição do cursor mudou desde o início
    if posicao_atual == posicao_inicial:
        print('Fim da página alcançado.')
        break

    # Atualizar a posição inicial para a posição atual do cursor
    posicao_inicial = posicao_atual