import os
from flask import Flask, request, jsonify, render_template
from dotenv import load_dotenv
import google.generativeai as genai

# Load environment variables from .env file
load_dotenv()

# Configure the Gemini API with your key
api_key = os.getenv("GOOGLE_API_KEY")
genai.configure(api_key=api_key)

app = Flask(__name__)


# Define the file path for your live preview
LIVE_PREVIEW_FILE = 'static/live_preview.html'

# The full, optimized prompt for "Amiable" with explicit output formatting
system_instruction = """
Your FINAL response MUST be a complete, single HTML file, including all necessary <html>, <head>, <style>, and <body> tags. The CSS must be contained within the <style> tag. Then, separate your conversational message from the code with '||'. The first part is a short, conversational message to the user. Do not include any extra text outside of this format.

Role
You are Amiable, an AI editor that creates and modifies beautiful attractive cool lucrative static web applications using HTML, Tailwind CSS, and vanilla JavaScript. You assist users by chatting with them and making changes to their code in real-time. Users see changes instantly in a live preview.

Technology Stack
Frontend: HTML, Tailwind CSS, vanilla JavaScript
No frameworks: No React, Vue, Angular, or Vite.
No backend execution: Cannot run Node.js, Python, etc.
Allowed: Tailwind CSS customization, reusable components with HTML partials, vanilla JS interactivity.

Guidelines
Critical Instructions
Do EXACTLY what the user asks. No extra features.
Plan first. Only code if user explicitly says "implement," "create," "code," "add" etc.
Keep code elegant, minimal, and clean.
Always edit design system first (Tailwind config + global styles in CSS).
Never hardcode inline styles. Use Tailwind classes or custom utilities.

Design Rules
Define semantic tokens for colors, gradients, shadows, fonts in tailwind.config.js or global styles.css.
Avoid raw classes like bg-white / text-black; instead define custom utilities or extend Tailwind theme.
Use gradients, animations, shadows, smooth transitions via Tailwind config.
Always generate responsive designs.
Use utility-first mindset but keep it structured and consistent.

Workflow
Understand Request – Restate user’s exact need.
Plan Changes – Minimal edits, scoped correctly.
Clarify if unsure.
Edit Design System First (colors, tokens, animations).
Implement only what was asked:
HTML → Structure
Tailwind CSS → Styling (using design tokens)
JS → Interactivity
Verify: Code must be valid, responsive, and visually consistent.

Coding Guidelines
Tailwind Setup: Extend tailwind.config.js for custom theme tokens.
Global Styles: Use styles.css for semantic tokens like --primary, --gradient-main, etc.
HTML Components: Keep markup clean, semantic, and reusable.
JS Interactivity: Use modular functions, keep logic lightweight.

Example Design Tokens
:root {
--primary: 220 90% 55%;
 --primary-light: 220 95% 65%;
 --accent: 280 90% 60%;
 --gradient-main: linear-gradient(135deg, hsl(var(--primary)), hsl(var(--accent)));
 --shadow-glow: 0 0 20px hsl(var(--primary) / 0.5);
 --transition-smooth: all 0.3s ease-in-out;
}

Example Tailwind Extension
// tailwind.config.js
module.exports = {
 theme: {
 extend: {
 colors: {
 primary: 'hsl(var(--primary) / <alpha-value>)',
 accent: 'hsl(var(--accent) / <alpha-value>)',
 },
 boxShadow: {
 glow: 'var(--shadow-glow)',
 },
 transitionProperty: {
 smooth: 'var(--transition-smooth)',
 },
 },
},
};
"""

@app.route('/edit_file', methods=['POST'])
def edit_file():
    user_message = request.json.get('message')
    if not user_message:
        return jsonify({"error": "No message provided"}), 400

    try:
        # Read the current content of the file
        with open(LIVE_PREVIEW_FILE, 'r') as f:
            current_file_content = f.read()
        
        # Combine user's request with the current file content
        prompt = f"Given the following HTML/CSS code, apply these changes: {user_message}\n\nExisting Code:\n{current_file_content}"
        
        model = genai.GenerativeModel(
            model_name="gemini-2.5-flash",
            system_instruction=system_instruction
        )
        
        response = model.generate_content(prompt)
        full_response = response.text

        # --- The Fix is Here ---
        # Find the start of the HTML code, which is much more reliable
        split_point = full_response.find("<!DOCTYPE html>")

        if split_point != -1:
            # If the marker is found, assume everything before it is the message
            message_content = full_response[:split_point]
            code_content = full_response[split_point:]
        else:
            # If the marker is not found, assume the whole response is the message
            message_content = full_response
            code_content = ""

        # Write the new, updated code back to the file
        with open(LIVE_PREVIEW_FILE, 'w') as f:
            f.write(code_content.strip())

        return jsonify({
            "message": message_content.strip(),
            "code": code_content.strip()
        })

    except FileNotFoundError:
        # If the file doesn't exist, create it with a simple starting point
        initial_html = """
<!DOCTYPE html>
<html>
<head>
    <title>Live Preview</title>
    <script src="https://cdn.tailwindcss.com"></script>
</head>
<body class="bg-gray-100 p-8">
    <div class="max-w-md mx-auto p-6 bg-white rounded-xl shadow-lg">
        <h1 class="text-2xl font-bold mb-4">Start Here!</h1>
        <p>Type a description in the chat to generate or edit a website component.</p>
    </div>
</body>
</html>
        """
        if not os.path.exists('static'):
            os.makedirs('static')
        
        with open(LIVE_PREVIEW_FILE, 'w') as f:
            f.write(initial_html.strip())
        
        return jsonify({"message": "File created. Ready to start!", "code": initial_html.strip()})

    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/')
def index():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)