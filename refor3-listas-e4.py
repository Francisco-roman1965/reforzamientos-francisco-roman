def main():
    # Lista inicial de estudiantes
    estudiantes = ["Ana", "Carlos", "María", "Pedro", "Laura"]

    print("=== PROGRAMA DE GESTIÓN DE ESTUDIANTES ===")
    print(f"Lista actual de estudiantes: {estudiantes}")

    # Solicitar el nombre del estudiante a eliminar
    nombre = input("\nIngrese el nombre del estudiante a eliminar: ").strip()

    # Verificar si el estudiante está en la lista
    if nombre in estudiantes:
        # Eliminar el estudiante de la lista
        estudiantes.remove(nombre)
        print(f"✅ '{nombre}' ha sido eliminado de la lista.")
    else:
        # Si no existe, mostrar mensaje y agregarlo
        print(f"❌ '{nombre}' no se encuentra en la lista.")
        estudiantes.append(nombre)
        print(f"✅ '{nombre}' ha sido agregado a la lista.")

    # Mostrar la lista actualizada
    print(f"\n📋 Lista actualizada de estudiantes: {estudiantes}")


if __name__ == "__main__":
    main()