from flask import Flask, render_template, request, jsonify
from scraper import scraper_function
from gpt import run_gpt
from accessgpt import run_prompt

app = Flask(__name__)



@app.route('/')
def index():
    return render_template('home.html')
@app.route('/swayamGPT')
def swayamGPT():
    return render_template('swayamGPT.html')

@app.route('/swayamGPT/scrape', methods=['POST'])
def scrape():
    url = request.form['url']
    questions = scraper_function(url)
    return jsonify(questions)

@app.route('/swayamGPT/process_question', methods=['POST'])
def process_question():
    data = request.json
    question = data.get('question')  # Retrieve question from JSON data
    selected_option = data.get('selectedOption')  # Retrieve selected option from JSON data

    result = run_gpt(question, selected_option)  # Call run_gpt with both question and selected option
    return jsonify(result)



@app.route('/accessGPT')
def accessGPT():
    return render_template('accessGPT.html')

@app.route('/accessGPT/get_response', methods=['POST'])
def get_response():
    data = request.json
    prompt = data.get('prompt')  # Retrieve question from JSON data
    selected_option = data.get('selectedOption')  # Retrieve selected option from JSON data

    result = run_prompt(prompt, selected_option)  # Call run_gpt with both question and selected option
    return jsonify(result)



if __name__ == '__main__':
    app.run(debug=True)
