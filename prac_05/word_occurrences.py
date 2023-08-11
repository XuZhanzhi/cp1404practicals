word_to_count = {}
text = input("Text: ")
words = text.split()
for word in words:
    frequency = word_to_count.get(word, 0)
    word_to_count[word] = frequency + 1

words = list(word_to_count.keys())
words.sort()

for word in words:
    print(f"{word} : {word_to_count[word]}")
