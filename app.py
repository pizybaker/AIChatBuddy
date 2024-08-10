import openai
from flask import Flask, request, render_template

api_key = yourOPENAI_KEY
openai.api_key = api_key
app = Flask(__name__)

def chat_gpt_response(prompt):
    instructions = "YOUR INSTRUCTIONS TO AI"
    response = openai.chat.completions.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": instructions},
            {"role": "user", "content": prompt}
        ]
    )
    return response.choices[0].message.content

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        prompt = request.form['prompt']
        response = chat_gpt_response(prompt)
        return response  
    
    return render_template('index.html')  

if __name__ == '__main__':
    app.run(debug=True) 



