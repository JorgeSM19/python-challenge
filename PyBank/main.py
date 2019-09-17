print("\n")
print("Financial Analysis")
print("--------------------------------------")
#Comando para importar CSV
import csv
import os

#Seleccionar la ruta donde está el archivo que posteriormente leeré
budget_csv = os.path.join(".","PyBank","Resources","RBD.csv")

#Creo tres variables
Fechas = []
Totales = []
Razones_Cambio = [0]

#Leer el archivo que anteriormente buscamos
with open(budget_csv, "r") as csvfile:
    #Leo mi archivo y defino como se partirá mi archivo
    csvreader = csv.reader(csvfile, delimiter = ",")
    #Leo el header del archivo
    csvheader = next(csvreader)

    for column in csvreader:
        Fechas.append(column[0])
        Totales.append(int(column[1]))
    for x in range(1, len(Totales)):
        cambio = (Totales[x]) - (Totales[x-1])
        Razones_Cambio.append(cambio)

    #Imprimo los resultados en Terminal    
    print("Total Months:", len(Fechas))
    print("Total: $" + str(sum(Totales)))
    print("Average Change: $", round(sum(Razones_Cambio)/(len(Razones_Cambio)-1), 2))
    print("Greatest Increase in Profits: ", Fechas[Razones_Cambio.index(max(Razones_Cambio))], "$" + str(max(Razones_Cambio)))
    print("Greatest Decrease in Profits: ", Fechas[Razones_Cambio.index(min(Razones_Cambio))], "$" + str(min(Razones_Cambio)))


#Selecciono la ruta donde quiero que se guarde mi nuevo documento
    Final_path = os.path.join(".","PyBank","Financial_Analysis.csv")
#Doy instrucción de escribir en el nuevo documento
    with open(Final_path, "w") as datafile:
        writer = csv.writer(datafile)
        writer.writerow(["Total Months", "Total", "Average Change", "Greatest Increase in Profits", "Greatest Increase Date", "Greatest Decrease in Profits", "Greatest Decrease Date"])
#Escribo el resultado en las celdas
        writer.writerow([len(Fechas), "$" + str(sum(Totales)), "$" + str(round(sum(Razones_Cambio)/(len(Razones_Cambio)-1), 2)), "$" + str(max(Razones_Cambio)),
        Fechas[Razones_Cambio.index(max(Razones_Cambio))], "$" + str(min(Razones_Cambio)), Fechas[Razones_Cambio.index(min(Razones_Cambio))]])
   





        

        


