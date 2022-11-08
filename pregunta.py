"""
Ingestión de datos - Reporte de clusteres
-----------------------------------------------------------------------------------------

Construya un dataframe de Pandas a partir del archivo 'clusters_report.txt', teniendo en
cuenta que los nombres de las columnas deben ser en minusculas, reemplazando los espacios
por guiones bajos; y que las palabras clave deben estar separadas por coma y con un solo 
espacio entre palabra y palabra.


"""
import pandas as pd
import re

def ingest_data():

    datos = open("clusters_report.txt", mode='r')
    columnas = ["", "", "", ""]

    for i in range(2):
        columna_index = i
        num_espacios = 0
        for char in datos.readline().strip():
            if char!=' ':
                if num_espacios == 1:
                    columnas[columna_index] += '_'
                elif num_espacios > 1:
                    columna_index += 1
                num_espacios = 0
                columnas[columna_index] += char
            else:
                num_espacios +=1
        
        if i==0:
            columnas[1] += '_'
            columnas[2] += '_'
    
    columnas = [i.lower() for i in columnas]
    datos_organizados= open("datos_organizados.txt","w+")
    datos_organizados.write(";".join(columnas)+"\n")


    for i in range(2): #saltarse lineas 3 y 4
        next(datos)

    ultimo_char = ''
    fila_organizada = ""
    for linea in datos.readlines():
        if len(linea.lstrip(" "))>1:
            linea = " "+linea.strip()
        
        num_espacios = 0
        print(num_espacios, linea)
        for char in linea:
            if char!=' ':
                if num_espacios==1:
                    fila_organizada += ' '
                elif num_espacios>1:
                    if ultimo_char!="%" and not ultimo_char.isdecimal():
                        fila_organizada += " "
                    else:
                        fila_organizada += ";"
                num_espacios = 0
                ultimo_char = char
                fila_organizada += char

            elif len(fila_organizada)>0:
                num_espacios +=1
                print(num_espacios)

    fila_organizada = fila_organizada.replace(",;", ", ")
    fila_organizada = fila_organizada.replace(" %", "")
    datos_organizados.write(fila_organizada)
    
    datos_organizados.close()
    df = pd.read_csv("datos_organizados.txt", sep=";")
    return df.principales_palabras_clave.to_list()[0]

print(ingest_data())