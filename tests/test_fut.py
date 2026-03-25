import unittest

from src.fut import MatchResult, goal_difference, total_points


class MatchResultTests(unittest.TestCase):
    def test_winner(self):
        self.assertEqual(MatchResult(2, 1).winner(), "home")
        self.assertEqual(MatchResult(0, 3).winner(), "away")
        self.assertEqual(MatchResult(1, 1).winner(), "draw")

    def test_points_for_home(self):
        self.assertEqual(MatchResult(2, 1).points_for_home(), 3)
        self.assertEqual(MatchResult(1, 1).points_for_home(), 1)
        self.assertEqual(MatchResult(0, 2).points_for_home(), 0)

    def test_aggregations(self):
        matches = [MatchResult(2, 1), MatchResult(1, 1), MatchResult(0, 2)]
        self.assertEqual(total_points(matches), 4)
        self.assertEqual(goal_difference(matches), -1)


if __name__ == "__main__":
    unittest.main()
