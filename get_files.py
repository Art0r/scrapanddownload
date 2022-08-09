import os
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

DATA_FOLDER = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'data')
CHROMEDRIVER_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'chromedriver')
WEBSITE = "https://www.gov.br/receitafederal/pt-br/assuntos/orientacao-tributaria/cadastros/consultas/dados-publicos" \
          "-cnpj "

options = Options()
options.headless = True

service = Service(executable_path=CHROMEDRIVER_PATH)
driver = Chrome(service=service, options=options)
driver.get(WEBSITE)

links = driver.find_elements(by="xpath", value="//*[@class='external-link']")
links = links[:30:]

if not os.path.isdir(DATA_FOLDER):
    os.makedirs(DATA_FOLDER)

file = open(os.path.join(DATA_FOLDER, 'links.txt'), 'w')
file.writelines(link.get_attribute('href') + '\n' for link in links)
file.close()
driver.close()

os.system("wget -i ./data/links.txt -P ./data")
os.system("unzip './data/*.zip' -d ./data")
