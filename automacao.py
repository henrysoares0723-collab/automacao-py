
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

pyautogui.click(x=821, y=258)
pyautogui.write('MOLO000251')
pyautogui.press('Tab')
pyautogui.write('Logitech')
pyautogui.press('Tab')
pyautogui.write('Mouse')

pyautogui.press('Tab')
pyautogui.write('Acessorios')

pyautogui.press('Tab')
pyautogui.write(' 1 ')

pyautogui.press('Tab')
pyautogui.write('25.95')
pyautogui.press('Tab')

pyautogui.write('NaN')
pyautogui.press('Tab')

pyautogui.press('Enter')


