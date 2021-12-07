class Car:

    def __init__(self, coordinat_x, coordinat_y, travel_direction):
        self.coordinat_x = coordinat_x
        self.coordinat_y = coordinat_y
        self.travel_direction = travel_direction
        self.distanse = 0

    def move(self):
        print("Едем на машине!")
        speed = float(input("C какой скоростью едем (в км/ч)? "))
        time = float(input("Cколько времени едем (в часах)? "))
        distanse_travel = speed * time
        self.distanse += distanse_travel
        print(f"В направлении {self.travel_direction} проехали {distanse_travel} км. Всего {self.distanse} км.")
        user = input("Едем дальше? ")
        if user in ["1", "ok", "yes", "да", "ок"]:
            travel_user = input("Меняем направление? ")
            if travel_user in ["1", "ok", "yes", "да", "ок"]:
                self.travel_direction = input("Введите направление: ")
            self.move()
        else:
            print("В гараж! Пока.")


class Bus(Car):

    def __init__(self, coordinat_x, coordinat_y, travel_direction, count_passenger):
        super().__init__(coordinat_x, coordinat_y, travel_direction)
        self.__count_passenger = count_passenger
        self.passenger = 0
        self.money_fare = 0
        self.distanse_bus = 0

    def end_rouse(self):
        print(f"Конечная! Идем отдыхать. Сегодня заработал {self.money_fare} денег.")
        print(f"{self.money_fare * 0.1} зарплата. Остальное в кассу!")
        self.money_fare = 0
        self.distanse_bus = 0

    def money(self, passenger_enter):
        rate = float(input("Сколько стоит проезд? "))
        money_stop = rate * passenger_enter
        self.money_fare += money_stop
        print(f"Остановка принесла {money_stop} денег. Всего за день {self.money_fare} денег")

    def enter(self):
        passenger_enter = int(input("Cколько пассажиров хочет войти? "))
        if self.__count_passenger == self.passenger:
            print("Автобус полон!!! Никого не взять.")
        elif passenger_enter + self.passenger > self.__count_passenger:
            place = self.__count_passenger - self.passenger
            self.passenger = self.__count_passenger
            print(f"Автобус взял {place} пассажиров, {passenger_enter - place} ждут следующего автобуса.")
            self.money(place)
        else:
            self.passenger += passenger_enter
            print(f"В автобусе {self.passenger} пассажиров.")
            self.money(self.passenger)

    def out(self):
        while True:
            passenger_out = int(input("Cколько пассажиров хочет выйти? "))
            if self.passenger >= passenger_out:
                self.passenger -= passenger_out
                print(f"В автобусе {self.passenger} пассажиров.")
                break
            print("Количество выходящих не может быть больше, чем есть в автобусе.")

    def move(self):
        print("Поехали на автобусе!!!")
        speed = float(input("C какой скоростью едем (в км/ч)? "))
        time = float(input("Cколько времени едем (в часах)? "))
        distanse_travel = speed * time
        self.distanse_bus += distanse_travel
        print(f"В направлении {self.travel_direction} проехали {distanse_travel} км. Всего {self.distanse_bus} км.")
        user = input("Едем дальше? ")
        if user in ["1", "ok", "yes", "да", "ок"]:
            travel_user = input("Меняем направление? - 1\nСадим пассажиров - 2\nВысаживаем пассажиров - 3 ")
            if travel_user == "1":
                self.travel_direction = input("Введите направление: ")
                self.move()
            elif travel_user == "2":
                self.enter()
            elif travel_user == "3":
                self.out()
            self.move()
        else:
            self.end_rouse()


print("Едем на машине.")
car1 = Car(float(input("Координата X начала пути: ")), float(input("Координата Y начала пути: ")),
           float(input("Направление пути: ")))
car1.move()
print("Пересядем на автобус")
bus_1 = Bus(float(input("Координата X начала пути: ")), float(input("Координата Y начала пути: ")),
            float(input("Направление пути: ")), int(input("Количество посадочных мест автобуса: ")))
bus_1.move()

# зачёт!
