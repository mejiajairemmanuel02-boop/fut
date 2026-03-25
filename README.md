# fut

Pequeña librería en Python para calcular métricas básicas de partidos de fútbol.

## Qué incluye

- `MatchResult`: modelo inmutable para representar un marcador.
- `total_points`: suma de puntos del equipo local en varios partidos.
- `goal_difference`: diferencia de goles acumulada del equipo local.

## Uso rápido

```python
from src.fut import MatchResult, total_points, goal_difference

matches = [MatchResult(2, 1), MatchResult(1, 1), MatchResult(0, 2)]
print(total_points(matches))   # 4
print(goal_difference(matches))  # -1
```

## Ejecutar pruebas

```bash
python -m unittest discover -s tests -v
```
