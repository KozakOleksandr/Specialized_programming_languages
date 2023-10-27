import math

class _Calculator_engine:

    def __init__(self):
        self.settings = {
            "decimalPlaces": 2,
            "useMemory": True
        }
        self.memory = None  # Словник для збереження значень в пам'яті
        self.history = []  # Список для збереження історії обчислень

    # Метод для зберігання значення в пам'яті
    def _storeInMemory(self, value):
        self.memory = value

    # Метод для отримання значення з пам'яті
    def _recallFromMemory(self):
        return self.memory

    # Метод для додавання запису в історію обчислень
    def _addToHistory(self, expression, result):
        historyEntry = f'Вираз:{expression} Результат:{result}'
        self.history.append(historyEntry)

    # Метод для перегляду історії обчислень
    def _viewHistory(self):
        if not self.history:
            print("Даних в істрії ще немає!")
        for historyEntry in self.history:
            print(historyEntry)

    def _changeSettings(self):

        print("1. Зміна знаків після коми")
        print("2. Налаштування функції пам'яті.")

        choice = input("Введіть ваш вибір: ")
        if choice == '1':
            try:
                places = int(input("Введіть читсло скільки знаків після коми повино бути (0-20): "))
                if 0 <= places <= 20:
                    self.settings["decimalPlaces"] = places
                    print(f"Встановлено {places} знаків після коми!")
                else:
                    print("Кількість знаків що ви ввели виходить за межі дозволеного.")
            except ValueError:
                print("Некоректний ввід.")
        elif choice == '2':
            self.settings["useMemory"] = not self.settings["useMemory"]
            status = "enabled" if self.settings["useMemory"] else "disabled"
            print(f"Статус функції пам'яті {status}.")

    def _calculateValue (self,firstNumber, secondNumber,operator):
            try:
                if operator == '-':
                    return firstNumber - secondNumber
                if operator == '+':
                    return firstNumber + secondNumber
                if operator == '*':
                    return firstNumber * secondNumber
                if operator == '%':
                    return firstNumber % secondNumber
                if operator == '^':
                    return firstNumber ** secondNumber
                if operator == '√':
                    return math.sqrt(firstNumber)
                if operator == '/':
                    if secondNumber == 0:  # Перевірка чи значення не нуль
                        print("Помилка: Ділення на нуль!")
                        return None
                    return firstNumber / secondNumber
            except Exception as e:
                print(f"Виникла помилка: {e}")
                return None

    def _getParamValue(self, inputMessage):
        while True:
            try:
                param = float(input(inputMessage))
                return param
            except ValueError:
                print("Невіртний формат числа, Будь ласк, ввдедіть число знову")

    def _getOperator(self, inputOperatorMasseg):
        while True:
            operator = input(inputOperatorMasseg)
            if operator in ('+', '-', '*', '/', '%', '^', '√'):
                return operator
            else:
                print("Неправильний оператор. Спробуйте ще раз.")

    def _userMenu(self):
        print("\nМеню калькулятора:")
        print("1. Перейти до обчислення виразу.")
        print("2. Змінити налаштування.")
        print("3. Переглянути історію.")
        print("4. Вихід.")