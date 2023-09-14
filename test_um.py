import pytest
from um import count

def main():
    test_case()
    test_surrounded_noncharacters()
    test_um_in_word()

def test_case():
    assert count("Um thanks for the album.") == 1
    assert count("Um, thanks, um...") == 2

def test_surrounded_noncharacters():
    assert count("um") == 1
    assert count("um?") == 1
    assert count (" um ") == 1

def test_um_in_word():
    assert count("yummy") == 0

if __name__ == "__main__":
    main()
