while True:
    try:
        print("============================||==========================")
        num = int(input("Ingresa un número: "))
       
        if num < 0:
            break
        elif num % 2 == 0:
            print("El número es par")
            
        else:
            print("El número es impar")
           
    except ValueError:
        
        print("Por favor, ingresa un número válido.")
