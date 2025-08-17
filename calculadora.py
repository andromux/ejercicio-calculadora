def sumar(a, b):
    return a + b

def restar(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    if b == 0:
        return "Error: no es posible dividir entre 0"
    else:
        return a / b

def obtener_numero():
    while True:
        try:
            texto = input("Ingresa un numero: ")
            numero = float(texto)
            return numero
        except ValueError:
            print("Debes ingresar un numero")
        except KeyboardInterrupt:
            print("Programa cancelado por el usuario")
            exit()


def calculadora():
        print("Bienvenido a mi calculadora")
        print("está calculadora hace operaciones basicas")

        while True:
            print("Suma, Resta, Divide, Multiplica")
            print("1 Sumar")
            print("2 Resta")
            print("3 Dividir")
            print("4 Multiplicar")
            print("5 Salir")

            opcion = input("Ingresa que deseas realizar 1-5").strip()

            if opcion == "1":
                print("Ingresa los numeros a sumar")
                print("primer numero: ")
                num1 = obtener_numero()
                print("Segundo numero: ")
                num2 = obtener_numero()
                resultado = sumar(num1, num2)

                print(f"Resultado:  {resultado}")

            elif opcion == "2":
                print("Vamos a restar")
                print("primer numero: ")
                num1 = obtener_numero()
                print("segundo numero")
                num2 = obtener_numero()
                resultado = restar(num1, num2)
                print(f"Resultado: {resultado}")

            elif opcion == "3":
                print("Vamos a dividir")
                print("INgresa el primer Numero")
                num1 = obtener_numero()
                print("segundo numero")
                num2 = obtener_numero()
                resultado = dividir(num1, num2)

                if isinstance(resultado, str):
                    print(f"{resultado}")
                else:
                    print(f"el resultado es: {resultado}")


            elif opcion == "4":
                print("vamos a multiplicar")
                print("Primer Numero: ")
                num1 = obtener_numero()
                print("Segundo Numero")
                num2 = obtener_numero()

                resultado = multiplicar(num1, num2)

                print(f"El Resultado es: {resultado}")

            elif opcion == "5":
                print("Vamonos a dormir Ya ")
                break

            else:
                print("Opcion INvalida")
                print("Elige un numero del 1 al 5")

            input("Presiona ENTER para continuar")

if __name__ == "__main__":
        calculadora()
