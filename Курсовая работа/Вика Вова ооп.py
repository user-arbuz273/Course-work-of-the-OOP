import pandas as pd

def choice_group_viewing():
    choice_group = input("Введите код группы, чьё расписание хотите увидеть ")
    #20250
    if choice_group == "20250":
        cols = [0,1,2,3,4,5,6]
        df = pd.read_excel('20250.xlsx', usecols=cols)
        pd.set_option('display.max_columns', None,
                        'display.max_rows', None)
        pd.options.display.expand_frame_repr = False
        print(df)
    #20290
    if choice_group == "20290":
        cols = [0,1,2,3,4,5,6]
        df = pd.read_excel('20290.xlsx', usecols=cols)
        pd.set_option('display.max_columns', None,
                        'display.max_rows', None)
        pd.options.display.expand_frame_repr = False
        print(df)
    #20291
    if choice_group == "20291":
        cols = [0,1,2,3,4,5,6]
        df = pd.read_excel('20291.xlsx', usecols=cols)
        pd.set_option('display.max_columns', None,
                        'display.max_rows', None)
        pd.options.display.expand_frame_repr = False
        print(df)

    print("Хотите посмотреть расписание других групп?")
    choice1 = input("yes/no  ")
    if choice1 == "yes":
        return choice_group_viewing()

choice_group_viewing()