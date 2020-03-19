

# test/my_mod_test.py

import unittest

from my_lambdata.my_mod import enlarge

class TestMyMod(unittest.TestCase):

    def test_enlarge(self):
        self.assertEqual(enlarge(5), 500)
        #self.assertEqual(True, True)

if __name__ == '__main__':
    unittest.main()
