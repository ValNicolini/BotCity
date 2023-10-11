
# pip install cookiecutter
# cookiecutter https://github.com/botcity-dev/bot-python-template
# pip install -e botone

from botcity.core import DesktopBot
# Uncomment the line below for integrations with BotMaestro
# Using the Maestro SDK
# from botcity.maestro import *


class Bot(DesktopBot):
    def action(self, execution=None):
        # Uncomment to silence Maestro errors when disconnected
        # if self.maestro:
        #     self.maestro.RAISE_NOT_CONNECTED = False

        # Fetch the Activity ID from the task:
        # task = self.maestro.get_task(execution.task_id)
        # activity_id = task.activity_id

        # Opens the BotCity website.
        # self.execute(r'C:\Users\Val_N\OneDrive\Área de Trabalho\Spotify.lnk')
        # self.execute(r'C:\Users\silva.valdenir\Desktop\Spotify.lnk')
        # #if not self.find( "Busca", matching=0.97, waiting_time=10000):
        #     #self.not_found("Busca")
        # if not self.find( "Busca", matching=0.97, waiting_time=10000):
        #      self.not_found("Busca")
        # self.click()
        #
        #
        #
        #
        # # if not self.find( "Digitar", matching=0.97, waiting_time=10000):
        # #     self.not_found("Digitar")
        # # self.click()
        # # self.paste('Queen')
        #
        # if not self.find( "Digitar", matching=0.97, waiting_time=1000):
        #       self.not_found("Digitar")
        # self.paste('Queen')
        #
        # # if not self.find( "Melhores", matching=0.97, waiting_time=10000):
        # #      self.not_found("Melhores")
        # if not self.find( "Melhores", matching=0.97, waiting_time=10000):
        #     self.not_found("Melhores")
        # self.click()
        #
        # # if not self.find( "Esperar", matching=0.97, waiting_time=10000):
        # #    self.not_found("Esperar")
        # # self.scroll_down(600)
        # # if not self.find( "Musica", matching=0.97, waiting_time=10000):
        # #      self.not_found("Musica")
        # if not self.find( "Esperar", matching=0.97, waiting_time=10000):
        #     self.not_found("Esperar")
        # self.scroll_down(700)
        # if not self.find( "Musica", matching=0.97, waiting_time=10000):
        #     self.not_found("Musica")
        #
        # self.double_click()
        # if not self.find( "Play", matching=0.97, waiting_time=10000):
        #     self.not_found("Play")
        # self.click()
        #
        #
        # # if not self.find( "Play", matching=0.97, waiting_time=10000):
        # #     self.not_found("Play")
        # #
        #

        self.execute(r'C:\Users\Public\Desktop\Firefox.lnk')
        if not self.find( "Oficial", matching=0.97, waiting_time=10000):
            self.not_found("Oficial")
        self.click()
        if not self.find( "Aceitar", matching=0.97, waiting_time=10000):
            self.not_found("Aceitar")
        self.click()
        if not self.find( "Financeiro", matching=0.97, waiting_time=10000):
            self.not_found("Financeiro")
        self.click()
        if not self.find( "Relatorios", matching=0.97, waiting_time=10000):
            self.not_found("Relatorios")
        self.click()
        if not self.find( "Boletos pagos", matching=0.97, waiting_time=10000):
            self.not_found("Boletos pagos")
        self.click()
        if not self.find( "Data", matching=0.97, waiting_time=10000):
            self.not_found("Data")
        self.click()
        if not self.find( "Digitar", matching=0.97, waiting_time=10000):
            self.not_found("Digitar")
        self.paste('11/10/2023')
        if not self.find( "Data1", matching=0.97, waiting_time=10000):
            self.not_found("Data1")
        self.click()
        self.paste('11/10/2023')
        if not self.find( "Baixar", matching=0.97, waiting_time=10000):
            self.not_found("Baixar")
        self.click()
        if not self.find( "Ok", matching=0.97, waiting_time=10000):
            self.not_found("Ok")
        self.click()
        if not self.find( "Espera", matching=0.97, waiting_time=10000):
            self.not_found("Espera")
        self.execute(r'C:\Users\silva.valdenir\Downloads')

        
        if not self.find( "Arquivo", matching=0.97, waiting_time=10000):
            self.not_found("Arquivo")
        
        self.double_click()
        
        
        
         


    def not_found(self, label):
        print(f"Element not found: {label}")


if __name__ == '__main__':
    Bot.main()
