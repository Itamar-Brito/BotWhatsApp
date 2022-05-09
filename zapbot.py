from selenium import webdriver
import time

class WhatsappBot:
    def __init__(self):
        self.mensagem = "TESTE DE MENSAGEM! BOT"
        self.grupos = ["C0d1nG", "NOTAS INVESTIMENTO", "Adelano"]
        options = webdriver.ChromeOptions()
        options.add_argument('lang=pt-br')
        self.driver = webdriver.Chrome(executable_path=r'./chromedriver.exe')

    def EnviarMensagens(self):
        #<span dir="auto" title="C0d1nG" class="ggj6brxn gfz4du6o r7fjleex g0rxnol2 lhj4utae le5p0ye3 l7jjieqr i0jNr">C0d1nG</span>
        #<div tabindex="-1" class="p3_M1"><div tabindex="-1" class="_1UWac _1LbR4"><div class="_2vbn4" style="visibility: visible;">Mensagem</div><div title="Mensagem" role="textbox" class="_13NKt copyable-text selectable-text" contenteditable="true" data-tab="10" dir="ltr" spellcheck="true"></div></div></div>
        #<span data-testid="send" data-icon="send" class=""><svg viewBox="0 0 24 24" width="24" height="24" class=""><path fill="currentColor" d="M1.101 21.757 23.8 12.028 1.101 2.3l.011 7.912 13.623 1.816-13.623 1.817-.011 7.912z"></path></svg></span>
        self.driver.get('https://web.whatsapp.com/')
        time.sleep(30)
        for grupo in self.grupos:
            grupoToSend = self.driver.find_element_by_xpath(F"//span[@title='{grupo}']")
            time.sleep(1)
            grupoToSend.click()
            chatbox = self.driver.find_element_by_class_name('p3_M1')
            time.sleep(1)
            chatbox.click()
            time.sleep(1)
            chatbox.send_keys(self.mensagem)
            botaoEnviar = self.driver.find_element_by_xpath("/html/body/div[1]/div/div/div[4]/div/footer/div[1]/div/span[2]/div/div[2]/div[2]/button")
            # botaoEnviar = self.driver.find_element_by_class_name("_3HQNh")
            time.sleep(1)
            botaoEnviar.click()
            time.sleep(3)


bot = WhatsappBot()
bot.EnviarMensagens()