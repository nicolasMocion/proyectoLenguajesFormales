def validar_correo(cadena):
    #Definir estado inicial
    estado = 'q0'

    for char in cadena:
        if estado == 'q0':
            # correo debe empezar con letra o numero
            if char.isalnum():
                estado = 'q1'
            else:
                return False # Error
        
        elif estado == 'q1':
            # antes del @
            if char.isalnum() or char in ['.', '_', '-']:
                estado = 'q1'
            elif char == '@':
                estado = 'q2'
            else:
                return False #error
        
        elif estado == 'q2':
            # despues del @
            if char.isalpha():
                estado = 'q3'
            else:
                return False
        
        elif estado == 'q3':
            # Leyendo el dominio
            if char.isalpha() or char == '-':
                estado = 'q3'
            elif char == '.':
                estado = 'q4'
            else:
                return False
                
        elif estado == 'q4':
            # La extensión (.com, .co) debe empezar con letra
            if char.isalpha():
                estado = 'q5'
            else:
                return False
                
        elif estado == 'q5':
            # Leyendo el resto de la extensión
            if char.isalpha():
                estado = 'q5'
            else:
                return False
            
        # El autómata solo acepta la cadena si termina en el estado q5
    return estado == 'q5'



# --- Casos de Prueba Iniciales ---
#print(validar_correo("test@ejemplo.com"))      # Esperado: True
#print(validar_correo("usuario.name@udq.edu"))  # Esperado: True
#print(validar_correo("falla@dominio..com"))    # Esperado: False
#print(validar_correo("@sinusuario.com"))       # Esperado: False



def validar_placa(cadena):
    # Una placa estándar tiene exactamente 6 caracteres
    if len(cadena) != 6:
        return False
        
    estado = 'q0'
    # Normalizamos la entrada para simplificar la validación
    cadena = cadena.upper()
    
    for char in cadena:
        if estado == 'q0':
            if char.isalpha():
                estado = 'q1'
            else:
                return False
                
        elif estado == 'q1':
            if char.isalpha():
                estado = 'q2'
            else:
                return False
                
        elif estado == 'q2':
            if char.isalpha():
                estado = 'q3'
            else:
                return False
                
        elif estado == 'q3':
            if char.isdigit():
                estado = 'q4'
            else:
                return False
                
        elif estado == 'q4':
            if char.isdigit():
                estado = 'q5'
            else:
                return False
                
        elif estado == 'q5':
            if char.isdigit():
                estado = 'q6' # Estado final de aceptación
            else:
                return False

    # El autómata solo es válido si terminó exactamente en q6
    return estado == 'q6'

# --- Casos de Prueba Iniciales ---
#print("--- Pruebas de Placas ---")
#print(validar_placa("ABC123"))  # Esperado: True (Placa correcta)
#print(validar_placa("xyz987"))  # Esperado: True (Minúsculas aceptadas)
#print(validar_placa("AB1234"))  # Esperado: False (Falta una letra, sobra un número)
#print(validar_placa("ABCD12"))  # Esperado: False (Sobra una letra, falta un número)
#print(validar_placa("AB-123"))  # Esperado: False (Caracteres especiales no permitidos)

def validar_telefono(cadena):
    # Longitud exacta de 10 dígitos
    if len(cadena) != 10:
        return False
        
    estado = 'q0'
    for char in cadena:
        if estado == 'q0':
            if char.isdigit():
                estado = 'q1' # Podemos ciclar en q1 contando o simplemente validar todos
            else:
                return False
        elif estado == 'q1':
            if not char.isdigit():
                return False
    
    return True

#-- Pruebas
#print(validar_telefono("3001234567")) # True
#print(validar_telefono("300123456A")) # False


def validar_fecha(cadena):
    # Formato exacto: DD/MM/AAAA (10 caracteres)
    if len(cadena) != 10:
        return False
        
    # Validar posiciones estáticas (los separadores)
    if cadena[2] != '/' or cadena[5] != '/':
        return False
        
    # Extraer componentes asumiendo que ya pasaron la prueba de los separadores
    dia_str = cadena[0:2]
    mes_str = cadena[3:5]
    anio_str = cadena[6:10]
    
    # Validar que los componentes sean puros números
    if not (dia_str.isdigit() and mes_str.isdigit() and anio_str.isdigit()):
        return False
        
    # Validar rangos lógicos
    dia = int(dia_str)
    mes = int(mes_str)
    anio = int(anio_str)
    
    if not (1 <= mes <= 12):
        return False
        
    # Validación básica de días (se puede expandir para años bisiestos si se desea)
    dias_por_mes = {1:31, 2:29, 3:31, 4:30, 5:31, 6:30, 7:31, 8:31, 9:30, 10:31, 11:30, 12:31}
    
    if not (1 <= dia <= dias_por_mes[mes]):
        return False
        
    return True

