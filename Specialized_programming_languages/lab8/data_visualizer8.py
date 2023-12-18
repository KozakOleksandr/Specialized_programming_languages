import pandas as pd
import matplotlib.pyplot as plt


class DataVisualizer:
    def __init__(self, csv_file):
        self.data = self.load_data(csv_file)

    @staticmethod
    def load_data(csv_file):
        # Завантаження даних
        try:
            return pd.read_csv(csv_file)
        except FileNotFoundError:
            print(f"Файл не знайдено: {csv_file}")
            return None

    def explore_data(self):
        # Дослідження даних
        if self.data is not None:
            return self.data.describe()
        else:
            return "Дані не завантажено."

    def basic_visualization(self, column_name):
        # Базова візуалізація (наприклад, гістограма)
        if self.data is not None and column_name in self.data.columns:
            self.data[column_name].hist()
            plt.xlabel(column_name)
            plt.ylabel('Частота')
            plt.title(f'Гістограма для {column_name}')
            plt.show()
        else:
            print(f"Колонка {column_name} не знайдена.")

    def advanced_visualization(self, column_x, column_y):
        # Складна візуалізація (наприклад, діаграма розсіювання)
        if self.data is not None:
            plt.scatter(self.data[column_x], self.data[column_y])
            plt.xlabel(column_x)
            plt.ylabel(column_y)
            plt.title(f'Діаграма розсіювання: {column_x} vs {column_y}')
            plt.show()
        else:
            print("Дані не завантажено або колонки не знайдено.")

    def multiple_subplots(self, columns):
        # Створення декількох піддіаграм
        if self.data is not None:
            fig, axs = plt.subplots(len(columns), figsize=(10, 5))
            for i, col in enumerate(columns):
                if col in self.data.columns:
                    axs[i].plot(self.data[col])
                    axs[i].set_title(col)
                else:
                    print(f"Колонка {col} не знайдена.")
            plt.tight_layout()
            plt.show()
        else:
            print("Дані не завантажено.")

    def export_visualization(self, filename, file_format='png'):
        # Експорт останньої візуалізації
        plt.savefig(f'{filename}.{file_format}')
