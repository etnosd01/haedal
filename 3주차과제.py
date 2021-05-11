class pizza:
    pizza_count = 0

    def __init__(self, name, price1, price2):
        self.name = name
        self.price1 = price1
        self.price2 = price2
        pizza.pizza_count += 1

    def info(self):
        print(f'메뉴: {self.name}')
        print(f'M 가격: {self.price1}')
        print(f'L 가격: {self.price2}')
        print()


pizza1 = pizza('갈릭버터쉬림프', 17940, 21540)
pizza2 = pizza('직화불고기', 17940, 21540)
pizza3 = pizza('수퍼슈프림', 17340, 20940)

pizza1.info()
pizza2.info()
pizza3.info()
