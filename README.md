
# Support Soul - A Mental Health Discord Bot

Support Soul is a Discord bot built to provide mental health resources and support within Discord servers.

## Features

- **Mental Health Resources** - Users can access lists of mental health resources for issues like depression, ADHD, self-harm etc. Just type `/help` to get started.

- **Self-Harm Message Flagging** - The bot scans messages in the server for signs of self-harm intent. If detected, it flags the message to a logging channel and provides the user with mental health resources.

- **Chatbot** - Support Soul has a conversational chatbot powered by AI to provide encouraging messages and mental health advice to users privately if they message it. 

- **Server Configuration** - Admins can configure settings like enabling message scanning and setting the logging channel.

- **Slash Command Interface** - The bot uses Discord's slash commands for an intuitive interface.

## Implementation

Support Soul is built in Python using the Discord.py API wrapper. Key technical features include:

- OpenAI API for flagging self-harm messages and powering the chatbot.

- Firebase Realtime Database to store server settings and message history.

- Discord slash commands and bot events for detection and interactions.

- Colorama and Discord embed for formatting messages.

The goal is to create a bot that feels helpful and approachable while also keeping communities safe. Support Soul aims to provide an additional layer of care and moderation for mental health in Discord servers.
