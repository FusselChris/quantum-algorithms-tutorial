import unittest
from src.black_hole_toy import black_hole_toy_model

class TestBlackHoleToy(unittest.TestCase):
    def test_black_hole_toy_model(self):
        _, ent = black_hole_toy_model()
        self.assertGreater(ent, 0)  # Entropy should be positive for entangled system
        self.assertLess(ent, 1.1)   # Upper bound for 1-qubit entropy (~1 for max entanglement)

if __name__ == '__main__':
    unittest.main()
