import os

restaurants = [{'name': 'Minas Steakhouse', 'type': 'Barbecue', 'active': False},
    {'name': 'Flying Sushi', 'type': 'Japanese', 'active': True},
    {'name': 'McDonalds', 'type': 'Fast Food', 'active': False},
    {'name': 'King', 'type': 'Italian', 'active': True},]

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
    restaurant_type = input(f'Which cousine is the {restaurant_name}? ')
    restaurant_active = False
    restaurants.append({'name': restaurant_name, 'type': restaurant_type, 'active': restaurant_active})
    print(f'The restaurant {restaurant_name} was created with success')
    go_back_to_main_menu()

def list_restaurants():
    show_subtitle('List of all restaurants')
    print(f'{'Restaurant Name'.ljust(20)} | {'Cuisine'.ljust(20)} | {'Status'.ljust(20)}')
    for restaurant in restaurants:
        print(f' - {restaurant["name"].ljust(20)} | {restaurant["type"].ljust(20)} | {"Active" if restaurant["active"] else "Inactive"}')
    go_back_to_main_menu()

def activate_restaurant():
    show_subtitle('Alternate the status of a restaurant')
    restaurant_name = input('Type the name of the restaurant you want to alternate the status: ')
    restaurant_found = False
    for restaurant in restaurants:
        if restaurant['name'] == restaurant_name:
            restaurant_found = True
            restaurant['active'] = not restaurant['active']
            message = f'the restaurant {restaurant_name} was activated with success' if restaurant['active'] else f'the restaurant {restaurant_name} was deactivated with success'
            print(message)
    if not restaurant_found:
        print(f'The restaurant {restaurant_name} was not found')
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
            activate_restaurant()
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