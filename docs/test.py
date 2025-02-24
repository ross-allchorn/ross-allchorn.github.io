import unittest
from snake_game import Snake, Game

# test.py
# This file contains unit tests for the snake game.
# The tests will ensure that the game logic works correctly and help prevent future bugs.
class TestSnakeGame(unittest.TestCase):

    def setUp(self):
        self.game = Game()
        self.snake = self.game.snake

    def test_snake_initial_length(self):
        self.assertEqual(len(self.snake.body), 3)

    def test_snake_initial_position(self):
        self.assertEqual(self.snake.body[0], (5, 5))

    def test_snake_move(self):
        initial_head_position = self.snake.body[0]
        self.snake.move()
        new_head_position = self.snake.body[0]
        self.assertNotEqual(initial_head_position, new_head_position)

    def test_snake_grow(self):
        initial_length = len(self.snake.body)
        self.snake.grow()
        new_length = len(self.snake.body)
        self.assertEqual(new_length, initial_length + 1)

    def test_game_over(self):
        self.snake.body = [(5, 5), (5, 6), (5, 7)]
        self.snake.direction = (0, -1)
        self.snake.move()
        self.assertTrue(self.game.is_game_over())

if __name__ == '__main__':
    unittest.main()