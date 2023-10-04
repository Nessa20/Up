# 1º aula --> Power UP
#- automação de tarefas
#- criaçao de Bots
#- economizar horas de trabalho
#- RPA e Web Scraping
 
# clicar com mouse comando: pyautogui.click
# escrever um texto comando: pyautogui.write
# abertar uma tecla comando: pyautogui.press
# combinacao de teclas comando: pyautogui.hotkey (atalho)
# pip install pyautogui

# Passo a passo do projeto
# Passo 1: Entrar no sistema da 
    # https://dlp.hashtagtreinamentos.com/python/intensivao/login
import pyautogui
import time

pyautogui.PAUSE = 0.5

# abrir o chrome
pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.press("enter")

# entrar no link
link = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"
pyautogui.write(link)
pyautogui.press("enter")

# esperar o site carregar
time.sleep(3)

# Passo 2: Fazer Login
pyautogui.click(x=773, y=455 )
pyautogui.write("pythonimpressionador@gmail.com")

pyautogui.press("tab") # passar para o campo de senha
pyautogui.write("sua senha aqui")

pyautogui.press("tab") # passei pro botão de login
pyautogui.press("enter")

time.sleep(3)

# Passo 3: Importa a base de dados de 
# instalar pip install pandas numpy openpyxl --> rodar no terminal
import pandas

tabela = pandas.read_csv("produtos.csv")
print(tabela)

for linha in tabela.index:
    # Passo 4: Cadastrar um produto
    pyautogui.click(x=756, y=300)

    codigo = tabela.loc[linha, "codigo"]

    # preencher os campos
    pyautogui.write(str(codigo))
    # str --> transforma o que esta dentro dele em texto
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "marca"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "tipo"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "categoria"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "preco_unitario"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "custo"]))
    pyautogui.press("tab")

    obs = tabela.loc[linha, "obs"]
    if not pandas.isna(obs)
        pyautogui.write(str(obs))
   
    # apertar para enviar
    pyautogui.press("tab")
    pyautogui.press("enter")

    # voltar para cima
    pyautogui.scroll(50000)

# Passo 5: Repetir o cadastro para todos os produtos
