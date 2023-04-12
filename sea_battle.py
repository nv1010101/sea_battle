from random import randint
from itertools import product


class Field:

    def __init__(self):
        self.counter_of_ships = None
        self.size = None
        self.field = None
        self.ship_point = "■"
        self.name = ""
        self.field_viz = None
        # self.list_of_ship = (3, 2, 2, 1, 1, 1, 1)

    def is_loose(self):
        number_of_ships = self.count_of_ships()
        if number_of_ships <= 0:
            return True
        else:
            return False

    def init_field(self, name):
        self.field = [["O"] * 8 for _ in range(8)]
        self.name = name
        self.game_board_creation()

    def rendering(self, invisible):
        print("\n", self.name)
        print(f"    1   2   3   4   5   6 ")
        for i in range(1, 7):
            st = f"{i} | "
            for j in range(1, 7):
                st = st + f"{self.field[i][j]} | "
            if invisible:
                st = st.replace('■', 'O')
                print(st)
            else:
                print(st)

    def game_board_creation(self):
        counter = 0
        while counter != 11:
            for i in (3, 2, 2, 1, 1, 1, 1):
                self.add_ship(i)
                counter = self.count_of_ships()

    def add_ship(self, size):
        self.size = size
        vertical = randint(0, 1)

        if self.size == 1:  # одноточечный корабль
            y, x = randint(1, 6), randint(1, 6)
            if self.field[y][x] == "O":
                self.field[y][x] = "■"
                self.near_1_point_ship(x, y, s="O")
                # return True

        elif size == 2 and vertical == 0:  # двухточечный корабль горизонтальный
            y, x = randint(2, 6), randint(2, 6)

            if self.field[y][x] == self.field[y][x - 1] == "O":
                self.field[y][x] = "■"
                self.field[y][x - 1] = "■"
                self.near_2_point_ship_horizontal(x, y, s="O")

        elif size == 2 and vertical == 1:  # двухточечный корабль вертикальный
            y, x = randint(2, 6), randint(1, 6)
            if self.field[y][x] == self.field[y - 1][x] == "O":
                self.field[y][x] = "■"
                self.field[y - 1][x] = "■"
                self.near_2_point_ship_vertical(x, y, s="O")

        elif size == 3 and vertical == 0:  # трехточечный корабль горизонтальный
            y, x = randint(1, 6), randint(3, 6)
            if self.field[y][x] == self.field[y][x - 1] == self.field[y][x - 2] == "O":
                self.field[y][x] = "■"
                self.field[y][x - 1] = "■"
                self.field[y][x - 2] = "■"
                self.near_3_point_ship_horizontal(x, y, s="O")

        elif size == 3 and vertical == 1:  # трехточечный корабль вертикальный
            y, x = randint(3, 6), randint(3, 6)
            if self.field[y][x] == self.field[y - 1][x] == self.field[y - 2][x] == "O":
                self.field[y][x] = "■"
                self.field[y - 1][x] = "■"
                self.field[y - 2][x] = "■"
                self.near_3_point_ship_vertical(x, y, s="O")

    #
    # def is_add_1(self, x0, y0):
    #     for y in range(y0 - 1, y0 + 1):
    #         for x in range(x0 - 1, x0 + 1): # range ???
    #             if self.field[y][x] == "■":
    #                 return False
    #     return True

    # def is_add_2(self, x0, y0, orientation="H"):
    #     if orientation == "H":
    #         for y in range(y0 - 1, y0 + 1):
    #             for x in range(x0 - 1, x0 + 2): # range ???
    #                 if self.field[y][x] == "■":
    #                     return False
    #         return True
    #     else:
    #         for y in range(y0 - 1, y0 + 2):
    #             for x in range(x0 - 1, x0 + 1): # range ???
    #                 if self.field[y][x] == "■":
    #                     return False
    #         return True

    def near_1_point_ship(self, x, y, s):
        # todo переименовать is_add_1

        self.field[y + 1][x] = s  # вверх
        self.field[y - 1][x] = s  # низ

        for i in (y, y + 1, y - 1):
            self.field[i][x + 1] = s  # право

        for i in (y, y + 1, y - 1):
            self.field[i][x - 1] = s  # низ

    def near_2_point_ship_horizontal(self, x, y, s):
        for i in (y, y + 1, y - 1):
            self.field[i][x - 2] = s  # лево
            self.field[i][x + 1] = s  # право

        self.field[y - 1][x - 1] = s  # вверх
        self.field[y - 1][x] = s
        self.field[y + 1][x - 1] = s  # низ
        self.field[y + 1][x] = s

    def near_2_point_ship_vertical(self, x, y, s):
        for i in (y, y + 1, y - 1, y - 2):
            self.field[i][x - 1] = s  # лево
            self.field[i][x + 1] = s  # право

        self.field[y - 2][x] = s  # вверх
        self.field[y + 1][x] = s  # низ

    def near_3_point_ship_horizontal(self, x, y, s):
        for i in (y, y + 1, y - 1):
            self.field[i][x - 3] = s  # лево
            self.field[i][x + 1] = s  # право

        for i in (x, x - 1, x - 2):  # вверх
            self.field[y - 1][i] = s

        for i in (x, x - 1, x - 2):  # вверх
            self.field[y + 1][i] = s

    def near_3_point_ship_vertical(self, x, y, s):
        for i in (y, y + 1, y - 1, y - 2):
            self.field[i][x - 1] = s  # лево
            self.field[i][x + 1] = s  # право

        for i in (x, x + 1, x - 1):  # вверх
            self.field[y - 3][i] = s
        self.field[y + 1][x] = s  # низ

    def count_of_ships(self):
        self.counter_of_ships = 0
        for i in self.field:
            for j in i:
                if j == "■":
                    self.counter_of_ships += 1
        return self.counter_of_ships

    def ship_shooting(self, y, x):
        if self.field[y][x] == "O":
            self.field[y][x] = "."
            return

        counter = 0
        for a, b in product((y, y + 1, y - 1), (x, x + 1, x - 1)):  # подсчет поврежденных ячеек корабля в окрестности

            if self.field[a][b] == "X":
                counter += 1
                y2, x2 = a, b

                for a, b in product((y2, y2 + 1, y2 - 1), (x2, x2 + 1, x2 - 1)):
                    if self.field[a][b] == "X":
                        counter += 1
                        y3, x3 = a, b

        if counter == 0:  # однопалубный корабль
            flag_found = False
            self.field[y][x] = "X"

            for a, b in product((y, y + 1, y - 1), (x, x + 1, x - 1)):
                if self.field[a][b] == "■":
                    flag_found = True

            if not flag_found:
                for a, b in product((y, y + 1, y - 1), (x, x + 1, x - 1)):
                    self.field[a][b] = "."
                    self.field[y][x] = "X"

        if counter == 2:  # двухпалубный корабль с одной поврежденной ячейкой
            print(counter)
            for a, b in product((y, y + 1, y - 1), (x, x + 1, x - 1)):
                self.field[a][b] = "."

            for a, b in product((y2, y2 + 1, y2 - 1), (x2, x2 + 1, x2 - 1)):
                self.field[a][b] = "."

            self.field[y][x] = "X"
            self.field[y2][x2] = "X"

        if counter == 3:  # трехпалубный корабль с двумя поврежденными ячейками
            for a, b in product((y, y + 1, y - 1), (x, x + 1, x - 1)):
                self.field[a][b] = "."

            for a, b in product((y2, y2 + 1, y2 - 1), (x2, x2 + 1, x2 - 1)):
                self.field[a][b] = "."

            for a, b in product((y3, y3 + 1, y3 - 1), (x3, x3 + 1, x3 - 1)):
                self.field[a][b] = "."

            self.field[y][x] = "X"
            self.field[y2][x2] = "X"
            self.field[y3][x3] = "X"

        if counter == 4:  # трехпалубный корабль с одной поврежденной ячейкой по центру

            for a, b in product((y, y + 1, y - 1), (x, x + 1, x - 1)):
                if self.field[a][b] == "X":
                    self.field[a][b] = "■"
                    y1, x1 = a, b
                    self.field[y][x] = "X"
                    break
            for a, b in product((y1, y1 + 1, y - 1), (x1, x1 + 1, x1 - 1)):
                self.field[a][b] = "."

            for a, b in product((y2, y2 + 1, y2 - 1), (x2, x2 + 1, x2 - 1)):
                self.field[a][b] = "."

            for a, b in product((y3, y3 + 1, y3 - 1), (x3, x3 + 1, x3 - 1)):
                self.field[a][b] = "."

            self.field[y1][x1] = "X"
            self.field[y][x] = "X"
            self.field[y3][x3] = "X"


