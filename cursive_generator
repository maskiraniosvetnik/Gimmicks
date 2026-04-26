"""
CURSIVE WRITER
A beautiful cursive text tool for elegant handwriting simulation.
"""

import random
import re

CURSES = [
    "fucking",
    "bloody",
    "damn",
    "goddamn",
    "freaking",
    "cursed",
    "wretched",
    "unholy",
]

INTENSIFIERS = [
    "bloody fucking",
    "goddamn fucking",
    "absolute fucking",
    "whole fucking",
]

def random_curse():
    if random.random() < 0.15:
        return random.choice(INTENSIFIERS)
    return random.choice(CURSES)

def cursify(text):
    # Split into words
    words = text.split()
    if not words:
        return text

    result = []
    i = 0
    while i < len(words):
        word = words[i]
        clean = word.strip(".,!?;:\"'").lower()

        # Insert curse before nouns/adjectives/interesting words
        # Skip very short words, articles, prepositions
        skip = {"a", "an", "the", "is", "are", "was", "were", "be",
                "to", "of", "in", "on", "at", "by", "or", "and",
                "but", "for", "nor", "so", "yet", "i", "you", "he",
                "she", "it", "we", "they", "my", "your", "his", "her",
                "its", "our", "do", "did", "not", "no", "up", "out"}

        if clean and clean not in skip and len(clean) > 3 and random.random() < 0.35:
            # Preserve original word capitalisation for the curse
            curse = random_curse()
            if word[0].isupper():
                curse = curse.capitalize()
            result.append(curse)

        result.append(word)
        i += 1

    return " ".join(result)

def main():
    print()
    print("  CURSIVE WRITER - converting your text to beautiful cursive")
    print("  Type 'quit' to exit.")
    print()

    while True:
        try:
            user_input = input("  in  > ").strip()
        except (EOFError, KeyboardInterrupt):
            print()
            break

        if not user_input:
            continue
        if user_input.lower() in ("quit", "exit", "q"):
            print()
            print("  Good fucking bye.")
            print()
            break

        output = cursify(user_input)
        print("  out > " + output)
        print()

if __name__ == "__main__":
    main()
