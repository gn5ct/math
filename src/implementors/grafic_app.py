from src.core import chek, calk, random_primer
import dearpygui.dearpygui as dpg
import time

class GUI:
    def __init__(self):
        self.example = random_primer()
        self.answer = calk(self.example)
        self.player_name = ''
        self.leader

    def login(self):
        self.player_name = dpg.get_value(item='name')
        dpg.delete_item('login_group')
        dpg.show_item('game_groups')

    def update(self):
        self.example = random_primer()
        self.answer = calk(self.example)
        dpg.set_value('text', self.example)
        dpg.set_value('answer', 0)

    def paint_answer(self):
        user_answer = dpg.get_value(item='answer')
        result = chek(correct=self.answer, user_input=user_answer)
        print(result)
        if result == True:
            dpg.add_text('правильно', tag='_', parent='main')
        else:
            dpg.add_text('неправильно', tag='_', parent='main')
        time.sleep(4)
        dpg.delete_item('_')
        self.update()

    def start(self):
        dpg.create_context()
        dpg.create_viewport(width=332, height=342)
        with dpg.font_registry():
            with dpg.font('./ofont.ru_L.ttf', 20, tag='ofont'):
                dpg.add_font_range_hint(dpg.mvFontRangeHint_Cyrillic)
        with dpg.window(tag='main'):
            with dpg.group(tag='login_group'):
                dpg.add_text('Введите имя - ')
                dpg.add_input_text(tag='name')
                dpg.add_button(label='Старт', callback=self.login)
            with dpg.group(tag='game_groups'):
                dpg.add_text(self.example, tag='example')
                dpg.add_input_float(tag='answer')
                dpg.add_button(label='Проверить', callback=self.paint_answer)
                dpg.hide_item('game_groups')

        dpg.set_primary_window(window='main', value=True)
        dpg.bind_font('ofont')
        dpg.setup_dearpygui()
        dpg.show_viewport()
        dpg.start_dearpygui()
        dpg.destroy_context()

def graphic_version():
    t = GUI()
    t.start()


