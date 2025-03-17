# Metaheurísticas para Optimización

## **Colaboradores**
- [Poncho_ajmv](https://github.com/poncho-ajmv)
- [rcardocg](https://github.com/rcardocg)
- [JoseEspanaD](https://github.com/JoseEspanaD)
- [LesterHernandez](https://github.com/LesterHernandez)
- [CrisIsaac-SH](https://github.com/CrisIsaac-SH)

Las tres primeras personas en venir con nosotros y decir que es "ad hoc" se ganan unas galletas caseras.
## Introducción
Las metaheurísticas son estrategias de optimización utilizadas para resolver problemas complejos donde encontrar una solución óptima exacta sería computacionalmente costoso o ineficiente. A diferencia de los métodos de búsqueda local, las metaheurísticas permiten explorar el espacio de soluciones de manera más amplia y evitar quedar atrapadas en óptimos locales.

Este repositorio contiene implementaciones de diversas metaheurísticas aplicadas a problemas de optimización, incluyendo:
- **Búsqueda Tabú**
- **Templado Simulado**
- **Algoritmos Genéticos**

## Metaheurísticas Implementadas
### 1. Búsqueda Tabú
La búsqueda tabú es un algoritmo basado en la mejora de soluciones mediante la exploración local, con mecanismos para evitar ciclos repetitivos y mejorar la búsqueda.
#### Características clave:
- Usa una **lista tabú** para evitar retrocesos inmediatos.
- Explora soluciones vecinas y permite moverse a soluciones peores temporalmente.
- Mejora la capacidad de escapar de óptimos locales.

### 2. Templado Simulado
El templado simulado se basa en el proceso de enfriamiento de los metales para aceptar soluciones subóptimas en etapas tempranas, mejorando la exploración global.

#### Características clave:
- Controlado por un **parámetro de temperatura** que decrece gradualmente.
- Permite aceptar soluciones peores al principio para evitar óptimos locales.
- Utiliza una función de probabilidad para tomar decisiones de aceptación de nuevas soluciones.

### 3. Algoritmos Genéticos
Los algoritmos genéticos (AG) imitan la evolución biológica mediante la selección natural, cruzamiento y mutación para mejorar soluciones a través de generaciones.
#### Características clave:
- Usa una **población de soluciones** que evoluciona iterativamente.
- Se aplican operadores de **selección, cruce y mutación**.
- Balancea exploración y explotación para mejorar la calidad de las soluciones.

## Aplicaciones
Las metaheurísticas tienen aplicaciones en diversos campos, como:
- **Optimización de rutas**: Problema del Viajante (TSP), logística y transporte.
- **Diseño de circuitos electrónicos**: Minimizar movimientos en manufactura.
- **Planificación y programación**: Asignación de tareas y recursos.

## Estructura del Repositorio
- `busqueda_tabu.py` - Implementación de la Búsqueda Tabú.
- `busquedatabunoresticciones.py` - Implementación de la Búsqueda Tabú sin restricciones.
- `templado_simulado.py` - Implementación del Templado Simulado sin animacion.
- `animaciontempladosimulado.py` - Implementación del Templado Simulado con algoritmo.
- `algoritmo_genetico.py` - Implementación de Algoritmos Genéticos.
- `README.md` - Este documento.

## Uso
Para ejecutar cualquiera de las implementaciones, simplemente ejecuta:
```bash
python nombre_del_script.py
```
Asegúrate de tener instaladas las dependencias necesarias.

## Recursos
Para mayor información, revisa los siguientes recursos:
- [Video sobre el Problema del Viajante](https://www.youtube.com/watch?v=yGvYQYKdmeU)
- [Metaheurísticas en optimización](https://www.youtube.com/watch?v=K88hTnzo-tI)

## Contribuciones
Las contribuciones son bienvenidas. Puedes enviar un _pull request_ con mejoras o nuevas implementaciones.


## Licencia
Este proyecto está bajo la licencia MIT. Puedes usarlo libremente para propósitos educativos y de investigación.
