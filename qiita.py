import pyperclip as ppc
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

# driver = webdriver.Chrome('chromedriver')
# # ()内のURLに移動(ここではgoogleの初期画面)
# driver.get('https://www.deepl.com/translator')
# stextarea = driver.find_element_by_css_selector('.lmt__textarea.lmt__source_textarea.lmt__textarea_base_style')
# ttextarea = driver.find_element_by_css_selector('.lmt__textarea.lmt__target_textarea.lmt__textarea_base_style')
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
    #4500文字以降で一番初めのピリオドの位置を見つける
    find_comma = join_lines.find('.')
    if find_comma != -1:
        _tmpblock += join_lines[:find_comma+1]
        join_lines = join_lines[find_comma+1:]
    separated_block.append(_tmpblock)

#deepLの翻訳ページにアクセス
driver = webdriver.Chrome('chromedriver')
driver.get('https://www.deepl.com/translator')
#stextareaにseparated_blockの内容をペーストし、翻訳結果がttextareaの部分に返ってくるのでそれをoutput_textに連結します
#cssのセレクタ名は今後変更になる場合があります。chromeの検証ツール等を使って確認してください
stextarea = driver.find_element_by_css_selector('.lmt__textarea.lmt__source_textarea.lmt__textarea_base_style')
ttextarea = driver.find_element_by_css_selector('.lmt__textarea.lmt__target_textarea.lmt__textarea_base_style')

output_text = ''
for block in separated_block:

    ppc.copy(block)
    stextarea.send_keys(Keys.CONTROL,"v")
    #翻訳が返ってくるまで待ちます(もう少し短くていいかも、、、)
    time.sleep(15)

    output_text += ttextarea.get_property("value")
    #英文入力フォームを空にします
    stextarea.send_keys(Keys.CONTROL, "a")
    stextarea.send_keys(Keys.BACKSPACE)
    
driver.quit()
ppc.copy(output_text)
f = open('output.txt','w')
f.write(output_text)
f.close()