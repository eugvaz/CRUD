# pip install mysql-connector-python
# pip install pymysql (alternatyva jei anas  neveikia)

import mysql.connector

DB_CONFIG = {
    'host':'localhost', #127.0.0.1 alternatyva rasymui "localhost" ;)
    'port': 3306,
    'user':'root',
    'password':"root",
    'database':'my_pets'
}
headers = ['id','name','species','birth_year']

def get_conn():
    return mysql.connector.connect(**DB_CONFIG) #tiketina, kad islukstena duomenis pagal virsutine duomenu baze

def load_my_pets():
    conn = get_conn() #jungtis( begiai)
    cur = conn.cursor() # traukinukas, kuris vazineja begiais
    cur.execute('select * from my_pets')
    rows = cur.fetchall() # rezultatas, kuris uzsikrove
    cur.close()
    conn.close()

    my_pets_list = []
    for row in rows:
        my_pet = {}
        for col_num in range(len(headers)):
            my_pet[headers[col_num]] = str(row[col_num])
        my_pets_list.append(my_pet)
    return my_pets_list

def print_info():
    print("____________________________________________________________________________")
    print("1. Atvaizduoti mano gyvūnų sąrašą")
    print("2. Įtraukti gyvūną į mano gyvūnų sąrašą")
    print("3. Koreguoti mano gyvūnų sąrašą")
    print("4. Šalinti gyvūną iš mano gyvūnų sąrašo")
    print("5. Išeiti iš programos")
    print("____________________________Pasirinkite:____________________________________")

def print_my_pets(my_pets):
    my_pets = load_my_pets()
    for my_pet in my_pets:
        print(
            f"{my_pet['id']}. Gyvūno vardas- {my_pet['name']}.Gyvūno rūšis- {my_pet["species"]}. Gimimo metai:{my_pet["birth_year"]}")

def create_my_pet(my_pets,id_counter):
    print("Gyvūno įtraukimas į sąrašą:")
    print("Įveskite gyvūno vardą")
    name = input()
    print("Įveskite gyvūno rūšį")
    species = input()
    print("Įveskite gyvūno gimimo metus")
    birth_year = input()

    conn = get_conn()
    cur = conn.cursor()
    cur.execute(f"INSERT INTO my_pets(name,species,birth_year) VALUES(%s,%s,%s)",(name,species,birth_year))
    conn.commit()
    cur.close()
    conn.close()

def edit_my_pet(my_pets):
    print("Gyvūnų sąrašo redagavimas")
    print("Įveskite gyvūno id iš sąrašo, kurį norite redaguoti")
    edit_id = input()

    conn = get_conn()
    cur = conn.cursor()
    cur.execute("select * from my_pets where id = %s", (edit_id,))
    row = cur.fetchone()
    cur.close()
    conn.close()
    if row:
        print(f'{row[0]}. Koreguojamo gyvūno sąraše vardas- {row[1]},gyvūno rūšis-{row[2]}. Gimimo metai:{row[3]}')
        print("Įveskite gyvūno vardą")
        name = input()
        print("Įveskite gyvūno rūšį")
        species = input()
        print("Įveskite gyvūno gimimo metus")
        birth_year = input()
        #break
        conn = get_conn()
        cur = conn.cursor()
        cur.execute(
            'UPDATE `my_pets`SET `name`= %s,`species`= %s,`birth_year`= %s WHERE id = %s;',(name,species,birth_year,edit_id)
        )
        conn.commit()
        cur.close()
        conn.close()
    else:
        ("Įrašo su tokiu id nėra")

def remove_my_pet(my_pets):
    print("Gyvūno šalinimas iš sąrašo")
    print("Įveskite gyvūno id, kurį norite pašalinti iš sąrašo")
    del_id = input()
    conn = get_conn()
    cur = conn.cursor()

    cur.execute("select * from my_pets where id = %s", (del_id,))
    row = cur.fetchone()
    if row:
        print(f'{row[0]}.Šalinimo iš sąrašo gyvūno vardas- {row[1]},gyvūno rūšis-{row[2]}. Gimimo metai:{row[3]}')
        cur.execute('DELETE FROM `my_pets`WHERE id = %s', (del_id,))
        conn.commit()
    else:
        print("Įrašo su tokiu id nėra.")
    cur.close()
    conn.close()
