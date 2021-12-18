import unittest
from controls import max_score

class GameTests(unittest.TestCase):

    def test_INCorrectFiledata(self):
        g = open('bestresult.txt', 'w+')
        g.write(str('ffoofo'))
        g.close()
        self.assertEqual(max_score(),0)
    def test_CorrectFiledata(self):
        g = open('bestresult.txt', 'w+')
        g.write(str('0'))
        g.close()
        self.assertEqual(max_score(),0)

if __name__ == "__main__":
    unittest.main()