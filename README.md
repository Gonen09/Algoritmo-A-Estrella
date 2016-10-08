# Algoritmo-A-Estrella
Algoritmo a* con intefaz de usuario en Python

Desarrollo de buscador en laberintos con meta cambiante, utilizando el algoritmo A*.-

Objetivo:

Mostrar el camino recorrido del desde un punto A hasta un B en un laberinto predeterminado,
en ocasiones el punto B puede cambiar de ubicación mientras se va mostrando el recorrido.
En ese caso se debe mostrar el nuevo camino.

Resumen:

Para poder cumplir el objetivo se guardan las posiciones iniciales de A y B, para mostrar
el recorrido mostramos las posiciones una por una del camino entregado por el algoritmo A*,
Si el punto B cambia de posición, se modifica el mapa con las nuevas posiciones de A y B
(A cambia a la última posición del camino y B a la nueva posición que cambia al azar) y se
repite el algoritmo de A*. Previamente se ha guardado en una lista las posiciones anteriores
a la cual se le suman las nuevas. El algoritmo termina cuando el camino llega hasta el punto B.
