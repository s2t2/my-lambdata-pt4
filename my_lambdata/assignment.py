# my_lambdata/assignment.py (functional approach)

import pandas

# State abbreviation -> Full Name and visa versa. FL -> Florida, etc.
# (Handle Washington DC and territories like Puerto Rico etc.)
# take a pandas dataframe that has state abbreviations
# ... and write a function to add corresponding state names

def add_state_names():
    pass


if __name__ == "__main__":

    df = pandas.DataFrame({"abbrev": ["CA", "CT", "CO", "TX", "DC"]})
    print(df.head())

    df2 = pandas.DataFrame({"abbrev": ["OH", "MI", "CO", "TX", "PA"]})
    print(df2.head())
