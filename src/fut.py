"""Utilidades simples para analizar resultados de fútbol."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Iterable


@dataclass(frozen=True)
class MatchResult:
    """Representa el marcador de un partido de fútbol."""

    home_goals: int
    away_goals: int

    def winner(self) -> str:
        """Devuelve el ganador: 'home', 'away' o 'draw'."""
        if self.home_goals > self.away_goals:
            return "home"
        if self.away_goals > self.home_goals:
            return "away"
        return "draw"

    def points_for_home(self) -> int:
        """Calcula los puntos del local según reglas estándar (3/1/0)."""
        winner = self.winner()
        if winner == "home":
            return 3
        if winner == "draw":
            return 1
        return 0


def total_points(results: Iterable[MatchResult]) -> int:
    """Suma los puntos del equipo local en una lista de partidos."""
    return sum(result.points_for_home() for result in results)


def goal_difference(results: Iterable[MatchResult]) -> int:
    """Diferencia de goles (a favor - en contra) del equipo local."""
    return sum(result.home_goals - result.away_goals for result in results)
