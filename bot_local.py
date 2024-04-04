# # # BOT local Automatizado

# Abrir o LibreOffice Calc
# Escrever uma fórmula
# Colocar borda na célula da fórmula

import pyautogui
import time

# # Colocando o delay entre os comandos do pyautogui

pyautogui.PAUSE = 2

# Pressionando a tecla windows

pyautogui.press('win')

# Escrevendo o nome do aplicativo e abrindo (LibreOffice Calc)

pyautogui.write('LibreOffice Calc')
pyautogui.press('backspace')
pyautogui.press('enter')

# Selecionando a célula para inserir a fórmula

pyautogui.press('right')
pyautogui.press('down')

# Escrevendo a fórmula na célula específica

pyautogui.write('=5*10')
pyautogui.press('enter')
pyautogui.press('up')

# Colocando a borda na célula

pyautogui.click(x=1173, y=107)
pyautogui.click(x=1236, y=194)

time.sleep(5)
print(pyautogui.position())
