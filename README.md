# Personal Assistant

## 🚀 Getting Started

This project is a personal assistant that interacts using voice commands, executes predefined actions, and communicates with ChatGPT. Follow the instructions below to set up and run the project.

### 📌 Installing Dependencies
Before running the project, you need to install the required dependencies listed in `requirements.txt`:
```bash
pip install -r requirements.txt
```

### 🔑 Setting Up Environment Variables
You need to create a `.env` file in the root directory of the project and include your **OpenAI API Key**:
```env
OPENAI_API_KEY=your_openai_api_key_here
```
This key is required to interact with ChatGPT. You can use your preferred model by modifying the API key accordingly.

### 🤖 Customizing AI Models
If you want to use another AI model instead of ChatGPT, you will need to modify `model_ai.py` accordingly.

### 🗣️ Changing the Voice System
By default, the assistant uses a free voice synthesis system in `speaker.py`. If you prefer using an AI-powered voice, you can edit this file to integrate a different speech synthesis model.

### 🔧 Modifying Command Execution
The command execution logic is handled in `command_control.py`. You can keep it as is or modify it to add or change commands as needed.

---

## ✅ Running the Project
Once everything is set up, you can start the assistant by running:
```bash
python main.py
```

Enjoy your personal assistant! 🚀

