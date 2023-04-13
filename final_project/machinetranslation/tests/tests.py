import unittest

from machinetranslation import english_to_french, french_to_english

class TestEnglishToFrench(unittest.TestCase):
    def test1(self):
        self.assertEqual(english_to_french("Hello"), "Bonjour")
        self.assertNotEqual(english_to_french("None"), "")
        self.assertNotEqual(english_to_french("Hello"),"Hello")
    
class TestFrenchToEnglish(unittest.TestCase):
    def test1(self):
        self.assertEqual(french_to_english("Bonjour"),"Hello")
        self.assertNotEqual(french_to_english("None"), "")
        self.assertNotEqual(french_to_english("Bonjour"),"Bonjour")

if __name__ == '__main__':
    unittest.main()