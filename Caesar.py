print('Hello this is a Caesar cipher')
def caesar(cipher, rot, language, text): # Функция 
    if language == 'ru': 
        alp = rus_lower
        ALP = rus_upper
        length = 32
    elif language == 'en':
        alp = eng_lower
        ALP = eng_upper
        length = 26
    text_decryption = ''
    if cipher == 1:
        for i in text:
            if i.isalpha() and i.islower():
                text_decryption += alp[(alp.find(i) + rot) % length]
            elif i.isalpha() and i.isupper():
                text_decryption += ALP[(ALP.find(i) + rot) % length]
            else:
                text_decryption += i
        return text_decryption
    if cipher == 2:
        for i in text:
            if i.isalpha() and i.islower():
                text_decryption += alp[(alp.find(i) - rot) % length]
            elif i.isalpha() and i.isupper():
                text_decryption += ALP[(ALP.find(i) - rot) % length]
            else:
                text_decryption += i
        return text_decryption

eng_lower = 'abcdefghijklmnopqrstuvwxyz'
eng_upper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
rus_lower = "абвгдежзийклмнопрстуфхцчшщъыьэюя"
rus_upper = "АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"

print('What are you need encryption or decryption?')  # уточняем информацию зашифровать или расшифровать
while True:  # выясняем зашифровать или расшифровать
    cipher = input('If you want encryption enter "1" if you want decryption enter "2" ')
    if not cipher.isdigit() or 0 < int(cipher) > 2:
        print('This wrong')
        continue
    elif int(cipher) == 0:
        print('This wrong')
        continue
    else:
        break
cipher = int(cipher)  # перевод в целое число
print('What language you have?')
while True:  # Сбор инф. и проверка на язык
    lan = input('If you have English enter "en", if Russian enter "ru" ')
    if lan.lower() == 'en' or lan.lower() == 'ru':
        break
    else:
        print('This is wrong')
        continue
language = lan.lower()  # Перевод в нижний регистр
print('shift step (with shift to the right) ')
while True:  # сбор инф. по сдвигу
    step = input('Введите цифру от 1 до 28 ')
    if not step.isdigit() or 0 < int(step) > 29:
        print('This wrong')
        continue
    elif int(step) == 0:
        print('This wrong')
        continue
    else:
        break
step = int(step)  # сдвиг делаем числом
text = input('Ведите сюда свой текст ')
print(caesar(cipher, step, language, text))
