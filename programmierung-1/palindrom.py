# START
# 1. Read a word from the user
# and prepare the word for comparison:
word = input("Enter a word: ").lower()
# 2. Generate the word in reverse:
word_backwards = word[::-1]
# 3. IF word EQUALS word in reverse THEN
if word == word_backwards:
    # output:"... is a palindrome"
    print(f"{word} is a palindrome")
# ELSE
else:
    # output:"... is not a palindrome"
    print(f"{word} is not a palindrome")
# END
