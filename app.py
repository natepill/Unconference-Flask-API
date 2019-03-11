from flask import Flask, jsonify
from scripts.csv_to_json import *

'''This API is a microservice used for Make School's Unconference Slack Bot reminder utility'''

app = Flask(__name__)



@app.route("/")
def return_schedule_json():
    csv_file = 'test-data.csv'
    fieldnames = ("Date","Speaker 1","Topic 1","Speaker 2","Topic 2","Speaker 3","Topic 3","Speaker 4","Topic 4")
    jsonfile = 'file.json'


    schedule_json_array = convert_to_json(csv_file, fieldnames, json_file = 'file.json')

    final_object = map_date_keys(schedule_json_array)

    return jsonify(final_object)
    # print(final_object)


if __name__ == "__main__":
    app.run(debug=True)
