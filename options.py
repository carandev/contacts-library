from db import connect

def create_contact():
    name = input('Ingresa el nombre del contacto: ')
    phone_number = input('Ingresa el número de teléfono: ')

    connection = connect()

    with connection:
        with connection.cursor() as cursor:
            sql = f"insert into contacts (name, phone_number) values ('{name}', '{phone_number}')"
            cursor.execute(sql)

        connection.commit()

def show_contacts():
    connection = connect()
    
    with connection:
        with connection.cursor() as cursor:
            sql = "select * from contacts"
            cursor.execute(sql)
            contacts = cursor.fetchall()
            
            for contact in contacts:
                print("-------------------------")
                print("ID:", contact["id"])
                print("Nombre:", contact["name"])
                print("Número:", contact["phone_number"])

def delete_contact():
    show_contacts()
    id_delete = input("Ingrese el id del contacto a eliminar: ")

    connection = connect()

    with connection:
        with connection.cursor() as cursor:
            sql = f"delete from contacts where id={id_delete}"
            cursor.execute(sql)

        connection.commit()

def edit_contact():
    show_contacts()
    id_edit = input("Ingrese el id del contacto a editar: ")

    name = input("Ingrese el nuevo nombre para el contacto: ")
    phone_number = input("Ingrese el nuevo número para el contacto: ")

    connection = connect()

    with connection:
        with connection.cursor() as cursor:
            sql = f"update contacts set name='{name}', phone_number='{phone_number}' where id={id_edit}"
            cursor.execute(sql)

        connection.commit()