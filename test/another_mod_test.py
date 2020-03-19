

# test/another_mod_test.py

from my_lambdata.my_mod import enlarge

def test_enlarge():
    #self.assertEqual(enlarge(5), 500)
    assert enlarge(5) == 500
