
# utils.py

EXIT_WORDS = ["exit", "quit", "bye", "stop"]

def should_exit(text):
    return text.lower().strip() in EXIT_WORDS

