from MenuInterfaz import MenuInterfaz
from PartidaJuego import PartidaJuego
import os 
import yaml
class Juego():

    def __init__(self):
        self.menuInterfaz = MenuInterfaz()
        self.verbsDict = {} #este contiene de clave a los verbos y valor toda su info en otro 
        
        

        for verbYAML in os.listdir('./resources/verbs'):
            with open('./resources/verbs/' + verbYAML, 'r', encoding='utf-8') as file:
                verbDict = yaml.safe_load(file)
                verbName = os.path.splitext(verbYAML)[0]
                self.verbsDict[verbName] = verbDict

    def iniciar(self) -> None:
        """
            Muestra menus y liga a la opcion seleccionada
        """
        opcionPrincipal = self.menuInterfaz.showMenuPrincipal()
        if opcionPrincipal == 0:
            modoVerbal = self.menuInterfaz.showMenuModoVerbal()
            tiempoVerbal = self.menuInterfaz.showMenuTiempoVerbal(modoVerbal)
            numeroVerbs = self.menuInterfaz.showMenuNumeroVerbs()
            self.jugar(modoVerbal, tiempoVerbal, numeroVerbs)
        if opcionPrincipal == 1:
            pass
        if opcionPrincipal == 2:
            pass
        if opcionPrincipal == 3:
            pass
    def jugar(self, modoVerbal: str, tiempoVerbal: str, numeroVerbs: int) -> None:
        partidaJuego = PartidaJuego(modoVerbal, tiempoVerbal, numeroVerbs, self.verbsDict)
        aciertos = partidaJuego.comenzarPartida()
        print(f"aciertos totatles/totales = {aciertos}/{numeroVerbs * 6}")

        

if __name__ == '__main__':
    juego = Juego()
    juego.iniciar()
