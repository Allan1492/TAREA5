def contador_frecuencias(me_abre_xarchivo):
    
    frecuencias = {}
    
    try:
        with open(me_abre_xarchivo, 'r', encoding='utf-8') as archivo:
            contenido = archivo.read()
            
            for caracter in contenido:
                if caracter.isalpha():  # Verifica si el carácter es una letra
                    if caracter in frecuencias:
                        frecuencias[caracter] += 1
                    else:
                        frecuencias[caracter] = 1

    except FileNotFoundError:
        print(f"Error: El archivo '{me_abre_xarchivo}' no existe.")
        return None
    return frecuencias
