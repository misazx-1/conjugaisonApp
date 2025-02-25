import os 
from typing import List
import yaml
class MenuInterfaz():

    optionsPrincipales = [
        "Jugar", 
        "Ver verbos disponibles", 
        "Agregar verbo",
        "Salir"
        ]

    def __init__(self):
        with open('./resources/modosVerbalesTiempos.yaml', 'r', encoding='utf-8') as file:
            self.modosVerbalesTiempos = yaml.safe_load(file)
            

    def showOptions(self, options: List[str]) -> None:
        """
            Muestra las opciones de manera enumerada
        """
        for row, option in enumerate(options):
            print(str(row) + '. ' + option + '\n')

    def limpiarTerminal(self) -> None:
        """
            Metodo para limpiar terminal
        """
        if os.name == 'nt':  # windows
            os.system('cls')
        else:  # linux/max
            os.system('clear')
    
    def showMenuPrincipal(self) -> int:
        """
            Muestra las opciones disponbiels
        """
        self.limpiarTerminal()

        self.showOptions(self.optionsPrincipales)

        try:
            seleccion = int(input())
            return seleccion
        except: #si las opcion es invalidad reiniciamos menu
            print("Selección invalidad\n")
            return self.showMenuPrincipal()

    def showMenuModoVerbal(self) -> str:
        """
            Muestra menu para selección de modo verbal.
            Retorna el modo verbal a usar en str.
        """
        self.limpiarTerminal()
        
        modosVerbales = list(self.modosVerbalesTiempos.keys())
        print(f"modos verbales lista {modosVerbales}")
        self.showOptions(modosVerbales)

        try:
            
            seleccion = modosVerbales[int(input())]
            return seleccion
        except: #si las opcion es invalidad reiniciamos menu
            print("Selección invalidad\n")
            return self.showMenuModoVerbal()
    
    def showMenuTiempoVerbal(self, modoVerbal: str) -> str:
        """
            Muestra menu para selección de tiempo verbal.
            Retorna el tiempo verbal a usar en str.
        """
        self.limpiarTerminal()
        print("modo verbal seleccionado " + modoVerbal)
        self.showOptions(self.modosVerbalesTiempos[modoVerbal])

        try:
            seleccion = self.modosVerbalesTiempos[modoVerbal][int(input())]
            return seleccion
        except: #si las opcion es invalidad reiniciamos menu
            print("Selección invalidad\n")
            return self.showMenuTiempoVerbal(self, modoVerbal)
    
    def showMenuNumeroVerbs(self) -> int:
        """
        """
        self.limpiarTerminal()
        try:
            return int(input("Ingresa número de verbos a conjugar\n"))
        except:
            return self.showMenuNumeroVerbs()
        
        

        

    

        
    
