
# 🧠 Smart Goal Planner Agent

![Smart Goal Planner UI](https://drive.google.com/file/d/1wMTpdC0TIC1XIISpGThrpBOukSS-NDu-/view?usp=sharing)

## 📌 Overview

**Smart Goal Planner Agent** is a Streamlit-based AI tool that helps users break down high-level goals (like “Learn Python in 5 days”) into a manageable, day-wise plan using a generative AI model (Gemini). It also incorporates a simple reinforcement learning (RL) loop to learn from user feedback and refine future plans.

---

## 🚀 Features

- ✅ Plan generation using **Gemini API** (Google Generative AI)
- ✅ Daily step-by-step breakdown of goals
- ✅ Interactive feedback from users
- ✅ Adaptive learning using **Reinforcement Learning**

---

## 🔧 Tech Stack

- Python 🐍
- [Streamlit](https://streamlit.io/)
- Google Gemini API (Generative AI)
- Reinforcement Learning logic

---

## 🖥️ How to Run Locally

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name
```

### 2. Install Dependencies

Make sure you have Python 3.9+ and pip installed.

```bash
pip install -r requirements.txt
```

### 3. Setup Environment Variables

Create a `.env` file in the root folder and add your Gemini API key:

```env
GEMINI_API_KEY=your_api_key_here
```

### 4. Run the App

```bash
streamlit run main.py
```

---

## 📷 Screenshot

![App Screenshot](https://drive.google.com/uc?id=18y6cHjlIXN3CLOXU0KHbfncDohuW0AKz)

---

## 💡 How It Works

1. **Goal Input**: User enters a high-level goal.
2. **Gemini Generation**: Goal is passed to Google Gemini to create a 5-day plan.
3. **Interactive Feedback**: User gives feedback on each day's step.
4. **RL Update**: Feedback is used to update internal strategy with reinforcement logic.

---

## 📁 Project Structure

```
.
├── main.py              # Streamlit frontend
├── gemini_agent.py      # Gemini goal planning logic
├── rl.py                # Reinforcement learning logic
├── .env                 # API key (not shared)
├── requirements.txt     # Required Python libraries
└── README.md
```

---

## 🧠 Powered By

- [Google Generative AI (Gemini)](https://ai.google.dev/)
- [Streamlit](https://streamlit.io/)
- Basic RL strategy for feedback learning

---

## 🙌 Contributions

PRs are welcome! If you find bugs or want to suggest improvements, feel free to open an issue or fork the repo.

---
