# Web-Based Code Editor

A simple, full-stack web application that functions as a real-time code editor. It allows users to write and execute code in multiple programming languages (Python, C++, and Java) directly from a web browser.

---

## 🚀 Features

- 💻 **Multi-Language Support**: Execute code in Python, C++, and Java.
- ⚡ **Real-time Output**: View results (stdout and stderr) directly in the browser.
- 🔐 **Secure Execution**: Code runs in an isolated, temporary environment.
- 🌙 **Minimalist UI**: Clean, responsive dark-themed interface.

---

## 🛠️ Technologies Used

### Backend
- **Python**: Core backend language.
- **Flask**: Web framework for API endpoints.
- **Flask-CORS**: Enables Cross-Origin Resource Sharing.
- **subprocess**: Executes external commands safely.
- **tempfile**: Creates secure temporary directories for code execution.

### Frontend
- **HTML**: Markup structure.
- **CSS**: Styling with a modern dark theme.
- **JavaScript**: Client-side logic and API interaction.

---

## 📦 Getting Started

Follow these steps to set up and run the project locally.

### ✅ Prerequisites

- Python 3.x installed
- `pip` (Python package manager)

## 📁 Project Structure

```text
code_editor/
├── app.py
├── static/
│   ├── styles.css
│   └── script.js
└── templates/
    └── index.html
```

## 🔧 Installation

### 1. Clone the Repository or Set Up the Files Manually

Create a directory called `code_editor` and place the following files:

- `app.py`
- `static/styles.css`
- `static/script.js`
- `templates/index.html`

### 2. Install Required Dependencies

Open your terminal and navigate to the project directory:

```bash
pip install Flask Flask-Cors

```

---

## ▶️ Running the Application
### 1. Start the Flask Server:
```bash
python app.py
```
- By default, it runs on http://127.0.0.1:5000

### 2. Serve the Frontend:

To serve index.html, use a development server such as Live Server in VS Code.
Run it on port 3001 to avoid CORS issues

### 3. Access the Editor:

```
Open your browser and go to:
👉 http://127.0.0.1:3001
```
The frontend will communicate with the Flask backend on port 5000.

## Screenshots

<p float="left">
  <img src="https://github.com/user-attachments/assets/e74d2d69-e492-4203-a36f-190d5dd37f45" alt="Dashboard Screenshot" width="45%" style="margin-right:10px;" />
  <img src="https://github.com/user-attachments/assets/c5b7ccd6-51b6-4ff8-80a9-205a907ad7fc" alt="Output Screenshot" width="45% height= "50%" />
</p>




---
