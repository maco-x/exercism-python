import unittest

from exercism import hamming


# Tests adapted from `problem-specifications//canonical-data.json` @ v2.0.1

class HammingTest(unittest.TestCase):

    def test_empty_strands(self):
        self.assertEqual(hamming("", ""), 0)

    def test_identical_strands(self):
        self.assertEqual(hamming("A", "A"), 0)

    def test_long_identical_strands(self):
        self.assertEqual(hamming("GGACTGA", "GGACTGA"), 0)

    def test_complete_distance_in_single_nucleotide_strands(self):
        self.assertEqual(hamming("A", "G"), 1)

    def test_complete_distance_in_small_strands(self):
        self.assertEqual(hamming("AG", "CT"), 2)

    def test_small_distance_in_small_strands(self):
        self.assertEqual(hamming("AT", "CT"), 1)

    def test_small_distance(self):
        self.assertEqual(hamming("GGACG", "GGTCG"), 1)

    def test_small_distance_in_long_strands(self):
        self.assertEqual(hamming("ACCAGGG", "ACTATGG"), 2)

    def test_non_unique_character_in_first_strand(self):
        self.assertEqual(hamming("AAG", "AAA"), 1)

    def test_non_unique_character_in_second_strand(self):
        self.assertEqual(hamming("AAA", "AAG"), 1)

    def test_same_nucleotides_in_different_positions(self):
        self.assertEqual(hamming("TAG", "GAT"), 2)

    def test_large_distance(self):
        self.assertEqual(hamming("GATACA", "GCATAA"), 4)

    def test_large_distance_in_off_by_one_strand(self):
        self.assertEqual(hamming("GGACGGATTCTG", "AGGACGGATTCT"), 9)

    def test_disallow_first_strand_longer(self):
        with self.assertRaisesWithMessage(ValueError):
            hamming("AATG", "AAA")

    def test_disallow_second_strand_longer(self):
        with self.assertRaisesWithMessage(ValueError):
            hamming("ATA", "AGTG")

    # Utility functions
    def setUp(self):
        try:
            self.assertRaisesRegex = self.assertRaisesRegexp
        except AttributeError:
            pass

    def assertRaisesWithMessage(self, exception):
        return self.assertRaisesRegex(exception, r".+")


if __name__ == '__main__':
    unittest.main()