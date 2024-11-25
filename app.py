import os

restaurants = ['Bobs Burguer', 'Sushi Rock']

def show_options():
    print('Flavour Express\n')
    print('1. Create Restaurant')
    print('2. List Restaurant')
    print('3. Activate Restaurant')
    print('4. Exit\n')

def show_subtitle(text):
    os.system('clear')
    print(text)
    print()


def go_back_to_main_menu():
    input('Type any key to go back to main menu ')
    main()

def end_program():
    os.system('clear') 

def invalid_option():
    print('Invalid option!\n')
    go_back_to_main_menu()

def create_restaurant():
    show_subtitle('Create a new restaurant')
    restaurant_name = input('Type new restaurant name: ')
    restaurants.append(restaurant_name)
    print(f'The restaurant {restaurant_name} was created with success')
    go_back_to_main_menu()

def list_restaurants():
    show_subtitle('List of all restaurants')
    
    for restaurant in restaurants:
        print(f'Restaurant {restaurant}')
    go_back_to_main_menu()

def choose_option():
    try:
        chosen_option = int(input('Choose an option: '))
        print(f'You chosen {chosen_option}')
        if chosen_option == 1:
            create_restaurant()
        elif chosen_option == 2:
            list_restaurants()
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