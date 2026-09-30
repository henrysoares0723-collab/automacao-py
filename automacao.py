#Logica do codigo 

#1 - Entrar no sistema da empresa
#2 - Fazer login 
#3 - Abrir a base de dados 
#4 - Cadastrar um produto 
#5 - Repetir a etapa 4 ate acabar a lista de produtos 


import pyautogui
import time 

pyautogui.PAUSE = 0.5
link = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"

pyautogui.press('Win')
pyautogui.write('Chrome')
pyautogui.press('Enter')

pyautogui.write(link)
pyautogui.press('Enter')
time.sleep(3)

pyautogui.click(x=711, y=38)