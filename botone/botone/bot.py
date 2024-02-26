
# pip install cookiecutter
# cookiecutter https://github.com/botcity-dev/bot-python-template
# pip install -e botone
from selenium.webdriver.common.keys import Keys
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


        if not self.find( "Inicio", matching=0.97, waiting_time=10000):
            self.not_found("Inicio")
        self.wait(1000)
        self.click()

        if not self.find( "Conectar", matching=0.97, waiting_time=10000):
           self.not_found("Conectar")
        self.wait(2000)
        self.click()
        self.page_down()
        # if not self.find( "Caixa", matching=0.97, waiting_time=10000):
        #    self.not_found("Caixa")
        # self.click()
        # self.paste('imp')
        # self.wait(1000)
        # self.type_down()
        # if not self.find( "Balde", matching=0.97, waiting_time=10000):
        #    self.not_found("Balde")
        # self.click()
        # self.wait(1000)
        #
        # if not self.find( "Selecionar", matching=0.97, waiting_time=10000):
        #    self.not_found("Selecionar")
        # self.click()
        #
        
        
       
        











    def not_found(self, label):
        print(f"Element not found: {label}")


if __name__ == '__main__':
    Bot.main()

