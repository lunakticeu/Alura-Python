import os

def show_options():
    print('Flavour Express\n')
    print('1. Create Restaurant')
    print('2. List Restaurant')
    print('3. Activate Restaurant')
    print('4. Exit\n')

def end_program():
    os.system('clear') 

def invalid_option():
    print('Invalid option!\n')
    input('Type any key to re-start program: ')
    main()

def create_restaurant():
    os.system('clear')
    print('Create a new restaurant')
    restaurant_name = str(input('Type new restaurant name: '))


def choose_option():
    try:
        chosen_option = int(input('Choose an option: '))
        print(f'You chosen {chosen_option}')
        if chosen_option == 1:
            create_restaurant()
        elif chosen_option == 2:
            print('List Restaurant')
        elif chosen_option == 3:
            print('Activate Restaurant')
        elif chosen_option == 4:
            end_program()
        else:
            invalid_option()
    except:
        invalid_option()

def main():
    os.system('clear')
    show_options()
    choose_option()

if __name__ == '__main__':
    main()

