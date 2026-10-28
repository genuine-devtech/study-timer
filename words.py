import random #this is to select random
from nltk.corpus import wordnet

#turn wordnet shorts codes into readable word types
WORD_TYPES = {
    'n': 'noun',
    'v': 'verb',
    'a': 'adjective',
    's': 'adjective satellite',
    'r': 'adverb'
}

_word_list = []

def _get_word_list():
    if not _word_list:
        for word in wordnet.all_lemma_names():
            if word.isalpha() and word.islower() and 4 <= len(word) <= 12:
                _word_list.append(word)
    return _word_list

def get_random_word():
    word = random.choice(_get_word_list())
    meaning = wordnet.synsets(word)[0]
    word_type = WORD_TYPES.get(meaning.pos(), 'word')
    return word, word_type, meaning.definition()

if __name__ == "__main__":
    word, word_type, definition = get_random_word()
    print(f"{word} ({word_type}): {definition}")


