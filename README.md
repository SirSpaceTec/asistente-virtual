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

## 🎵 Audio Processing Setup (macOS, Linux, and Windows)

The project uses `pydub` for audio processing, which depends on `ffmpeg` or `avconv`.

---

## Installation and Configuration

### macOS and Linux:

#### Installation:
Install `ffmpeg` using your package manager. For example, on macOS with Homebrew:

```bash
brew install ffmpeg
```

Or on Linux (Debian/Ubuntu):

```bash
sudo apt update && sudo apt install ffmpeg
```

#### Configuration:
In your code (e.g., in `speaker.py`), set the converter path by reading the environment variable:

```python
import os
from pydub import AudioSegment
from dotenv import load_dotenv

load_dotenv()
PATH_FFMPEG = os.getenv("PATH_FFMPEG")
if PATH_FFMPEG:
    AudioSegment.converter = PATH_FFMPEG
```

---

### Windows:

#### Installation:
Download a precompiled version of `ffmpeg` from the official website or install it using Chocolatey:

```bash
choco install ffmpeg
```

#### Configuration:
Either add the `ffmpeg` directory (e.g., `C:\ffmpeg\bin`) to your system `PATH`, or specify the full path in the `.env` file:

```env
PATH_FFMPEG=C:\ffmpeg\bin\ffmpeg.exe
```

Then, in your code, set the converter path as shown above.


### 🔧 Modifying Command Execution
The command execution logic is handled in `command_control.py`. You can keep it as is or modify it to add or change commands as needed.

---

## ✅ Running the Project
Once everything is set up, you can start the assistant by running:
```bash
python main.py
```

Enjoy your personal assistant! 🚀

