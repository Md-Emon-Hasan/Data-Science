# List Comprehensions
print("List Comprehensions:")
sentence = "the quick brown fox jumps over the lazy dog"
words = sentence.split()
word_length = []
for word in words:
    # if word != "the":
        # word_length.append(len(word))
    word_length.append(len(word))
print(words)
print(word_length)

sentence = "the quick brown fox jumps over the lazy dog"
words = sentence.split()
word_lengths = [len(word) for word in words if word != "the"]
print(words)
print(word_lengths)

# exercise
print("exercise:")
numbers = [34.6, -203.4, 44.9, 68.3, -12.2, 44.6, 12.7]
newlist = [int(x) for x in numbers if x > 0]
print(newlist)

# method
print("method:")
numbers = [34.6, -203.4, 44.9, 68.3, -12.2, 44.6, 12.7]
for x in numbers:
    if x > 0:
        print(x)

