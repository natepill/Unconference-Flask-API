import csv
import json
from collections import OrderedDict


'''Reads in the entire DOWNLOADED Unconference CSV file, converts it to a usable JSON array and returns it'''
'''The converted JSON is also written to a json file for immidiete reference'''



#TODO: If I can remap the headers of the json objects then I can

# TODO: Remapping headers will look like:
    # Iterate over each json object,
    # Use the date key, value from each json object and make the current json object the value of a new json object
    # The new json object will by "<actual date>": {<object with key,values of who is speaking and their topic>}
    # NOTE: I can probably remove the date key,value from the original object
    # NOTE: The result from this remapping will be that we can look up who is


#NOTE: If I remap the headers then I shouldn't store the json objects into an array (maybe pass in a json array into a function)

def remap(json_arry):



# TODO: Create a function that writes current csv lines to a json file and returns the json object itselfself.

# NOTE: Do I want to have the entire csv already read into the API and reference that? Probably, cause I'm not currently making requests to download the Google Sheet



# TODO: Need to wrap some blocks in try if json_file doesnt exist or if blocks
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

    print(json_array[0])
    return json_array

def main():
    csv_file = 'test-data.csv'
    fieldnames = ("Date","Speaker 1","Topic 1","Speaker 2","Topic 2","Speaker 3","Topic 3","Speaker 4","Topic 4")
    jsonfile = 'file.json'

    schedule_json = convert_to_json(csv_file, fieldnames, json_file = 'file.json')

    # print(schedule_json)



if __name__ == "__main__":
    main()
