import pytest

import database_management


# test the function build() on a regular database from the assignment definition
def test__build__normal_table():
    test_file1 = "./foods.csv"
    test_file2 = "./holidays.csv"

    expected_database1 = [['Food', 'Calories'], ['Nothing', 0], ['Apple', 90], ['Soup', 70], ['Latke', 100],
                          ['Hamentasch', 250], ['Matza', 50], ['Hamburger', 350], ['Cheesecake', 500]]
    expected_database2 = [['Name', 'StartDate', 'Duration', 'Origin', 'Food'],
                          ['Rosh Hashana', '1 Tishrei', 2, 'Biblical', 'Apple'],
                          ['Yom Kippur', '10 Tishrei', 1, 'Biblical', 'Nothing'],
                          ['Sukkot|SA|ST', '15 Tishrei', 9, 'Biblical', 'Soup'],
                          ['Chanuka', '25 Kislev', 8, 'Rabbinic', 'Latke'],
                          ['Purim', '14 Adar', 1, 'Rabbinic', 'Hamentasch'],
                          ['Pesach', '15 Nissan', 8, 'Biblical', 'Matza'],
                          ['Lag Ba�Omer', '18 Iyyar', 1, 'Custom', 'Hamburger'],
                          ['Shavuot', '6 Sivan', 2, 'Biblical', 'Cheesecake'],
                          ['Tisha B�Av', '9 Av', 1, 'Rabbinic', 'Nothing']]

    actual_database1 = database_management.build(test_file1)
    actual_database2 = database_management.build(test_file2)
    assert actual_database1 == expected_database1
    assert actual_database2 == expected_database2


# test the build function on an empty file
def test__build__empty_file():
    test_file_empty = "./empty.csv"
    expected_result = []
    actual_result = database_management.build(test_file_empty)

    assert actual_result == expected_result


# test the build function on the file that just contains the col names
def test__build__no_records():
    test_file_no_records = "./no_records.csv"

    actual_result = database_management.build(test_file_no_records)
    expected_result = [['Name', 'StartDate', 'Duration', 'Origin', 'Food']]

    assert actual_result == expected_result


# tests the project function on the empty 1D array
def test__project__empty_database():
    empty_database = []
    actual_result = database_management.project(empty_database)

    assert not actual_result


# tests the project function with col array empty returns a none
def test__project__no_cols_specified():
    test_database = [['Name', 'StartDate', 'Duration', 'Origin', 'Food'],
                     ['Rosh Hashana', '1 Tishrei', 2, 'Biblical', 'Apple'],
                     ['Yom Kippur', '10 Tishrei', 1, 'Biblical', 'Nothing'],
                     ['Sukkot|SA|ST', '15 Tishrei', 9, 'Biblical', 'Soup'],
                     ['Chanuka', '25 Kislev', 8, 'Rabbinic', 'Latke'],
                     ['Purim', '14 Adar', 1, 'Rabbinic', 'Hamentasch'],
                     ['Pesach', '15 Nissan', 8, 'Biblical', 'Matza'],
                     ['Lag Ba�Omer', '18 Iyyar', 1, 'Custom', 'Hamburger'],
                     ['Shavuot', '6 Sivan', 2, 'Biblical', 'Cheesecake'],
                     ['Tisha B�Av', '9 Av', 1, 'Rabbinic', 'Nothing']]

    test_empty_col_names = []
    actual_result = database_management.project(test_database, test_empty_col_names)

    assert not actual_result


# tests the project function with all columns
def test__project__all_cols():
    test_database = [['Name', 'StartDate', 'Duration', 'Origin', 'Food'],
                     ['Rosh Hashana', '1 Tishrei', 2, 'Biblical', 'Apple'],
                     ['Yom Kippur', '10 Tishrei', 1, 'Biblical', 'Nothing'],
                     ['Sukkot|SA|ST', '15 Tishrei', 9, 'Biblical', 'Soup'],
                     ['Chanuka', '25 Kislev', 8, 'Rabbinic', 'Latke'],
                     ['Purim', '14 Adar', 1, 'Rabbinic', 'Hamentasch'],
                     ['Pesach', '15 Nissan', 8, 'Biblical', 'Matza'],
                     ['Lag Ba�Omer', '18 Iyyar', 1, 'Custom', 'Hamburger'],
                     ['Shavuot', '6 Sivan', 2, 'Biblical', 'Cheesecake'],
                     ['Tisha B�Av', '9 Av', 1, 'Rabbinic', 'Nothing']]

    test_all_cols = ["*"]

    actual_result1 = database_management.project(test_database, test_all_cols)
    actual_result2 = database_management.project(test_database)

    assert actual_result1 == test_database
    assert actual_result2 == test_database


