# AIChatBuddy

## Description
AIChatBuddy (or Whatsnap) is a unique chat simulation project designed to replicate the experience of chatting with a real person. This web-based app allows users to engage in conversations with an AI that responds naturally, mimicking human interaction. The AI is designed to simulate a realistic messaging environment where users can exchange messages just like they would with a friend.

In addition to its web-based functionality, AIChatBuddy (or Whatsnap) can also be integrated with WhatsApp. This feature enables users to interact with the AI directly through WhatsApp, making the chat experience even more accessible and convenient. Code for integrating WhatsApp is available in the same repository under the "whatsapp-integration" folder.

## Features
  1. Realistic Conversations: The AI responds like a friend, asking questions and providing thoughtful replies based on user input.

  2. Typing Simulation: To enhance realism, the app simulates typing delays before the AI responds.
  3. Dynamic Interactions: The AI adapts its responses to the conversation, making the interaction feel lively and genuine.
  4. Preloaded Conversations: When the app is loaded, the index file includes a few preloaded conversations to get users started right away.

## How it works 
The app is built using Flask for the backend, where the AI handles user inputs and generates responses. The frontend is designed to mimic popular messaging apps, providing users with a familiar and comfortable interface.

   1. User Input: The user types a message into the chat interface.

   2. AI Processing: The input is sent to the backend, where the AI generates a context-aware response using the OpenAI API.

   3. Response Display: After a short simulated typing delay, the AI's response is displayed in the chat interface.

## Demo

1. User mentions they're feeling sick, and the AI responds with good wishes and shares a comforting soup recipe.


![ss1whatsnap](https://github.com/user-attachments/assets/be1450fd-5784-4889-bffb-ab32da7cb33e)




2. User expresses stress about job interviews and mentions 50+ rejections. The AI offers words of encouragement and motivation.


![ss2whatsnap](https://github.com/user-attachments/assets/65937d6a-0e0f-4fe0-9c03-4952099bc60c)


3. Watch the video below to see the Whatsnap web app in action. It showcases the interactive chat experience and how the AI responds to user messages in real time.
 

https://github.com/user-attachments/assets/b41c73d1-4a93-4f1f-88f9-f6aff9da3649



