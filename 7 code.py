def subsequences(s, i=0, current=""):
    if i == len(s):
        print(current)
        return

    # Exclude the current character
    subsequences(s, i + 1, current)

    # Include the current character
    subsequences(s, i + 1, current + s[i])

subsequences("abc")
