#AUTHOR: FERNANDO EMANUEL RAMIREZ AHUMADA
#ESTE SCRIPT SE ENCARGA DE DIVIDIR EL ARCHIVO EN PARTES DE 1.5MB

import os
import csv

def dividir_csv(archivo, tamaño_mb):
    tamaño_bytes = tamaño_mb * 1024 * 1024  # Convertir MB a bytes
    with open(archivo, 'r', encoding='utf-8') as archivo_csv:
        lector_csv = csv.reader(archivo_csv)
        encabezado = next(lector_csv)  # Guardar la primera línea (encabezado)
        
        # Crear las primeras partes de archivo
        parte = 1
        archivo_parte = open(f'{archivo}_parte{parte}.csv', 'w', newline='', encoding='utf-8')
        escritor_csv = csv.writer(archivo_parte)
        escritor_csv.writerow(encabezado)  # Escribir encabezado solo en el primer archivo
        
        total_bytes = 0
        for fila in lector_csv:
            # Contabilizar el tamaño de la fila
            fila_str = ','.join(fila)
            total_bytes += len(fila_str.encode('utf-8'))
            
            if total_bytes > tamaño_bytes:
                archivo_parte.close()  # Cerrar el archivo actual
                
                # Crear un nuevo archivo si el tamaño supera el límite
                parte += 1
                archivo_parte = open(f'{archivo}_parte{parte}.csv', 'w', newline='', encoding='utf-8')
                escritor_csv = csv.writer(archivo_parte)
                
                total_bytes = len(fila_str.encode('utf-8'))  # Reiniciar el contador de bytes con la fila actual

            # Escribir la fila en el archivo
            escritor_csv.writerow(fila)
        
        archivo_parte.close()  # Cerrar el último archivo

# Llamar a la función con 1.5 MB
dividir_csv('direccion.csv', 1.5)  # Dividir en partes de 1.5MB