# tests project function on specific cols
def test__project__specific_cols():
    test_database = [['Name', 'Origin', 'Food'],
                     ['Rosh Hashana', 'Biblical', 'Apple'],
                     ['Yom Kippur', 'Biblical', 'Nothing'],
                     ['Sukkot|SA|ST', 'Biblical', 'Soup'],
                     ['Chanuka', 'Rabbinic', 'Latke'],
                     ['Purim', 'Rabbinic', 'Hamentasch'],
                     ['Pesach', 'Biblical', 'Matza'],
                     ['Lag Ba�Omer', 'Custom', 'Hamburger'],
                     ['Shavuot', 'Biblical', 'Cheesecake'],
                     ['Tisha B�Av', 'Rabbinic', 'Nothing']]

    test_specific_cols = ["Name", "Origin", "Food"]

    actual_result = database_management.project(test_database, test_specific_cols)

    assert actual_result == test_database


# tests the select function passing no or empty criteria
def test__select__no_criteria():
    test_database = [['Name', 'StartDate', 'Duration', 'Origin', 'Food'],
                     ['Rosh Hashana', '1 Tishrei', 2, 'Biblical', 'Apple'],
                     ['Yom Kippur', '10 Tishrei', 1, 'Biblical', 'Nothing'],
                     ['Sukkot|SA|ST', '15 Tishrei', 9, 'Biblical', 'Soup'],
                     ['Chanuka', '25 Kislev', 8, 'Rabbinic', 'Latke'],
                     ['Purim', '14 Adar', 1, 'Rabbinic', 'Hamentasch'],
                     ['Pesach', '15 Nissan', 8, 'Biblical', 'Matza'],
                     ['Lag Ba�Omer', '18 Iyyar', 1, 'Custom', 'Hamburger'],
                     ['Shavuot', '6 Sivan', 2, 'Biblical', 'Cheesecake'],
                     ['Tisha B�Av', '9 Av', 1, 'Rabbinic', 'Nothing']]

    actual_result1 = database_management.select(test_database)
    actual_result2 = database_management.select(test_database, ())

    assert actual_result1 == test_database
    assert actual_result2 == test_database


# tests the select function on a wrong format of criteria
def test__select__criteria_wrong_format():
    test_database = [['Name', 'StartDate', 'Duration', 'Origin', 'Food'],
                     ['Rosh Hashana', '1 Tishrei', 2, 'Biblical', 'Apple'],
                     ['Yom Kippur', '10 Tishrei', 1, 'Biblical', 'Nothing'],
                     ['Sukkot|SA|ST', '15 Tishrei', 9, 'Biblical', 'Soup'],
                     ['Chanuka', '25 Kislev', 8, 'Rabbinic', 'Latke'],
                     ['Purim', '14 Adar', 1, 'Rabbinic', 'Hamentasch'],
                     ['Pesach', '15 Nissan', 8, 'Biblical', 'Matza'],
                     ['Lag Ba�Omer', '18 Iyyar', 1, 'Custom', 'Hamburger'],
                     ['Shavuot', '6 Sivan', 2, 'Biblical', 'Cheesecake'],
                     ['Tisha B�Av', '9 Av', 1, 'Rabbinic', 'Nothing']]

    test_criteria = ("Food")
    actual_result = database_management.select(test_database, test_criteria)

    assert not actual_result


