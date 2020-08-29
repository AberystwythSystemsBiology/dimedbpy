import unittest
import dimedbpy


class RunTest(unittest.TestCase):

    def test_get_metabolite_by_name(self):
        metabolte = dimedbpy.get_metabolites("name", "Sucrose")
        # Assert that Sucrose has been found
        self.assertNotEqual(len(metabolte), 0)
        # Assert that the mol form is C12H22O11.
        self.assertTrue(metabolte[0].molecular_formula == "C12H22O11")

    def test_mass_positive_search(self):
        # Formic acid (CH2O2) - [M+H]1+ = ~47.01 m/z
        metabolites = dimedbpy.mass_search(47)
        print(metabolites)
        #self.assertTrue(type(metabolites) == list)


if __name__ == "__main__":
    unittest.main()
