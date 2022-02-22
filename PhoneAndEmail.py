#! python3
#Находит телефонные номера и почту в буфере обмена

import pyperclip,re

phoneRegex = re.compile(r'''(
        (\d{3}|\(\d{3}\))?   #территориальный код
        (\s|-|\.)?           #разделитель
        (\d{3})              #первые 3 цифры
        (\s|-|\.)            #разделитель
        (\d{4})              #последние 4 цифры
        (\s*(ext|x|ext.)\s*(\d{2,5}))?
)''',re.VERBOSE)

# Создание регулярного выражения  для адрессов почты
emailRegex = re.compile(r'''(
            [a-zA-Z0-9._%+-]+       #имя пльзователя
            @                       #символ @
            [a-zA-Z0-9.-]+          #тмя домена
            (\.[a-zA-Z] {2,4})      #остальная часть адресса 
)''',re.VERBOSE)
#Найти соответствия в тексте содержащемся в буфере обмена
text = str(pyperclip.paste())
matches = []
for groups in phoneRegex.findall(text):
    phoneNum = '-'.join([groups[1], groups[3], groups[5]])
    if groups[8] != '':
        phoneNum += ' x' + groups[8]
    matches.append(phoneNum)
for groups in emailRegex.findall(text):
    matches.append(groups[0])
#Скопировать результат в буфер обмена
if len(matches) > 0:
    pyperclip.copy('\n'.join(matches))
    print('Скопированно в буфер обмена:')
    print('\n'.join(matches))
else:
    print('Телефонные номера и адресса почт не обнаружены.')


