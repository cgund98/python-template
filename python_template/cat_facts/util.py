def count_words(text: str) -> int:
    """
    Naive method of counting the number of words in a body of text.
    """
    words = text.split(" ")
    words_count = len(words)

    return words_count
