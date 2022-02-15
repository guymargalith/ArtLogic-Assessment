#!/usr/bin/env python
from lib.csvfile import rows_to_csv, csv_to_rows

def create_new_stock_numbers(filepath, filepath_new, filepath_faulty):
    """
   Cleans the the csv file from rows with missing artist names, and then redefines the stock
   number using the following format-

   A stock number consists of 2 parts:
	
		SA 001
	
	The first part is the prefix (SA)
	The second part is the number part (001).

    These numbers are unique.

    The prefix generally represents the artist's first letters of their first and last names,
    except in the case where that prefix is already in use.
    
    filpath defines where to retrieve the csv file, filepath_new defines where to create the new spreadsheet, 
    and filepath_faulty defines where to store records with missing artists names.
    """
    dicts = csv_to_rows(filepath)

    dicts_clean = [row for row in dicts if row['Artist']]
    new_codes = []
    name_code_dicts = {}
    missing_names = [row for row in dicts if not row['Artist']]

    for row in dicts_clean:
        if row['Artist'] in name_code_dicts:
            name_code = name_code_dicts[row['Artist']]
        else:
            name_list = row['Artist'].upper().split(' ')
            if len(name_list) < 2:
                name_code = name_list[0][0] + name_list[0][1]
            else:
                if len(name_list) > 2:
                    if len(name_list[1]) == 1:
                        index = 2
                    else:
                        index = 1
                else:
                    index = 1
                name_code = name_list[0][0] + name_list[index][0]
            if name_code in name_code_dicts.values():
                i = 0
                while name_code in name_code_dicts.values():
                    i+=1
                    if row['Artist'][i] == " ":
                        continue
                    name_code = name_list[0][0] + row['Artist'][i].upper()
            name_code_dicts[row['Artist']] = name_code

            
        number_code = 1

        stock_number = name_code + " " + "{:03d}".format(number_code)

        while stock_number in new_codes:
            number_code += 1
            stock_number = name_code + " " + "{:03d}".format(number_code)


        row["Stock number"] = stock_number
        new_codes.append(stock_number)

    keys = ['\ufeff','Artist','ID','Stock number','Title','Dimensions']
    rows_to_csv(filepath_new, dicts_clean, keys)
    rows_to_csv(filepath_faulty, missing_names, keys)             


    

