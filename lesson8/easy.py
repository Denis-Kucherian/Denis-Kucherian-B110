from random import randint


def numbers_card(c, min, max):     # создаём неодинаковые номера из интервала
    list1 = []
    while len(list1) < c:
        new = randint(min, max)
        if new not in list1:
            list1.append(new)
    return list1


class Card:               # карточка
    rows = 3              # строка
    cols = 9              # столбец
    nums_in_row = 5       # количество чисел в строке
    data = None           #
    emptynum = 0          #
    crossednum = -1       #

    def __init__(self):
        rand = numbers_card(15, 1, 90)     # список из 15 случайных неодинаковых чисел

        self.data = []
        for i in range(0, self.rows):
            tmp = sorted(rand[self.nums_in_row * i: self.nums_in_row * (i + 1)])
            empty_nums_count = self.cols - self.nums_in_row
            for j in range(0, empty_nums_count):
                index = randint(0, len(tmp))
                tmp.insert(index, self.emptynum)
            self.data += tmp

    def __str__(self):
        delimiter = '--------------------------'
        ret = delimiter + '\n'
        for index, num in enumerate(self.data):
            if num == self.emptynum:
                ret += '  '
            elif num == self.crossednum:
                ret += ' -'
            elif num < 10:
                ret += f' {str(num)}'
            else:
                ret += str(num)

            if (index + 1) % self.cols == 0:
                ret += '\n'
            else:
                ret += ' '

        return ret + delimiter

    def __contains__(self, item):
        return item in self.data

    def cross_num(self, num):
        for index, item in enumerate(self.data):
            if item == num:
                self.data[index] = self.crossednum
                return
        raise ValueError(f'Number not in card: {num}')

    def closed(self) -> bool:
        return set(self.data) == {self.emptynum, self.crossednum}


class Game:
    __usercard = None
    __compcard = None
    __numkegs = 90
    __kegs = []
    __gameover = False

    def __init__(self):
        self.__usercard = Card()
        self.__compcard = Card()
        self.__kegs = numbers_card(self.__numkegs, 1, 90)

    def play_round(self) -> int:
        """
        :return:
        0 - game must go on
        1 - user wins
        2 - computer wins
        """

        keg = self.__kegs.pop()
        print(f'Новый бочонок: {keg} (осталось {len(self.__kegs)})')
        print(f'----- Ваша карточка ------\n{self.__usercard}')
        print(f'-- Карточка компьютера ---\n{self.__compcard}')

        useranswer = input('Зачеркнуть цифру? (y/n)').lower().strip()
        if useranswer == 'y' and not keg in self.__usercard or \
                useranswer != 'y' and keg in self.__usercard:
            return 2

        if keg in self.__usercard:
            self.__usercard.cross_num(keg)
            if self.__usercard.closed():
                return 1
        if keg in self.__compcard:
            self.__compcard.cross_num(keg)
            if self.__compcard.closed():
                return 2

        return 0


if __name__ == '__main__':
    game = Game()
    while True:
        score = game.play_round()
        if score == 1:
            print('You win')
            break
        elif score == 2:
            print('You lose')
            break
