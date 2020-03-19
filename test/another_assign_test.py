
# test/another_assign_test.py

from my_lambdata.assignment import CustomFrame

def test_add_state_names():
    custom_df = CustomFrame({"abbrev": ["CA", "CT", "CO", "TX", "DC"]})
    # assert "name" should be a column
    #self.assertTrue("name" not in list(custom_df.columns))
    assert "name" not in list(custom_df.columns)

    custom_df.add_state_names()
    # assert "name" should be a column
    #self.assertTrue("name" in list(custom_df.columns))
    assert "name" in list(custom_df.columns)
    # assert "California" should exist in a column called "name"
    # assert that first row, name is "Cali" and abbrev is "CA"
    #self.assertEqual(custom_df["abbrev"][0], "CA")
    #self.assertEqual(custom_df["name"][0], "Cali")
    assert custom_df["abbrev"][0] == "CA"
    assert custom_df["name"][0] == "Cali"