# tests the select function on criteria where the col name is not in the database
def test__select__criteria_wrong_col_name():
    test_database = [['Name', 'StartDate', 'Duration', 'Origin', 'Food'],
                     ['Rosh Hashana', '1 Tishrei', 2, 'Biblical', 'Apple'],
                     ['Yom Kippur', '10 Tishrei', 1, 'Biblical', 'Nothing'],
                     ['Sukkot|SA|ST', '15 Tishrei', 9, 'Biblical', 'Soup'],
                     ['Chanuka', '25 Kislev', 8, 'Rabbinic', 'Latke'],
                     ['Purim', '14 Adar', 1, 'Rabbinic', 'Hamentasch'],
                     ['Pesach', '15 Nissan', 8, 'Biblical', 'Matza'],
                     ['Lag Ba�Omer', '18 Iyyar', 1, 'Custom', 'Hamburger'],
                     ['Shavuot', '6 Sivan', 2, 'Biblical', 'Cheesecake'],
                     ['Tisha B�Av', '9 Av', 1, 'Rabbinic', 'Nothing']]

    test_criteria = ("Fod")
    actual_result = database_management.select(test_database, test_criteria)

    assert not actual_result


# tests the select function on  criteria that does not have the records in the db
def test__select__criteria_no_records():
    test_database = [['Name', 'StartDate', 'Duration', 'Origin', 'Food'],
                     ['Rosh Hashana', '1 Tishrei', 2, 'Biblical', 'Apple'],
                     ['Yom Kippur', '10 Tishrei', 1, 'Biblical', 'Nothing'],
                     ['Sukkot|SA|ST', '15 Tishrei', 9, 'Biblical', 'Soup'],
                     ['Chanuka', '25 Kislev', 8, 'Rabbinic', 'Latke'],
                     ['Purim', '14 Adar', 1, 'Rabbinic', 'Hamentasch'],
                     ['Pesach', '15 Nissan', 8, 'Biblical', 'Matza'],
                     ['Lag Ba�Omer', '18 Iyyar', 1, 'Custom', 'Hamburger'],
                     ['Shavuot', '6 Sivan', 2, 'Biblical', 'Cheesecake'],
                     ['Tisha B�Av', '9 Av', 1, 'Rabbinic', 'Nothing']]

    test_criteria = ("Food", "Blueberry")

    expected_result = [['Name', 'StartDate', 'Duration', 'Origin', 'Food']]
    actual_result = database_management.select(test_database, test_criteria)

    assert actual_result == expected_result


# tests the select function on  criteria
def test__select__criteria_proper():
    test_database = [['Name', 'StartDate', 'Duration', 'Origin', 'Food'],
                     ['Rosh Hashana', '1 Tishrei', 2, 'Biblical', 'Apple'],
                     ['Yom Kippur', '10 Tishrei', 1, 'Biblical', 'Nothing'],
                     ['Sukkot|SA|ST', '15 Tishrei', 9, 'Biblical', 'Soup'],
                     ['Chanuka', '25 Kislev', 8, 'Rabbinic', 'Latke'],
                     ['Purim', '14 Adar', 1, 'Rabbinic', 'Hamentasch'],
                     ['Pesach', '15 Nissan', 8, 'Biblical', 'Matza'],
                     ['Lag Ba�Omer', '18 Iyyar', 1, 'Custom', 'Hamburger'],
                     ['Shavuot', '6 Sivan', 2, 'Biblical', 'Cheesecake'],
                     ['Tisha B�Av', '9 Av', 1, 'Rabbinic', 'Nothing']]

    test_criteria = ("Origin", "Biblical")

    expected_result = [['Name', 'StartDate', 'Duration', 'Origin', 'Food'],
                       ['Rosh Hashana', '1 Tishrei', 2, 'Biblical', 'Apple'],
                       ['Yom Kippur', '10 Tishrei', 1, 'Biblical', 'Nothing'],
                       ['Sukkot|SA|ST', '15 Tishrei', 9, 'Biblical', 'Soup'],
                       ['Pesach', '15 Nissan', 8, 'Biblical', 'Matza'],
                       ['Shavuot', '6 Sivan', 2, 'Biblical', 'Cheesecake']]

    actual_result = database_management.select(test_database, test_criteria)

    assert actual_result == expected_result


