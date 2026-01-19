from app.data.role_skills import ROLE_SKILLS
import re

def normalize_text(text: str):
    words = re.findall(r"[a-zA-Z\+#]+", text.lower())
    tokens = set(words)

    for i in range(len(words) - 1):
        tokens.add(words[i] + " " + words[i + 1])
    return tokens

def predict_roles(text: str):
    tokens = normalize_text(text)
    results = []

    for role, skills in ROLE_SKILLS.items():
        skill_set = {s.lower() for s in skills}

        matched = skill_set.intersection(tokens)
        match_ratio = len(matched) / len(skill_set)

        if len(matched) == 0:
            confidence = 0
        else:
            confidence = round(30 + match_ratio * 70, 2)

        if confidence >= 80:
            suitability = "⭐ Most Suitable"
        elif confidence >= 60:
            suitability = "👍 Suitable"
        elif confidence >= 40:
            suitability = "⚠️ Less Suitable"
        else:
            suitability = "❓ May Work"

        results.append({
            "role": role,
            "confidence": confidence,
            "suitability": suitability
        })

    results = [r for r in results if r["confidence"] > 0]

    results.sort(key=lambda x: x["confidence"], reverse=True)

    return results
