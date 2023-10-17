import csv
import os
import random


class CSVHandler:
    def __init__(self, filename):
        self.filename = filename
        self.data = self.load_csv()

    def load_csv(self):
        with open(self.filename, 'r') as f:
            reader = csv.reader(f)
            data = list(reader)
        return data

    def show(self, output_type='top', num_rows=5, separator=','):
        if num_rows > len(self.data):
            print("В данных меньше {} строк. Вывод всех строк:".format(num_rows))
            num_rows = len(self.data)

        header_row = [self.data[0]]

        if output_type == 'top':
            rows = header_row + self.data[:num_rows]
        elif output_type == 'bottom':
            rows = header_row + self.data[-num_rows:]
        elif output_type == 'random':
            rows = header_row + random.sample(self.data, num_rows)

        # Find the maximum length of the column data for formatting
        col_widths = [max(len(str(x)) for x in col) for col in zip(*rows)]

        # Print header with column borders
        print('| ' + ' | '.join(word.ljust(col_widths[i]) for i, word in enumerate(rows[0])) + ' |')

        # Print separator line
        print('|-' + '-|-'.join('-' * col_width for col_width in col_widths) + '-|')

        # Print each row with column borders
        for row in rows[1:]:
            print('| ' + ' | '.join(word.ljust(col_widths[i]) for i, word in enumerate(row)) + ' |')

    def info(self):
        num_rows = len(self.data) - 1
        num_cols = len(self.data[0])
        print("{}x{}".format(num_rows, num_cols))

        for i in range(num_cols):
            col_data = [row[i] for row in self.data[1:] if row[i] != '']
            col_type = type(col_data[0]) if col_data else str
            print("{}\t{}\t{}".format(self.data[0][i], len(col_data), col_type))

    def del_nan(self):
        self.data = [row for row in self.data if '' not in row]

    def make_ds(self):
        random.shuffle(self.data)
        split_index = int(0.7 * len(self.data))
        train_data = self.data[:split_index]
        test_data = self.data[split_index:]

        if not os.path.exists('workdata'):
            os.makedirs('workdata')
            os.makedirs('workdata/Learning')
            os.makedirs('workdata/Testing')

        with open('workdata/Learning/train.csv', 'w') as f:
            writer = csv.writer(f)
            writer.writerows(train_data)

        with open('workdata/Testing/test.csv', 'w') as f:
            writer = csv.writer(f)
            writer.writerows(test_data)


handler = CSVHandler('pl.csv')
handler.show('random', 6)
handler.info()
handler.del_nan()
handler.show()
handler.info()
handler.make_ds()
