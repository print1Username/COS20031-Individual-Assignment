import os
from flask import Flask, render_template, request

import src.estate as estate
import src.gemini as gemini

basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__, template_folder = 'template')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SESSION_COOKIE_NAME'] = None

@app.route('/')
@app.route('/home')
def home():
    return render_template('index.html')

@app.route('/add_estate', methods = ['GET', 'POST'])
def add_new_estate():
    message = ''
    if request.method == 'POST':
        estate_id = request.form['estate_id']
        estate_name = request.form['estate_name']
        estate_description = request.form['estate_description']
        estate_price = request.form['estate_price']
        success = estate.add_estate(estate_id, estate_name, estate_description, estate_price)

        if success is True:
            message = f'Estate "{estate_name}" added successfully.'
        else:
            message = 'Estate added failed.'
    return render_template('add_estate.html', message = message)

@app.route('/search', methods=['GET', 'POST'])
def search_estate():
    if request.method == 'POST':
        search = request.form['estate_id']
        estate_list = estate.search_estate(search)
    else:
        estate_list = estate.database_estate()
    return render_template('search.html', estate = estate_list)

@app.route('/ask',  methods=['GET', 'POST'])
def ask_ai():
    if request.method == 'POST':
        question = request.form['question_ai']
        answer = gemini.ask_question(question)
    else:
        question = ''
        answer = ''
    return render_template('ask.html', question_ai = question, answer_ai = answer)

if __name__ == '__main__':
    estate.create_estate()
    estate.add_estate(1000, 'Estate 1', 'Description 1', 100000)
    estate.add_estate(1001, 'Estate 2', '', 110000)
    estate.add_estate(1002, 'Estate 3', '', 120000)
    app.run(debug = True)