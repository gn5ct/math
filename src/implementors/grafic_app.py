from src.core import chek, calk, random_primer
import dearpygui.dearpygui as dpg

class GUI:
    def __init__(self):
        self.example = random_primer()
        self.answer = calk(self.example)
    def paint_answer(self):
        user_answer = dpg.get_value(item='answer')
        result = chek(correct=self.answer, user_input=user_answer)
        print(result)
    def start(self):
        dpg.create_context()
        dpg.create_viewport(width=332, height=342)
        with dpg.font_registry():
            with dpg.font('./ofont.ru_Zeitmax.ttf', 20, tag='ofont'):
                dpg.add_font_range_hint(dpg.mvFontRangeHint_Cyrillic)
        with dpg.window(tag='main'):
            dpg.add_text(self.example)
            dpg.add_input_float(tag='answer')
            dpg.add_button(label='Проверить ответ', callback=self.paint_answer)
        dpg.set_primary_window(window='main', value=True)
        dpg.bind_font('ofont')
        dpg.setup_dearpygui()
        dpg.show_viewport()
        dpg.start_dearpygui()
        dpg.destroy_context()

def graphic_version():
    t = GUI()
    t.start()




