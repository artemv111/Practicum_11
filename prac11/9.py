punctuation = '.,!?;:()[]{}"\'<>@#№$%^&*=-'

lines = []
while True:
    line = input()
    if line == "":
        break
    lines.append(line)

text = " ".join(lines).lower()
words = text.split()

clean_words = []
for w in words:
    clean = ''.join(ch for ch in w if ch not in punctuation)
    if clean:
        clean_words.append(clean)

freq = {}
for word in clean_words:
    freq[word] = freq.get(word, 0) + 1

first = {}
for i, word in enumerate(clean_words):
    if word not in first:
        first[word] = i

unique = []
for word in clean_words:
    if word not in unique:
        unique.append(word)

unique.sort(key=lambda word: (-freq[word], first[word]))

for word in unique:
    print(word)