# Archivo principal
from modulo_contador import contador_frecuencias

# Llamo  la función con un archivo existente
me_abre_xarchivo = "archivo_nuevo.txt"
resultado = contador_frecuencias(me_abre_xarchivo)

# Mostrar el resultado
if resultado:
    print("Frecuencia de letras en el archivo:")
    for letra, frecuencia in sorted(resultado.items()):
        print(f"{letra}: {frecuencia}")
