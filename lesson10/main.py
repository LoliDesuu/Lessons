def single_root_words(root_word, *other_words):
    same_words = []
    for strings in other_words:
        if strings.lower().count(root_word.lower()) == True or root_word.lower().count(strings.lower()) == True:
            same_words.append(strings)
    return same_words


result1 = single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies')
result2 = single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel')

print(result1)
print(result2)
