import os
import fire
from termcolor import cprint, colored


class Ingress:
    def _print_file(self, filename, text_color="white", background=None):
        background_color = f"on_{background}" if background else None
        file_path = os.path.join("ascii_art", filename)

        with open(file_path) as f:
            for line in f:
                # print without new lines since they're included in the file
                cprint(line, text_color, background_color, end="")
        # print one new line at end to separate block
        print()

    def enl(self, text="green", background=None):
        self._print_file("enlightened-32x24.txt", text, background)

    def res(self, text="blue", background=None):
        self._print_file("resistance-32x24.txt", text, background)

    def both(self):
        enl_path = os.path.join("ascii_art", "enlightened-32x24.txt")
        res_path = os.path.join("ascii_art", "resistance-32x24.txt")
        with open(enl_path) as enlf, open(res_path) as resf:
            for (enl_line, res_line) in zip(enlf, resf):
                print(
                    colored(enl_line.rstrip("\n"), "green"),
                    colored(res_line.rstrip("\n"), "blue"),
                )
            print()


if __name__ == "__main__":
    fire.Fire(Ingress)
