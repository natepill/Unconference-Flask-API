import csv
import json


# TODO: Create a function that writes current csv lines to a json file and returns the json object itselfself.

# NOTE: Do I want to have the entire csv already read into the API and reference that? Probably, cause I'm not currently making requests to download the Google Sheet

csvfile = open('test-data.csv', 'r')
jsonfile = open('file.json', 'w')

fieldnames = ("Date","Speaker 1","Topic 1","Speaker 2","Topic 2","Speaker 3","Topic 3","Speaker 4","Topic 4")
reader = csv.DictReader(csvfile, fieldnames)

for row in reader:
    json.dump(row, jsonfile)
    jsonfile.write('\n')


# with open('test-data.csv', 'wr') as file:
#     file.read
