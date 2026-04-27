import random
import re

from data import (
    EMOTION_KEYWORDS, EMOTION_POOLS, DRAMATIC_ADJECTIVES,
    ARTIFACT_NOUNS, SUBTITLES, WING_NAMES, SIGNIFICANCE_PHRASES,
    CURATOR_NOTES, FOOTNOTES, ANOMALY_TYPES
)


def detect_emotion(text):
    text_lower = text.lower()
    scores = {k: 0 for k in EMOTION_KEYWORDS}
    for emotion, words in EMOTION_KEYWORDS.items():
        for w in words:
            if re.search(r'\b' + re.escape(w) + r'\b', text_lower):
                scores[emotion] += 1
    best = max(scores, key=scores.get)
    return best if scores[best] else random.choice(list(EMOTION_POOLS.keys()))


def generate_artifact_name(emotion):
    return (
        random.choice(DRAMATIC_ADJECTIVES) + " " + random.choice(ARTIFACT_NOUNS[emotion]),
        random.choice(SUBTITLES)
    )


def maybe_glitch(text):
    return re.sub(r'[aeiou]', '#', text, flags=re.IGNORECASE)


def build_exhibit(vent):
    emotion = detect_emotion(vent)
    name, subtitle = generate_artifact_name(emotion)

    anomaly = None
    roll = random.random()

    if roll < 0.01:
        anomaly = "FORBIDDEN"
        name = "CLASSIFIED ARTIFACT"
        subtitle = "ACCESS RESTRICTED"
    elif roll < 0.05:
        anomaly = random.choice(ANOMALY_TYPES)

    desc = f"This artifact captures a human in a state of {random.choice(EMOTION_POOLS[emotion])}. "
    desc += f'The statement reads: "{vent}". '

    if anomaly == "GLITCH":
        desc = maybe_glitch(desc)
    elif anomaly == "REDACTED":
        desc = re.sub(r'\w+', lambda m: "███" if random.random() < 0.2 else m.group(), desc)
    elif anomaly == "ECHO":
        desc += " The statement repeats. The statement repeats."
    elif anomaly == "CORRUPTED":
        desc = desc[::-1]
    elif anomaly == "FORBIDDEN":
        desc = "[DATA EXPUNGED]"

    return {
        "name": name,
        "subtitle": subtitle,
        "wing": random.choice(WING_NAMES),
        "desc": desc,
        "sig": random.choice(SIGNIFICANCE_PHRASES),
        "note": random.choice(CURATOR_NOTES),
        "foot": random.choice(FOOTNOTES),
        "anomaly": anomaly
    }
