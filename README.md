¡Perfecto! Te voy a crear dos versiones: una calculadora simple vacía para que practiques, y después la versión resuelta para que compares y entiendas.

"""
CALCULADORA SIMPLE - VERSIÓN DE PRÁCTICA
=========================================
Completa las funciones siguiendo las pistas.
¡No te preocupes por hacerlo perfecto la primera vez!
"""

# ==================== FUNCIONES BÁSICAS ====================

def sumar(a, b):
    """
    Función para sumar dos números.
    
    PISTA: return a + b
    """
    # Tu código aquí
    pass

def restar(a, b):
    """
    Función para restar dos números.
    
    PISTA: return a - b
    """
    # Tu código aquí
    pass

def multiplicar(a, b):
    """
    Función para multiplicar dos números.
    
    PISTA: return a * b
    """
    # Tu código aquí
    pass

def dividir(a, b):
    """
    Función para dividir dos números.
    
    PISTA: Primero verifica si b es diferente de 0
    Si b == 0: return "Error: División por cero"
    Si no: return a / b
    """
    # Tu código aquí
    pass

# ==================== FUNCIÓN DE VALIDACIÓN ====================

def obtener_numero():
    """
    Función para obtener un número válido del usuario.
    
    PISTAS:
    1. Usa input() para obtener texto del usuario
    2. Usa float() para convertir texto a número
    3. Usa try/except para manejar errores
    4. Si hay error, pide el número otra vez (usa while True)
    """
    while True:
        try:
            # Pedir número al usuario
            # Convertir a float
            # Si funciona, devolver el número
            pass
        except:
            # Si hay error, mostrar mensaje
            # El while True hará que se repita
            pass

# ==================== FUNCIÓN PRINCIPAL ====================

def calculadora():
    """
    Función principal que controla la calculadora.
    
    PISTAS:
    1. Usar while True para repetir el programa
    2. Mostrar menú con print()
    3. Obtener opción del usuario con input()
    4. Usar if/elif para cada opción
    5. Llamar a las funciones de operaciones
    6. Mostrar resultados
    7. Preguntar si quiere continuar
    """
    
    print("¡Bienvenido a la Calculadora Simple!")
    
    while True:
        # Mostrar menú
        print("\n--- MENÚ ---")
        print("1. Sumar")
        print("2. Restar")
        print("3. Multiplicar")
        print("4. Dividir")
        print("5. Salir")
        
        # Obtener opción del usuario
        opcion = input("Elige una opción (1-5): ")
        
        if opcion == "1":
            # SUMA
            # 1. Obtener primer número
            # 2. Obtener segundo número
            # 3. Llamar función sumar()
            # 4. Mostrar resultado
            pass
            
        elif opcion == "2":
            # RESTA (similar a suma)
            pass
            
        elif opcion == "3":
            # MULTIPLICACIÓN (similar a suma)
            pass
            
        elif opcion == "4":
            # DIVISIÓN (similar a suma, pero verificar si el resultado es error)
            pass
            
        elif opcion == "5":
            # SALIR
            print("¡Hasta luego!")
            break  # Sale del while True
            
        else:
            # Opción inválida
            print("Opción inválida. Intenta de nuevo.")

# ==================== EJECUTAR PROGRAMA ====================

# PISTA: Llamar a la función calculadora() para iniciar el programa
# calculadora()

"""
INSTRUCCIONES PARA COMPLETAR:

1. EMPIEZA CON LAS FUNCIONES BÁSICAS:
   - Completa sumar(), restar(), multiplicar()
   - Son muy simples: solo return con la operación

2. DESPUÉS TRABAJA EN dividir():
   - Recuerda verificar si b == 0
   - Si es cero, devuelve un mensaje de error
   - Si no es cero, devuelve a / b

3. LUEGO obtener_numero():
   - Esta es la más compleja
   - Usa while True para repetir hasta obtener número válido
   - Usa try/except para capturar errores de conversión

4. FINALMENTE calculadora():
   - Completa cada opción del menú
   - Para cada operación: obtener dos números, hacer cálculo, mostrar resultado

5. DESCOMENTA LA ÚLTIMA LÍNEA para ejecutar

CONSEJOS:
- Prueba cada función por separado
- No tengas miedo de cometer errores
- Usa print() para ver qué está pasando
- Empieza simple y ve añadiendo complejidad
"""

Ahora te doy la versión resuelta con explicaciones detalladas:

"""
CALCULADORA SIMPLE - VERSIÓN RESUELTA
======================================
Esta versión incluye explicaciones detalladas de cada concepto.
"""

# ==================== FUNCIONES BÁSICAS ====================

def sumar(a, b):
    """
    Función para sumar dos números.
    
    EXPLICACIÓN:
    - 'def' define una función
    - 'sumar' es el nombre de la función
    - (a, b) son los parámetros que recibe
    - 'return' devuelve el resultado
    """
    resultado = a + b
    return resultado
    # También se puede escribir simplemente: return a + b

