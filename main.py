import random
import string


def generar_contraseña(longitud, incluir_mayusculas, incluir_numeros, incluir_simbolos):
	"""
    Genera una contraseña segura según los criterios proporcionados.

    Parámetros:
    - longitud (int): Cantidad de caracteres que tendrá la contraseña.
    - incluir_mayusculas (bool): Si incluir letras mayúsculas.
    - incluir_numeros (bool): Si incluir números en la contraseña.
    - incluir_simbolos (bool): Si incluir caracteres especiales como símbolos.

    Retorna:
    - contraseña (str): La contraseña generada con los criterios indicados.
    """
	# Iniciar el conjunto de caracteres solo con letras minúsculas
	caracteres = string.ascii_lowercase

	# Agregar letras mayúsculas si el usuario lo solicita
	if incluir_mayusculas:
		caracteres += string.ascii_uppercase

	# Agregar números si el usuario lo solicita
	if incluir_numeros:
		caracteres += string.digits

	# Agregar caracteres especiales si el usuario lo solicita
	if incluir_simbolos:
		caracteres += string.punctuation

	# Generar la contraseña seleccionando caracteres aleatoriamente del conjunto
	contraseña = ''.join(random.choice(caracteres) for _ in range(longitud))
	return contraseña


def main():
	"""
    Función principal que interactúa con el usuario para generar contraseñas.
    Permite configurar los criterios de la contraseña y preguntar si desea generar otra.
    """
	print("¡Bienvenido al Generador de Contraseñas Seguras!")  # Mensaje de bienvenida

	while True:  # Comienza un bucle infinito para permitir generar múltiples contraseñas
		try:
			# Solicitar al usuario la longitud de la contraseña y convertirla en entero
			longitud = int(input("\nIngrese la longitud de la contraseña (8-20 recomendado): "))

			# Preguntar al usuario si desea incluir distintos tipos de caracteres
			incluir_mayusculas = input("¿Incluir letras mayúsculas? (s/n): ").lower() == 's'
			incluir_numeros = input("¿Incluir números? (s/n): ").lower() == 's'
			incluir_simbolos = input("¿Incluir símbolos? (s/n): ").lower() == 's'

			# Llamar a la función para generar la contraseña con los criterios indicados
			contraseña_generada = generar_contraseña(longitud, incluir_mayusculas, incluir_numeros, incluir_simbolos)

			# Mostrar la contraseña generada al usuario
			print(f"\nTu contraseña segura es: {contraseña_generada}")

		except ValueError:
			# Capturar errores si el usuario no ingresa un número válido
			print("Por favor, ingrese un número válido para la longitud.")

		# Preguntar si el usuario desea generar otra contraseña
		otra = input("\n¿Desea generar otra contraseña? (s/n): ").lower()
		if otra != 's':  # Si el usuario responde algo distinto a 's', termina el bucle
			break

	# Mensaje de despedida y evitar cierre inmediato de la ventana
	print("\nGracias por usar el Generador de Contraseñas Seguras. ¡Hasta luego!")
	input("\nPresione Enter para cerrar el programa.")  # Esperar a que el usuario presione Enter


if __name__ == "__main__":
	main()
