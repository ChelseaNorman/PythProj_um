import re
import sys


def main():
    print(count(input("Text: ")))

#Find how many times a certain group of characters are in input
def count(s):
    words = re.findall(r"\bum\b", s, re.IGNORECASE)
    return len(words)

if __name__ == "__main__":
    main()