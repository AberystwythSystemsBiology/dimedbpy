import unittest
import dimedbpy

class RunTest(unittest.TestCase):

    def test_get_metabolites(self):
        metabolte = dimedbpy.get_metabolites("NAme", "Sucrose")
        print(metabolte)

if __name__ == '__main__':
    unittest.main()