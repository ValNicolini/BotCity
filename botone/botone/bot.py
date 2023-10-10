
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
        self.execute(r'C:\Users\silva.valdenir\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Microsoft Teams classic (work or school).lnk')
        if not self.find( "Pesquisar", matching=0.97, waiting_time=10000):
           self.not_found("Pesquisar")
        self.click()
        self.paste('Jhully Nayara Azevedo')
        if not self.find( "Nome", matching=0.97, waiting_time=10000):
            self.not_found("Nome")
        self.click()
        if not self.find( "Mensagem", matching=0.97, waiting_time=10000):
            self.not_found("Mensagem")
        self.click()
        self.paste('Jhully isso é apenas um teste!')
        self.enter()
        
        
        

        # Uncomment to mark this task as finished on BotMaestro
        # self.maestro.finish_task(
        #     task_id=execution.task_id,
        #     status=AutomationTaskFinishStatus.SUCCESS,
        #     message="Task Finished OK."
        # )

    def not_found(self, label):
        print(f"Element not found: {label}")


if __name__ == '__main__':
    Bot.main()
