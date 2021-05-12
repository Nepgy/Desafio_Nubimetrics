import pytest
#from ('./7_Desafio.py') import generarPathMensuales
from 'Desafio 02\2_desafio.py' import *

def test_desafio_02(tmpdir):
    try open('Desafio 02\\2_desafio.py', mode= 'r')
    
    assert 


def test_desafio_03():
    assert
    

def test_desafio_04():
    assert 


def test_desafio_05():
    assert 


def test_desafio_06():
    assert 


def test_desafio_07():

    assert generarPathMensuales(año, mes, dia)

@pytest.mark.parametrize(
    "input_a, input_b, input_c, expected"[
            (2020,11,5,5)
            (2019,9,17,17)
            (2032,12,9,9)
            (2020,5,30,30)
    ]
)
def test_desafio_07_multi(input_a, input_b, input_c, expected):
    assert len(generarPathMensuales(input_a, input_b, input_c)) == expected

def test_desafio_08():
    assert 


def test_desafio_09():
    assert 


def test_desafio_10():
    assert 


def test_desafio_11():
    assert