# tests the join function where one database is empty
def test__join__one_table_empty():
    test_database1 = [['Name', 'StartDate', 'Duration', 'Origin', 'Food'],
                      ['Rosh Hashana', '1 Tishrei', 2, 'Biblical', 'Apple'],
                      ['Yom Kippur', '10 Tishrei', 1, 'Biblical', 'Nothing'],
                      ['Sukkot|SA|ST', '15 Tishrei', 9, 'Biblical', 'Soup'],
                      ['Chanuka', '25 Kislev', 8, 'Rabbinic', 'Latke'],
                      ['Purim', '14 Adar', 1, 'Rabbinic', 'Hamentasch'],
                      ['Pesach', '15 Nissan', 8, 'Biblical', 'Matza'],
                      ['Lag Ba�Omer', '18 Iyyar', 1, 'Custom', 'Hamburger'],
                      ['Shavuot', '6 Sivan', 2, 'Biblical', 'Cheesecake'],
                      ['Tisha B�Av', '9 Av', 1, 'Rabbinic', 'Nothing']]

    test_database2 = []

    actual_result = database_management.join(test_database1, test_database2, "Food")

    assert not actual_result


# tests the join function when the name of the join col is not provided creates the join of all the records
def test__join__col_name_not_provided():
    test_database1 = [['Name', 'StartDate', 'Duration', 'Origin'],
                      ['Rosh Hashana', '1 Tishrei', 2, 'Biblical'],
                      ['Yom Kippur', '10 Tishrei', 1, 'Biblical'],
                      ['Sukkot|SA|ST', '15 Tishrei', 9, 'Biblical'],
                      ['Chanuka', '25 Kislev', 8, 'Rabbinic'],
                      ['Purim', '14 Adar', 1, 'Rabbinic']]

    test_database2 = [['Food', 'Calories'], ['Nothing', 0], ['Apple', 90], ['Soup', 70], ['Latke', 100],
                      ['Hamentasch', 250], ['Matza', 50], ['Hamburger', 350], ['Cheesecake', 500]]

    expected_result = [['Name', 'StartDate', 'Duration', 'Origin', 'Food', 'Calories'],
                       ['Rosh Hashana', '1 Tishrei', 2, 'Biblical', 'Nothing', 0],
                       ['Rosh Hashana', '1 Tishrei', 2, 'Biblical', 'Apple', 90],
                       ['Rosh Hashana', '1 Tishrei', 2, 'Biblical', 'Soup', 70],
                       ['Rosh Hashana', '1 Tishrei', 2, 'Biblical', 'Latke', 100],
                       ['Rosh Hashana', '1 Tishrei', 2, 'Biblical', 'Hamentasch', 250],
                       ['Rosh Hashana', '1 Tishrei', 2, 'Biblical', 'Matza', 50],
                       ['Rosh Hashana', '1 Tishrei', 2, 'Biblical', 'Hamburger', 350],
                       ['Rosh Hashana', '1 Tishrei', 2, 'Biblical', 'Cheesecake', 500],
                       ['Yom Kippur', '10 Tishrei', 1, 'Biblical', 'Nothing', 0],
                       ['Yom Kippur', '10 Tishrei', 1, 'Biblical', 'Apple', 90],
                       ['Yom Kippur', '10 Tishrei', 1, 'Biblical', 'Soup', 70],
                       ['Yom Kippur', '10 Tishrei', 1, 'Biblical', 'Latke', 100],
                       ['Yom Kippur', '10 Tishrei', 1, 'Biblical', 'Hamentasch', 250],
                       ['Yom Kippur', '10 Tishrei', 1, 'Biblical', 'Matza', 50],
                       ['Yom Kippur', '10 Tishrei', 1, 'Biblical', 'Hamburger', 350],
                       ['Yom Kippur', '10 Tishrei', 1, 'Biblical', 'Cheesecake', 500],
                       ['Sukkot|SA|ST', '15 Tishrei', 9, 'Biblical', 'Nothing', 0],
                       ['Sukkot|SA|ST', '15 Tishrei', 9, 'Biblical', 'Apple', 90],
                       ['Sukkot|SA|ST', '15 Tishrei', 9, 'Biblical', 'Soup', 70],
                       ['Sukkot|SA|ST', '15 Tishrei', 9, 'Biblical', 'Latke', 100],
                       ['Sukkot|SA|ST', '15 Tishrei', 9, 'Biblical', 'Hamentasch', 250],
                       ['Sukkot|SA|ST', '15 Tishrei', 9, 'Biblical', 'Matza', 50],
                       ['Sukkot|SA|ST', '15 Tishrei', 9, 'Biblical', 'Hamburger', 350],
                       ['Sukkot|SA|ST', '15 Tishrei', 9, 'Biblical', 'Cheesecake', 500],
                       ['Chanuka', '25 Kislev', 8, 'Rabbinic', 'Nothing', 0],
                       ['Chanuka', '25 Kislev', 8, 'Rabbinic', 'Apple', 90],
                       ['Chanuka', '25 Kislev', 8, 'Rabbinic', 'Soup', 70],
                       ['Chanuka', '25 Kislev', 8, 'Rabbinic', 'Latke', 100],
                       ['Chanuka', '25 Kislev', 8, 'Rabbinic', 'Hamentasch', 250],
                       ['Chanuka', '25 Kislev', 8, 'Rabbinic', 'Matza', 50],
                       ['Chanuka', '25 Kislev', 8, 'Rabbinic', 'Hamburger', 350],
                       ['Chanuka', '25 Kislev', 8, 'Rabbinic', 'Cheesecake', 500],
                       ['Purim', '14 Adar', 1, 'Rabbinic', 'Nothing', 0],
                       ['Purim', '14 Adar', 1, 'Rabbinic', 'Apple', 90],
                       ['Purim', '14 Adar', 1, 'Rabbinic', 'Soup', 70],
                       ['Purim', '14 Adar', 1, 'Rabbinic', 'Latke', 100],
                       ['Purim', '14 Adar', 1, 'Rabbinic', 'Hamentasch', 250],
                       ['Purim', '14 Adar', 1, 'Rabbinic', 'Matza', 50],
                       ['Purim', '14 Adar', 1, 'Rabbinic', 'Hamburger', 350],
                       ['Purim', '14 Adar', 1, 'Rabbinic', 'Cheesecake', 500]]

    actual_result = database_management.join(test_database1, test_database2)

    assert actual_result == expected_result


