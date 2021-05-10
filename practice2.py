import shutil
import docx
shutil.copy("template.txt","input.txt")

doc = docx.Document()
doc.add_paragraph("aaa")
doc.add_paragraph("bbb")
title = "title"
doc.save(title+'.docx')