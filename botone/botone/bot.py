
# pip install cookiecutter
# cookiecutter https://github.com/botcity-dev/bot-python-template
# pip install -e botone
#apagar
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
        self.execute(r'C:\Users\Val_N\OneDrive\Área de Trabalho\Spotify.lnk')
        if not self.find( "Busca", matching=0.97, waiting_time=10000):
            self.not_found("Busca")
        self.click()
        
        if not self.find( "Digitar", matching=0.97, waiting_time=10000):
            self.not_found("Digitar")
        self.click()
        
        self.paste('Queen')

        if not self.find( "Melhores", matching=0.97, waiting_time=10000):
            self.not_found("Melhores")
        self.click()
        if not self.find( "Esperar", matching=0.97, waiting_time=10000):
            self.not_found("Esperar")
        self.scroll_down(600)
        if not self.find( "Musica", matching=0.97, waiting_time=10000):
            self.not_found("Musica")
        self.double_click()

        if not self.find( "Play", matching=0.97, waiting_time=10000):
            self.not_found("Play")
        
        




    def not_found(self, label):
        print(f"Element not found: {label}")


if __name__ == '__main__':
    Bot.main()