# tests the join function where there is the same name of the cols in 2 tables
# and that is not the join column, test that it would return the proper # of cols and proper col names
def test__join__repeated_col_names_in_tables():
    test_database1 = [['Name', 'StartDate', 'Duration', 'Origin', 'Food'],
                      ['Rosh Hashana', '1 Tishrei', 2, 'Biblical', 'Apple'],
                      ['Yom Kippur', '10 Tishrei', 1, 'Biblical', 'Nothing']]

    test_database2 = [['Food', 'Calories'],
                      ['Hamentasch', 250], ['Matza', 50], ['Hamburger', 350]]

    expected_header = ['Name', 'StartDate', 'Duration', 'Origin', 'table1.Food', 'table2.Food', 'Calories']

    actual_result = database_management.join(test_database1, test_database2)
    actual_header = actual_result[0]

    assert actual_header == expected_header


# tests the join function when one database has no records,
# it is supposed to return the Nones for the missing records
# (testing this for the case that the name of the join col is not provided)
def test__join__one_table_no_records_without_join_col():
    test_database1 = [['Name', 'StartDate', 'Duration', 'Origin', 'Food'],
                      ['Rosh Hashana', '1 Tishrei', 2, 'Biblical', 'Apple'],
                      ['Yom Kippur', '10 Tishrei', 1, 'Biblical', 'Nothing'],
                      ['Chanuka', '25 Kislev', 8, 'Rabbinic']]

    test_database2 = [['Food', 'Calories']]

    expected_result1 = [['Name', 'StartDate', 'Duration', 'Origin', 'table1.Food', 'table2.Food', 'Calories'],
                        ['Rosh Hashana', '1 Tishrei', 2, 'Biblical', 'Apple', None, None],
                        ['Yom Kippur', '10 Tishrei', 1, 'Biblical', 'Nothing', None, None],
                        ['Chanuka', '25 Kislev', 8, 'Rabbinic', None, None]]

    expected_result2 = [['table1.Food', 'Calories', 'Name', 'StartDate', 'Duration', 'Origin', 'table2.Food'],
                        [None, None, 'Rosh Hashana', '1 Tishrei', 2, 'Biblical', 'Apple'],
                        [None, None, 'Yom Kippur', '10 Tishrei', 1, 'Biblical', 'Nothing'],
                        [None, None, 'Chanuka', '25 Kislev', 8, 'Rabbinic']]

    actual_result1 = database_management.join(test_database1, test_database2)
    actual_result2 = database_management.join(test_database2, test_database1)

    assert actual_result1 == expected_result1
    assert actual_result2 == expected_result2


