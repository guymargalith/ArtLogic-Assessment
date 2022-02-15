# -*- coding: utf-8 -*-
#!/usr/bin/env python
import csv

def rows_to_csv(filepath, rows, columns=[]):
    """
    Takes list of dictionaries and filepath and outputs a spreadsheet
    Params:
        rows(list):
            A list of dictionaries
        
        columns(list):
            A list of the key in the rows that you want to export in the csv file
            by defult it will display all
            
    """
    with open(filepath, 'w', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=columns)
        writer.writerows(rows)
        
   


    
def csv_to_rows(filepath):
    """
    Converts csv file to list of dicts.
    """
    with open(filepath, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        return [row for row in reader]
            
