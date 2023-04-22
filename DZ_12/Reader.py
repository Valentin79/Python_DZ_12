import csv

def reader1(file):
    with open(file, "r", encoding='utf-8') as f:
        result = f.read()
    return result


if __name__ == '__main__':
    ...