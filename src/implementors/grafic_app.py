from src.core import chek, calk, random_primer
from src.implementors.point_text import Text_points
import dearpygui.dearpygui as dpg
import time

class GUI:
    def __init__(self):
        self.example = random_primer()
        self.answer = calk(self.example)
        self.player_name = ''
        self.leader = Text_points()

    def login(self):
        self.player_name = dpg.get_value(item='name')
        dpg.set_value(item='player_name', value=self.player_name)
        dpg.delete_item('login_group')
        dpg.show_item('game_groups')
        self.leader.add_players(name=self.player_name)


    def update(self):
        self.example = random_primer()
        self.answer = calk(self.example)
        dpg.set_value('example', self.example)
        dpg.set_value('answer', self.answer)

    def paint_answer(self):
        user_answer = dpg.get_value(item='answer')
        result = chek(correct=self.answer, user_input=user_answer)
        print(result)
        if result == True:
            dpg.add_text('правильно', tag='_', parent='main')
            self.leader.plus_point(self.player_name)
        else:
            dpg.add_text('неправильно', tag='_', parent='main')
            self.leader.minus_point(self.player_name)

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
            with dpg.tab_bar():
                with dpg.tab(label='главная'):
                    with dpg.group(tag='login_group'):
                        dpg.add_text('Введите имя - ')
                        dpg.add_input_text(tag='name')
                        dpg.add_button(label='Старт', callback=self.login)
                    with dpg.group(tag='game_groups'):
                        dpg.add_text(tag='player_name')
                        dpg.add_text(self.example, tag='example')
                        dpg.add_input_float(tag='answer')
                        dpg.add_button(label='Проверить', callback=self.paint_answer)
                        dpg.add_button(label='сохранить', callback=self.leader.save)
                        dpg.hide_item('game_groups')
                with dpg.tab(label='лидеры'):
                    dpg.add_text('таблица')
                    self.leader.load()
                    for y in self.leader.players:
                        dpg.add_text(f'имя - {y},  очки - {self.leader.players[y]}')

        dpg.set_primary_window(window='main', value=True)
        dpg.bind_font('ofont')
        dpg.setup_dearpygui()
        dpg.show_viewport()
        dpg.start_dearpygui()
        dpg.destroy_context()

def graphic_version():
    t = GUI()
    t.start()


