word = input("Enter a word: ")
# compare in lowercase so that "Anna" counts as a palindrome
word_lowercase = word.lower()
word_backwards = word_lowercase[::-1]

if word_lowercase == word_backwards:
    print(f"{word} is a palindrome")
else:
    print(f"{word} is not a palindrome")