def restar(a, b):
    """
    Función para restar dos números.
    
    EXPLICACIÓN:
    - Similar a sumar, pero con operador -
    - El orden importa: a - b es diferente de b - a
    """
    return a - b

def multiplicar(a, b):
    """
    Función para multiplicar dos números.
    
    EXPLICACIÓN:
    - Usa el operador * para multiplicación
    - En Python, * funciona con enteros y decimales
    """
    return a * b

def dividir(a, b):
    """
    Función para dividir dos números con validación.
    
    EXPLICACIÓN DETALLADA:
    - Antes de dividir, verificamos si el divisor (b) es cero
    - La división por cero causa un error matemático
    - Usamos 'if' para verificar la condición
    - Si b == 0, devolvemos un mensaje de error
    - Si b != 0, hacemos la división normal
    """
    if b == 0:
        return "Error: No se puede dividir por cero"
    else:
        return a / b
    
    # Versión más corta:
    # return "Error: No se puede dividir por cero" if b == 0 else a / b

# ==================== FUNCIÓN DE VALIDACIÓN ====================

def obtener_numero():
    """
    Función para obtener un número válido del usuario.
    
    EXPLICACIÓN DE TRY/EXCEPT:
    
    ¿Qué es try/except?
    - try: "intenta ejecutar este código"
    - except: "si hay un error, ejecuta esto en su lugar"
    
    ¿Por qué lo necesitamos?
    - input() siempre devuelve texto (string)
    - float() convierte texto a número
    - Si el usuario escribe "hola", float("hola") causa un error
    - try/except evita que el programa se cierre
    
    ¿Qué es while True?
    - Es un bucle infinito
    - Solo se detiene cuando usamos 'return' o 'break'
    - Permite repetir hasta obtener un número válido
    """
    while True:  # Repite hasta obtener número válido
        try:
            # Intenta convertir la entrada del usuario a número
            texto = input("Ingresa un número: ")
            numero = float(texto)
            return numero  # Si funciona, devuelve el número y sale de la función
        
        except ValueError:
            # Si hay error (usuario escribió texto no numérico)
            print("❌ Eso no es un número válido. Intenta de nuevo.")
            # El while True hace que vuelva a preguntar
        
        except KeyboardInterrupt:
            # Si el usuario presiona Ctrl+C para cancelar
            print("\n👋 Programa cancelado.")
            exit()  # Termina el programa completamente

# ==================== FUNCIÓN PRINCIPAL ====================

def calculadora():
    """
    Función principal que controla toda la calculadora.
    
    EXPLICACIÓN DEL FLUJO:
    1. Saluda al usuario
    2. Entra en un bucle infinito (while True)
    3. Muestra el menú de opciones
    4. Obtiene la elección del usuario
    5. Ejecuta la operación correspondiente
    6. Muestra el resultado
    7. Vuelve al paso 3 (a menos que elija salir)
    
    EXPLICACIÓN DE IF/ELIF/ELSE:
    - if: "si la condición es verdadera"
    - elif: "si no, pero si esta otra condición es verdadera"
    - else: "si ninguna condición anterior fue verdadera"
    """
    
    print("🧮 ¡Bienvenido a la Calculadora Simple!")
    print("Esta calculadora puede hacer operaciones básicas.")
    
    while True:  # Bucle principal del programa
        
        # ========== MOSTRAR MENÚ ==========
        print("\n" + "="*30)
        print("     CALCULADORA SIMPLE")
        print("="*30)
        print("1. ➕ Sumar")
        print("2. ➖ Restar")
        print("3. ✖️  Multiplicar")
        print("4. ➗ Dividir")
        print("5. ❌ Salir")
        print("="*30)
        
        # ========== OBTENER OPCIÓN DEL USUARIO ==========
        opcion = input("Elige una opción (1-5): ").strip()
        # .strip() elimina espacios en blanco al inicio y final
        
        # ========== PROCESAR CADA OPCIÓN ==========
        
        if opcion == "1":
            # SUMA
            print("\n➕ SUMA")
            print("Voy a pedirte dos números para sumar.")
            
            # Obtener los dos números
            print("Primer número:")
            num1 = obtener_numero()
            print("Segundo número:")
            num2 = obtener_numero()
            
            # Realizar la operación
            resultado = sumar(num1, num2)
            
            # Mostrar el resultado
            print(f"\n🎉 Resultado: {num1} + {num2} = {resultado}")
            
        elif opcion == "2":
            # RESTA
            print("\n➖ RESTA")
            print("Voy a pedirte dos números para restar.")
            
            print("Primer número (del cual se va a restar):")
            num1 = obtener_numero()
            print("Segundo número (que se va a restar):")
            num2 = obtener_numero()
            
            resultado = restar(num1, num2)
            print(f"\n🎉 Resultado: {num1} - {num2} = {resultado}")
            
        elif opcion == "3":
            # MULTIPLICACIÓN
            print("\n✖️ MULTIPLICACIÓN")
            print("Voy a pedirte dos números para multiplicar.")
            
            print("Primer número:")
            num1 = obtener_numero()
            print("Segundo número:")
            num2 = obtener_numero()
            
            resultado = multiplicar(num1, num2)
            print(f"\n🎉 Resultado: {num1} × {num2} = {resultado}")
            
        elif opcion == "4":
            # DIVISIÓN
            print("\n➗ DIVISIÓN")
            print("Voy a pedirte dos números para dividir.")
            
            print("Dividendo (número que se va a dividir):")
            num1 = obtener_numero()
            print("Divisor (número por el cual dividir):")
            num2 = obtener_numero()
            
            resultado = dividir(num1, num2)
            
            # Verificar si hubo error
            if isinstance(resultado, str):  # Si es texto, es un mensaje de error
                print(f"\n❌ {resultado}")
            else:  # Si es número, es el resultado correcto
                print(f"\n🎉 Resultado: {num1} ÷ {num2} = {resultado}")
                
        elif opcion == "5":
            # SALIR
            print("\n👋 ¡Gracias por usar la calculadora!")
            print("¡Hasta luego!")
            break  # Sale del while True, terminando el programa
            
        else:
            # OPCIÓN INVÁLIDA
            print("\n❌ Opción inválida.")
            print("Por favor elige un número del 1 al 5.")
        
        # ========== PAUSA ANTES DE CONTINUAR ==========
        input("\n⏎ Presiona Enter para continuar...")
        # Esto hace que el programa espere hasta que el usuario presione Enter

