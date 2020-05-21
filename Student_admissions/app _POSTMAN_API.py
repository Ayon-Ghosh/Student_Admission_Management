from flask import Flask, request, jsonify
import pymongo

app = Flask(__name__)

# for calling the API from POSTMAN/ SOAPUI
@app.route('/student_admin_via_postman', methods=['POST']) # for calling the API from Postman/SOAPUI
def student_management():
    if request.method == 'POST':
        operation = request.json['operation']
        Serial_No = request.json['Serial No']
        GRE_Score = request.json['GRE Score']
        TOEFL_SCore = request.json['TOEFL SCore']
        SOP = request.json['SOP']
        LOR = request.json['LOR']
        CGPA = request.json['CGPA']
        Research = request.json['Research']
        Chance_of_Admit = request.json['Chance of Admit']

        dbConn = pymongo.MongoClient("mongodb://localhost:27017/")  # opening a connection to Mongo
        dbname = 'demoDB'
        db = dbConn[dbname]
        collection_name = 'mongo_demo'
        collection = db[collection_name]
        my_dict = {'Serial No': Serial_No, 'GRE Score': GRE_Score, 'TOEFL SCore': TOEFL_SCore, 'SOP': SOP,
                   'LOR': LOR, 'CGPA': CGPA, 'Research': Research, 'Chance of Admit': Chance_of_Admit}
        print(my_dict)
        print('xxxxxxxxxx')
        my_db_query = {k: v for k, v in my_dict.items() if v}
        print(my_db_query)
        print('xxxxxxxxxx')
        results = list(collection.find(my_db_query))
        print(results)

        if operation == 'Add':
            if not results:
                x = collection.insert_one(my_db_query)
                print('The record is added')
                return jsonify('The record is added')
            else:
                print('The record is already present')
                return jsonify('The record is already present')

        if operation == 'Search':
            for result in results:
                print(result)
            return jsonify(results)

        if operation == 'View List':
            results = list(collection.find({}))
            return jsonify(results)


if __name__ == '__main__':
    app.run(debug=True)
