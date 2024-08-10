import openai
import requests
from flask import Flask, request, render_template, jsonify

# Configuration
api_key = "YOUROPENAI_KEY"
openai.api_key = api_key
app = Flask(__name__)

# Store conversation history
conversation_history = []

def chat_gpt_response(messages):
    instructions = (YOUR_INSTRUCTIONS)
    response = openai.chat.completions.create(
        model="gpt-4",
        messages=[
            {"role":"system", "content": instructions},
            *messages
        ]
    )
    return response.choices[0].message.content

@app.route('/', methods=['GET', 'POST'])
def index():
    global conversation_history
    if request.method == 'POST':
        user_message = request.form.get('prompt')
        
        # Add user message to conversation history
        conversation_history.append({"role": "user", "content": user_message})

        # Generate response based on conversation history
        response_text = chat_gpt_response(conversation_history)
        
        # Add GPT response to conversation history
        conversation_history.append({"role": "assistant", "content": response_text})
        
        return jsonify({"response": response_text})
    
    return render_template('index.html')

@app.route('/whatsapp', methods=['POST'])
def whatsapp():
    """Handle incoming messages from WhatsApp."""
    incoming_msg = request.values.get('Body', '').strip()
    sender = request.values.get('From', '')
    
    # Add incoming message to conversation history
    conversation_history.append({"role": "user", "content": incoming_msg})

    # Generate response based on conversation history
    response_text = chat_gpt_response(conversation_history)
    
    # Add GPT response to conversation history
    conversation_history.append({"role": "assistant", "content": response_text})

    # Send the response back to WhatsApp
    from twilio.rest import Client
    account_sid = youraccount_sid
    auth_token = youraccount_auth_token
    client = Client(account_sid, auth_token)

    message = client.messages.create(
        from_='twilio_whatsapp_number',
        body=response_text,
        to=sender
    )

    return str(message.sid)

if __name__ == '__main__':
    app.run(debug=True)
