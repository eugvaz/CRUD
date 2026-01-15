def load_default_data():
    return [
        {"id": 1,
         "name": "Justinianas",
         "species": "cat",
         "birth_year": 1997
         },
        {"id": 2,
         "name": "Tigras",
         "species": "cat",
         "birth_year": 1997
         },
        {"id": 3,
         "name": "Dikas",
         "species": "dog",
         "birth_year": 1998
         },
        {"id": 4,
         "name": "Bobikas",
         "species": "dog",
         "birth_year": 2007
         },
        {"id": 5,
         "name": "Džeimsas",
         "species": "cat",
         "birth_year": 2010
         },
    ]

def print_info():
    print("____________________________________________________________________________")
    print("1. Atvaizduoti mano gyvūnų sąrašą")
    print("2. Įtraukti gyvūną į mano gyvūnų sąrašą")
    print("3. Koreguoti mano gyvūnų sąrašą")
    print("4. Šalinti gyvūną iš mano gyvūnų sąrašo")
    print("5. Išeiti iš programos")
    print("____________________________Pasirinkite:____________________________________")

def print_my_pets(my_pets):
    for my_pet in my_pets:
        print(
            f'{my_pet['id']}. Gyvūno vardas- {my_pet['name']}.Gyvūno rūšis- {my_pet["species"]}. Gimimo metai:{my_pet["birth_year"]}')

def create_my_pet(my_pets,id_counter):
    print("Gyvūno įtraukimas į sąrašą:")
    print("Įveskite gyvūno vardą")
    name = input()
    print("Įveskite gyvūno rūšį")
    species = input()
    print("Įveskite gyvūno gimimo metus")
    birth_year = input()
    id_counter += 1
    my_pet = {"id": id_counter,
              "name": name,
              "species": species,
              "birth_year": birth_year
              }
    my_pets.append(my_pet)
    return id_counter

def edit_my_pet(my_pets):
    print("Gyvūnų sąrašo redagavimas")
    print("Įveskite gyvūno id iš sąrašo, kurį norite redaguoti")
    edit_id = input()
    for my_pet in my_pets:
        if edit_id == str(my_pet["id"]):
            print(f'{my_pet['id']}. Gyvūno vardas- {my_pet['name']}. Gyvūno rūšis- {my_pet["species"]}. '
                  f'Gimimo metai:{my_pet["birth_year"]}')
            print("Įveskite gyvūno vardą")
            my_pet['name'] = input()
            print("Įveskite gyvūno rūšį")
            my_pet['species'] = input()
            print("Įveskite gyvūno gimimo metus")
            my_pet['birth_year'] = input()
            break

def remove_my_pet(my_pets):
    print("Gyvūno šalinimas iš sąrašo")
    print("Įveskite gyvūno id, kurį norite pašalinti iš sąrašo")
    del_id = input()
    for my_pet in my_pets:
        if del_id == str(my_pet['id']):
            print(f'{my_pet['id']}. Šalinimo iš sąrašo gyvūno vardas- {my_pet['name']}, '
                  f'gyvūno rūšis- {my_pet["species"]}. Gimimo metai:{my_pet["birth_year"]}')
            my_pets.remove(my_pet)