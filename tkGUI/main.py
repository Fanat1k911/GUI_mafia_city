import customtkinter as ctk
import tkinter as tk
from tkinter.ttk import Style
from PIL import Image, ImageTk

# Глобальные размеры окна приложения, относительно размера и расположения окна игры
global_height = 500
global_width = 700

# gameplay lists
resurces = ['Центр карго', 'Денежный центр', 'Склад амуниции', 'Металлургический завод']
killers = ['Наёмники', 'Призрак', 'Жнец', 'Арес', 'Черный риф', 'Скелетон']
main_window = ['Помощь леди', 'Помощь клану', 'Награда', 'SVIP', 'Богатый урожай', 'Вытянуть модификацию', 'Общее меню',
               'Получить золото(бонус)', 'Совместные задания клана', 'Инвестиции клана', 'Подарки клана',
               'Стратегический курс', 'Вылечить раненных', 'Инвестировать', 'Услуги киллеров', 'Констабандист']

# help lists
# набор цветов
colors = ['gray', 'brown', 'red', 'orange', 'yellow', 'lime', 'green', 'cyan', 'blue', 'navy',
          'magenta', 'purple', 'violet', 'pink']
# Заголовки фреймов
draw_frames = ['Главная', 'Ресурсы', 'Наемники', 'Уличные группировки']


class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        ctk.set_appearance_mode('light')
        ctk.set_default_color_theme('green')

        self.wm_title('FARM MACHINE')
        # self.geometry("100+100")
        self.resizable(False, False)
        self.logo = ctk.CTkImage(
            dark_image=Image.open('/Users/a12345/PycharmProjects/autoGUI_39/tkGUI/softImage/vertical-gf.jpg'),
            size=(global_height, global_width),
        )
        self.label = ctk.CTkLabel(master=self, text='', image=self.logo)
        self.label_logo = self.label
        self.label_logo.grid(column=1, rowspan=len(draw_frames), columnspan=global_width)

        state_glavnaya = ctk.BooleanVar()
        state_recurces = ctk.BooleanVar()
        state_killers = ctk.BooleanVar()
        state_street_killers = ctk.BooleanVar()
        state_glavnaya.set(True)
        # state_glavnaya.trace_add('w', on_change)

        for stage in range(0, len(draw_frames)):
            self.main_stage = tk.LabelFrame(master=self,
                                            text=draw_frames[stage],
                                            bg=colors[7])
            self.main_stage.grid(row=stage, column=0, sticky='we')
            print(colors[stage])

            if draw_frames[stage] == 'Главная':
                self.ckButton = ctk.CTkCheckBox(master=self.main_stage,
                                                text='Главный сценарий',
                                                variable=state_glavnaya,
                                                height=global_height / len(draw_frames))
                self.ckButton.grid(row=0, column=0)
                for text in range(len(main_window)):
                    self.main_chkbtn = ctk.CTkCheckBox(master=self.main_stage,
                                                       text=main_window[text],
                                                       checkbox_height=12,
                                                       checkbox_width=12)
                    self.main_chkbtn.grid(row=text, column=0)
                # self.comboButton = ctk.CTkComboBox(master=self.main_stage, values=main_window)
                # self.comboButton.grid(row=1, column=0)
            elif draw_frames[stage] == 'Наемники':
                self.ckButton = ctk.CTkCheckBox(master=self.main_stage,
                                                text=draw_frames[stage],
                                                height=global_height / len(draw_frames))
                self.ckButton.grid(row=0, column=0)
                self.comboButton = ctk.CTkComboBox(master=self.main_stage, values=killers)
                self.comboButton.grid(row=1, column=0)
            elif draw_frames[stage] == 'Ресурсы':
                self.ckButton = ctk.CTkCheckBox(master=self.main_stage,
                                                text=draw_frames[stage],
                                                height=global_height / len(draw_frames))
                self.ckButton.grid(row=0, column=0)
                self.comboButton = ctk.CTkComboBox(master=self.main_stage, values=resurces)
                self.comboButton.grid(row=1, column=0)
            elif draw_frames[stage] == 'Уличные группировки':
                self.ckButton = ctk.CTkCheckBox(master=self.main_stage,
                                                text=draw_frames[stage],
                                                height=global_height / len(draw_frames))
                self.ckButton.grid(row=0, column=0)
                values = [str(i) for i in range(40, 26, -1)]
                self.comboButton = ctk.CTkComboBox(master=self.main_stage, values=values)
                self.comboButton.grid(row=1, column=0)

        # Labels


if __name__ == '__main__':
    app = App()
    app.mainloop()
