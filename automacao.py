
import pyautogui
import time 
import pandas as pd 

pyautogui.PAUSE = 0.5
link = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"

pyautogui.press('Win')
pyautogui.write('Chrome')
pyautogui.press('Enter')

pyautogui.write(link)
pyautogui.press('Enter')
time.sleep(3)

pyautogui.click(x=775, y=374)
pyautogui.write('Henrycardoso@gmail.com')
pyautogui.press('Tab')
pyautogui.write('Henry2007')
pyautogui.press('Tab')
pyautogui.press('Enter')

time.sleep(4)

tabela = pd.read_csv('produtos.csv')
print(tabela)

for linha in tabela.index:
    pyautogui.click(x=821, y=258)

    codigo = str(tabela.loc[linha, 'codigo'])
    pyautogui.write(codigo)
    pyautogui.press('Tab')

    marca = tabela.loc[linha, 'marca']
    pyautogui.write(marca)
    pyautogui.press('Tab')


    tipo = str(tabela.loc[linha, 'tipo']) 
    pyautogui.write(tipo)
    pyautogui.press('Tab')

    categoria = str(tabela.loc[linha, 'categoria'])
    pyautogui.write(categoria)
    pyautogui.press('Tab')

    preco = str(tabela.loc[linha, 'preco_unitario'])
    pyautogui.write(preco)
    pyautogui.press('Tab')

    custo = str(tabela.loc[linha, 'custo'])
    pyautogui.write(custo)
    pyautogui.press('Tab')

    obs = str(tabela.loc[linha, 'obs'])
    if obs != 'NaN':
        pyautogui.write(obs)
    pyautogui.press('Tab')

    pyautogui.press('Enter')
    pyautogui.scroll(5000)


