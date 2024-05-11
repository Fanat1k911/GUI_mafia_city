import pyautogui as pg
import pygetwindow as pw
import cv2
import psutil
import random


def main_script():
    for proc in psutil.process_iter():
        if proc.name() == 'BlueStacks':
            print(proc)

    help_path = '/Users/a12345/PycharmProjects/autoGUI_39/screenshots/main_menu.png'
    looking = False

    pos = pg.locateOnScreen(help_path, confidence=0.7)
    pg.moveTo(int(pos[0] / 2), int(pos[1] / 2))
    pg.doubleClick(int(pos[0] / 2) + 5, int(pos[1] / 2) + 10, interval=0.1)


def zero_position_window():
    geometry_window_before = pw._pygetwindow_macos.getWindowGeometry('BlueStacks')
    print(f'Расположение и размер окна:{geometry_window_before}')
    left = int(geometry_window_before[0])
    top = int(geometry_window_before[1])
    print(left, top)
    pg.moveTo((left + 40), (top + 30))
    pg.mouseDown(left + 40, top + 30, button='left', duration=1)
    pg.mouseUp(40, 25, button='left', duration=1)
    geometry_window_after = pw._pygetwindow_macos.getWindowGeometry('BlueStacks')
    print(f'Расположение и размер окна:{geometry_window_after}')
    end_pos_x = geometry_window_after[2]
    end_pos_y = geometry_window_after[3]
    pg.moveTo(end_pos_x, end_pos_y)
    pg.sleep(3)
    pg.moveTo(end_pos_x, end_pos_y + 20)
    pg.hotkey('command', 'control')
    pg.dragTo(end_pos_x + 100, end_pos_y + 100, button='left', duration=0.5)


# zero_position_window()

while True:
    try:
        position = pg.locateOnScreen('screenshots/get_loot.png', confidence=0.7)
        print('cords main_menu ===>', int(position[0] / 2), int(position[1] / 2))
        pg.sleep(3)
    except KeyboardInterrupt as e:
        print(e)
        pg.sleep(3)
    except pg.ImageNotFoundException as ie:
        print(ie)
        pg.sleep(3)