class Player:
    def __init__(self):
        self.list_of_coordinates = []
        self.coordinates = ()
        
    def input_coordinates_from_player(self):
        while True:
            try:
                x = int(input("Введите координату по x: "))
                y = int(input("Введите координату по y: "))
                coordinates = tuple((x, y))

                if coordinates in self.list_of_coordinates:
                    print("Вы уже стреляли в эту клетку! Повторите попытку!")
                    continue

                if y in range(1, 7) and x in range(1, 7):
                    self.list_of_coordinates.append(coordinates)
                    return y, x

                else:
                    print("Ошибка ввода! Только целые числа от 11 до 6. Пожалуйста повторите! ")
                    continue

            except IndexError:
                print("Ошибка ввода! Только целые числа от 1 до 6. Пожалуйста повторите! ")
            except ValueError:
                print("Ошибка ввода! Только целые числа от 1 до 6. Пожалуйста повторите! ")

    def get_coordinates_for_ai(self):
        while True:
            x = randint(1, 6)
            y = randint(1, 6)
            coordinates = tuple((y, x))

            if coordinates in self.list_of_coordinates:
                # print("AI ты же уже стрелял в эту клетку! Повтори попытку!")
                continue
            else:
                self.list_of_coordinates.append(coordinates)
                # print(self.list_of_coordinates)
                print(f"AI стреляет в клетку: x {x} y {y} ")
                return y, x

class Game:
    plr_field = Field()
    ai_field = Field()
    pl = Player()
    ai = Player()
    plr_field.init_field("Поле игрока")
    ai_field.init_field("Поле AI")

    plr_field.rendering(invisible=False)
    ai_field.rendering(invisible=True)

    def game_loop(self):
        print("\nМорской бой \nИгра началась!")

        while True:
            y, x = self.pl.input_coordinates_from_player()
            self.ai_field.ship_shooting(y, x)
            self.plr_field.rendering(invisible=False)
            self.ai_field.rendering(invisible=True)

            if self.ai_field.is_loose():
                print("Победил Игрок")
                break

            y, x = self.ai.get_coordinates_for_ai()
            self.plr_field.ship_shooting(y, x)
            self.plr_field.rendering(invisible=False)
            self.ai_field.rendering(invisible=False)

            if self.plr_field.is_loose():
                print("Победил АИ")
                break

            # print("Остаток общего здоровья у кораблей у игрока: ", self.plr_field.count_of_ships())
            # print("Остаток общего здоровья у кораблей у AI: ", self.ai_field.count_of_ships())


g = Game()
g.game_loop()
