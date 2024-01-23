import redis

red = redis.Redis(
    host='redis-11660.c323.us-east-1-2.ec2.cloud.redislabs.com',
    port=11660,
    password='2rsRkyLQCBTB9beK5BYeSyRh8MrvmcjB'
)


def set_name_number():

    name_to_save = input("Enter name to save: ")
    number_to_save = input("Enter phone number to save: ")
    red.set(name_to_save, number_to_save)
    print('New entry saved')
    user_interface()


def get_number_by_name():
    get_number = input("Enter name to get: ")

    if red.exists(get_number):
        value = red.get(get_number)
        decoded_value = value.decode('utf-8')
        print(f'Number of {get_number} is: ', decoded_value)

    else:
        print(f'No entry found for {get_number}')

    user_interface()


def delete_number_by_name():
    name_number_to_delete = input("Enter name to delete: ")

    if red.exists(name_number_to_delete):
        red.delete(name_number_to_delete)
        print(f"{name_number_to_delete}'s entry was successfully deleted")

    else:
        print(f"No entry found for {name_number_to_delete}")

    user_interface()


def phonebook():
    print('Phonebook items:')
    keys = red.keys()
    decoded_keys = [key.decode('utf-8') for key in keys]
    for key in decoded_keys:
        print(key)
    user_interface()


def clear_phonebook():
    prompt = input("You are going to delete all entries! Are you sure? y/n: ")
    if prompt == 'y':
        red.flushdb()
        print('Phonebook is cleared')
        user_interface()
    else:
        print('Action cancelled')
        user_interface()


def user_interface():

    user_input = input('\nYour choice: ')

    if user_input == "n":
        set_name_number()

    elif user_input == "g":
        get_number_by_name()

    elif user_input == "d":
        delete_number_by_name()

    elif user_input == "exit":
        print('bye!')
        exit()

    elif user_input == "clear":
        clear_phonebook()

    elif user_input == "list":
        phonebook()

    else:
        print("\nWrong input, try again!")
        user_interface()


def greeting():

    print('\nHi! This is a magic phonebook!\nIt asks for names and numbers of people you never call to!')
    print('To save new such person type "n"\nTo get somebody\'s number type "g"'
          '\nTo delete type "d"\nTo view all of them type "list"\n'
          'To clear all the book type "clear"\nAnd "exit" for exit: ')
    user_interface()


greeting()
