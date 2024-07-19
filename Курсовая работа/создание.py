import openpyxl

class Creation():
    def __init__(self):
        self.name = ['0', 'День недели', 'Время', 'Неделя', 'Аудитория', 'Группа', 'Предмет', 'Преподаватель']
        self.name2 = ['0', 'a', 'b', 'c', 'd', 'e', 'f', 'g']
        self.name3 = ['0', 'A', 'B', 'C', 'D', 'E', 'F', 'G']
    def creating_schedule(self):
        wb = openpyxl.Workbook()
        list = wb.active
        for num in range(1, 8):
            f'{self.name2}1' == list[f"{self.name3[num]}1"]
            list[f"{self.name3[num]}1"] = f'{self.name[num]}'
        for i in range(2, 31):
            m = input('Добавить строчку? ')
            if m == 'yes':
                for j in range(0, 7):
                    n = input('Ввод ')
                    a2 = list[f"{self.name3[j + 1]}{i}"]
                    list[f'{self.name3[j + 1]}{i}'] = n
            else:
                break
        wb.save('новое расписание.xlsx')

cr= Creation()
cr.creating_schedule()
