from calculator_engine import _Calculator_engine


class Calculator(_Calculator_engine):

    def runCalculator(self):
        while True:

            self._userMenu()
            mainMenuChoice = input("Введіть ваш вибір: ")

            if mainMenuChoice == "1":
                if self.memory is not None:
                    print(f"Число в пам'яті {self.memory}")
                    getParamFromMemory = input("Взяти читсло з пам'яті? Y/N \n").strip().lower()
                    if getParamFromMemory == 'y':
                        firstParam = self.memory
                    else:
                        firstParam = self._getParamValue("Введіть перше число:\n")
                else:
                    firstParam = self._getParamValue("Введіть перше число:\n")

                operator = self._getOperator("Введіть математичний оператор (+, -, *, /, %, ^, √): ")
                if operator == '√':
                    resultOfCalculation = round(self._calculateValue(firstParam, None, operator),self.settings["decimalPlaces"])
                    expression = f" {operator}{firstParam}"
                    print("Результат обчислення виразу:\n",operator, firstParam, "=",resultOfCalculation)
                else:
                    secondParam = self._getParamValue("Введіть друге число:\n")
                    resultOfCalculation = round(self._calculateValue(firstParam, secondParam, operator),self.settings["decimalPlaces"])
                    expression = f"{firstParam} {operator} {secondParam}"
                    print("Результат обчислення виразу:\n",firstParam, operator, secondParam, "=",resultOfCalculation)

                # Додавання результату до історії обчислень
                self._addToHistory(expression, resultOfCalculation)

                if self.settings["useMemory"]:
                    self._storeInMemory(resultOfCalculation)

            elif mainMenuChoice == '2':
                self._changeSettings()
            elif mainMenuChoice == '3':
                self._viewHistory()
            elif mainMenuChoice == '4':
                break