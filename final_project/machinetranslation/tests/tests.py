import unittest
import sys
sys.path.append('..')
from translator import english_to_french, french_to_english

class TestEnglishTranslator(unittest.TestCase):
    def test_english_to_french(self):
        self.assertEqual(english_to_french('Hello'), 'Bonjour')
        self.assertEqual(english_to_french(None), "Please type a phrase in English")

class TestFrenchTranslator(unittest.TestCase):
    def test_french_to_english(self):
        self.assertEqual(french_to_english('Bonjour'), 'Hello')
        self.assertEqual(french_to_english(None), "Please type a phrase in French")

if __name__ == '__main__':
    unittest.main()