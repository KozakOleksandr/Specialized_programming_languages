from calculator_engine import Calculator_engine


class Calculator(Calculator_engine):

    def runCalculator(self):
        while True:

            self.userMenu()
            main_menu_choice = input("Enter your choice: ")

            if main_menu_choice == "1":
                if self.memory is not None:
                    print(f"Number in memory {self.memory}")
                    get_param_from_memory = input("Take the number from memory? Y/N \n").strip().lower()
                    if get_param_from_memory == 'y':
                        first_param = self.memory
                    else:
                        first_param = self.getParamValue("Enter first param:\n")
                else:
                    first_param = self.getParamValue("Enter first param:\n")

                operator = self.getOperator("Enter the operator from the ones presented (+, -, *, /, %, ^, √): ")
                if operator == '√':
                    result_of_calculation = round(self.calculateValue(first_param, None, operator),self.settings["decimalPlaces"])
                    expression = f" {operator}{first_param}"
                    print("Result of expression:\n",operator, first_param, "=",result_of_calculation)
                else:
                    second_param = self.getParamValue("Enter second param:\n")
                    result_of_calculation = round(self.calculateValue(first_param, second_param, operator),self.settings["decimalPlaces"])
                    expression = f"{first_param} {operator} {second_param}"
                    print("Result of expression:\n", first_param, operator, second_param, "=", result_of_calculation)

                # Adding the result to the calculation history
                self.add_to_history(expression, result_of_calculation)

                if self.settings["useMemory"]:
                    self.store_in_memory(result_of_calculation)

            elif main_menu_choice == '2':
                self.change_settings()
            elif main_menu_choice == '3':
                self.view_history()
            elif main_menu_choice == '4':
                break