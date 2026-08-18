Clase 1 — Conceptos de POO y su expresión en Python
Facultad de Ingeniería del Ejército · POO en Python

← Todos los ejercicios
Préstamo de biblioteca
Una biblioteca presta ejemplares por 7 días. Necesitamos representar un préstamo sin diccionarios ni funciones que calculen reglas por afuera.

Creá la clase Prestamo en solucion/prestamo.py. Al crearla recibe titulo, nombre_socio y dias_transcurridos. Un préstamo es válido solo si el título y el socio no están vacíos, y los días transcurridos no son negativos. Para datos inválidos, lanzá ValueError.

Su protocolo público debe ser:

prestamo = Prestamo("El principito", "Ana", 9)

assert prestamo.esta_vencido() is True
assert prestamo.dias_de_retraso() == 2
assert prestamo.resumen() == "El principito — Ana — vencido (2 días)"
Reglas:

esta_vencido() devuelve True solo si pasaron más de 7 días.
dias_de_retraso() devuelve 0 si todavía está en término.
resumen() devuelve "<título> — <socio> — en término" o "<título> — <socio> — vencido (<n> días)".
El código que usa el préstamo no debe calcular si venció ni sus días de retraso leyendo atributos.
Prestamo

+titulo

+nombre_socio

+dias_transcurridos

+esta_vencido() : bool

+dias_de_retraso() : int

+resumen() : str

Evidencia a entregar
solucion/prestamo.py con la clase.
tests/test_prestamo.py con al menos cuatro tests: préstamo en término, préstamo vencido, retraso cero y un dato inválido.
Una respuesta breve (3 a 5 líneas): ¿qué regla quedó dentro de Prestamo y qué problema habría si la calculara quien usa el objeto?



RESPUESTA FINAL:
Dentro de Prestamo quedó la regla de los 7 días límite y la cuenta para saber si está vencido y cuántos días de demora lleva.

Si ese cálculo se hiciera por fuera, estaríamos desparramando la lógica por todo el sistema y rompiendo el encapsulamiento. El gran problema sería el mantenimiento: si mañana la biblioteca decide cambiar el plazo a 14 días, tendríamos que buscar y corregir esa cuenta en diez lugares distintos del código en vez de modificar un solo número dentro de la clase.
