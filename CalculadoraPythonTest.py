import pytest
from CalculadoraPython import CalculadoraPython

def test_somar():
    calculadorapython = CalculadoraPython(3,3)
    assert calculadorapython.somar() == 6

def test_diminuir():
    calculadorapython = CalculadoraPython(2,1)
    assert calculadorapython.diminuir() == 1

def test_multiplicar():
    calculadorapython = CalculadoraPython(2,4)
    assert calculadorapython.multiplicar() == 8

def test_dividir():
    calculadorapython = CalculadoraPython(15,5)
    assert calculadorapython.dividir() == 3
