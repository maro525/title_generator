import itertools
import random
import argparse

FILE = 'word.txt'
OUTPUT_FILE = 'title.txt'
DEFAULT_TITLE_LENGTH = 2


class TitleGenerator:

    def __init__(self):
        self.word_list = []
        self.title_list = []

    def load_file(self, FILE):
        with open(FILE, 'r') as reader:
            print("load...")
            for line in reader.read().splitlines():
                print("add {}".format(line))
                self.word_list.append(line)
            print("")

    def combination(self, length):
        comb = list(itertools.combinations(self.word_list, length))
        for c in comb:
            title = ""
            for i in range(length):
                title += c[i]
                title += " "
            print(title)
            self.title_list.append(title)
        random.shuffle(self.title_list)

    def write_to_file(self, filename):
        f = open(filename, "w")
        for t in self.title_list:
            f.write(t+"\n")
        f.close()


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--length', type=int, default=DEFAULT_TITLE_LENGTH,
                        help='desired word length')
    args = parser.parse_args()

    TG = TitleGenerator()
    TG.load_file(FILE)
    TG.combination(args.length)
    TG.write_to_file(OUTPUT_FILE)
