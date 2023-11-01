
# pip install cookiecutter
# cookiecutter https://github.com/botcity-dev/bot-python-template
# pip install -e botone
from selenium.webdriver.common.keys import Keys
from openpyxl import Workbook
from datetime import date
from botcity.core import DesktopBot
# Uncomment the line below for integrations with BotMaestro
# Using the Maestro SDK
# from botcity.maestro import *

wb = Workbook()
ws = wb.active
ws.title = 'boletos_pagos'

data_atual = date.today()
data = data_atual.strftime('%d/%m/%Y')



class Bot(DesktopBot):
    def action(self, execution=None):
#         # Uncomment to silence Maestro errors when disconnected
        # if self.maestro:
        #     self.maestro.RAISE_NOT_CONNECTED = False

        # Fetch the Activity ID from the task:
        # task = self.maestro.get_task(execution.task_id)
        # activity_id = task.activity_id

        # Opens the BotCity website.


        self.execute(r'C:\Users\Public\Desktop\Firefox.lnk')
        if not self.find("Oficial", matching=0.97, waiting_time=10000):
            self.not_found("Oficial")
        self.click()
        if not self.find("Aceitar", matching=0.97, waiting_time=10000):
            self.not_found("Aceitar")
        self.click()
        if not self.find("Financeiro", matching=0.97, waiting_time=10000):
            self.not_found("Financeiro")
        self.click()
        if not self.find("Relatorios", matching=0.97, waiting_time=10000):
            self.not_found("Relatorios")
        self.click()
        if not self.find("Boletos pagos", matching=0.97, waiting_time=10000):
            self.not_found("Boletos pagos")
        self.click()
        self.wait(1000)
        if not self.find( "Data", matching=0.97, waiting_time=10000):
            self.not_found("Data")
        self.click()
        self.paste(data)
        if not self.find("Data1", matching=0.97, waiting_time=10000):
            self.not_found("Data1")
        self.click()
        self.paste(data)
        if not self.find("Baixar", matching=0.97, waiting_time=10000):
            self.not_found("Baixar")
        self.click()
        if not self.find( "Ok", matching=0.97, waiting_time=10000):
            self.not_found("Ok")
        self.click()
        if not self.find("Espera", matching=0.97, waiting_time=20000):
            self.not_found("Espera")

        self.execute(r'C:\Users\silva.valdenir\Downloads')
        self.wait(1000)
        if not self.find("Arquivo", matching=0.97, waiting_time=10000):
            self.not_found("Arquivo")

        self.double_click()

        if not self.find("Fecha mensagem", matching=0.97, waiting_time=10000):
            self.not_found("Fecha mensagem")
        self.click()

        if not self.find("Pago", matching=0.97, waiting_time=10000):
            self.not_found("Pago")
        self.click()

        self.type_keys(['ctrl', 'space'])
        self.wait(1000)
        if not self.find("Copia_valor_total", matching=0.97, waiting_time=10000):
            self.not_found("Copia_valor_total")
        self.click()

        if not self.find("Total", matching=0.97, waiting_time=10000):
            self.not_found("Total")
        self.click()

        if not self.find("Fechar", matching=0.97, waiting_time=10000):
            self.not_found("Fechar")
        self.click()

        self.execute('notepad.exe')
        self.wait(1000)
        self.kb_type('Baixas Volks ',200)
        self.paste(data)
        self.enter()
        self.enter()
        self.kb_type('Valor Total: ', 200)
        self.control_v()
        self.wait(4000)
        if not self.find("FechaNote", matching=0.97, waiting_time=10000):
            self.not_found("FechaNote")
        self.click()
        if not self.find("NaoSalvar", matching=0.97, waiting_time=10000):
            self.not_found("NaoSalvar")
        self.click()
        if not self.find("Seleciona", matching=0.97, waiting_time=10000):
            self.not_found("Seleciona")
        self.click()
        
        if not self.find("Recorta", matching=0.97, waiting_time=10000):
            self.not_found("Recorta")
        self.click()
        if not self.find("Pasta", matching=0.97, waiting_time=10000):
            self.not_found("Pasta")
        self.double_click()
        self.control_v()
        if not self.find("Voltar", matching=0.97, waiting_time=10000):
            self.not_found("Voltar")
        self.click()
        
        











    def not_found(self, label):
        print(f"Element not found: {label}")


if __name__ == '__main__':
    Bot.main()
