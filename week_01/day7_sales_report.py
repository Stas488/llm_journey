from datetime import datetime

import json

def log(message, path = 'week_01/sales.log'):
    '''Пишет лог в файл {path} '''
    with open(path, 'a', encoding='utf-8') as f:
        f.write(f'[{datetime.now().strftime("%Y-%m-%d %H:%M:%S")}] {message}\n')

def convert(key, value):
    if key == 'quantity':
        return int(value)
    if key == 'price':
        return float(value)
    return value

def load_sales(path):
    with open(path, 'r', encoding='utf-8') as f:
        first_line = f.readline().strip().split(',')
        res = []
        count = 0
        for line in f:
            count+=1
            new_line = line.strip().split(',')
            if len(new_line) != len(first_line):
                log(f'Пропущена строка {count}: неверное число полей')
                continue
            try:
                dict_of_line = {key:convert(key, value) for key,value in zip(first_line, new_line)}
            except ValueError as e:
                log(f'Пропущена строка {count}: ValueError {e}')
                continue
            res.append(dict_of_line)
    return res

def compute_report(rows):
    revenue_by_product = {}
    quantity_by_product = {}
    total_revenue = 0

    for d in rows:
        product = d['product']
        rev = d['quantity'] * d['price']

        total_revenue += rev
        revenue_by_product[product] = revenue_by_product.get(product, 0) + rev
        quantity_by_product[product] = quantity_by_product.get(product, 0) + d['quantity']

    best_seller = max(quantity_by_product, key=quantity_by_product.get)

    return {
        'total_revenue': total_revenue,
        'revenue_by_product': revenue_by_product,
        'best_seller': best_seller,
        'rows_count': len(rows),
    }

def save_report(report, path):

    with open(path, 'w', encoding='utf-8') as f:
        json.dump(report, f, ensure_ascii=False, indent=2)


def main():
    try:
        rows = load_sales('week_01/sales.csv')
    except FileNotFoundError as e:
        log(f'Файл не найден: FileNotFoundError {e}')
        return
    log(f'загружено {len(rows)} строк')
    report = compute_report(rows)
    file_for_report = 'week_01/report.json'
    save_report(report, file_for_report)
    log(f'отчёт сохранён в файле {file_for_report}')


if __name__ == '__main__':
    main()