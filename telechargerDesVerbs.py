from bs4 import BeautifulSoup
import requests
from typing import Dict
import yaml


def getHTML(verb: str) -> BeautifulSoup:
    
    if "se " == verb[:3]: #cambia el link en pronominales
        url = f"https://leconjugueur.lefigaro.fr/conjugaison/verbe/{verb[3:]}_pronominal.html"
    elif "s’" == verb[:2]: #cambia el link en pronominales
        url = f"https://leconjugueur.lefigaro.fr/conjugaison/verbe/{verb[2:]}_pronominal.html"
    else:
        url = f"https://leconjugueur.lefigaro.fr/conjugaison/verbe/{verb}.html"
    print(url)
    response = requests.get(url)

    if response.status_code != 200:
        print(f"Error al obtener la página para el verbo: {verb}")
        return None

    return BeautifulSoup(response.text, "html.parser")

def getConjugaisonDict(soup: BeautifulSoup) -> Dict:
    conjugations = {}
    # los modos verbales son de h2 y esa class_
    modes = soup.find_all("h2", class_="modeBloc")  

    for mode in modes:
        mode_name = mode.get_text(strip=True)
        conjugations[mode_name] = {}
        # Estructura del html
        # Los tiempos verbales correspondientes a ese modo verbal son los div que le siguien , sobre el mismo nivel
        # Esto termina al momento de encontrar otro h2, correspondiente a otro modo verbal
        # Se iterar sobre los siguientes elementos/hermanos hasta encontrar otro <h2> o el final
        next_element = mode.find_next_sibling()
        while next_element and next_element.name != "h2":
            # next_element es un div que corresponde a un tiempo verbal
            # este div interno (temps_name_tag) tiene otro div que contiene de texto el nombre/etiqueta del tiempo verbal
            # el div next_element con tiene de texto las conjugaciones para cada persona, separadas por renglones <br>
            if next_element.name == "div" and "conjugBloc" in next_element.get("class", []): #confirmamos que sea un div, dada la estructura
                temps_name_tag = next_element.find("div", class_="tempsBloc") #revisasos el elemento interno, para conocer el tiempo verbal
                if temps_name_tag:
                    temps_name = temps_name_tag.get_text(strip=True)
                    
                    for br in next_element.find_all("br"): #remplazamos los <br> por saltos de linea, ya que se traducen por defecto a espacios
                        br.replace_with("\n")
                    # del texto de next_element quitamos el texto de su div hijo y separamos por renglons, cada uno corresponde a un pronombre
                    linesConjugaisons = next_element.get_text()\
                        .replace(temps_name, "")\
                        .splitlines()

                    #guardamos las conjugaciones    
                    conjugations[mode_name][temps_name] = linesConjugaisons
            
            next_element = next_element.find_next_sibling()  # continuamos la iteración

    return conjugations


if __name__ == '__main__':
    #se abre yaml con verbos a descargar
    with open("./resources/verbsATelecharger.yaml", "r", encoding="utf-8") as file:
        verbs = yaml.safe_load(file)['verbs']
        
    #se guardan yamls individuales
    for verb in verbs:
        print(verb)
        soup = getHTML(verb)
        conjuaisonDict = getConjugaisonDict(soup)
        with open('./resources/verbs/' + verb + '.yaml', 'w', encoding="utf-8") as file:
            yaml.dump(conjuaisonDict, file, allow_unicode=True, default_flow_style=False)

