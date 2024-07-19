import openpyxl
wb = openpyxl.Workbook()
list = wb.active
a1=list["A1"]
list["A1"]='День недели'

b1=list["B1"]
list["B1"]='Время'

c1=list["C1"]
list["C1"]='Неделя'

d1=list["D1"]
list["D1"]='Аудитория'

e1=list["E1"]
list["E1"]='Группа'

f1=list["E1"]
list["F1"]='Предмет'

g1=list["G1"]
list["G1"]='Преподаватель'

yach=['A','B','C','D','E','F','G']
for i in range(2,31):
    m = input('Добавить строчку? ')
    if m=='yes':
        for j in range(0,7):
            n=input('Ввод ')
            a2=list[f"{yach[j]}{i}"]
            list[f'{yach[j]}{i}']=n
    else:
        break
wb.save('новое расписание.xlsx')