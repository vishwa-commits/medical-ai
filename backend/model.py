# Mock diagnosis model (replace with real ML model)
DIAGNOSIS_KNOWLEDGE = {
    "headache": {
        "Migraine": {"min_age": 10, "gender": ["F"], "confidence": 0.75},
        "Tension Headache": {"min_age": 5, "gender": ["M", "F"], "confidence": 0.65},
        "Cluster Headache": {"min_age": 20, "gender": ["M"], "confidence": 0.45}
    },
    "fever": {
        "Common Cold": {"min_age": 0, "gender": ["M", "F"], "confidence": 0.85},
        "Flu": {"min_age": 0, "gender": ["M", "F"], "confidence": 0.70},
        "COVID-19": {"min_age": 0, "gender": ["M", "F"], "confidence": 0.55}
    }
}

def predict_diagnosis(symptoms: list[str], age: int, gender: str):
    """Predict possible conditions based on symptoms"""
    possible_conditions = []
    
    for symptom in symptoms:
        if symptom in DIAGNOSIS_KNOWLEDGE:
            for condition, data in DIAGNOSIS_KNOWLEDGE[symptom].items():
                if age >= data["min_age"] and gender in data["gender"]:
                    possible_conditions.append({
                        "condition": condition,
                        "confidence": data["confidence"]
                    })
    
    # Sort by highest confidence
    possible_conditions.sort(key=lambda x: x["confidence"], reverse=True)
    
    return possible_conditions[:3]  # Return top 3  