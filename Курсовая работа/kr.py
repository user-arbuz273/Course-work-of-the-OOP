# import pandas as pd
import openpyxl
# df = pd.read_excel('расписание потока.xlsx')
# parametr=input('Введите по какому параметру выполнить поиск:\n(День недели, Время, Неделя, Аудитория, Группа, Предмет, Преподаватель)\n')
# object=input('Введите объект поиска: ')
#
# df_new = df[df[f'{parametr}'] == f'{object}']
# pd.set_option('display.max_columns', None,
#                          'display.max_rows', None)
# pd.options.display.expand_frame_repr = False
# print(df_new)


class data_processing():
    def __init__(self, vvod):
        self.hours = vvod
        print(self.hours)
        self.data = [str(yach) for yach in input().split(', ')  ]# ввод данных в массив через ", "
        print(self.data)


class obrabotka(data_processing):
    def __init__(self,data):
        print(self.data)
    def obrabatuvatel(self):
        wbrg = openpyxl.load_workbook('Расписание группы.xlsx')
        sheetrg = wbrg.active
        search_sign = "NaN"
        for j in range(65, 72):
            for i in range(1, 29):
                if search_sign == sheetrg[f'{chr(j)}{i}'].value:
                    for b in range(0, 7):
                        print(str(sheetrg[f'{self.row[b]}{i}'].value), end=" ")
                    print("")

go = data_processing(input())

govb = obrabotka(data)