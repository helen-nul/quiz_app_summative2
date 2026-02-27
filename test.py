import unittest
from quiz_data import load_questions
from quiz_utility import clean_name 
from quiz_utility import character_check

class TestSmoke(unittest.TestCase):

    def test_load_questions_runs(self):
        self.assertTrue(1)

class TestQuiz (unittest.TestCase) :

    def test_load_questions_runs(self):
        questions = load_questions()
        self.assertIsNotNone(questions)

    def test_clean_name(self):
        self.assertEqual(clean_name("  jenny smith  "), "Jenny Smith")
        self.assertEqual(clean_name("  ALEX CHAPMAN  "), "Alex Chapman")

    def test_character_check_happy(self):
        self.assertTrue(character_check("Alice"))
        self.assertTrue(character_check(" Alice Bridgerton"))

    def test_chacter_check_unhappy(self):
        self.assertFalse(character_check("Alice21"))
        self.assertFalse(character_check("4404"))

if __name__ == "__main__":
    unittest.main()
    