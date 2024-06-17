from flask import Flask, request, jsonify, render_template
from load_model import BartBase

app = Flask(__name__)

model_name = "model/bart_base_fine_tunning"
bart = BartBase(model=model_name)


@app.route('/')
def home():
    return render_template('index.html')

# Flask route for summarization
@app.route('/summarize', methods=['POST'])
def summarize_text():
    data = request.get_json()
    text = data.get('text', '')
    if text:
        summary = bart(text)
        return jsonify({'summary': summary})
    else:
        return jsonify({'summary': 'No text provided.'})
    
    
if __name__ == '__main__':
    app.run(debug=True)