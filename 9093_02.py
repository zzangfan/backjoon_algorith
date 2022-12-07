def reverse_word(string):
    words = [word[::-1] for word in string.split()]

    return " ".join(words)

if __name__ == "__main__":
    for _ in range(int(input())):
        string = input()
        print(reverse_word(string))