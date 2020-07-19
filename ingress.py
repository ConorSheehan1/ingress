import os
import fire
from termcolor import cprint


class Ingress:
    def _print_file(self, filename, text_color="white"):
        file_path = os.path.join("ascii_art", filename)
        with open(file_path) as f:
            for line in f:
                cprint(line, text_color, end="")
        print()

    def enl(self, color="green"):
        self._print_file("enlightened-32x24.txt", color)

    def res(self, color="blue"):
        self._print_file("resistance-32x23.txt", color)


if __name__ == "__main__":
    fire.Fire(Ingress)
