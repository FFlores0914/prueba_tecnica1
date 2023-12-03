entero = int(input("Ingresa un número entero: "))
flotante = float(input("Ingresa un número flotante: "))
cadena = input("Ingresa una cadena de texto: ")
booleano_str = input("Ingresa un valor booleano (True/False): ")


booleano = booleano_str.lower() == "true"


print("\nValores ingresados:")
print(f"Número entero: {entero}")
print(f"Número flotante: {flotante}")
print(f"Cadena de texto: {cadena}")
print(f"Valor booleano: {booleano}")


print("\nConversiones de tipos:")
print(f"Entero convertido a flotante: {float(entero)}")
print(f"Flotante convertido a entero: {int(flotante)}")
print(f"Entero convertido a cadena: {str(entero)}")
print(f"Booleano convertido a cadena: {str(booleano)}")
