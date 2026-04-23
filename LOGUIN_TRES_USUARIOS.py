# ================================================
# SISTEMA DE LOGIN 
# ================================================

#Diccionario de usuarios 
#Cada clave representa un nombre de usuario.
#Cada valor es otro diccionario con dos claves internas:
#"password" (contraseña) y "rol" (tipo de usuario).

usuarios = {"admin":   {"password": "python123", "rol": "Administrador"},
            "usuariopro": {"password": "yolo321",   "rol": "Usuario"},
            "invitamosunloco":{"password": "guns76",  "rol": "Invitado"}}

#Constante de control 
INTENTOS_MAX = 3  #Número máximo de intentos permitidos

#Variable de control del bucle externo
#Si es True, el sistema sigue ejecutándose.
ejecutando_sistema = True

#Bucle externo
#Permite reiniciar todo el proceso si el usuario lo desea.
while ejecutando_sistema:
    print('_' * 45)
    print('         SISTEMA DE ACCESO SEGURO')
    print('_' * 45)

    #Variables internas
    #Se reinician en cada ciclo completo del sistema.
    intentos = 0        #Contador de intentos realizados
    acceso = False      #Estado del acceso True si se entrar
    rol_usuario = None  #Guarda el rol del usuario autenticado

    #Bucle interno
    #Controla los intentos de login hasta alcanzar el máximo.
    while intentos < INTENTOS_MAX and not acceso:
        intentos += 1
        print(f'\nIntento {intentos} de {INTENTOS_MAX}')
        print('-' * 30)

        try:
            #Entrada de datos
            #.strip() elimina espacios en blanco al inicio y al final.
            usuario_ing = input('Usuario    : ').strip()
            contrasena_ing = input('Contraseña : ').strip()

            #Verificación 
            #Se comprueba si el usuario existe en el diccionario.
            if usuario_ing in usuarios:
                #Si existe se compara la contraseña ingresada.
                if contrasena_ing == usuarios[usuario_ing]["password"]:
                    acceso = True
                    rol_usuario = usuarios[usuario_ing]["rol"]
                    print(f'\n✅ Acceso concedido. Bienvenido {usuario_ing} ({rol_usuario})')
                else:
                    #Usuario correcto pero contraseña incorrecta.
                    print('❌ Error: Contraseña incorrecta.')
            else:
                #Usuario no existe en el diccionario.
                print('❌ Error: Usuario no reconocido.')

            #Mostrar intentos restantes
            if not acceso:
                restantes = INTENTOS_MAX - intentos
                if restantes > 0:
                    print(f'⚠️ Intentos restantes: {restantes}')

        except Exception as e:

            #Manejo de errores inesperados
            #Captura cualquier excepción durante la entrada.
            print(f'⚠️ Error inesperado: {e}. Intente de nuevo.')

    #Cierre del ciclo de login
    print('\n' + '_' * 45)
    if acceso:

        #Si el acceso fue exitoso mostrar resumen y menú según rol
        print(f'🔓 Sesión iniciada en {intentos} intento(s).')
        print("\n--- MENÚ PRINCIPAL ---")

        #Menú según el rol
        # Se muestra un menú distinto para cada tipo de usuario
        if rol_usuario == "Administrador":
            print("1. Gestionar usuarios😼\n2. Ver reportes😒\n3. Configuración avanzada por ser el admin😎")
        elif rol_usuario == "Usuario":
            print("1. Consultar datos🎭\n2. Actualizar perfil👾\n3. Ver historial🙈")
        elif rol_usuario == "Invitado":
            print("1. Ver información pública🥹\n2. Solicitar acceso limitado😒")

        #Finaliza el sistema tras login exitoso.
        ejecutando_sistema = False

    else:
        # Si no se logró el acceso tras todos los intentos.
        print('🔒 CUENTA BLOQUEADA')
        print('Se superó el número máximo de intentos.')

        #Opción de reinicio
        respuesta = input('\n¿Desea reiniciar el proceso de acceso? (s/n): ').lower().strip()

        #.lower() convierte la respuesta a minúsculas.
        #.strip() elimina espacios en blanco.
        if respuesta != 's':
            print('Saliendo del sistema... Contacte al administrador.')
            ejecutando_sistema = False  # Termina el bucle externo

    print('_' * 45)
