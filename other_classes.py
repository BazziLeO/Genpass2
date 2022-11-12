from root_description import *


class Symbolbet:
    def __init__(self, symbolbet=''):
        self.symbolbet = symbolbet
        self.reserve_symbolbet = self.symbolbet
        self.black_string = ''

    def update_reserve(self):
        self.reserve_symbolbet = self.symbolbet

    def add_symbols(self, symbol_list):
        for symbol in symbol_list:
            if len(symbol) != 1:
                return {'Длина всех символов должна быть равна 1': 'Length of symbols should be equal 1'}
            elif self.black_string.count(symbol) == 1:
                return {f'Символ "{symbol}" состоит в черном списке!': f'Symbol "{symbol}" is in black list!'}
            elif self.symbolbet.count(symbol) > 0 or symbol_list.count(symbol) > 1:
                return {
                    'Нельзя, чтобы было несколько символов в symbolbet': 'Two or more similar symbols arent in symbolbet'}
            else:
                self.symbolbet += symbol
        return {'Символы успешно добавлены': 'Symbols correctly added'}

    def delete_symbols(self, symbol_list):
        for e in symbol_list:
            if self.symbolbet.count(e) == 1:
                self.symbolbet = change_symbol(self.symbolbet, e, '')
        return 'Символы успешно удалены'

    def stay_symbols(self, symbol_list):
        for e in symbol_list:
            if self.symbolbet.count(e) == 0:
                return f'Символ "{e}" отсутствует!'
        for e in self.symbolbet:
            if symbol_list.count(e) == 0:
                self.symbolbet = change_symbol(self.symbolbet, e, '')
        return 'Указанные символы оставлены, остальные - успешно удалены'

    def add_black_symbols(self, list_of_symbols):
        for s in list_of_symbols:
            if self.black_string.count(s) > 0 or list_of_symbols.count(s) > 1:
                return 'Нельзя, чтобы было несколько символов в black string'
            else:
                self.symbolbet = change_symbol(self.symbolbet, s, '')
                self.black_string += s

    def delete_black_symbols(self, list_of_symbols):
        for s in list_of_symbols:
            self.black_string = change_symbol(self.black_string, s, '')
            self.symbolbet += s

    def get(self):
        return self.symbolbet

    def get_black(self):
        return self.black_string


class RangeLen:
    def __init__(self, min_len=10, max_len=20):
        self.min_len = int(min_len)
        self.max_len = int(max_len)

    def set(self, min_len='10', max_len='20'):
        if not (str(min_len).isdigit() and str(max_len).isdigit()):
            return 'Являются ли ваши числа - числами?'
        elif int(min_len) > int(max_len):
            return 'Первое число всегда меньше чем второе'
        else:
            self.min_len, self.max_len = int(min_len), int(max_len)
            return 'Диапазон успешно введен'

    def get_random(self):
        return r(self.min_len, self.max_len)

    def get(self):
        return [self.min_len, self.max_len]


class Color:
    def __init__(self, red=0, blue=0, green=0):
        self.red = red
        self.blue = blue
        self.green = green
        self.color = f'#{red:02x}{green:02x}{blue:02x}'

    def set(self, red=0, blue=0, green=0):
        self.red = red
        self.blue = blue
        self.green = green
        self.color = f'#{red:02x}{green:02x}{blue:02x}'

    def get(self):
        return self.color


class Storage:
    def __init__(self, dictionary_of_elements):
        pass

    def add(self, name, description):
        pass

    def delete(self, index):
        pass

    def get(self, index):
        pass


class ScrollList:
    def __init__(self, length=0, scroll="usual"):
        self.scroll = scroll
        self.length = length
        if self.length == 0:
            self.index = 0
        else:
            self.index = 1

    def turn_right(self):
        if self.length > 0:
            if self.index < self.length:
                self.index += 1
            elif self.scroll == "circled" and self.index == self.length:
                self.index = 1

    def turn_left(self):
        if self.length > 0:
            if self.index > 1:
                self.index -= 1
            elif self.scroll == "circled" and self.index < 2:
                self.index = self.length

    def set_index(self, new_index):
        try:
            new_index = int(new_index)
        except:
            return "Error"
        if self.length > 0:
            if 0 < new_index < self.length + 1:
                self.index = new_index

    def get(self, argument):
        if argument == "index":
            return self.index
        elif argument == "length":
            return self.length


class UI:
    def __init__(self):
        self.widget_list = []

    def get_widgets(self):
        return self.widget_list
