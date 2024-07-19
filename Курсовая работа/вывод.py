import pandas as pd

class Choose():
    def __init__(self):
        self.cols = [0,1,2,3,4,5,6]
        self.groups = ['20250', '20290', '20291']

    def chosen_group_viewing(self, chosen_group):
        if chosen_group in self.groups:
            df = pd.read_excel(f'{chosen_group}.xlsx', usecols=self.cols)
            pd.set_option('display.max_columns', None,
                        'display.max_rows', None)
            pd.options.display.expand_frame_repr = False
            print(df)

            print("Хотите посмотреть расписание других групп?")
            choice1 = input("yes/no\n")
            if choice1 == "yes":
                return self.chosen_group_viewing(input())
        else:
            print('Введён неверный номер группы номер группы. Повторите попытку: ')
            return self.chosen_group_viewing(input())
        
ch = Choose()
ch.chosen_group_viewing(input())
            