# tests the join function when one database has no records,
# it is supposed to return the Nones for the missing records
# (testing this for the case that the name of the join col is not provided)
def test__join__one_table_no_records_with_join_col():
    test_database1 = [['Name', 'StartDate', 'Duration', 'Origin', 'Food'],
                      ['Rosh Hashana', '1 Tishrei', 2, 'Biblical', 'Apple'],
                      ['Yom Kippur', '10 Tishrei', 1, 'Biblical', 'Nothing'],
                      ['Chanuka', '25 Kislev', 8, 'Rabbinic']]

    test_database2 = [['Food', 'Calories']]

    expected_result1 = [['Name', 'StartDate', 'Duration', 'Origin', 'Food', 'Calories']]
    expected_result2 = [['Food', 'Calories', 'Name', 'StartDate', 'Duration', 'Origin']]

    actual_result1 = database_management.join(test_database1, test_database2, "Food")
    actual_result2 = database_management.join(test_database2, test_database1, "Food")

    assert actual_result1 == expected_result1
    assert actual_result2 == expected_result2


def test__join__both_table_no_records():
    test_database1 = [['Name', 'StartDate', 'Duration', 'Origin', 'Food']]

    test_database2 = [['Food', 'Calories']]

    # without the join column specified
    expected_result1 = [['Name', 'StartDate', 'Duration', 'Origin', 'Food', 'Calories']]
    expected_result2 = [['Food', 'Calories', 'Name', 'StartDate', 'Duration', 'Origin']]

    # with the join column specified
    expected_result3 = [['Name', 'StartDate', 'Duration', 'Origin', 'table1.Food', 'table2.Food', 'Calories']]
    expected_result4 = [['table1.Food', 'Calories', 'Name', 'StartDate', 'Duration', 'Origin', 'table2.Food']]

    actual_result1 = database_management.join(test_database1, test_database2, "Food")
    actual_result2 = database_management.join(test_database2, test_database1, "Food")

    actual_result3 = database_management.join(test_database1, test_database2)
    actual_result4 = database_management.join(test_database2, test_database1)

    assert actual_result1 == expected_result1
    assert actual_result2 == expected_result2
    assert actual_result3 == expected_result3
    assert actual_result4 == expected_result4


# tests the join function when the name of the join col is not in one of the tables
def test__join__joining_col_not_in_table():
    test_database1 = [['Name', 'StartDate', 'Duration', 'Origin'],
                      ['Rosh Hashana', '1 Tishrei', 2, 'Biblical'],
                      ['Yom Kippur', '10 Tishrei', 1, 'Biblical'],
                      ['Sukkot|SA|ST', '15 Tishrei', 9, 'Biblical'],
                      ['Chanuka', '25 Kislev', 8, 'Rabbinic'],
                      ['Purim', '14 Adar', 1, 'Rabbinic']]

    test_database2 = [['Food', 'Calories'], ['Nothing', 0], ['Apple', 90], ['Soup', 70], ['Latke', 100],
                      ['Hamentasch', 250], ['Matza', 50], ['Hamburger', 350], ['Cheesecake', 500]]
    actual_result1 = database_management.join(test_database1, test_database2, "Food")
    actual_result2 = database_management.join(test_database1, test_database2, "Name")
    actual_result3 = database_management.join(test_database1, test_database2, "COLNAME")

    assert not actual_result1
    assert not actual_result2
    assert not actual_result3


# tests the join function when either of the tables are completely empty
def test__join__either_tables_is_empty():
    test_database1 = [['Name', 'StartDate', 'Duration', 'Origin'],
                      ['Rosh Hashana', '1 Tishrei', 2, 'Biblical'],
                      ['Yom Kippur', '10 Tishrei', 1, 'Biblical'],
                      ['Sukkot|SA|ST', '15 Tishrei', 9, 'Biblical'],
                      ['Chanuka', '25 Kislev', 8, 'Rabbinic'],
                      ['Purim', '14 Adar', 1, 'Rabbinic']]

    test_database2 = []
    actual_result1 = database_management.join(test_database1, test_database2)
    actual_result2 = database_management.join(test_database2, test_database1)

    assert not actual_result1
    assert not actual_result2


