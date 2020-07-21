def unique_doubled(numbers):
    """write a set comprehension that takes a list of numbers and return
    a set of unique doubled numbers from that list"""
    numbers = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
    return {num*2 for num in numbers}


def unique_factorial():
    """write a set comprehension that returns a set containing the length of the factorial
     in the factorials between 0 and 20"""
    from math import factorial
    factorials = [factorial(number) for number in range(0, 20)]
    return {len(str(num)) for num in factorials}
    # return {len(str(math.factorial(0))) for x in range(0, 20)}


def unique_word(sentence):
    """write a set comprehension that takes a long sentence and returns a set
    containing only unique words. Make sure to account for punctuation and
    capitalization in the test string."""
    return {word.lower().replace('.', '').replace(',', '') for word in sentence.split()}


def unique_short_words(sentence):
    """write a set comprehension that takes a long sentence and returns a set
    containing only unique words that are three letters or fewer. Make sure to
    account for punctuation and capitalization in the test string."""
    return {word.lower().replace('.', '').replace(',', '') for word in sentence.split() if len(word.lower().replace('.', '').replace(',', '')) <= 3}


def unique_consonants(sentence):
    """Remove all of the vowels in a string [make a set of the unique non-vowels]"""
    return {letter for letter in sentence.lower() if letter.lower() not in 'aeiou '}
