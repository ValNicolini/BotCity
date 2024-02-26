import self
# pip install cookiecutter
# cookiecutter https://github.com/botcity-dev/bot-python-template
# pip install -e botone
from selenium.webdriver.common.keys import Keys
import pyautogui
from time import  sleep
# from openpyxl import Workbook
# from datetime import date
from botcity.core import DesktopBot
# Uncomment the line below for integrations with BotMaestro
# Using the Maestro SDK
# from botcity.maestro import *
class Bot(DesktopBot):
    def action(self, execution=None):
#         # Uncomment to silence Maestro errors when disconnected
        # if self.maestro:
        #     self.maestro.RAISE_NOT_CONNECTED = False

        # Fetch the Activity ID from the task:
        # task = self.maestro.get_task(execution.task_id)
        # activity_id = task.activity_id

        # Opens the BotCity website.


        self.execute(r'C:\Users\Public\Desktop\Google Chrome.lnk')
        # self.wait(1000)
        # if not self.find( "Pesquisa", matching=0.97, waiting_time=10000):
        #     self.not_found("Pesquisa")
        # self.click()
        # self.paste('Botcity')
        # self.enter()
        # self.wait(1000)
        # self.type_down()

        

        if not self.find( "Inicio", matching=0.97, waiting_time=10000):
            self.not_found("Inicio")
        self.wait(1000)
        self.click()

        if not self.find( "Conectar", matching=0.97, waiting_time=10000):
           self.not_found("Conectar")
        self.wait(2000)
        self.click()
        self.wait(1000)

        pyautogui.click(322, 643)
        self.wait(10000)

        pyautogui.click(323, 450)
        self.wait(50)
        pyautogui.click(324, 487)
        self.wait(50)
        pyautogui.click(324, 530)
        self.wait(50)
        pyautogui.click(323, 567)
        self.wait(50)
        pyautogui.click(323, 609)
        self.wait(50)
        pyautogui.click(323, 651)
        self.wait(50)
        pyautogui.click(329, 691)
        self.wait(1)
    T = 0
    while T >= 1000:
        pyautogui.scroll(10)
        sleep(1)
        pyautogui.click(323,690)
        T += 1
        # self.type_down()
        # self.wait(1)
        # pyautogui.click(329, 692)
        # self.type_down()
        # self.wait(1)
        # pyautogui.click(329, 692)
        # self.type_down()
        # self.wait(1)
        # pyautogui.click(329, 692)
        # self.type_down()
        # self.wait(1)
        # pyautogui.click(329, 692)
        # self.type_down()
        # self.wait(1)
        # pyautogui.click(329, 691)
        # self.type_down()
        # self.wait(1)
        # pyautogui.click(329, 691)
        # self.type_down()
        # self.wait(1)
        # pyautogui.click(329, 691)
        # self.type_down()
        # self.wait(1)
        # pyautogui.click(329, 691)
        # self.type_down()
        # self.wait(1)
        # pyautogui.click(329, 691)
        # self.type_down()
        # self.wait(1)
        # pyautogui.click(329, 691)
        # self.type_down()
        # self.wait(1)
        # pyautogui.click(329, 691)
        # self.type_down()
        # self.wait(1)
        # pyautogui.click(329, 691)
        # self.type_down()
        # self.wait(1)
        # pyautogui.click(329, 691)
        # self.type_down()
        # self.wait(1)
        # pyautogui.click(329, 691)
        # self.type_down()
        # self.wait(1)
        # pyautogui.click(329, 691)
        # self.type_down()
        # self.wait(1)
        # pyautogui.click(329, 691)
        # self.type_down()
        # self.wait(1)
        # pyautogui.click(329, 691)
        # self.type_down()
        # self.wait(1)
        # pyautogui.click(329, 691)
        # self.type_down()
        # self.wait(1)
        # pyautogui.click(329, 691)
        # self.type_down()
        # self.wait(1)
        # pyautogui.click(329, 691)
        # self.type_down()
        # self.wait(1)
        # pyautogui.click(329, 691)
        # self.type_down()
        # self.wait(1)
        # pyautogui.click(329, 691)
        # self.type_down()
        # self.wait(1)
        # pyautogui.click(329, 691)
        # self.type_down()
        # self.wait(1)
        # pyautogui.click(329, 691)
        # self.type_down()
        # self.wait(1)
        # pyautogui.click(329, 691)
        # self.type_down()
        # self.wait(1)
        # pyautogui.click(329, 691)
        # self.type_down()
        # self.wait(1)
        # pyautogui.click(329, 691)
        # pyautogui.click(1089,554)
        # if not self.find( "Deletar", matching=0.97, waiting_time=10000):
        #     self.not_found("Deletar")
        # self.wait(1000)
        # self.click()


        
        
        
        
        
        
        
       
      
           

        
        
       
        











    def not_found(self, label):
        print(f"Element not found: {label}")


if __name__ == '__main__':
    Bot.main()

