import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

def generate_plan(goal):
    try:
        model = genai.GenerativeModel("gemini-2.0-flash")  # ✅ Correct model name
        prompt = f"""
        You are a helpful goal planning assistant. Break this goal into a 5-day plan with one detailed and achievable step per day.

        User Goal: "{goal}"

        Respond as a bullet list, one bullet per day.
        """
        response = model.generate_content(prompt)
        text = response.text
        steps = [line.strip("-• ").strip() for line in text.splitlines() if line.strip()]
        return steps
    except Exception as e:
        return [f"❌ Gemini Error: {str(e)}"]
