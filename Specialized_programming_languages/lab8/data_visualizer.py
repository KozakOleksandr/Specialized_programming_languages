import pandas as pd
import matplotlib.pyplot as plt


class DataVisualizer:
    def __init__(self, csv_file):
        self.data = self.load_data(csv_file)

    @staticmethod
    def load_data(csv_file):
        try:
            # Loading data
            return pd.read_csv(csv_file)
        except FileNotFoundError:
            print(f"File not found: {csv_file}")
            return None

    def explore_data(self):
        # Explore data
        if self.data is not None:
            return self.data.describe()
        else:
            return "Data not loaded."

    def basic_visualization(self, column_name):
        # Basic visualization (e.g., histogram)
        if self.data is not None and column_name in self.data.columns:
            self.data[column_name].hist()
            plt.xlabel(column_name)
            plt.ylabel('Frequency')
            plt.title(f'Histogram for {column_name}')
            plt.show()
        else:
            print(f"Column {column_name} not found.")

    def advanced_visualization(self, column_x, column_y):
        # Advanced visualization (e.g., scatter plot)
        if self.data is not None:
            plt.scatter(self.data[column_x], self.data[column_y])
            plt.xlabel(column_x)
            plt.ylabel(column_y)
            plt.title(f'Scatter Plot: {column_x} vs {column_y}')
            plt.show()
        else:
            print("Data not loaded or columns not found.")

    def multiple_subplots(self, columns):
        # Creating multiple subplots
        if self.data is not None:
            fig, axs = plt.subplots(len(columns), figsize=(10, 5))
            for i, col in enumerate(columns):
                if col in self.data.columns:
                    axs[i].plot(self.data[col])
                    axs[i].set_title(col)
                else:
                    print(f"Column {col} not found.")
            plt.tight_layout()
            plt.show()
        else:
            print("Data not loaded.")

    def export_visualization(self, filename, file_format='png'):
        # Export the last visualization
        plt.savefig(f'{filename}.{file_format}')