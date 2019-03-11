import csv
import json
from collections import OrderedDict

'''Reads in the entire DOWNLOADED Unconference CSV file, converts it to a usable JSON array and returns it'''
'''The converted JSON is also written to a json file for immidiete reference'''
'''Change the csv_file, fieldnames, and jsonfile variable values in the main() function as desired'''


# NOTE: Do I want to have the entire csv already read into the API and reference that? Probably, cause I'm not currently making requests to download the Google Sheet
# NOTE: This script WILL THROW UNHANDLED ERRORS if a row doesn't have a Date value ---> TODO: Add in error handling empty Date cells if even needed



def map_date_keys(json_array):
    '''Maps over json array and returns a dictionary with key,value = "<Date>": {<object with key,values of who is speaking and their topic>}'''

    schedule_by_date = dict()

    for json_object in json_array:
        schedule_by_date[json_object["Date"]] = json_object
        del json_object['Date']

    return schedule_by_date


def convert_to_json(csv_file, fieldnames, json_file = None):
    '''Takes in csv file name, fieldnames headers, and optional jsonfile name to write the results to'''
    '''Will read csv file, convert it to an array of json objects, and return it'''
    csvfile = open(csv_file, 'r')

    if json_file != None:
        jsonfile = open('file.json', 'w')

    reader = csv.DictReader(csvfile, fieldnames)

    json_array = list()

    for row in reader:
        json_array.append(dict(row))
        if json_file != None:
            json.dump(row, jsonfile)
            jsonfile.write('\n')

    return json_array

def main():
    csv_file = 'test-data.csv'
    fieldnames = ("Date","Speaker 1","Topic 1","Speaker 2","Topic 2","Speaker 3","Topic 3","Speaker 4","Topic 4")
    jsonfile = 'file.json'


    schedule_json_array = convert_to_json(csv_file, fieldnames, json_file = 'file.json')

    final_object = map_date_keys(schedule_json_array)

    print(final_object)



if __name__ == "__main__":
    main()