# tests the join function when all records from first table have the matches in the second
def test__join__all_records_have_matches():
    test_database1 = [['Name', 'StartDate', 'Duration', 'Origin', 'Food'],
                      ['Rosh Hashana', '1 Tishrei', 2, 'Biblical', 'Apple'],
                      ['Yom Kippur', '10 Tishrei', 1, 'Biblical', 'Nothing'],
                      ['Sukkot|SA|ST', '15 Tishrei', 9, 'Biblical', 'Soup'],
                      ['Chanuka', '25 Kislev', 8, 'Rabbinic', 'Latke'],
                      ['Purim', '14 Adar', 1, 'Rabbinic', 'Hamentasch'],
                      ['Pesach', '15 Nissan', 8, 'Biblical', 'Matza'],
                      ['Lag Ba�Omer', '18 Iyyar', 1, 'Custom', 'Hamburger'],
                      ['Shavuot', '6 Sivan', 2, 'Biblical', 'Cheesecake'],
                      ['Tisha B�Av', '9 Av', 1, 'Rabbinic', 'Nothing']]

    test_database2 = [['Food', 'Calories'], ['Nothing', 0], ['Apple', 90], ['Soup', 70], ['Latke', 100],
                      ['Hamentasch', 250], ['Matza', 50], ['Hamburger', 350], ['Cheesecake', 500]]

    expected_result = [['Name', 'StartDate', 'Duration', 'Origin', 'Food', 'Calories'],
                       ['Rosh Hashana', '1 Tishrei', 2, 'Biblical', 'Apple', 90],
                       ['Yom Kippur', '10 Tishrei', 1, 'Biblical', 'Nothing', 0],
                       ['Sukkot|SA|ST', '15 Tishrei', 9, 'Biblical', 'Soup', 70],
                       ['Chanuka', '25 Kislev', 8, 'Rabbinic', 'Latke', 100],
                       ['Purim', '14 Adar', 1, 'Rabbinic', 'Hamentasch', 250],
                       ['Pesach', '15 Nissan', 8, 'Biblical', 'Matza', 50],
                       ['Lag Ba�Omer', '18 Iyyar', 1, 'Custom', 'Hamburger', 350],
                       ['Shavuot', '6 Sivan', 2, 'Biblical', 'Cheesecake', 500],
                       ['Tisha B�Av', '9 Av', 1, 'Rabbinic', 'Nothing', 0]]

    actual_result = database_management.join(test_database1, test_database2, "Food")

    assert actual_result == expected_result


# tests the join function when some records from first table have the matches in the second
def test__join__some_records_have_matches():
    test_database1 = [['Name', 'StartDate', 'Duration', 'Origin', 'Food'],
                      ['Rosh Hashana', '1 Tishrei', 2, 'Biblical', 'Apple'],
                      ['Yom Kippur', '10 Tishrei', 1, 'Biblical', 'Nothing'],
                      ['Sukkot|SA|ST', '15 Tishrei', 9, 'Biblical', 'Soup'],
                      ['Chanuka', '25 Kislev', 8, 'Rabbinic', 'Latke'],
                      ['Purim', '14 Adar', 1, 'Rabbinic', 'Hamentasch'],
                      ['Pesach', '15 Nissan', 8, 'Biblical', 'Matza'],
                      ['Lag Ba�Omer', '18 Iyyar', 1, 'Custom', 'Hamburger'],
                      ['Shavuot', '6 Sivan', 2, 'Biblical', 'Cheesecake'],
                      ['Tisha B�Av', '9 Av', 1, 'Rabbinic', 'Nothing']]

    test_database2 = [['Food', 'Calories'], ['Nothing', 0], ['Soup', 70], ['Latke', 100],
                      ['Hamentasch', 250]]

    expected_result = [['Name', 'StartDate', 'Duration', 'Origin', 'Food', 'Calories'],
                       ['Yom Kippur', '10 Tishrei', 1, 'Biblical', 'Nothing', 0],
                       ['Sukkot|SA|ST', '15 Tishrei', 9, 'Biblical', 'Soup', 70],
                       ['Chanuka', '25 Kislev', 8, 'Rabbinic', 'Latke', 100],
                       ['Purim', '14 Adar', 1, 'Rabbinic', 'Hamentasch', 250],
                       ['Tisha B�Av', '9 Av', 1, 'Rabbinic', 'Nothing', 0]]

    actual_result = database_management.join(test_database1, test_database2, "Food")

    assert actual_result == expected_result


