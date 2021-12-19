import unittest
from controls import max_score
from controls import overwriting_max_score

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
    def test_MaxScore1(self):
        max_score = overwriting_max_score(0,15)
        self.assertEqual(max_score,15)

    def test_MaxScore2(self):
        max_score = overwriting_max_score(16,15)
        self.assertEqual(max_score,16)

    def test_overwriting_max_score(self):
        g = open('bestresult.txt', 'w+')
        max_score = overwriting_max_score(10,15)
        f = g.readline()
        g.close()
        self.assertEqual(f,'')

    def test_overwriting_max_score2(self):
        g = open('bestresult.txt', 'w+')
        max_score = overwriting_max_score(100,15)
        f = g.readline()
        g.truncate(0)
        g.close()
        self.assertEqual(f,'100')



if __name__ == "__main__":
    unittest.main()