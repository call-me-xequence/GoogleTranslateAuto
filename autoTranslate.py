from selenium import webdriver
import time
#commit new branch
from bs4 import BeautifulSoup
import sys

options = webdriver.ChromeOptions()
options.add_argument("--disable-blink-features=AutomationControlled")
options.add_argument("--headless")

driver = webdriver.Chrome(executable_path = r"C:\Users\total\Downloads\chromedriver.exe", options = options)

driver.get("https://translate.google.com/?hl=ru&sl=en&tl=ru&op=translate")

if len (sys.argv) == 3:
    inp = open (sys.argv[1], "r", encoding= 'utf-8')
    out = open (sys.argv[2], "w", encoding= 'utf-8')
else:
    
    inp = open("input.txt", "r", encoding= 'utf-8')
    out = open("output.txt", "w", encoding= 'utf-8')


while True:
    # считываем строку
    line = inp.readline()
    # прерываем цикл, если строка пустая
    if not line:
        break
    if line == '\n':
        out.write('\n')
        continue

    #вставляем строку  в поле ввода
    webInpLine=  driver.find_element_by_class_name("er8xn")
    webInpLine.clear()
    webInpLine.send_keys(line)
    time.sleep(1)
    
    #записываем страницу 
    with open("index.html", "w", encoding='utf-8') as file:
            file.write(driver.page_source)
    
    #считываем сохраненную страницу
    with open("index.html", encoding='utf-8') as file:
            src =file.read()

    soup = BeautifulSoup(src, "lxml")

    #берем перевод и записывем в текстовый файл
    translatedStr = soup.find( class_= "NqnNQd").get_text()
    out.write(translatedStr+'\n')

    


# закрываем файлы
inp.close()
out.close()

