# pip install pytesseract pillow

import pytesseract
from PIL import Image

# Ссылка на картинку
img_path = input('Введите путь к папке: ')
img_path += ('\\', '')[img_path.endswith('\\')]

img_name = input('Введите имя файла: ')
img_name = img_path + img_name

# Открываем наш файл
img = Image.open(img_name)

# укажем путь до тессаракта
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'


# получим название файла
file_name = img.filename
file_name = file_name.split('.')[0]


# Чтобы повысить точность распознавания,
# мы можем передавать параметры конфига
custom_config = r'--oem 3 --psm 6'  # для текста
# custom_config = r'--oem 3 --psm 13'  # для чисел

lang = input('Укажите язык: ')

# вызываем метод image_to_string у pytesseract и указываем ссылку на картинку
# В скобках параметры lang и config
text = pytesseract.image_to_string(img, lang=lang, config=custom_config)
# print(text)


# сохраняем в файл
with open(f'{file_name}.txt', 'wt', encoding='utf-8') as text_file:
    text_file.write(text)
