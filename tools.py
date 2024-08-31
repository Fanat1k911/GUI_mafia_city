import pyautogui as pg
import pytesseract as tes
from PIL import Image


# while True:
#     print(pg.position())

# 360 681
# cords main_menu ===> 39 348 = x295
def text_from_screen(path_screen, **kwars):
    """
    Принимает на вход путь к скриншоту
     :arg: tuple(координаты)
    :return: str(текст)
    """
    # Преобразование скриншота в формат, подходящий для Pytesseract
    image = Image.open(path_screen)

    # Использование Pytesseract для извлечения текста
    text = tes.image_to_string(image, lang='rus')  # Укажите язык, если нужно

    # Использование Pytesseract для извлечения текста
    # Пример использования функции
    # Укажите координаты (x, y, width, height) для области, которую хотите захватить
    # region = (100, 100, 400, 200)  # (x, y, ширина, высота)
    print("Извлеченный текст:", text)
    return text


# text_from_screen('/Users/a12345/PycharmProjects/autoGUI_39/screenshots/get_loot.png')

print([i for i in range(27,41)])