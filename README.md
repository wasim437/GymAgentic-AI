# 💪 FitAgents: The Gym Agentic AI 🤖🏋️‍♂️

> An offline AI-powered personal trainer that gives you personalized **workout plans**, **diet plans**, and **daily motivation** using agent-based intelligence.

---

## 🧠 Overview

**FitAgents** is a multi-agent fitness assistant built with `CrewAI`, powered by local LLMs using `Ollama`. It features 3 specialized AI agents — a Workout Planner, Diet Advisor, and Motivation Bot — working together to create a personalized fitness journey for users.

---

## 🚀 Features

- 🤖 AI-generated **Workout Plans** for all fitness levels
- 🥗 Personalized **Diet Plans** for muscle gain or fat loss
- 🧠 Daily **Motivation & Affirmations** to keep you on track
- 💻 Runs **offline locally** using Ollama LLMs
- 🔄 Modular Agent System powered by CrewAI

---

## 🛠️ Tech Stack

| Tool               | Purpose                                          |
|--------------------|--------------------------------------------------|
| `Python`           | Core development language                        |
| `CrewAI`           | Agent framework for multi-agent orchestration   |
| `Ollama`           | Local LLM provider                               |
| `Langchain-Ollama` | Integration for using LLMs with Langchain       |
| `Gemma 2B (via Ollama)` | The AI model used for generating responses      |

---

## ⚙️ Setup Instructions

### 1. Install Python dependencies
```bash
pip install crewai langchain langchain_ollama

2. Install & Run Ollama

# Download Ollama
https://ollama.com

# Start the local LLM server
ollama serve

# Pull the required model
ollama pull gemma:2b


3. Run the main file
app.py


🤖 How FitAgents Work
This project uses CrewAI to define 3 agents:

🏋️ Workout Planner
Role: Creates exercise routines for beginners, intermediate or advanced users.

Powered by the LLM to understand fitness levels and generate detailed workouts.

🥗 Diet Advisor
Role: Suggests food plans tailored to fitness goals — like weight loss or muscle gain.

Outputs meal timing, macros (proteins, carbs, fats), and tips.

💬 Motivation Bot
Role: Delivers motivational quotes and positive affirmations to users.

Helps users stay committed on hard days.

Each agent is assigned a Task and the Crew runs them sequentially.
