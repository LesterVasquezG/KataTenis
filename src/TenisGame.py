
# Autor: Vasquez Galvan Lester
# Esta clase solo determina el ganador de un juego, un partido de tenis consta de 3 o 5 sets y un set cuenta con 6 juegos
# los puntos son 1=15, 2=30, 3=40 4=AD, 5= el segundo punto consecutivo despues del deuce

class TenisGame:
    def __init__(self,nomJug1,nomJug2):
        self.nombreJug1=nomJug1
        self.nombreJug2=nomJug2
    
    def ganador(self,puntaje1,puntaje2):
        #4-4 deuce y necesita un desempate
        #3-1 gana jugador 1, se debe ganar por diferencia de 2
        if (puntaje1==puntaje2==0):
            return "love"
        if puntaje1==puntaje2==1:
            return "15-15"
        if puntaje1==1 and puntaje2==0:
            return "15-0"
        if puntaje1==0 and puntaje2==1:
            return "0-15"
        if puntaje1==puntaje2==2:
            return "30-30"
        if puntaje1==2 and puntaje2==0:
            return "30-0"
        if puntaje1==0 and puntaje2==2:
            return "0-30"
        if puntaje1==3 and puntaje2==0:
            return "40-0"
        if puntaje1==0 and puntaje2==3:
            return "0-40"
        if puntaje1==2 and puntaje2==1:
            return "30-15"
        if puntaje1==1 and puntaje2==2:
            return "15-30"
        if puntaje1==3 and puntaje2==1:
            return "40-15"
        if puntaje1==1 and puntaje2==3:
            return "15-40"
        if puntaje1==2 and puntaje2==3:
            return "30-40"
        if puntaje1==3 and puntaje2==2:
            return "40-30"
        if (puntaje1==puntaje2==3)or(puntaje1==puntaje2==4):
            return "Deuce"
        if puntaje2==3 and puntaje1==4:
            return "Player-1-AD"
        if puntaje1==3 and puntaje2==4:
            return "Player-2-AD"
        if (( puntaje1==2 and puntaje2==4)or(puntaje1==1 and puntaje2==4)or (puntaje1==3 and puntaje2==5)or (puntaje1==0 and puntaje2==4)):
            return "Player-2-Gana"
        if (( puntaje2==2 and puntaje1==4)or(puntaje2==1 and puntaje1==4)or (puntaje2==3 and puntaje1==5)or(puntaje1==4 and puntaje2==0)):
            return "Player-1-Gana"        



         

                        




 

















