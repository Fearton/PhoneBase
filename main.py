def add_new_contact(contact_data):
    with open('phone_base.txt', 'a') as file:
        for value in contact_data:
            file.write(str(contact_data.get(value)))
            file.write(' ')
        file.write('\n')
    return True

def search_contact(contact_parameter):
    with open('phone_base.txt', 'r') as file:
        lines = file.readlines()

        for line in lines:
            if contact_parameter in line:
                print(line)
    return True

def import_file(file_name, number_of_line = 0):
    with open('phone_base.txt', 'a') as file:
        with open(file_name, 'r') as import_file:
            if number_of_line == 0:
                file.write(import_file.read())
                file.write('\n')
                return True
            lines = import_file.readlines()
            if number_of_line > 0 and number_of_line <= len(lines):
                file.write(lines[number_of_line - 1])
            else:
                print('Error 404: Not Found')
                last_menu()            
    return True

def export_file(file_name, number_of_line = 0):
    with open('phone_base.txt', 'r') as file:
        with open(file_name, 'a') as export_file:
            if number_of_line == 0:
                export_file.write(str(file.read()))
                return True
            lines = file.readlines()
            if number_of_line > 0 and number_of_line <= len(lines):
                export_file.write(lines[number_of_line - 1])
            else:
                print('Error 404: Not Found')
                last_menu()   
    return True

def print_all_base(file_name):
    number_of_line = 1
    with open(file_name, 'r') as file:
        for lines in file.readlines():
            print(f'[{number_of_line}] {lines}', end='')
            number_of_line += 1
    return True

def last_menu():
    print('-----------------------------')
    print('[1] -> Назад')
    print('[2] -> Выход из программы')
    number = int(input('Выберите действие: '))
    if number == 1:
        return main_menu()
    elif number == 2:
        return True
    else:
        print('Error 404: Not Found')
        return last_menu()

def main_menu():
    print('-----------------------------')
    print('[1] -> Ввод данных')
    print('[2] -> Вывод данных')
    print('[3] -> Поиск по базе данных')
    print('[4] -> Импорт базы данных')
    print('[5] -> Экспорт базы данных')
    print('[6] -> Выход из программы')
    number = int(input('Выберите действие: '))

    # Ввод данных
    if number == 1:
        print('-----------------------------')
        name = input('Введите имя: ')
        surname = input('Введите фамилию: ')
        patronymic = input('Введите отчество: ')
        phone_number = input('Введите номер телефона: ')
        
        contact = {
            'name': name,
            'surname': surname,
            'patronymic': patronymic,
            'phone_number': phone_number
        }

        add_new_contact(contact)
        last_menu()  

    # Ввывод данных
    elif number == 2:
        with open('phone_base.txt', 'r') as file:
            print('-----------------------------')
            print(file.read())
        last_menu()

    # Поиск
    elif number == 3:
        print('-----------------------------')
        parameter = input('Поиск: ')
        search_contact(parameter)
        last_menu()

    # Импорт
    elif number == 4:
        print('-----------------------------')
        import_file_name = input('Введите имя импортируемого файла: ')
        print('-----------------------------')
        print('[1] -> Импорт всей базы')
        print('[2] -> Иморт отдельной строки')
        number = int(input('Выберите действие: '))
        if number == 1:
            import_file(import_file_name)
            print('-----------------------------')
            print('Successfully imported')
            last_menu()
        elif number == 2:
            print('-----------------------------')
            print_all_base(import_file_name)
            print('\n')
            number = int(input('Выберите строку для импорта: '))
            if number > 0:
                import_file(import_file_name, number)
                print('-----------------------------')
                print('Successfully imported')
                last_menu()
            else:
                print('Error 404: Not Found')
                last_menu()  
            
    # Экспорт
    elif number == 5:
        print('-----------------------------')
        export_file_name = input('Введите имя файла для экспорта: ')
        print('-----------------------------')
        print('[1] -> Экспорт всей базы')
        print('[2] -> Экспорт отдельной строки')
        number = int(input('Выберите действие: '))
        if number == 1:
            export_file(export_file_name)
            print('-----------------------------')
            print('Successfully exported')
            last_menu()
        elif number == 2:
            print('-----------------------------')
            print_all_base('phone_base.txt')
            print('-----------------------------')
            number = int(input('Выберите строку для экспорта: '))
            if number > 0:
                export_file(export_file_name, number)
                print('-----------------------------')
                print('Successfully exported')
                last_menu()
            else:
                print('Error 404: Not Found')
                last_menu() 

    # Выход
    elif number == 6:
        return True
    
    else:
        print('Error 404: Not Found')
        return main_menu()


main_menu()