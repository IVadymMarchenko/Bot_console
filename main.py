#(KeyError, ValueError, IndexError

def input_error(func):
    def wrapper(*args, **kwargs):
        try:
            result = func(*args, **kwargs)
            return result
        except ValueError as e:
            return f"Помилка: Не вірне вхідне значення - {e}"
        except KeyError as e:
            return f"Помилка: Такого контакту не існує - {e} "
        except IndexError as e:
            return f"Помилка: введіть коректні данні - {e}"
    return wrapper


CONTACTS_DICT={'vadym': 2522}
@input_error
def hello(string='hello'):
    if string=='hello':
        return "How can I help you?"
    raise ValueError(string)
@input_error
def add(*args):
    if len(args) != 2 or args[0] in CONTACTS_DICT:
        raise ValueError("Введіть ім'я та телефон через пробіл після команди add, або контакт с таким ім'ям вже є в записах")
    CONTACTS_DICT[args[0]] = args[1]
    return f'контакт {args[0]} доданий до контактів'
@input_error
def change(*args):
    if len(args) == 2 and args[0] in CONTACTS_DICT:
        CONTACTS_DICT[args[0]]=args[1]
        return f'Телефон контакту {args[0]} успішно змінено на: {args[1]}'
    raise KeyError(f'"{args[0]}" або вы ввели не вірно телефон')
@input_error
def phone(name):
    if name and name in CONTACTS_DICT:
        return f'Телефон {name} - {CONTACTS_DICT[name]}'
    raise ValueError(f"<{name}>, Введіть им'я контакту який є в телефоній книзі")
@input_error
def show(string):
    contacts=[]
    if string and string=='show all':
        for name,phone in CONTACTS_DICT.items():
            contacts.append(f'{name}: {phone}\n')
        return ''.join(contacts)
    raise ValueError(string)

def main():
    while True:
        command=input('Введіть команду: ').strip().lower()
        if command in ["good bye", "close", "exit"]:
            print("Good bye!")
            break
        if command=='show all':
            result=show(command)
            print(result)
            continue
        split_commad=command.split()
        user_commad=split_commad[0]
        function_argument=split_commad[1:]
        function_dict={'hello': hello,
                       'add': add,
                       'change': change,
                       'phone':phone,
                       }
        if user_commad in function_dict:
            function_dict_command=function_dict[user_commad]
            result=function_dict_command(*function_argument)
            print(result)
        else:
            print(f"Помилка: Не відома команда - {user_commad}")

if __name__=='__main__':
    main()
















