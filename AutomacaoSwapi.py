import requests
from bs4 import BeautifulSoup
import matplotlib.pyplot
from tkinter import *

def pesquisa():

    tk.title("Carregando, Aguarde...")
    listaCerto = []
    listaErro = []

    lista =  ("people", "films", "starships", "species", "planets", 
    "vehicles")

    vezes = int(textbox.get())

    for itens in lista:
        for tentativa in range(1, vezes):
            page = requests.get(f"https://swapi.dev/api/{itens}/{tentativa}").text
            #print(itens, tentativa, page)
            if page.find('{"detail":"Not found"}'):
                listaCerto += [itens]
            else:
                listaErro += [itens]
    print(listaErro)        
    print(listaCerto)

    people = listaCerto.count("people")
    films = listaCerto.count("films")
    starships = listaCerto.count("starships")
    species = listaCerto.count("species")
    planets = listaCerto.count("planets")
    vehicles = listaCerto.count("vehicles")

    peopleerro = listaErro.count("people")
    filmserro = listaErro.count("films")
    starshipserro = listaErro.count("starships")
    specieserro = listaErro.count("species")
    planetserro = listaErro.count("planets")
    vehicleserro = listaErro.count("vehicles")


    peopleresult = people - peopleerro
    filmsresult = films - filmserro
    starshipsresult = starships - starshipserro
    speciesresult = species - specieserro
    planetresult = planets - planetserro
    vehiclesresult = vehicles - vehicleserro

    listagem = [people,films,starships,species,planets,vehicles]
    matplotlib.pyplot.title('Grafico Swapi - Encontrados')
    matplotlib.pyplot.plot(listagem, lista)
    matplotlib.pyplot.show()

    listagemerro = [peopleerro,filmserro,starshipserro,specieserro,planetserro,vehicleserro]
    matplotlib.pyplot.title('Grafico Swapi - Não Encontrados')
    matplotlib.pyplot.plot(listagemerro, lista)
    matplotlib.pyplot.show()

    listagemresult = [peopleresult,filmsresult, starshipsresult, speciesresult,planetresult,vehiclesresult]
    matplotlib.pyplot.title('Grafico Swapi Resultado Final (Encontrados x Não Encontrados)')
    matplotlib.pyplot.plot(listagemresult, lista)
    matplotlib.pyplot.show()

    tk.title("Automação Swapi")
    
tk = Tk()
tk.title("Automação Swapi")
Label(tk,text="Informe a quantidade de dados a consultar: ").pack()

textbox = Entry(tk,width=49)
textbox.place(x=1, y= 20)


Botao = Button(tk, width=10,text= 'Pesquisar', command= pesquisa).place(x=110, y=50)

tk.geometry("300x100")
tk.mainloop()