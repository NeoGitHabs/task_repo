from datetime import datetime, date


def my_tasks():
    list_zadach_history = ''
    list_zadach_all = ''
    list_zadach_today = ''

    while True:
        input_get_task = input('\nКошосузбу(add) же карайсызбы(look)?: ')
        if input_get_task == 'add':
            input_get_task_name = input('Эскертменин атын жазыныз: ')
            input_get_data = input('Датасын ушундай форматта жазыныз DD.MM.YYYY): ')
            try:
                date_object = datetime.strptime(input_get_data, '%d.%m.%Y').date()
                today = date.today()
                if date_object == today:
                    list_zadach_today += f'Эскертме: {input_get_task_name} датасы: {input_get_data}\n'
                else:
                    list_zadach_all += f'Эскертме: {input_get_task_name} датасы: {input_get_data}\n'
            except ValueError:
                print("Катаа: Датасын ушундай форматта жазыныз DD.MM.YYYY")

        elif input_get_task == 'look':
            get_look_task = input("Бугунку эскертмелерди коруу учун '1' деп, баарын коруу учун '2' деп жазыныз)?: ")
            if get_look_task == '1':
                if list_zadach_today:
                    print(list_zadach_today)
                else:
                    print('Бугункуго эскерме жок')
            elif get_look_task == '2':
                if list_zadach_all:
                    print(list_zadach_all)
                else:
                    print('Эч кандай эскертме жок!')
            else:
                print('1 же 2 деп гана жазыныз!')
        else:
            print("Катаа: 'add' же 'look' деп жазыныз!")
my_tasks()