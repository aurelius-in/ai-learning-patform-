import random

def synonym_replacement(text, synonyms_dict):
    words = text.split()
    new_words = [random.choice(synonyms_dict.get(word, [word])) for word in words]
    return " ".join(new_words)

def random_deletion(text, p=0.1):
    words = text.split()
    if len(words) == 1:
        return text
    new_words = [word for word in words if random.random() > p]
    if not new_words:
        new_words.append(random.choice(words))
    return " ".join(new_words)
