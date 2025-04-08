import re

def preprocess(text):
    # Lowercase
    text = text.lower()
    # Remove punctuation (keep only words)
    words = re.findall(r'\b\w+\b', text)
    return words

if __name__ == '__main__':
    words = preprocess(open('moby-dick.txt').read())
    with open('moby-dick-words.txt', 'w') as f:
        f.write(' '.join(words))

    sorted_words = sorted(set(words))
    with open('moby-dick-words-sorted.txt', 'w') as f:
        f.write(' '.join(sorted_words))
    
