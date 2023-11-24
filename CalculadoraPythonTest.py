import pytest
from CalculadoraPython import CalculadoraPython

def test_somar():
    assert CalculadoraPython.somar(3,3) == 6

def test_diminuir():
    assert CalculadoraPython.diminuir(2,1) == 1

def test_multiplicar():
    assert CalculadoraPython.multiplicar(2,4) == 8

def test_dividir():
    assert CalculadoraPython.dividir(15, 5) == 3