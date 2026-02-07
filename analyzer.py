import json
import re
from typing import List, Dict

# Load keyword list
with open("keywords.json", "r") as f:
    keywords = json.load(f)

def analyze_text_basic(text: str) -> Dict:
    suggestions = []

    # Action verbs
    if not any(verb in text.lower() for verb in keywords["action_verbs"]):
        suggestions.append("Try adding more action verbs to describe your achievements (e.g., led, developed, created).")

    # Tech skills
    missing_skills = [skill for skill in keywords["tech_skills"] if skill.lower() not in text.lower()]
    if missing_skills:
        suggestions.append(f"Consider adding relevant tech skills: {', '.join(missing_skills[:5])}")

    # Length check
    if len(text.split()) < 100:
        suggestions.append("Your text seems short. Consider expanding on your experience.")

    return {
        "score": max(100 - len(suggestions) * 15, 50),
        "suggestions": suggestions
    }

def analyze_text_openai(text: str, openai_api_key: str) -> Dict:
    import openai
    openai.api_key = openai_api_key

    prompt = f"""You are a professional career coach. Analyze the following resume/LinkedIn bio and provide constructive feedback for improvement. Be specific and helpful.

Text:
{text}
"""

    try:
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[{"role": "user", "content": prompt}],
            max_tokens=300
        )
        feedback = response.choices[0].message.content.strip()
        return {
            "score": 85,
            "suggestions": [feedback]
        }
    except Exception as e:
        return {"score": 50, "suggestions": [f"OpenAI API error: {str(e)}"]}
