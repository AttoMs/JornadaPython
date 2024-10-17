# Passo 1: Entrar no sistema da empresa https://dlp.hashtagtreinamentos.com/python/intensivao/login
import time
import pyautogui
# pyautogui.write - escreve um texto
# pyautogui.click - clicar com o mouse
# pyautogui.press - apertar uma tecla
# pyautogui.hotkey - apertar um atalho de teclado (Ctrl, C)

pyautogui.PAUSE = 0.5

pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.press("enter")

# Passo 2: Fazer login

pyautogui.click(x=456, y=70)
link = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"
pyautogui.write(link)
pyautogui.press("Enter")

# uma pausa de 3 segundos
time.sleep(3)
pyautogui.click(x=702, y=412)
pyautogui.write("lucasmotta.nave@gmail.com")

pyautogui.press("tab")
pyautogui.write("minha senha aqui")

#aperta botão de logar
pyautogui.click(x=665, y=581)

time.sleep(3)

# Passo 3: Importar a base de dados
import pandas

tabela = pandas.read_csv("produtos.csv")
print(tabela)

# Passo 4: Cadastrar 1 produto
linha = 0

for linha in tabela.index:
    pyautogui.click(x=611, y=294)
    # codigo
    codigo  = tabela.loc[linha, "codigo"]
    pyautogui.write(str(codigo)) 
    pyautogui.press("tab")

    # marca
    marca  = tabela.loc[linha, "marca"]
    pyautogui.write(str(marca))
    pyautogui.press("tab")

    # tipo 
    tipo  = tabela.loc[linha, "tipo"]
    pyautogui.write(str(tipo))
    pyautogui.press("tab")

    # categoria
    categoria  = tabela.loc[linha, "categoria"]
    pyautogui.write(str(categoria))
    pyautogui.press("tab")

    # preço
    preco  = tabela.loc[linha, "preco_unitario"]
    pyautogui.write(str(preco))
    pyautogui.press("tab")

    # custo
    custo  = tabela.loc[linha, "custo"]
    pyautogui.write(str(custo))
    pyautogui.press("tab")

    # obs
    obs  = tabela.loc[linha, "obs"]
    if not pandas.isna(obs): # 'isna' checa se não é vazio  4   
        pyautogui.write(str(obs))
    pyautogui.press("tab")

    # clicar no botão enviar
    pyautogui.press("enter")
    pyautogui.scroll(5000)

# Passo 5: Repetir o processo de cadastro até acabar os produtos