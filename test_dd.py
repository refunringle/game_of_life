import unittest
import dd as game
import random

generation = [
    [True, False, False, True, False],
    [False, True, False, True, True],
    [True, False, True, True, True],
    [False, False, True, False, False],
    [True, False, True, False, False]
]


class GameTestCase(unittest.TestCase):

    def test_get_random_generation(self):
        for i in range(5):
            width, height = random.randint(0, 9), random.randint(0, 9)
            world = game.get_random_generation(width, height)
            self.assert_generation(height, width, world)

    def assert_generation(self, height, width, world):
        self.assertEqual(height, len(world))
        for inner_list in world:
            self.assertEqual(width, len(inner_list))
            for value in inner_list:
                self.assertIn(value, (True, False))

    def test_compose_out(self):
        out = game.compose_out([False, False, True, False, False])
        self.assertEqual("..#..", out)
        out = game.compose_out([True, True, True, False, False])
        self.assertEqual("###..", out)
        out = game.compose_out([False, False, True, False, True])
        self.assertEqual("..#.#", out)

    def test_get_next_generation(self):
        expected = [
            [True, False, False, True, False],
            [False, True, False, False, False],
            [True, False, False, False, False],
            [True, False, True, False, False],
            [False, False, True, True, True]
        ]
        self.assertEqual(expected, game.get_next_generation(generation))

    def test_offset(self):
        self.assertEqual(0, game.offset(5, 5))
        self.assertEqual(4, game.offset(-1, 5))
        self.assertEqual(2, game.offset(2, 5))
        self.assertEqual(3, game.offset(3, 4))
        self.assertEqual(0, game.offset(0, 2))

    def test_count_alive_neighbours(self):
        count = game.count_alive_neighbours(generation, 2, 1)
        self.assertEqual(5, count)
        count = game.count_alive_neighbours(generation, 0, 0)
        self.assertEqual(3, count)
        count = game.count_alive_neighbours(generation, 4, 2)
        self.assertEqual(4, count)


if __name__ == '__main__':
    unittest.main()