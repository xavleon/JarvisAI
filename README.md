# 🧠 Jarvis AI – Your Voice-Activated Assistant

Jarvis is a personal voice-activated AI assistant powered by GPT and ElevenLabs, capable of understanding natural speech, executing desktop tasks, and speaking back with a lifelike voice.

Inspired by Tony Stark’s J.A.R.V.I.S., this assistant runs locally and responds to your voice in real-time — with customizable actions and personality.

---

## 🎯 Features

- 🎙️ Wake-word detection (`"Hey Jarvis"`)
- 🧠 AI-powered conversations (OpenAI GPT-3.5/4)
- 🗂️ Desktop automation (open apps, create folders, search Google)
- 🔊 Realistic speech output (ElevenLabs API)
- 🌐 Internet-aware search handling
- 🧩 Easy to extend with new skills (weather, memory, APIs)

---

## ⚙️ Tech Stack

| Layer        | Technology                     |
|--------------|--------------------------------|
| Language     | Python 3.10+                   |
| LLM          | OpenAI GPT-3.5 / GPT-4 API     |
| Voice Input  | `speech_recognition`           |
| Voice Output | `ElevenLabs API` + `playsound` |
| Automation   | `os`, `subprocess`             |
| Env Config   | `python-dotenv`                |

---

## 🚀 Getting Started

### 1. Clone the Repo
```bash
git clone https://github.com/xavleon/JarvisAI.git
cd JarvisAI
