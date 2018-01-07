import unittest

from exercism import bob


# Tests adapted from `problem-specifications//canonical-data.json` @ v1.0.0

class BobTests(unittest.TestCase):
    def test_stating_something(self):
        self.assertEqual(bob("Tom-ay-to, tom-aaaah-to."), "Whatever.")

    def test_shouting(self):
        self.assertEqual(bob("WATCH OUT!"), "Whoa, chill out!")

    def test_shouting_gibberish(self):
        self.assertEqual(bob("FCECDFCAAB"), "Whoa, chill out!")

    def test_asking_a_question(self):
        self.assertEqual(
            bob("Does this cryogenic chamber make me look fat?"), "Sure.")

    def test_asking_a_numeric_question(self):
        self.assertEqual(bob("You are, what, like 15?"), "Sure.")

    def test_asking_gibberish(self):
        self.assertEqual(bob("fffbbcbeab?"), "Sure.")

    def test_talking_forcefully(self):
        self.assertEqual(
            bob("Let's go make out behind the gym!"), "Whatever.")

    def test_using_acronyms_in_regular_speech(self):
        self.assertEqual(
            bob("It's OK if you don't want to go to the DMV."),
            "Whatever.")

    def test_forceful_question(self):
        self.assertEqual(
            bob("WHAT THE HELL WERE YOU THINKING?"), "Whoa, chill out!")

    def test_shouting_numbers(self):
        self.assertEqual(bob("1, 2, 3 GO!"), "Whoa, chill out!")

    def test_only_numbers(self):
        self.assertEqual(bob("1, 2, 3"), "Whatever.")

    def test_question_with_only_numbers(self):
        self.assertEqual(bob("4?"), "Sure.")

    def test_shouting_with_special_characters(self):
        self.assertEqual(
            bob("ZOMG THE %^*@#$(*^ ZOMBIES ARE COMING!!11!!1!"),
            "Whoa, chill out!")

    def test_shouting_with_no_exclamation_mark(self):
        self.assertEqual(bob("I HATE YOU"), "Whoa, chill out!")

    def test_statement_containing_question_mark(self):
        self.assertEqual(
            bob("Ending with ? means a question."), "Whatever.")

    def test_non_letters_with_question(self):
        self.assertEqual(bob(":) ?"), "Sure.")

    def test_prattling_on(self):
        self.assertEqual(
            bob("Wait! Hang on. Are you going to be OK?"), "Sure.")

    def test_silence(self):
        self.assertEqual(bob(""), "Fine. Be that way!")

    def test_prolonged_silence(self):
        self.assertEqual(bob("          "), "Fine. Be that way!")

    def test_alternate_silence(self):
        self.assertEqual(bob("\t\t\t\t\t\t\t\t\t\t"), "Fine. Be that way!")

    def test_multiple_line_question(self):
        self.assertEqual(
            bob("\nDoes this cryogenic chamber make me look fat?\nno"),
            "Whatever.")

    def test_starting_with_whitespace(self):
        self.assertEqual(bob("         hmmmmmmm..."), "Whatever.")

    def test_ending_with_whitespace(self):
        self.assertEqual(
            bob("Okay if like my  spacebar  quite a bit?   "), "Sure.")

    def test_other_whitespace(self):
        self.assertEqual(bob("\n\r \t"), "Fine. Be that way!")

    def test_non_question_ending_with_whitespace(self):
        self.assertEqual(
            bob("This is a statement ending with whitespace      "),
            "Whatever.")


if __name__ == '__main__':
    unittest.main()