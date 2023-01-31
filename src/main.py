
import requests
from bs4 import BeautifulSoup
import studente
import mioTelegram
from ischedule import schedule, run_loop


URLS = ["https://docs.google.com/spreadsheets/d/e/2PACX-1vSxa-l5fqDBv5hOuNQ5q0kW19YOpPHAMe-kITWnBR567PIBhYkklOzpbjz-td77hY-jBw5_KGyz1fX7/pubhtml?gid=6878166&&range=A1:H&widget=false&chrome=false&headers=false&",
        "https://docs.google.com/spreadsheets/d/e/2PACX-1vSxa-l5fqDBv5hOuNQ5q0kW19YOpPHAMe-kITWnBR567PIBhYkklOzpbjz-td77hY-jBw5_KGyz1fX7/pubhtml?gid=695965261&range=A1:H&widget=false&chrome=false&headers=false&"]

IDS = ["6878166",
       "695965261"]

codici = []

#ogni volta devo svuotarla immagino
def riempiLista(s):
    index = 0
    limit = 30
    studenti=[]
    for riga in s:

        materia = riga.contents[1].string
        if materia!=None and index!=0:
            
            genere = riga.contents[2].string
            eta = riga.contents[3].string
            anno = riga.contents[4].string
            lezioni = riga.contents[5].string
            go = riga.contents[6].string
            
            info = riga.contents[7].get_text()
            numero = riga.contents[8].string.split()[1]

            codici.append(numero)
            studenti.append(studente.student(materia, genere, eta, anno, lezioni, go, info, numero))
        
        index +=1
        if index >= limit: #piccola cosa quasi inutile per ridurre
            return studenti

def leggiVecchiCodici(i):
    with open(f'codici{i}.txt', 'r', encoding="utf-8") as f:
        return f.read()

def scriviCodici(i):
    with open(f'codici{i}.txt', 'w', encoding="utf-8") as f:
        for c in codici:
            f.write(f"{c} ")

def mergeCodici(vecchi, studenti):
    for s in studenti:
        if s.numero not in vecchi:
            mioTelegram.inviaMessaggio(s)

def main():
    print("prima riga")

    for i in range(2):
        r = requests.get(URLS[i])
        soup = BeautifulSoup(r.content, 'html.parser')
        print("prima riga")
        #mioTelegram.invio("inizio ricerca")
        print("prima riga")
        s = soup.find("div", {"id":IDS[i]}) #file di informatica, potrebbe cambiare nel tempo?
        s = s.contents[0].contents[0].contents[1]  #questo è il tbody

        vecchiCodici = leggiVecchiCodici(i)
        studenti = riempiLista(s)
        print(studenti[0])
        mergeCodici(vecchiCodici, studenti)
        scriviCodici(i)


if __name__ == "__main__":
    main()
    schedule(main, interval=2*60)
    run_loop()
