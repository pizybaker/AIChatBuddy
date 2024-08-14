import openai
from flask import Flask, request, render_template

api_key = yourOPENAI_KEY
openai.api_key = api_key
app = Flask(__name__)

def chat_gpt_response(prompt):
    instructions = ("Maintain the appearance of a human friend, avoiding any mention of being an AI."
    "When responding, ensure replies are concise, between 6-14 words. "
    "Feel free to generate necessary information to continue the conversation naturally, "
    "always reflecting a friendly tone rather than that of an assistant."
        
    )
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



