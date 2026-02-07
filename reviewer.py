import json
import re
from typing import Dict,List

# open the key_words file to read action verbs and tech skills words
with open("key_words.json","r") as f:
    # use loads to read from string else use load to read from file
    keywords=json.load(f)
    # print(keywords)

# define a basic text analysis function
# use of RegEx
def text_analysis(text: str) -> Dict:
    suggestions = []

    # Action verbs check
    found_action_verbs = any(
        re.search(rf"\b{re.escape(verb)}\b", text, re.IGNORECASE)
        for verb in keywords["action_verbs"]
    )
    if not found_action_verbs:
        suggestions.append("Consider using strong action verbs to describe your achievements.")

    # Tech skills check
    found_tech_skills = any(
        re.search(rf"\b{re.escape(skill)}\b", text, re.IGNORECASE)
        for skill in keywords["tech_skills"]
    )
    if not found_tech_skills:
        suggestions.append("You might want to mention relevant technical skills or tools.")

    # Length check (based on total character count)
    length_score = 0
    text_length = len(text.strip())
    if text_length < 500:
        length_score = 70
        suggestions.append("The text seems too short. Consider expanding on your experience and skills.")
    elif 500 <= text_length <= 1500:
        length_score = 85
        suggestions.append("Looks good, but you can enrich it further with quantifiable achievements.")
    else:
        length_score = 100
        suggestions.append("Great! Your text length is detailed and well-rounded.")

    # Final score (can be enhanced with weighting)
    final_score = length_score
    if not found_action_verbs:
        final_score -= 5
    if not found_tech_skills:
        final_score -= 5

    return {
        "score": max(0, min(100, final_score)),  # keep score between 0–100
        "suggestions": suggestions
    }

# Define a Gemini analysis function
def ai_analysis(text: str, gemini_key: str) -> Dict:
    import google.generativeai as genai
    genai.configure(api_key=gemini_key)
    # model = genai.GenerativeModel("gemini-2.0-flash")
    prompt =(
        f"""You are a professional career coach. Analyze the following resume/LinkedIn bio 
        and provide constructive feedback for improvement. Be specific and helpful.

        Resume/Bio:
        {text}
        """        
    )
    try:
        model=genai.GenerativeModel("gemini-2.0-flash")
        response=model.generate_content(prompt)
        feedback=response.text.strip()

        return{
            "score":85,
            "suggestions":[feedback]
        }

    except Exception as e:
        return{
            "score":50,
            "suggestions": [f"Gemini API error: {str(e)}"]
        }
