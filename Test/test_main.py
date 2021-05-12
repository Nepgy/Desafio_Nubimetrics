import unittest
import os

from dependencias import *



def test_desafio_02():
    try:
        desafio_2()
        pathJ = pathJson()
        pathF = pathFolder()
        os.remove(pathJ)
        os.rmdir(pathF)
        Flag = True
    except:
        Flag = False
        
    assert Flag == True


def test_desafio_03():
    
    try:
        desafio_3()
        os.remove('Currencies.csv')
        os.remove('log.csv')
        Flag = True
    except:
        Flag = False
    
    assert Flag == True


def test_desafio_04():

    try:
        desafio_4()
        os.remove('Sales_DF.parquet')
        Flag = True
    except:
        Flag = False
    
    assert Flag == True


def test_desafio_05():
    try:
        desafio_5()
        os.remove('Sales_DF_row_key.parquet')
        Flag = True
    except:
        Flag = False
    
    assert Flag == True    


def test_desafio_06():
    try:
        desafio_6()
        os.remove('ventas_nivel_ordenado.parquet')
        os.remove('df_sales_nivel_ordenado.parquet')
        Flag = True
    except:
        Flag = False
    
    assert Flag == True    


def test_desafio_07():
    Flag = (generarPathMensuales(2021, 11, 14) == ['https://importantdata@location/2021/11/1/', 'https://importantdata@location/2021/11/2/', 'https://importantdata@location/2021/11/3/', 'https://importantdata@location/2021/11/4/', 'https://importantdata@location/2021/11/5/', 'https://importantdata@location/2021/11/6/', 'https://importantdata@location/2021/11/7/', 'https://importantdata@location/2021/11/8/', 'https://importantdata@location/2021/11/9/', 'https://importantdata@location/2021/11/10/', 'https://importantdata@location/2021/11/11/', 'https://importantdata@location/2021/11/12/', 'https://importantdata@location/2021/11/13/', 'https://importantdata@location/2021/11/14/'])
    Flag = (generarPathMensuales(2022, 1, 5) == ['https://importantdata@location/2022/1/1/', 'https://importantdata@location/2022/1/2/', 'https://importantdata@location/2022/1/3/', 'https://importantdata@location/2022/1/4/', 'https://importantdata@location/2022/1/5/'])
    Flag = (generarPathMensuales(1997, 5, 9) == ['https://importantdata@location/1997/5/1/', 'https://importantdata@location/1997/5/2/', 'https://importantdata@location/1997/5/3/', 'https://importantdata@location/1997/5/4/', 'https://importantdata@location/1997/5/5/', 'https://importantdata@location/1997/5/6/', 'https://importantdata@location/1997/5/7/', 'https://importantdata@location/1997/5/8/', 'https://importantdata@location/1997/5/9/'])

    assert Flag == True


def test_desafio_08():
    Flag = (generarPathUltimosDias(20201105, 2) == ['https://importantdata@location/2020/11/5/', 'https://importantdata@location/2020/11/4/'])
    Flag = (generarPathUltimosDias(19870803, 3) == ['https://importantdata@location/1987/08/3/', 'https://importantdata@location/1987/08/2/', 'https://importantdata@location/1987/08/1/'])
    Flag = (generarPathUltimosDias(20211113, 4) == ['https://importantdata@location/2021/11/13/', 'https://importantdata@location/2021/11/12/', 'https://importantdata@location/2021/11/11/', 'https://importantdata@location/2021/11/10/'])

    assert Flag == True


#Aplicando los test
test_desafio_02()
test_desafio_03()
test_desafio_04()
test_desafio_05()
test_desafio_06()
test_desafio_07()
test_desafio_08()