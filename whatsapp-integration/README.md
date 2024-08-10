# AIChatBuddy-Integration-whatsapp

## Overview

This project is an enhanced version of the original AIChatBuddy (also known as Whatsnap), now integrated with WhatsApp for seamless communication.
This integration allows the AI to interact with users through WhatsApp, simulating a natural conversation experience as if chatting with a friend.

## Features

  1. WhatsApp Integration: The AI now interacts with users directly through WhatsApp, providing a more accessible and real-time communication channel.
     
  2. Friendly Chat Experience: The AI is programmed to respond as a friend rather than an assistant, offering personalized and empathetic replies.
  
  3. Dynamic Conversations: The AI manages conversation history and responds based on the context of previous interactions.
 
  4. Webhook Configuration: To receive and handle incoming messages, a webhook is set up using ngrok.


## How It Works

 1. User Interaction: Users send messages to a WhatsApp number provided by Twilio.

 2. Message Handling: The messages are received by the Flask application through a webhook configured with ngrok. This webhook URL is set up in the Twilio console to route incoming WhatsApp messages to your Flask server.

 3. Processing Messages: The Flask application uses OpenAI’s API to generate responses. It interprets the received messages, maintains conversation context, and provides replies as a friendly chat companion.

 4. Reply Delivery: The Flask application sends the generated responses back to Twilio, which then forwards them to the user on WhatsApp.

 5. Continuous Interaction: The conversation continues seamlessly, with the AI responding to each message in a friendly and contextually relevant manner.

## Demo

### In this demo, AIChatBuddy engages in a casual conversation, sharing that it has been learning about cooking and mentions a recipe by name. The video showcases its friendly and conversational style.

![whatsapp_integration_s2](https://github.com/user-attachments/assets/38375d1a-cfd6-473f-b31c-13d7a20cd042)

The video showcases its friendly and conversational style.

https://github.com/user-attachments/assets/5e9fc679-4763-4475-b0df-4a3a2786ff2b




