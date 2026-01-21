import sys


def main() -> None:
    print("=== Command Quest ===\n")

    len_sys = len(sys.argv)
    has_argument = True if len_sys > 1 else False

    if (has_argument is False):
        print("No arguments provided!")

    print("Program name: ", sys.argv[0])

    if (has_argument is True):
        print(f"Arguments received: {len_sys - 1}")
        i: int = 1
        for arg in sys.argv[1:]:
            print(f"Argument {i}: {arg}")
            i += 1

    print(f"Total arguments: {len_sys}\n")


if __name__ == "__main__":
    main()