# ==================== EJECUTAR PROGRAMA ====================

if __name__ == "__main__":
    """
    EXPLICACIÓN DE if __name__ == "__main__":
    
    Esta es una forma elegante de decir:
    "Solo ejecuta calculadora() si este archivo se ejecuta directamente,
     no si se importa desde otro archivo"
    
    Es una buena práctica en Python.
    """
    calculadora()

"""
🎓 CONCEPTOS CLAVE APRENDIDOS:

1. FUNCIONES:
   - Se definen con 'def nombre(parámetros):'
   - Pueden recibir información (parámetros)
   - Pueden devolver información (return)
   - Ayudan a organizar y reutilizar código

2. TRY/EXCEPT:
   - Maneja errores sin que el programa se cierre
   - try: código que puede fallar
   - except: qué hacer si falla
   - Permite crear programas robustos

3. WHILE TRUE:
   - Crea bucles infinitos controlados
   - Se detienen con 'break' o 'return'
   - Útiles para menús y validación de entrada

4. IF/ELIF/ELSE:
   - Permiten tomar decisiones en el código
   - Solo se ejecuta una rama
   - elif = "else if" (si no, pero si...)

5. VALIDACIÓN DE ENTRADA:
   - Nunca confíes en que el usuario ingrese datos correctos
   - Siempre valida y maneja errores
   - Da mensajes claros cuando algo sale mal

6. ORGANIZACIÓN DE CÓDIGO:
   - Una función, una responsabilidad
   - Nombres descriptivos para funciones y variables
   - Comentarios para explicar el "por qué", no el "qué"

💡 PRÓXIMOS PASOS PARA MEJORAR:
- Agregar más operaciones (potencia, raíz cuadrada)
- Guardar historial de operaciones
- Mejorar la interfaz visual
- Agregar más validaciones
"""

## 🎯 Plan de Práctica Recomendado:

### **Paso 1: Practica con la versión vacía**
1. Intenta completar las funciones básicas (`sumar`, `restar`, etc.)
2. No te preocupes por hacer todo perfecto
3. Prueba cada función individualmente antes de integrar

### **Paso 2: Compara con la versión resuelta**
1. Compara tu código con mi solución
2. Entiende las diferencias
3. No te desanimes si tu versión es diferente - ¡puede estar igual de bien!

### **Paso 3: Conceptos clave a entender**

**🔧 FUNCIONES:**
```python
def mi_funcion(parametro1, parametro2):
    resultado = parametro1 + parametro2
    return resultado
```

**🛡️ TRY/EXCEPT:**
```python
try:
    numero = float(input("Número: "))  # Puede fallar
    print("Éxito!")
except ValueError:
    print("Error: No es un número")  # Se ejecuta si falla
```

**🔄 WHILE TRUE:**
```python
while True:
    respuesta = input("¿Continuar? (s/n): ")
    if respuesta == 'n':
        break  # Sale del bucle
    print("Continuando...")
```

### **Paso 4: Ejercicios adicionales**
Una vez que domines lo básico, intenta agregar:
1. **Validación mejorada**: Que no acepte números negativos para ciertas operaciones
2. **Más operaciones**: Potencia, porcentaje, etc.
3. **Historial simple**: Una lista que guarde las últimas 5 operaciones
4. **Interfaz mejorada**: Colores o símbolos más llamativos

### **🤔 Preguntas para reflexionar mientras programas:**
- ¿Qué pasa si el usuario ingresa texto en lugar de un número?
- ¿Cómo puedo hacer que mi programa sea más amigable?
- ¿Qué otras validaciones necesito?
- ¿Cómo puedo organizar mejor mi código?

¡Empieza con la versión de práctica y no dudes en preguntar si te atascas en alguna parte específica!
