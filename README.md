# Amiable-Lovable-Clone

## Overview
The **Amiable-Lovable-Clone (AI Coding Assistant)** is an innovative project designed to showcase expertise in Artificial Intelligence (AI), Machine Learning (ML), and MLOps. This project demonstrates the ability to integrate advanced AI models, build interactive web applications, and manage real-time workflows. It is an excellent portfolio piece for professionals aspiring to AI/ML/MLOps roles.

## Features
- **Generative AI Integration**: Utilizes Google's Gemini API for generating and editing HTML/CSS code dynamically based on user input.
- **Real-Time Live Preview**: Updates a live preview file (`static/live_preview.html`) instantly, showcasing changes in real-time.
- **Chat Logging**: Logs user interactions and AI responses for better traceability and debugging.
- **Flask Backend**: Implements a robust backend using Flask to handle user requests and manage file operations.
- **Tailwind CSS**: Ensures modern, responsive, and clean UI designs.

## Why This Project Stands Out
1. **AI Expertise**: Demonstrates the ability to work with generative AI models and APIs.
2. **Full-Stack Development**: Combines backend (Flask) and frontend (HTML, CSS, JavaScript) skills.
3. **MLOps Practices**: Highlights the importance of logging, version control, and modular design.
4. **Real-World Application**: Simulates a real-world scenario where AI assists in web development tasks.
5. **Scalability**: The modular design allows for easy extension and integration with other AI models or APIs.

## Project Structure
```
AI Coding Assistant/
├── app.py                # Flask application
├── static/
│   ├── live_preview.html # Live preview file
│   ├── style.css         # Global styles
├── templates/
│   ├── index.html        # Main HTML template
├── README.md             # Project documentation
```

## How It Works
1. **User Input**: The user provides a description of the desired changes via a chat interface.
2. **AI Processing**: The input is processed by the Gemini API, which generates the required HTML/CSS code.
3. **Live Preview**: The generated code is written to `live_preview.html`, allowing the user to see changes instantly.
4. **Logging**: All interactions are logged in `chat_log.txt` for traceability.

## Prerequisites
- Python 3.8+
- Flask
- Google Gemini API Key
- Tailwind CSS
- **Environment File**: Create a `.env` file in the root directory and add your Google API key:
  ```env
  GOOGLE_API_KEY=your_google_api_key_here
  ```


## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/your-repo/ai-coding-assistant.git
   ```
2. Navigate to the project directory:
   ```bash
   cd ai-coding-assistant
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Run the application:
   ```bash
   python app.py
   ```
5. Open your browser and navigate to `http://127.0.0.1:5000`.

## Video Demo

Check out the 

https://github.com/user-attachments/assets/fe7bf0a1-55a5-4e1e-938d-0e0892a9b7f1

 where the AI Coding Assistant generates a fully functional coffee cafe website in real-time.

## Future Enhancements
- **Support for Additional Frameworks**: Extend support to other CSS frameworks like Bootstrap.
- **Enhanced AI Models**: Integrate more advanced AI models for better code generation.
- **User Authentication**: Add user authentication for personalized experiences.
- **Cloud Deployment**: Deploy the application on cloud platforms like AWS or Azure.
- **Local AI Models**: Integrate models like Ollama LLaVA or QwenCoder to make the application fully local, eliminating the need for external API dependencies.
