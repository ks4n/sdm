from selenium import webdriver
from time import sleep


class Botzera:
    def __init__(self):
        self.driver = webdriver.Firefox()
        self.ip_missao = ''
        self.driver.get('https://hackerwars.io')
        self.missoes_resolvidas = 0

    def limpar_log(self):
        self.driver.get('https://hackerwars.io/internet?view=logs')
        sleep(1)
        self.driver.find_element_by_name("log").click()
        sleep(1)
        self.driver.find_element_by_name("log").clear()
        sleep(1)
        self.driver.find_element_by_name("log").send_keys("    ")
        sleep(1)
        self.driver.find_element_by_xpath("//input[@value='Edit log file']").click()
        print('log limpo')
        sleep(5)

    def verificar_missao(self):
        self.driver.get('https://hackerwars.io/missions')
        sleep(2)
        try:
            self.driver.find_element_by_link_text("Destroy server").click()
            sleep(3)
            id_missao = str(self.driver.current_url).split('id=')[1]
            self.driver.find_element_by_xpath(f"//span[@value='{id_missao}']").click()
            sleep(3)
            self.driver.find_element_by_xpath("//input[@value='Accept']").click()
            sleep(2)
            print('achou missao')
            Botzera.get_info_missao(self)
        except:
            print('sem missao ddos')
            sleep(60)

    def get_info_missao(self):
        self.driver.get('https://hackerwars.io/missions')
        sleep(5)
        self.ip_missao = self.driver.find_element_by_class_name('link-default').text
        Botzera.logar_no_ip(self)

    def logar_no_ip(self):
        self.driver.get(f'https://hackerwars.io/internet?ip=0.0.0.0')  # isto serve para evitar erro de ja esta logado
        self.driver.get(f'https://hackerwars.io/internet?ip={self.ip_missao}')
        sleep(2)
        self.driver.get('https://hackerwars.io/internet?action=login')
        sleep(3)
        if 'root' not in self.driver.page_source:
            for c in range(3):
                self.driver.get('https://hackerwars.io/internet?action=hack&method=xp')
                sleep(4)

        self.driver.find_element_by_xpath("//input[@value='Login']").click()
        sleep(2)
        Botzera.limpar_log(self)
        sleep(4)
        Botzera.enviar_ddos(self)

    def completar_missao(self):
        self.driver.get('https://hackerwars.io/missions')
        get_btn_complete = str(self.driver.page_source).split('<span class="btn btn-success mission-complete" value="')[1].split('">Complete Mission</span>')[0]
        print(get_btn_complete)
        sleep(5)
        self.driver.find_element_by_xpath(f"//span[@value='{get_btn_complete}']").click()
        sleep(10)
        self.driver.find_element_by_id("modal-submit").click()
        sleep(10)
        self.missoes_resolvidas += 1
        print(f'Foram resolvidas {self.missoes_resolvidas} missoes')
        Botzera.main(self)

    def enviar_ddos(self):
        while True:
            self.driver.get('https://hackerwars.io/missions')
            sleep(2)
            if 'Complete Mission' in self.driver.page_source:
                self.driver.get(f'https://hackerwars.io/internet?ip=0.0.0.0')
                sleep(1)
                self.driver.get(f'https://hackerwars.io/internet?ip={self.ip_missao}')
                sleep(3)
                self.driver.get('https://hackerwars.io/internet?action=login')
                sleep(1)
                self.driver.find_element_by_xpath("//input[@value='Login']").click()
                sleep(2)
                Botzera.limpar_log(self)
                sleep(1)
                Botzera.completar_missao(self)

            else:
                Botzera.limpar_log(self)
                self.driver.get("https://hackerwars.io/list?action=ddos")
                self.driver.find_element_by_name("ip").click()
                self.driver.find_element_by_name("ip").clear()
                self.driver.find_element_by_name("ip").send_keys(f'{self.ip_missao}')
                self.driver.find_element_by_xpath("//input[@value='Launch DDoS!']").click()
                sleep(310)

    def main(self):
        while True:
            Botzera.verificar_missao(self)



ddos = Botzera()
login = input('Fez loggin aperta enter')
ddos.main()
