from list_CRUD import *

my_pets = load_default_data()
id_counter = 5

while True:
    print_info()
    ivestis = input()
    match ivestis:
        case "1":
           print_my_pets(my_pets)
        case "2":
           id_counter = create_my_pet(my_pets,id_counter)
        case "3":
           edit_my_pet(my_pets)
        case "4":
           remove_my_pet(my_pets)
        case "5":
            print("Išeiti iš programos")
            break
