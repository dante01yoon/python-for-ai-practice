def is_palindrome(word):
    word = word.lower()
    return word == word[::-1]


for w in ["Racecar", "Python", "Level", "Noon"]:
    print(w, is_palindrome(w))
