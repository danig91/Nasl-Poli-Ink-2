from BankAccount import BankAccount


def run(bank_account):
    while True:
        print(f"\nВаш баланс {bank_account.balance} \u20BF\n")
        try:
            info = int(input("Выберите действие:\n"
                             "1 - Внести депозит\n"
                             "2 - Снять наличные\n"
                             "0 - Завершить программу\n"))
            if info == 1:
                bank_account.balance = (
                    abs(float(input("Пополнение на сумму:\n>> "))))
            elif info == 2:
                bank_account.balance = \
                    -abs(float(input("Сумма для снятия:\n>> ")))
            elif info == 0:
                break
            else:
                print("Соответствие не найдено!")

        except ValueError:
            print("Ввод некорректного значения!")


bank_account = BankAccount()
run(bank_account)
