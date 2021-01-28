from tabulate import tabulate


# reads a CSV file into a 2-D table with the first “row” being the column headings
def build(file_name):
    file_list = open(file_name, 'r').readlines()
    database = []
    if not len(file_list):
        # notify the user that the file was empty
        # and therefore it will return the empty 1D array
        print("The file is empty!")

    for string in file_list:
        row = string.strip().split(",")
        row_modified = []
        for entry in row:
            # all the entries are read in as strings,
            # check if the entry in the row is the number and if it is, store it as such
            if entry.isnumeric():
                row_modified.append(int(entry))
            else:
                row_modified.append(entry)
        database.append(row_modified)

    return database


# displays a two-dimensional table with column headings in a pretty, tabular format
# columns can be left-justified, right-justified, or - optionally - “smart-justified”
#     (e.g. strings to the left, numbers to the right)
# see https://www.w3schools.com/python/ref_string_format.asp
def display(table):
    # if the table does not even have the column names then there is nothing to output
    if not len(table):
        return
    print(tabulate(table, headers="firstrow", tablefmt='fancy_grid'))


# returns a new 2-D table with only the column names provided in the list column_names
# if column_names is “*”, then include all columns
def project(table, column_names=["*"]):
    # if the empty array was passed in, there is nothing to project
    if not len(table):
        return
    if column_names == ["*"]:
        display(table)
        return table
    else:
        modified_table = []
        index_range = []
        modified_header = []
        # here we are guaranteed that the table at least has the column names
        for i in range(len(table[0])):
            if table[0][i] in column_names:
                modified_header.append(table[0][i])
                index_range.append(i)
        if modified_header:
            modified_table.append(modified_header)
        # if the header is empty that means either no columns were provided, or they are invalid,
        # notify the user and return
        else:
            print("No columns were found.")
            return
        if len(table) == 1:
            display(modified_table)
            return modified_table
        # at this point we are guaranteed that there is at least one record in the DB
        for record in range(1, len(table)):
            selected_record = []
            for idx in index_range:
                selected_record.append(table[record][idx])
            modified_table.append(selected_record)
        return modified_table


# return a table of all rows that satisfy the criteria,
#     a tuple of the form (column_name,column_value)
# if no criteria is provided, return all rows
# Example: for the “holiday” table, if criteria is ("Food","Nothing") then it should
# return the rows for Yom Kippur and Tisha B’Av
def select(table, criteria=None):
    if not len(table):
        return
    result = [table[0]]
    if criteria:
        # if the form of the criteria is wrong, then return False as error
        if len(criteria) != 2:
            print("Criteria in the wrong form!")
            return False
        # if the column specified in the criteria is not in the table, return None,
        # because no records can possibly be found
        if criteria[0] not in table[0]:
            print("Column not in the table")
            return None
        for i in range(len(table[0])):
            if table[0][i] == criteria[0]:
                for j in range(1, len(table)):
                    if table[j][i] == criteria[1]:
                        result.append(table[j])
        display(result)
        return result
    else:
        return table


# use a nested loop to match rows between the two tables based on the join_column provided
# if join_column is not provided, then provide a cross-product, that is a copy of each row
#     in table1 together with a row from table2
#     so if table1 has 10 rows and table2 has 5 rows, you would get 50 rows
def join(table1, table2, join_column=None):
    result = []
    if not (len(table1) and len(table2)):
        print("One of the tables is empty, cannot perform join")
        return False

    # if the join column not provided, and the tables have at least the names of the columns
    if not join_column and table1 and table2:
        # create the joined header for the table, which is the merging of the headers,
        # we are going to be operating on the rest of the table without the header.
        header1 = table1[0]
        header2 = table2[0]
        # handle the case in which we are asked to provide the cross-product of 2 tables
        # that have one of the names of the columns in common, we are going to call it table1.ColName, table2.ColName,
        # for example, here if we do it to tables holidays and food, it would have table1.Food and table2.Food
        header = []
        for i in range(len(table1[0])):
            if table1[0][i] in table2[0]:
                header.append("table1." + table1[0][i])
            else:
                header.append(table1[0][i])
        for col_name in header2:
            if col_name in header1:
                header.append("table2." + col_name)
            else:
                header.append(col_name)
        result.append(header)

        # check the scenario in which either of the databases is empty, which means that there are no records,
        # but there are the names of the columns

        # if both of them are empty then return the empty database with the column names
        if len(table1) < 2 and len(table2) < 2:
            return result

        # if one of the tables is empty, for example the first one,
        # then put the second table and the None values for the rest of the columns
        # that are from the first table
        elif len(table1) < 2:
            table2_records = table2[1:]
            for line in table2_records:
                result.append([None] * len(header1) + line)

        elif len(table2) < 2:
            table1_records = table1[1:]
            for line in table1_records:
                result.append(line + [None] * len(header2))

        # in this case for either tables are are going to return the table that

        table1_records = table1[1:]
        table2_records = table2[1:]

        for line1 in table1_records:
            for line2 in table2_records:
                result.append(line1 + line2)
    else:
        # check tha the column exists in both tables to be able to join on it
        if join_column in table1[0] and join_column in table2[0]:
            header = []
            # this will get overwritten
            index_join1 = 0
            index_join2 = 0
            for i in range(len(table1[0])):
                if table1[0][i] == join_column:
                    index_join1 = i
                    header.append(table1[0][i])
                elif table1[0][i] in table2[0]:
                    header.append("table1." + table1[0][i])
                else:
                    header.append(table1[0][i])
            for i in range(len(table2[0])):
                col_name = table2[0][i]
                if col_name == join_column:
                    index_join2 = i
                else:
                    # if there is a repeated col name that is not the one we are joining on
                    # do the Name1
                    if col_name in table1[0]:
                        header.append("table2." + col_name)
                    else:
                        header.append(col_name)
            result.append(header)
            # if either of them are empty then return the empty database with the column names,
            # because cannot join on the col when there are no records
            if len(table1) < 2 or len(table2) < 2:
                return result

            for index in range(1, len(table1)):
                col_value = table1[index][index_join1]
                for row in range(1, len(table2)):
                    if table2[row][index_join2] == col_value:
                        # when joining there is no need to repeat the same col twice, that is why we need to check
                        # if the col we are joining on the last col in the second database,
                        # we are going to append all table except the last part,
                        # otherwise we will slice the table to cut out the column we are joining on
                        if index_join2 != len(table2[0]) - 1:
                            result.append(table1[index] + table2[row][:index_join2] + table2[row][index_join2 + 1:])
                        else:
                            result.append(table1[index] + table2[row][:index_join2])
        else:
            print("Joining column not found in table")
            return False
    return result


# create a sorted copy of the table in ascending order by the values in column column_name
def sort(table, column_name):
    if not column_name:
        print("Please, provide the column name")
        return False
    sort_index = -1
    if len(table) <= 1:
        return table
    for i in range(len(table[0])):
        if table[0][i] == column_name:
            sort_index = i
    if sort_index == -1:
        print("The sorting column is not in the table")
        return False
    else:
        sorted_table = [table[0]]
        table_copy = table[1:]
        table_copy.sort(key=lambda x: x[sort_index])
        return sorted_table + table_copy


if __name__ == '__main__':
    # run to see that the functions work with one another
    display(project(join(build("holidays.csv"), build("foods.csv"), join_column="Food"),
                    ["Name", "Food", "Calories"]))


