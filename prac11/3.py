sentence = input()
punctuation = '.,!?;:()[]{}"\'<>@#№$%^&*=-'

words = sentence.split()
clean_words = [''.join(i for i in word if i not in punctuation) for word in words]

print(clean_words)