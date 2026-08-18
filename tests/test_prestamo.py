import pytest
from solucion.prestamo import Prestamo

# si dias de retraso es 6, 6-7=0 entonces assert p1.dias_de_retraso() == 0 es TRUE
def test_prestamo_en_termino():
    
    p1 = Prestamo("El senor de los anillos", "Frodo", 6)
    assert p1.esta_vencido() == False
    assert p1.dias_de_retraso() == 0
    assert p1.resumen() == "El senor de los anillos — Frodo — en término"

# si dias de retraso es 8, 8-7=1 entonces assert p1.dias_de_retraso() == 1 es TRUE
def test_prestamo_vencido():
    p1 = Prestamo("El senor de los anillos", "Frodo", 8)
    assert p1.esta_vencido() == True
    assert p1.dias_de_retraso() == 1
    assert p1.resumen() == "El senor de los anillos — Frodo — vencido (1 días)"

# si dias de retraso es 7, 7-7=0 entonces assert p1.dias_de_retraso() == 0 es TRUE
def test_retraso_cero():
    p1 = Prestamo("El senor de los anillos", "Frodo", 7)
    assert p1.esta_vencido() == False
    assert p1.dias_de_retraso() == 0
    assert p1.resumen() == "El senor de los anillos — Frodo — en término"


def test_dato_invalido():
    with pytest.raises(ValueError):
        Prestamo("", "", 7)
    
# Si con Prestamo("", "", 7) te sale ValueError -> dare la prueba como aprobada --> 4 passed in 0.01s
