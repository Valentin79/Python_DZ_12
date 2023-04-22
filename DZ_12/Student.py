import Reader

class Name:

    def __set_name__(self, owner, name):
        self.param_name = '_' + name

    def __get__(self, instance, owner):
        return getattr(instance, self.param_name)

    def __set__(self, instance, value):
        self.validate(value)
        setattr(instance, self.param_name, value)

    def validate(self, value):
        if not value.isalpha():
            raise ValueError("Имя должно иметь только буквы")
        if not value[0].isupper():
            raise ValueError("Имя должно начинаться с заглавной буквы")


class Range:

    def __init__(self, min_value: int = None, max_value: int = None):
        self.min_value = min_value
        self.max_value = max_value

    def __set_name__(self, owner, name):
        self.param_name = '_' + name

    def __get__(self, instance, owner):
        return getattr(instance, self.param_name)

    def __set__(self, instance, value):
        self.validate(value)
        setattr(instance, self.param_name, value)

    def validate(self, value):
        if not isinstance(value, int):
            raise TypeError(f'Значение {value} должно быть целым число')
        if self.min_value is not None and value < self.min_value:
            raise ValueError(f'Значение {value} должно быть больше или равно{self.min_value}')
        if self.max_value is not None and value > self.max_value:
            raise ValueError(f'Значение {value} должно быть меньше{self.max_value}')


class Student:
    first_name = Name()
    last_name = Name()
    patronymic = Name()
    grade = Range(2, 5)
    ball = Range(0, 100)
    list_subject = []
    all_table_grades = {}
    all_table_balls = {}

    def __init__(self, first_name, last_name, patronymic):
        self.first_name = first_name
        self.last_name = last_name
        self.patronymic = patronymic
        self.list_subject = Reader.reader1("Subject.csv")
        self.all_table_grades = {}
        self.all_table_balls = {}

    def give_a_grade(self, subject, *args):
        """Записываем оценки по предмету: subject - предмет; *args - оценки"""
        subject = subject.capitalize()
        if subject not in self.list_subject:
            print("Предмет не найден")
        else:
            num_list = self.all_table_grades.get(subject)  # берем уже существующие оценки
            if num_list == None:  # при первой инициализации метод .append не работает
                for i in args:  # Вызываем проверку
                    self.grade = i
                num_list = list(args)  # если прошла - записываем первые числа
            else:
                for i in args:  # проверка
                    self.grade = i
                    num_list.append(int(self.grade))  # добавляем числа к существующим

            print(f"{self}: {subject}: {num_list}")
            self.all_table_grades[subject] = num_list  # записываем результат в общий словарь

    def give_a_ball(self, subject, *args):
        """
        Записываем баллы по предмету: subject - предмет; *args - баллы
        (копия метода give_a_grade, только для баллов)
        """
        subject = subject.capitalize()
        if subject not in self.list_subject:
            print("Предмет не найден")
        else:
            num_list = self.all_table_balls.get(subject)  # берем уже существующие баллы
            if num_list == None:  # при первой инициализации метод .append не работает
                for i in args:  # Вызываем проверку
                    self.ball = i
                num_list = list(args)  # если прошла - записываем первые числа
            else:
                for i in args:  # проверка
                    self.ball = i
                    num_list.append(int(self.ball))  # добавляем числа к существующим

            print(f"{self}: {subject}: {num_list}")
            self.all_table_balls[subject] = num_list  # записываем результат в общий словарь

    def _arithmetic_mean(self, num_list):
        result = sum(map(int, num_list)) / len(num_list)
        return f"{'%.2f' % result}"

    def mean_table_grade(self):
        print(self)
        total = []
        for key, value in self.all_table_grades.items():
            for i in map(int, value):
                self.grade = i
            print(f"Имеет оценки по {key}: {value}, В среднем: {Student._arithmetic_mean(self, value)}")
            total.extend(value)
        print(f"Средняя оценка по всем предметам: {Student._arithmetic_mean(self, total)}")

    def mean_table_balls(self):
        print(self)
        total = []
        for key, value in self.all_table_balls.items():
            for i in map(int, value):
                self.ball = i
            print(f"Имеет баллы по {key}: {value}, В среднем: {Student._arithmetic_mean(self, value)}")
            total.extend(value)
        print(f"Средний балл по всем предметам: {(Student._arithmetic_mean(self, total))}")

    def __str__(self):
        return f"Студент {self.first_name} {self.last_name} {self.patronymic}"


if __name__ == '__main__':
    ...

