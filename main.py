from options import delete_contact, edit_contact, create_contact, show_contacts

option = 1

while option != 0:
    print("Libreta de contactos")
    option = int(input('1. Ingresar contacto\n'+
                    '2. Eliminar contacto\n'+
                    '3. Editar contacto\n'+
                    '4. Mostrar contactos\n'+
                    '0. Salir\n'))

    if option == 1:
        create_contact()

    elif option == 2:
        delete_contact()
    
    elif option == 3:
        edit_contact()

    elif option == 4:
        show_contacts()