#!/usr/bin/python

import Constants, math

suma = 0
longitud = int(input(Constants.CAP06_INPUT_PROMPT))
notas = []

for i in range(0, longitud):
    notas.append(input(Constants.INPUT_PROMPT.format(i + 1)))
    try:    
        suma += float(notas[i])
    except ValueError: 
        print(Constants.INVALID_VALUE)
  
promedio = (math.ceil((suma/len(notas)) * 10)) / 10

print(Constants.CAP06_OUTPUT_PROMPT.format(str(notas)))
print(Constants.OUTPUT_PROMPT.format(promedio))