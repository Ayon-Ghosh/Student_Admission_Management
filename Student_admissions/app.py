from flask import Flask, render_template, request, jsonify
import pymongo

app = Flask(__name__)


# To renderHomepage
@app.route('/', methods=['POST', 'GET'])
def home_page():
    return render_template('home.html')


# This will be called from UI
@app.route('/results', methods=['POST'])
def student_management():
    if request.method == 'POST':
        operation = request.form['operation']
        Serial_No = request.form['Serial No']
        GRE_Score = request.form['GRE Score']
        TOEFL_SCore = request.form['TOEFL SCore']
        SOP = request.form['SOP']
        LOR = request.form['LOR']
        CGPA = request.form['CGPA']
        Research = request.form['Research']
        Chance_of_Admit = request.form['Chance of Admit']

        Update_Serial_No = request.form['Update Serial No']
        Update_GRE_Score = request.form['Update GRE Score']
        Update_TOEFL_SCore = request.form['Update TOEFL SCore']
        Update_SOP = request.form['Update SOP']
        Update_LOR = request.form['Update LOR']
        Update_CGPA = request.form['Update CGPA']
        Update_Research = request.form['Update Research']
        Update_Chance_of_Admit = request.form['Update Chance of Admit']

        dbConn = pymongo.MongoClient("mongodb://localhost:27017/")  # opening a connection to Mongo
        dbname = 'demoDB'
        db = dbConn[dbname]
        collection_name = 'mongo_demo'
        collection = db[collection_name]
        my_dict = {'Serial No': Serial_No, 'GRE Score': GRE_Score, 'TOEFL SCore': TOEFL_SCore, 'SOP': SOP,
                   'LOR': LOR, 'CGPA': CGPA, 'Research': Research, 'Chance of Admit': Chance_of_Admit}
        update_dict = {'Update_Serial No': Update_Serial_No, 'Update_GRE Score': Update_GRE_Score, 'Update_TOEFL SCore': Update_TOEFL_SCore, 'Update_SOP': Update_SOP,
                   'Update_LOR': Update_LOR, 'Update_CGPA': Update_CGPA, 'Update_Research': Update_Research, 'Update_Chance of Admit': Update_Chance_of_Admit}
        print(my_dict)
        print('xxxxxxxxxx')
        print(update_dict)
        print('xxxxxxxxxx')
        my_db_query = {k: v for k, v in my_dict.items() if v}
        print(my_db_query)
        print('xxxxxxxxxx')
        update_db_query = {k: v for k, v in update_dict.items() if v}
        print(update_db_query)
        print('xxxxxxxxxx')
        results = list(collection.find(my_db_query))
        print(results)

        if operation == 'Add':
            if not results:
                x = collection.insert_one(my_db_query)
                print('The record is added')
                return 'The record is added'
            else:
                print('The record is already present')
                return 'The record is already present'

        if operation == 'Search':
            for result in results:
                print(result)
            return render_template('results.html', results=results)

        if operation == 'View List':
            results = list(collection.find({}))
            return render_template('results.html', results=results)

        if operation == 'Update':

            set_new_value = {'$set': update_db_query}
            x = collection.update_many(my_db_query, set_new_value)
            update_results = list(collection.find(update_db_query))
            print(x.modified_count)
            return render_template('results.html', results=update_results)


if __name__ == '__main__':
    app.run(debug=True)
    #run_simple("localhost", 5000, app)
