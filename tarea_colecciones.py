contactos = {}

def agregar_contacto(nombre, telefono):
    contactos[nombre] = telefono
    print(f"Contacto '{nombre}' agregado exitosamente.")

def mostrar_contactos():
    if not contactos:
        print("La agenda está vacía.")
    else:
        print("\n--- Lista de Contactos ---")
        for nombre, telefono in contactos.items():
            print(f"Nombre: {nombre} | Teléfono: {telefono}")
        print("---------------------------\n")

def consultar_contacto(nombre):
    if nombre in contactos:
        print(f"El teléfono de {nombre} es: {contactos[nombre]}")
    else:
        print(f"No se encontró ningún contacto con el nombre '{nombre}'.")

agregar_contacto("Carlos", "0991234567")
agregar_contacto("Ana", "0987654321")
agregar_contacto("Luis", "0971122334")

mostrar_contactos()

consultar_contacto("Luis")