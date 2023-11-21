import json
counter = 0

with open('files/inventory.csv','r') as file:
    for line in file:
        if(counter == 0):
            headers = line
            headers = headers.split(',')
        else:
            dictLine = {}
            counterHeader = 0
            for column in line.split(','):
                dictLine[headers[counterHeader]] = column
                counterHeader += 1
            #interpolar: metemos un string dentro de otro. Concatenar es lo mismo pero con diferente sintaxis 
            #Concantenando seria 
            #with open('output/'+strcounter'.json','w') as outputFile:
            with open(f'output/{counter}.json','w') as outputFile:
                json.dump(dictLine, outputFile, indent=0)
        counter += 1
       

     

print(headers)
print(line)
