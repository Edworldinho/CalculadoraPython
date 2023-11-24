import pytest
from CalculadoraPython import CalculadoraPython

def test_somar():
    calculadorapython = CalculadoraPython(3,3)
    assert CalculadoraPython.somar(self) == 6

def test_diminuir():
    calculadorapython = CalculadoraPython(2,1)
    assert CalculadoraPython.diminuir(self) == 1

def test_multiplicar():
    calculadorapython = CalculadoraPython(2,4)
    assert CalculadoraPython.multiplicar(self) == 8

def test_dividir():
    calculadorapython = CalculadoraPython(15,5)
    assert CalculadoraPython.dividir(self) == 3
