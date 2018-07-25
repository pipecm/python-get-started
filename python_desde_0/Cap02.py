import Constants, math

suma = 0
indice = 0
exit = False
while (exit == False):
    nota = input(Constants.INPUT_PROMPT.format(indice + 1))
    if (nota == Constants.EXIT_CMD): 
        exit = True
    else:
        try:    
            suma += float(nota)
            indice += 1
        except ValueError: 
            print(Constants.INVALID_VALUE)
        
promedio = (math.ceil((suma/indice) * 10)) / 10
print(Constants.OUTPUT_PROMPT.format(promedio)) 