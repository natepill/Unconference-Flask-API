import csv
import json


'''Reads in the entire DOWNLOADED Unconference CSV file, converts it to a usable JSON array and returns it'''
'''The converted JSON is also written to a json file for immidiete reference'''

#TODO: If I can remap the headers of the json objects then I can

# TODO: Remapping headers will look like:
    # Iterate over each json object,
    # Use the date key, value from each json object and make the current json object the value of a new json object
    # The new json object will by "<actual date>": {<object with key,values of who is speaking and their topic>}
    # NOTE: I can probably remove the date key,value from the original object
    # NOTE: The result from this remapping will be that we can look up who is


#NOTE: If I remap the headers then I shouldn't store the json objects into an array



# TODO: Create a function that writes current csv lines to a json file and returns the json object itselfself.

# NOTE: Do I want to have the entire csv already read into the API and reference that? Probably, cause I'm not currently making requests to download the Google Sheet



# TODO: Need to wrap some blocks in try if json_file doesnt exist or if blocks
def convert_to_json(csv_file, fieldnames, json_file = None):
    csvfile = open(csv_file, 'r')
    jsonfile = open('file.json', 'w')

    reader = csv.DictReader(csvfile, fieldnames)

    json_array = list()

    for row in reader:
        json.dump(row, json_array) #NOTE: Idk if this will work: I'm trying to get a json array
        json.dump(row, jsonfile)
        jsonfile.write('\n')


def main():
    csv_file = 'test-data.csv'
    fieldnames = ("Date","Speaker 1","Topic 1","Speaker 2","Topic 2","Speaker 3","Topic 3","Speaker 4","Topic 4")
    jsonfile = 'file.json'

    schedule_json = convert_to_json(csv_file, fieldnames, json_file = 'file.json')





if __name__ == "__main__":
    def main():
