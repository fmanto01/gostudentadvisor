
import requests
from bs4 import BeautifulSoup
import studente
import mioTelegram
from ischedule import schedule, run_loop

studenti = []
codici = []


#ogni volta devo svuotarla immagino
def riempiLista(s):
    index = 0
    limit = 20
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
            break

def leggiVecchiCodici():
    with open('codici.txt', 'r', encoding="utf-8") as f:
        return f.read()

def scriviCodici():
    with open('codici.txt', 'w', encoding="utf-8") as f:
        for c in codici:
            f.write(f"{c} ")

def mergeCodici(vecchi, studenti):
    for s in studenti:
        if s.numero not in vecchi:
            
            mioTelegram.inviaMessaggio(s)

def main():
    print("prima riga")
    URL = "https://docs.google.com/spreadsheets/d/e/2PACX-1vSxa-l5fqDBv5hOuNQ5q0kW19YOpPHAMe-kITWnBR567PIBhYkklOzpbjz-td77hY-jBw5_KGyz1fX7/pubhtml?gid=6878166&&range=A1:H&widget=false&chrome=false&headers=false&"
    r = requests.get(URL)
    soup = BeautifulSoup(r.content, 'html.parser')
    print("prima riga")
    mioTelegram.invio("inizio ricerca")
    print("prima riga")
    s = soup.find("div", {"id":"6878166"}) #file di informatica, potrebbe cambiare nel tempo?
    s = s.contents[0].contents[0].contents[1]  #questo è il tbody

    vecchiCodici = leggiVecchiCodici()
    riempiLista(s)
    print(studenti[0])
    mergeCodici(vecchiCodici, studenti)
    scriviCodici()


if __name__ == "__main__":
    main()
