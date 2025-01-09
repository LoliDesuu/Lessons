import re

class WordsFinder:
    def __init__(self, *file_names:list):
        self.file_names = file_names

    def get_all_words(self):
        all_lines = list()
        for file in self.file_names:
            with open(file, encoding='utf-8') as select_file:
                for line in select_file:
                    new_line = re.sub(r'[^\w\s\']', '', line.lower())
                    all_lines.extend(new_line.split())
        all_words = dict.fromkeys(self.file_names, all_lines)
        return all_words

    def find(self, word):
        all_words = self.get_all_words()
        key = all_words.keys()
        for name, words in all_words.items():
            if word.lower() in words:
                return dict.fromkeys(key, words.index(word.lower())+1)

    def count(self, word):
        all_words = self.get_all_words()
        list_words = list(all_words.values())
        flat_list = list_words[0]
        key = all_words.keys()
        return dict.fromkeys(key, flat_list.count(word.lower()))


finder2 = WordsFinder('test_file.txt')
print(finder2.get_all_words())
print(finder2.find('TEXT'))
print(finder2.count('teXT'))