# Este script elimina una línea específica de un archivo de texto y añade una nueva.

archivo = r'c:\Users\LuIs Delgado\OneDrive\Escritorio\Python\Coursera\Automatizacion_Scripting_Python\Archivo_prueba.txt'

# Leer el contenido del archivo
with open(archivo, 'r', encoding='utf-8') as file:
    content = file.readlines()
    print("Contenido antes de la eliminación:")
    print(''.join(content))

# Eliminar la segunda línea (índice 1)
if len(content) > 1:
    del content[1]

# Escribir el contenido modificado de nuevo
with open(archivo, 'w', encoding='utf-8') as file:
    file.writelines(content)
    print("Contenido después de la eliminación:")
    print(''.join(content))

# Añadir una nueva línea al final
with open(archivo, 'a', encoding='utf-8') as file:
    file.write("\nESTAMOS APRENDIENDO A ADICIONAR LÍNEAS DESDE PYTHON.")
    print("Estamos aprendiendo a añadir líneas de texto con Python.")
