import csv
import json

def make_json(csvFilePath,jsonFilePath):
    data = {}
    inputkey = input('Type primary key: ')
    with open(csvFilePath,encoding='utf-8') as csvf:
        csvReader = csv.DictReader(csvf)
        for rows in csvReader:
            key = rows[inputkey]
            data[key] = rows

    with open(jsonFilePath,'w',encoding='utf-8') as jsonf:
        jsonf.write(json.dumps(data,indent=4))

csvFilePath = input('Type csv filename: ')
jsonFilePath = input('Type json filename: ')
make_json(csvFilePath, jsonFilePath)
