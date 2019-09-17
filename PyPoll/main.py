print("\n")
print("Election Results")
print("--------------------------------")
#Comando para importar CSV
import csv
import os
#Seleccionar la ruta donde está el archivo que posteriormente leeré
election_csv = os.path.join(".","PyPoll","Resources","Election_data.csv")

#Creo ocho variables
Candidate = []
Khan = 0
Correy = 0
Li = 0
OTooley = 0
Num_Candidate = 0   
Votes_Candidates = [Khan, Correy, Li, OTooley]
Candidates = ["Khan", "Correy", "Li", "O'Tooley"]

#Leer el archivo que anteriormente buscamos
with open(election_csv, "r") as csvfile:
    #Leo mi archivo y defino como se partirá mi archivo
    csvreader = csv.reader(csvfile, delimiter = ",")
    #Leo el header del archivo
    csvheader = next(csvreader)

    for column in csvreader:
        Candidate.append(column[2]) 

#Imprimo en terminal el número de votos que hubo
print("Total Votes:", len(Candidate))
print("--------------------------------")

#Imprimo el número de votos por participante y el porcentaje que tienen de la votación
print("Khan: ", str(round((Candidate.count("Khan")/len(Candidate))*100, 3)) + "%", "(" + str(Candidate.count("Khan")) + ")")
print("Correy: ", str(round((Candidate.count("Correy")/len(Candidate))*100, 3)) + "%", "(" + str(Candidate.count("Correy")) + ")") 
print("Li: ", str(round((Candidate.count("Li")/len(Candidate))*100, 3)) + "%", "(" + str(Candidate.count("Li")) + ")") 
print("O'Tooley: ", str(round((Candidate.count("O'Tooley")/len(Candidate))*100, 3)) + "%", "(" + str(Candidate.count("O'Tooley")) + ")")

print("--------------------------------")
#Imprimo al ganador de la votación
print("Winner: ", Candidates[Votes_Candidates.index(max(Votes_Candidates))])

#Selecciono la ruta donde quiero que se guarde mi nuevo documento
Final_path = os.path.join(".","PyPoll","Elections_Results.csv")
#Doy instrucción de escribir en el nuevo documento
with open(Final_path, "w") as datafile:
        writer = csv.writer(datafile)
        writer.writerow(["Total Votes", "Total Votes for Khan", "Percentage", " Total Votes for Correy", "Percentage", "Total Votes for Li", "Percentage",
        "Total Votes for O'Tooley", "Percentage", "Winner"])
# Escribo los resultados
        writer.writerow([len(Candidate), str(Candidate.count("Khan")), str(round((Candidate.count("Khan")/len(Candidate))*100, 3)) + "%", str(Candidate.count("Correy")), str(round((Candidate.count("Correy")/len(Candidate))*100, 3)) + "%",
        str(Candidate.count("Li")), str(round((Candidate.count("Li")/len(Candidate))*100, 3)) + "%", str(Candidate.count("O'Tooley")), str(round((Candidate.count("O'Tooley")/len(Candidate))*100, 3)) + "%", 
        Candidates[Votes_Candidates.index(max(Votes_Candidates))]])
