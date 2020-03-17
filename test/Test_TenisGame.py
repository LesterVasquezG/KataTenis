#Autor: Vasquez Galvan Lester
import sys
import unittest
from src.TenisGame import TenisGame

class Test_Tenis(unittest.TestCase):
    def test_prueba1(self):
        juego1=TenisGame("Player 1","Player 2")
        result=juego1.ganador(0,0)
        self.assertEqual("love",result) ##Estan en 0 puntos

    def test_prueba2(self):
        juego2=TenisGame("Player 1","Player 2")
        result=juego2.ganador(3,3)
        self.assertEqual("Deuce",result) ##Estan en Deuce

    def test_prueba3(self):
        juego3=TenisGame("Player 1","Player 2")
        result=juego3.ganador(4,3)
        self.assertEqual("Player-1-AD",result) #Player 1 esta en ventaja 40(Ad)-30

    def test_prueba4(self):
        juego4=TenisGame("Player 1","Player 2")
        result=juego4.ganador(3,4)
        self.assertEqual("Player-2-AD",result) #Player 2 esta en ventaja 30-40(Ad)

    def test_prueba5(self):
        juego5=TenisGame("Player 1","Player 2")
        result=juego5.ganador(1,4)
        self.assertEqual("Player-2-Gana",result) #Player 2 Gana 15-40+

