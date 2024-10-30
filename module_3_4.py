def single_root_words(root_word, *other_words):
    same_words = []

    for word in other_words:
        if root_word in word or word in root_word:

            same_words.append(word)

            return same_words


    print(same_words)

single_root_words('five',
                  'five', 'six', 'seven', 'fifteen', 'sixteen', 'seventeen', 'fifty', 'sixty', 'seventy')
