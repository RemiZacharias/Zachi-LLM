from collections import Counter

with open("the-verdict.txt", encoding="utf_8") as f:
    raw_corpus = f.read()
    num_merges = 30

def get_pair_frequencies(vocab):
    pairs = Counter()

    for word in vocab.values():
        for i in range(len(word) - 1):
            pair = (word[i], word[i + 1])
            pairs[pair] += 1

    return pairs


def merge_bpe(vocab, pair):
    updated_vocab = {}

    for word, characters in vocab.items():
        word_new_tokens = []
        i = 0

        while i < len(characters):
            if i < len(characters) - 1 and (characters[i], characters[i + 1]) == pair:
                word_new_tokens.append(pair)
                i += 2
            else:
                word_new_tokens.append(characters[i])
                i += 1

        updated_vocab[word] = word_new_tokens

    return updated_vocab


def append_new_tokens(word, characters):


def apply_bpe(word, merges):
    corpus_bpe_applied = list(word)

    for pair in merges:
        new_tokens = []
        i = 0

        while i < len(corpus_bpe_applied):
            if i < len(corpus_bpe_applied) - 1 and (corpus_bpe_applied[i], corpus_bpe_applied[i + 1]) == pair:
                new_tokens.append(pair)
                i += 2
            else:
                new_tokens.append(corpus_bpe_applied[i])
                i += 1

        corpus_bpe_applied = new_tokens
    return corpus_bpe_applied