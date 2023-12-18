from data_visualizer import DataVisualizer

def runner():
    print("Лабораторна робота №8: Візуалізація даних з CSV-файлу")
    while True:
        csv_file = input("Введіть назву CSV-файлу: ")
        visualizer = DataVisualizer(csv_file)

        if visualizer.data is not None:
            break
        else:
            print("Файл не знайдено або виникла помилка. Будь ласка, спробуйте ще раз.")

    while True:
        print("\nДоступні опції:")
        print("1 - Дослідити дані")
        print("2 - Базова візуалізація")
        print("3 - Складна візуалізація")
        print("4 - Декілька піддіаграм")
        print("5 - Експорт візуалізації")
        print("0 - Вийти")

        choice = input("Виберіть опцію: ")

        if choice == '1':
            print("\nРезультат дослідження даних:")
            print(visualizer.explore_data())

        elif choice == '2':
            col = input("Введіть назву колонки для базової візуалізації: ")
            visualizer.basic_visualization(col)

        elif choice == '3':
            col_x = input("Введіть назву першої колонки: ")
            col_y = input("Введіть назву другої колонки: ")
            visualizer.advanced_visualization(col_x, col_y)

        elif choice == '4':
            cols = input("Введіть назви колонок через кому для множинних піддіаграм: ").split(',')
            visualizer.multiple_subplots(cols)

        elif choice == '5':
            filename = input("Введіть назву файлу для експорту: ")
            visualizer.export_visualization(filename)

        elif choice == '0':
            break

        else:
            print("Невідома опція. Спробуйте знову.")
