
from stream import Stream
from skaner2 import Scanner2
from kolor import Colour

if __name__ == "__main__":

    stream = Stream("equation.txt")
    scanner = Scanner2(stream)
    tokens = scanner.tokenize()

    for token in tokens:
        print(token)
