"""Emotion detection module."""

def emotion_detector(text_to_analyze):
    """Detect the dominant emotion from the input text."""

    if not text_to_analyze or not text_to_analyze.strip():
        return {
            "anger": None,
            "disgust": None,
            "fear": None,
            "joy": None,
            "sadness": None,
            "dominant_emotion": None
        }

    text = text_to_analyze.lower()

    emotion_words = {
        "anger": [
            "angry", "anger", "furious", "mad",
            "hate", "annoyed", "irritated"
        ],
        "disgust": [
            "disgusting", "disgust", "gross",
            "awful", "nasty", "revolting"
        ],
        "fear": [
            "afraid", "fear", "scared", "terrified",
            "worried", "danger", "frightened"
        ],
        "joy": [
            "happy", "joy", "glad", "excited",
            "love", "wonderful", "great", "good"
        ],
        "sadness": [
            "sad", "unhappy", "depressed", "cry",
            "crying", "lonely", "upset"
        ]
    }

    scores = {
        "anger": 0.0,
        "disgust": 0.0,
        "fear": 0.0,
        "joy": 0.0,
        "sadness": 0.0
    }

    for emotion, words in emotion_words.items():
        for word in words:
            if word in text:
                scores[emotion] += 1.0

    if max(scores.values()) == 0:
        dominant_emotion = "neutral"
    else:
        dominant_emotion = max(scores, key=scores.get)

    total = sum(scores.values())

    if total > 0:
        for emotion in scores:
            scores[emotion] = round(scores[emotion] / total, 2)

    scores["dominant_emotion"] = dominant_emotion

    return scores
