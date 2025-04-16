import random
import string

def generar_contraseña(longitud, incluir_mayusculas, incluir_numeros, incluir_simbolos):
    """
    Genera una contraseña segura según los criterios proporcionados.
    - longitud: longitud de la contraseña.
    - incluir_mayusculas: booleano, incluir mayúsculas.
    - incluir_numeros: booleano, incluir números.
    - incluir_simbolos: booleano, incluir caracteres especiales.
    """
    # Conjunto inicial: letras minúsculas
    caracteres = string.ascii_lowercase

    if incluir_mayusculas:
        caracteres += string.ascii_uppercase
    if incluir_numeros:
        caracteres += string.digits
    if incluir_simbolos:
        caracteres += string.punctuation

    # Generar contraseña aleatoria
    contraseña = ''.join(random.choice(caracteres) for _ in range(longitud))
    return contraseña

def main():
    print("¡Bienvenido al Generador de Contraseñas Seguras!")
    while True:  # Bucle para permitir generar múltiples contraseñas
        try:
            # Configuración interactiva
            longitud = int(input("\nIngrese la longitud de la contraseña (8-20 recomendado): "))
            incluir_mayusculas = input("¿Incluir letras mayúsculas? (s/n): ").lower() == 's'
            incluir_numeros = input("¿Incluir números? (s/n): ").lower() == 's'
            incluir_simbolos = input("¿Incluir símbolos? (s/n): ").lower() == 's'

            # Generar y mostrar la contraseña
            contraseña_generada = generar_contraseña(longitud, incluir_mayusculas, incluir_numeros, incluir_simbolos)
            print(f"\nTu contraseña segura es: {contraseña_generada}")
        except ValueError:
            print("Por favor, ingrese un número válido para la longitud.")

        # Preguntar si se desea generar otra contraseña
        otra = input("\n¿Desea generar otra contraseña? (s/n): ").lower()
        if otra != 's':
            break

    print("\nGracias por usar el Generador de Contraseñas Seguras. ¡Hasta luego!")
    input("\nPresione Enter para cerrar el programa.")

if __name__ == "__main__":
    main()