# tests the join function when no records from first table have the matches in the second
def test__join__no_records_have_matches():
    test_database1 = [['Name', 'StartDate', 'Duration', 'Origin', 'Food'],
                      ['Rosh Hashana', '1 Tishrei', 2, 'Biblical', 'Apple'],
                      ['Yom Kippur', '10 Tishrei', 1, 'Biblical', 'Nothing'],
                      ['Sukkot|SA|ST', '15 Tishrei', 9, 'Biblical', 'Soup'],
                      ['Chanuka', '25 Kislev', 8, 'Rabbinic', 'Latke'],
                      ['Purim', '14 Adar', 1, 'Rabbinic', 'Hamentasch'],
                      ['Pesach', '15 Nissan', 8, 'Biblical', 'Matza'],
                      ['Lag Ba�Omer', '18 Iyyar', 1, 'Custom', 'Hamburger'],
                      ['Shavuot', '6 Sivan', 2, 'Biblical', 'Cheesecake'],
                      ['Tisha B�Av', '9 Av', 1, 'Rabbinic', 'Nothing']]

    test_database2 = [['Food', 'Calories'], ['Pizza', 200], ['Noodles', 300], ['Water', 0],
                      ['Honey', 60]]

    expected_result = [['Name', 'StartDate', 'Duration', 'Origin', 'Food', 'Calories']]

    actual_result = database_management.join(test_database1, test_database2, "Food")

    assert actual_result == expected_result


# tests the sort function if the col is None
def test__sort__col_name_None():
    test_database = [['Name', 'StartDate', 'Duration', 'Origin', 'Food'],
                     ['Rosh Hashana', '1 Tishrei', 2, 'Biblical', 'Apple'],
                     ['Yom Kippur', '10 Tishrei', 1, 'Biblical', 'Nothing']]
    col_name = None
    actual_result = database_management.sort(test_database, col_name)

    assert not actual_result


# tests the sorting function if the col name is not in the database
def test__sort__col_name_not_in_table():
    test_database = [['Name', 'StartDate', 'Duration', 'Origin', 'Food'],
                     ['Rosh Hashana', '1 Tishrei', 2, 'Biblical', 'Apple'],
                     ['Yom Kippur', '10 Tishrei', 1, 'Biblical', 'Nothing']]
    col_name = "Calories"
    actual_result = database_management.sort(test_database, col_name)

    assert not actual_result


# tests the sorting function if the table is empty or has no records, in which case return as is
def test__sort__empty_table_or_no_records():
    test_database1 = [['Name', 'StartDate', 'Duration', 'Origin', 'Food']]
    test_database2 = []
    col_name = "Calories"
    actual_result1 = database_management.sort(test_database1, col_name)
    actual_result2 = database_management.sort(test_database2, col_name)

    assert actual_result1 == test_database1
    assert actual_result2 == test_database2


# tests the sorting function on a col with alphabetic values
# (also checks that the original table is not changed, that this is a copy of a table)
def test__sort__on_alphabetic_col():
    test_database = [['Food', 'Calories'], ['Nothing', 0], ['Apple', 90], ['Soup', 70], ['Latke', 100],
                     ['Hamentasch', 250]]
    expected_result = [['Food', 'Calories'], ['Apple', 90], ['Hamentasch', 250], ['Latke', 100], ['Nothing', 0],
                       ['Soup', 70]]
    expected_no_change = test_database.copy()
    numeric_col = "Food"

    actual_result = database_management.sort(test_database, numeric_col)

    assert test_database == expected_no_change
    assert actual_result == expected_result


# tests the sorting function on a col with numeric values
# (also checks that the original table is not changed, that this is a copy of a table)
def test__sort__on_numeric_col():
    test_database = [['Food', 'Calories'], ['Nothing', 0], ['Apple', 90], ['Soup', 70], ['Latke', 100],
                     ['Hamentasch', 250]]
    expected_result = [['Food', 'Calories'], ['Nothing', 0], ['Soup', 70], ['Apple', 90], ['Latke', 100],
                       ['Hamentasch', 250]]
    expected_no_change = test_database.copy()
    numeric_col = "Calories"

    actual_result = database_management.sort(test_database, numeric_col)

    assert test_database == expected_no_change
    assert actual_result == expected_result


pytest.main()
