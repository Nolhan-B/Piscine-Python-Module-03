import sys


def main() -> None:
    print("=== Player Score Analytics ===")

    len_sys = len(sys.argv)
    has_argument = True if len_sys > 1 else False

    if (has_argument is False):
        print("No scores provided. Usage: pyhton3 ft_score_analytics.py "
              "<score1> <score2>...\n")
    else:
        arr: list[int] = []
        for e in sys.argv[1:]:
            is_digit = True
            for d in e:
                if d not in "0123456789":
                    is_digit = False
            if is_digit is True:
                arr.append(int(e))

        len_arr: int = len(arr)
        sum_arr: int = sum(arr)
        max_arr: int = max(arr)
        min_arr: int = min(arr)
        print(f"Scores processed: {arr}")
        print(f"Total players: {len_arr}")
        print(f"Total score: {sum_arr}")
        print(f"Average score: {sum_arr/len_arr:.2f}")
        print(f"High score: {max_arr}")
        print(f"Low score: {min_arr}")
        print(f"Score range: {max_arr - min_arr}\n")


if __name__ == "__main__":
    main()