# Pruebas
# print(validar_fecha("15/08/2026")) # True
# print(validar_fecha("32/01/2024")) # False


def validar_contrasena(cadena):
    if len(cadena) < 8:
        return False
        
    # Inicializamos las "banderas" (flags) en falso
    tiene_mayus = False
    tiene_minus = False
    tiene_num = False
    tiene_especial = False
    
    especiales = "!@#$%^&*()-_+=<>?/.,;:[]{}"
    
    # Un solo ciclo de lectura (O(n))
    for char in cadena:
        if char.isupper():
            tiene_mayus = True
        elif char.islower():
            tiene_minus = True
        elif char.isdigit():
            tiene_num = True
        elif char in especiales:
            tiene_especial = True
            
    # El estado de aceptación requiere que todas las banderas estén encendidas
    return tiene_mayus and tiene_minus and tiene_num and tiene_especial

# Pruebas
# print(validar_contrasena("Admin123!")) # True
# print(validar_contrasena("admin123"))  # False (Falta mayúscula y especial)



def validar_url(cadena):
    idx = 0
    # 1. Omitir el protocolo si está presente
    if cadena.startswith("https://"): 
        idx = 8
    elif cadena.startswith("http://"): 
        idx = 7
        
    # Variables de estado
    segmentos_leidos = 0
    longitud_segmento_actual = 0
    es_tld_valido = True 
    
    # 2. Ciclo principal de lectura
    while idx < len(cadena):
        char = cadena[idx]
        
        if char.isalnum() or char == '-':
            longitud_segmento_actual += 1
            # Si hay un número o guión, este bloque de texto ya no puede ser el TLD
            if not char.isalpha():
                es_tld_valido = False
                
        elif char == '.':
            # Falla si hay dos puntos seguidos (..) o empieza con un punto
            if longitud_segmento_actual == 0:
                return False 
                
            segmentos_leidos += 1
            longitud_segmento_actual = 0 # Reseteamos el contador para el siguiente bloque
            es_tld_valido = True         # Asumimos que el próximo bloque será el TLD
            
        else:
            # Espacios o caracteres extraños rompen la URL inmediatamente
            return False
            
        idx += 1
        
    # 3. Estado de Aceptación (Condiciones estrictas)
    # - Debe tener al menos un punto (ej: dominio.com)
    # - El último bloque (TLD) debe tener 2 o más caracteres (ej: .co, .com, .org)
    # - El último bloque debe contener EXCLUSIVAMENTE letras
    return (segmentos_leidos >= 1) and (longitud_segmento_actual >= 2) and es_tld_valido


# Pruebas
print(validar_url("1.")) # True
print(validar_url("http://dominio.co"))      # True
print(validar_url("www.sinprotocolo.com"))   # False





def buscar_patrones_en_texto(texto):
    """
    Escanea un bloque de texto, lo tokeniza y clasifica los fragmentos 
    utilizando los autómatas definidos.
    """
    # 1. Fase de tokenización básica (separar por espacios)
    tokens = texto.split()
    
    # 2. Inicializar la estructura de datos para los resultados
    resultados = {
        "correos": [],
        "placas": [],
        "telefonos": [],
        "fechas": [],
        "urls": []
    }
    
    # 3. Fase de evaluación
    for token in tokens:
        # Limpiamos signos de puntuación que puedan estar pegados al final del token 
        # (ej. "correo@udq.edu," -> "correo@udq.edu")
        token_limpio = token.strip(".,;()[]\"'")
        
        # Pasamos el token por nuestra batería de validadores
        if validar_correo(token_limpio):
            resultados["correos"].append(token_limpio)
        elif validar_placa(token_limpio):
            resultados["placas"].append(token_limpio.upper())
        elif validar_telefono(token_limpio):
            resultados["telefonos"].append(token_limpio)
        elif validar_fecha(token_limpio):
            resultados["fechas"].append(token_limpio)
        elif validar_url(token_limpio):
            resultados["urls"].append(token_limpio)
            
    return resultados


# 3. PRUEBA DE FUNCIONAMIENTO (UNIT TEST)

if __name__ == "__main__":
    texto_prueba = """
    El evento se realizará el 15/08/2026. Por favor confirmar asistencia al 
    correo contacto@empresa.com o al celular 3001234567. 
    Para más detalles visite http://www.evento-anual.co. 
    Recuerde registrar su vehículo, por ejemplo la placa ABC123, en la portería.
    """
    
    hallazgos = buscar_patrones_en_texto(texto_prueba)
    
    print("--- Resultados del Escaneo ---")
    for categoria, lista in hallazgos.items():
        print(f"{categoria.capitalize()}: {lista}")