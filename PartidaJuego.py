from typing import Dict, List
import os
import random

class PartidaJuego():

    pronombres = [
        'je', # 'Premiere personne du singulier',
        'tu',# 'Deuxième personne du singulier',
        'il/elle/on', # 'Troisième personne du singulier',
        'nous', # 'Première personne du pluriel',
        'vous', # 'Deuxième personne du pluriel',
        'ils/ellse'# 'Troisième personne du plurie'
    ]

    def __init__(self, modoVerbal: str, tiempoVerbal: str, numeroVerbs: int, verbosDict: Dict[str, Dict[str, Dict[str, List[str]]]]):
        self.modoVerbal = modoVerbal
        self.tiempoVerbal = tiempoVerbal
        self.numeroVerbs = numeroVerbs
        self.verbosDict = verbosDict

    def limpiarTerminal(self) -> None:
        """
            Metodo para limpiar terminal
        """
        if os.name == 'nt':  # windows
            os.system('cls')
        else:  # linux/max
            os.system('clear')

    def setVerbs(self) -> None:
        self.verbs = random.sample(list(self.verbosDict.keys()), self.numeroVerbs)

    def comenzarPartida(self) -> int:
        """
            Comienza partida interactiva
            retorn numero de aciertos
        """
        self.setVerbs()

        aciertos = 0

        for verb in self.verbs:
            self.limpiarTerminal()
            for index, pronombre in enumerate(self.pronombres):
                print(f"Conjugaison " + pronombre + ": " + verb)
                repite = True 
                repitio = False
                while repite:
                    reponse = input()
                    correctResponse = self.verbosDict[verb][self.modoVerbal][self.tiempoVerbal][index]
                    if reponse == correctResponse:
                        repite = False
                        if not repitio:
                            aciertos += 1

                    else:
                        print('Incorrecto, intenta otra vez')
                        repitio = True
        return aciertos




