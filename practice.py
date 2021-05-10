import pyperclip as ppc
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import os

# userdata_dir = 'UserData'  # カレントディレクトリの直下に作る場合
# os.makedirs(userdata_dir, exist_ok=True)

# options = webdriver.ChromeOptions()
# options.add_argument('--user-data-dir=' + userdata_dir)

# driver = webdriver.Chrome(options=options)
# driver = webdriver.Chrome('chromedriver')
# ()内のURLに移動(ここではgoogleの初期画面)

from selenium import webdriver
        
# options = webdriver.chrome.options.Options()
# profile_path = r"C:\Users\tamada\AppData\Local\Google\Chrome\User"
# options.add_argument('--user-data-dir=' + profile_path)
# # driver = webdriver.Chrome(executable_path='path_to_chromedriver', options=options)
# driver = webdriver.Chrome(options=options)
# driver.get('https://www.evernote.com/Home.action#n=e138c2df-f807-825a-55e9-0375f4b62ef9&s=s509&ses=4&sh=2&sds=5&')

options = Options()
PROFILE_PATH = r"C:\Users\tamada\AppData\Local\Google\Chrome\User Data\Profile 2"
options.add_argument('--user-data-dir=' + PROFILE_PATH)
driver = webdriver.Chrome(options=options)
driver.get('https://www.evernote.com/Home.action#n=e138c2df-f807-825a-55e9-0375f4b62ef9&s=s509&ses=4&sh=2&sds=5&')

ttextarea = driver.find_element_by_css_selector('RichTextArea-entinymce')
translated_text = ttextarea.get_property("value")
print(translated_text)
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
# print(join_lines)

<<<<<<< HEAD
#前から4500文字＋アルファをとってきて配列に入れるるる
=======
#前から4500文字＋アルファをとってきて配列に入れますう
>>>>>>> sub2
separated_block = []
while join_lines != "":
    _tmpblock = join_lines[0:4500]
    join_lines = join_lines[4500:]
    find_comma = join_lines.find('.')
    if find_comma != -1:
        _tmpblock += join_lines[:find_comma+1]
        join_lines = join_lines[find_comma+1:]
    separated_block.append(_tmpblock)

for block in separated_block:
    print(block)
    print('----------------------')