import pyperclip as ppc
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.common.action_chains import ActionChains
# from threading import Thread, Lock
import time

# options = webdriver.ChromeOptions()
# options.add_experimental_option("excludeSwitches", ["enable-logging"])
# driver = webdriver.Chrome(executable_path='chromedriver.exe')
# url = "https://office54.net"
# driver.get(url)

driver = webdriver.Chrome('chromedriver')
# ()内のURLに移動(ここではgoogleの初期画面)
driver.get('https://www.deepl.com/translator')
stextarea = driver.find_element_by_css_selector('.lmt__textarea.lmt__source_textarea.lmt__textarea_base_style')
ttextarea = driver.find_element_by_css_selector('.lmt__textarea.lmt__target_textarea.lmt__textarea_base_style')
f = open('sakura.txt', 'r',encoding="utf-8")
data = f.read()
f.close()
# print(data)
# # data.replace('\r\n','aaa')
# print('----------------')
# print(data.rstrip('\n'))

#一行ずつ配列に入れる（改行文字も入ってくれる）
with open('input.txt','r',encoding="utf-8") as f:
    lines = f.readlines()
    # print(lines)

#改行文字を消す    
def remove_n(n):
    return n.rstrip('\n')
remove_n_lines = list(map(remove_n,lines))

#文字列連結
join_lines = ' '.join(remove_n_lines)
print(join_lines)

#前から4500文字＋アルファをとってきて配列に入れる
separated_block = []
while join_lines != "":
    _tmpblock = join_lines[0:4500]
    join_lines = join_lines[4500:]
    find_comma = join_lines.find('.')
    if find_comma != -1:
        _tmpblock += join_lines[:find_comma+1]
        join_lines = join_lines[find_comma+1:]
    separated_block.append(_tmpblock)

output_text = ''
for block in separated_block:

    ppc.copy(block)
    stextarea.send_keys(Keys.CONTROL,"v")
    time.sleep(15)

    translated_text = ttextarea.get_property("value")
    # stextarea.send_keys(Keys.CONTROL, "a")
    stextarea.send_keys(Keys.CONTROL, "a")
    stextarea.send_keys(Keys.BACKSPACE)
    # driver.quit()
    output_text += translated_text
driver.quit()
ppc.copy(output_text)
f = open('output.txt','w')
f.write(output_text)
f.close()