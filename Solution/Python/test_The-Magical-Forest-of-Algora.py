import unittest
from unittest.mock import patch
import random

from The-Magical-Forest-of-Algora import dance_moves, forest_state

class ForestTests(unittest.TestCase):
    def test_dance_moves(self):
        # Test if all dance moves have effects defined
        for move in dance_moves:
            self.assertIn(move, dance_moves.keys(), f"Effect not defined for dance move: {move}")

    def test_forest_state(self):
        # Test if the initial state of the forest is 'Normal'
        self.assertEqual(forest_state, 'Normal', "Initial state of the forest is not 'Normal'")

    @patch('random.choice')
    def test_dance_sequence(self, mock_choice):
        # Test the dance sequence for a specified number of times
        mock_choice.side_effect = ['Twirl', 'Spin', 'Leap', 'Spin', 'Twirl']
        expected_states = ['Enchanted', 'Calm', 'Magical', 'Normal', 'Enchanted']
        actual_states = []

        for sequence in range(5):
            lox_move = random.choice(['Twirl', 'Leap', 'Spin'])
            drako_move = random.choice(['Spin', 'Twirl', 'Leap', 'Leap', 'Spin'])

            if (lox_move, drako_move) in dance_moves:
                effect = dance_moves[(lox_move, drako_move)]
                if effect == 'Fireflies light up the forest':
                    forest_state = 'Enchanted'
                elif effect == 'Gentle rain starts falling':
                    forest_state = 'Calm'
                elif effect == 'A rainbow appears in the sky':
                    forest_state = 'Magical'

            actual_states.append(forest_state)

        self.assertEqual(actual_states, expected_states, "Incorrect state of the forest after dance sequence")

if __name__ == '__main__':
    unittest.main()