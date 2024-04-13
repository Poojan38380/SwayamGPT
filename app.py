from flask import Flask, render_template, request, jsonify
from scraper import scraper_function
from gpt import run_gpt
from accessgpt import run_prompt

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('home.html')

@app.route('/swayamgpt')
def swayamGPT():
    return render_template('swayamGPT.html')

@app.route('/swayamgpt/scrape', methods=['POST'])
def scrape():
    url = request.form.get('url')
    if not url:
        return jsonify({'error': 'URL parameter is required'}), 400

    questions = scraper_function(url)
    return jsonify(questions)

@app.route('/swayamgpt/process_question', methods=['POST'])
def process_question():
    data = request.json
    question = data.get('question')
    selected_option = data.get('selectedOption')

    if not question or not selected_option:
        return jsonify({'error': 'Question and selected option are required'}), 400

    result = run_gpt(question, selected_option)
    return jsonify(result)

@app.route('/accessgpt')
def accessGPT():
    return render_template('accessGPT.html')

@app.route('/accessgpt/get_response', methods=['POST'])
def get_response():
    data = request.json
    prompt = data.get('prompt')
    selected_option = data.get('selectedOption')

    if not prompt or not selected_option:
        return jsonify({'error': 'Prompt and selected option are required'}), 400

    result = run_prompt(prompt, selected_option)
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=False,host ='0.0.0.0')
