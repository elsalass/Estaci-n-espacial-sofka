from cgi import print_arguments
from spacecraft import Spacecraft
from launcher_spacecraft import Launcher_spacecraft
from unmanned import Unmanned
from manned import Manned

def main():

    launcher_spacecraft1 = Launcher_spacecraft("Saturno V", "Vehículo Lanzadera", "EE.UU.", 2900, "H(liq) + O(liq)", "1967 - 1973", "Permitio transportar la nave tripulada Apolo hasta la luna!!", 3500, 100, 118)

    print(vars(launcher_spacecraft1))
    print(" ")

    launcher_spacecraft2 = Launcher_spacecraft("Energia", "Vehículo lanzadera", "Rusia/Ucrania", 2400, "Queroseno+O(liq)", "1987 - 1988", "Ponía en orbita al transbordador Buran", 3060, 60, 100 )

    print(vars(launcher_spacecraft2))
    print(" ")


    launcher_spacecraft3 = Launcher_spacecraft("Ariane 5", "Vehículo Lanzadero", "Unión Europea", 777 , "Sólido+N(liq.)+O(liq.)", "1996 - Act.", "Servir como lanzadera del minitransbordador Hermes", 3700, 30, 115)

    print(vars(launcher_spacecraft3))
    print(" ")

    unmanned1 = Unmanned("ATV", "Naves no tripuladas", "Unión europea", 10, "MMH+NO", "2008 - Act.","Vehículo automatico capaz de tomar decisiones por si solo", 0.2, "Estudiar cuerpos celestes", True)

    print(vars(unmanned1))
    print(" ")

    unmanned2 = Unmanned("Pionero Xl", "Naves no tripuladas", "EE.UU.", 258, "NO4+MMH", "1973 - Act.", "Se desplaza sin energia de forma inercial", 26, "Estudiar Júpiter", True) 

    print(vars(unmanned2))
    print(" ")

    unmanned3 = Unmanned("Mariner lV", "Naves no tripuladas", "EE.UU.", 234, "N2H4", "1965 - Act.", "La primera que sobrevoló el planeta", 22.44, "Estudiar Marte", False)

    print(vars(unmanned3))
    print(" ")

    manned1 = Manned ("Skylab", "Naves tripuladas", "EE.UU.", 77, "Queroseno+H(liq.)","1973 - 1979", "Primera estaciónn espacial estadounidense", 0, 3, False, 435)

    print(vars(manned1))
    print(" ")

    manned2 = Manned ("Salyut", "Naves tripuladas", "Rusia", 20, "N2O4+UDMH", "1982 -1991", "El segundo de la historia", 3, 3, False, 248.9)

    print(vars(manned2))
    print(" ")

if __name__ == "__main__":
    main()
