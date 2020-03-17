# my_lambdata/assignment.py (functional approach)

import pandas

def add_state_names(my_df):
    """
    Adds corresponding state names to a dataframe.

    Param: my_df (pandas.DataFrame) containing a column called "abbrev"
    """
    new_df = my_df.copy()
    # type(new_df["abbrev"]) #> <class 'pandas.core.series.Series'>
    # see: https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.map.html
    names_map = {
        "CA": "Cali",
        "CT": "Conn",
        "CO": "Colorado"
        # todo: more abbrevs!
    }
    new_df["name"] = new_df["abbrev"].map(names_map)
    return new_df

if __name__ == "__main__":

    print("--------------")
    df = pandas.DataFrame({"abbrev": ["CA", "CT", "CO", "TX", "DC"]})
    print(df.head())
    new_df = add_state_names(df)
    print(new_df.head())

    print("--------------")
    df2 = pandas.DataFrame({"abbrev": ["OH", "MI", "CO", "TX", "PA"]})
    print(df2.head())
    new_df2 = add_state_names(df2)
    print(new_df2.head())
