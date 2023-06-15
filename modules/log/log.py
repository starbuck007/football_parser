from pprint import pprint
import datetime


def add(result, path, action, print_console=False):
    with open('log/log.txt', 'a+') as f:
        date = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        row = {'date': date, 'action': action, 'path': path, 'count_rows': len(result), 'data': result}
        print(row, file=f)

        if print_console:
            pprint(row)

        return row
