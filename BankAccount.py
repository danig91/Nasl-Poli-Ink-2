# Создайте класс BankAccount с приватным атрибутом balance.
# Реализуйте методы для депозита, снятия и проверки баланса.
# Используйте методы доступа для работы с приватным атрибутом.

from random import randint


class BankAccount:
    def __init__(self):
        self.__balance = randint(0, 1_000_000)

    @property
    def balance(self):
        return self.__balance

    @balance.setter
    def balance(self, cash):
        new_balance = cash + self.__balance

        if new_balance < 0:
            print("Недостаточно средств!")
        else:
            self.__balance = new_balance
