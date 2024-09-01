# Voice-Activated-Desktop-Assistant-Using-Python

Project Overview
The Voice-Activated Desktop Assistant is a Python-based application designed to perform a variety of tasks on a user's computer using voice commands. This assistant leverages speech recognition and text-to-speech synthesis to interact with the user, perform web searches, send emails, manage notes, and open applications, among other functions. The goal of this project is to create a hands-free tool that enhances productivity and accessibility for users.

Key Features
Voice Recognition and Command Processing:

The assistant listens to voice commands through the microphone, converts the speech into text, and processes the command to perform specific tasks.
Text-to-Speech Feedback:

Provides spoken responses to the user using the pyttsx3 library, making interactions more natural and user-friendly.
Web Search Capabilities:

Allows the user to search for information on Google or YouTube by simply asking the assistant to "search Google for [query]" or "search YouTube for [query]."
Wikipedia Integration:

Retrieves and reads out a brief summary of any topic the user requests using the wikipedia module.
Opening Popular Websites:

Opens frequently used websites such as YouTube, Google, and Stack Overflow via simple voice commands.
Application Launcher:

Opens local applications like Visual Studio Code or any other executable specified by the user.
Time Reporting:

Tells the current time in response to the user’s query.
Email Sending:

Sends emails to specified recipients using the smtplib module. The assistant can take dictation from the user for the content of the email.
Note Taking:

Takes notes as dictated by the user and saves them in a text file (notes.txt). The file is automatically opened in Notepad for easy editing and viewing.
