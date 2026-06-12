# 🎙️ Voice-to-Text (Faster-Whisper)

A lightweight Python tool that converts audio files into accurate text transcripts using **Faster-Whisper** (a high-performance implementation of OpenAI’s Whisper model).

---

## 🚀 Overview

This project transcribes audio files locally and outputs clean `.txt` transcripts.
It is designed as a simple, fast, and privacy-friendly alternative to cloud-based speech-to-text APIs.

---

## ✨ Features

* 🎧 Supports audio transcription using Faster-Whisper
* ⚡ Fast inference with optimized Whisper models
* 💻 Runs locally (no cloud API required)
* 📄 Outputs structured `.txt` transcript files
* 🔧 Simple Python script-based workflow

---

## 🛠️ Tech Stack

* Python 3.9+
* Faster-Whisper
* FFmpeg
* NumPy
* CTranslate2 backend

---

## 📁 Project Structure

```
voice-to-text/
│
├── audio/               # Input audio files
│   └── sample.m4a
│
├── output/              # Generated transcripts
│   └── sample.txt
│
├── src/
│   └── transcribe.py   # Main transcription script
│
├── requirements.txt
├── README.md
└── .gitignore
```

---

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/brentreichler/voice-to-text.git
cd voice-to-text
```

### 2. Create virtual environment

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Install FFmpeg

On Ubuntu/Debian:

```bash
sudo apt update
sudo apt install ffmpeg
```

Verify:

```bash
ffmpeg -version
```

---

## ▶️ Usage

Place your audio file inside the `audio/` folder and run:

```bash
python src/transcribe.py
```

The transcript will be saved in the `output/` folder as a `.txt` file.

---

## 📌 Example Output

```
Transcription saved.
output/sample.txt
```

The name of the .txt file will be the same name as the audio file.
---

## 🧠 What I Learned

* Working with Python virtual environments on Linux
* Managing system dependencies (FFmpeg)
* Using Faster-Whisper for local speech-to-text inference
* Structuring a Python project for GitHub
* Using Git for version control and project tracking

---

## 🔮 Future Improvements

* CLI support (e.g. `python transcribe.py input.wav`)
* Batch processing of multiple audio files
* Subtitle output (.srt / .vtt)
* GPU acceleration support (CUDA)
* Progress indicator for long audio files

---

## 📜 License

This project is released under the MIT License.

---

## 👤 Author

Built by brentreichler
GitHub: https://github.com/brentreichler

---

## ⭐ If you like this project

Feel free to star the repository or connect on LinkedIn.
