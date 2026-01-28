import math
import sys


def parse_pos(s: str) -> tuple:
    parts = s.split(",")

    if len(parts) != 3:
        raise ValueError("Error parsing coordinate: Expected 3 coordinates")

    x = int(parts[0])
    y = int(parts[1])
    z = int(parts[2])

    return (x, y, z)


def main() -> None:
    print("=== Game Coordinate System ===\n")

    pos_0: tuple = (0, 0, 0)
    pos_1: tuple = (10, 20, 5)

    x1, y1, z1 = pos_0
    x2, y2, z2 = pos_1

    distance: float = math.sqrt(
        (x2 - x1) ** 2 +
        (y2 - y1) ** 2 +
        (z2 - z1) ** 2
    )

    print(f"Position Created: {pos_1}")
    print(f"Distance between {pos_0} and {pos_1}: {distance:.2f}\n")
    try:
        parse_value: str = sys.argv[1]
        value_pos: tuple = parse_pos(parse_value)
    except (Exception, ValueError) as e:
        print(f"[ERROR] : {e}, Params should be: \"<xvalue>,<yvalue,<zvalue>\"")
        parse_value: str = "3,4,0"
        print(f"Now using : \"{parse_value}\" as default value.\n")
    value_pos: tuple = parse_pos(parse_value)
    print(f"Parsing coordinates: \"{parse_value}\"")
    print(f"Position Parsed: {value_pos}")

    x2, y2, z2 = value_pos

    distance: float = math.sqrt(
        (x2 - x1) ** 2 +
        (y2 - y1) ** 2 +
        (z2 - z1) ** 2
    )

    print(f"Distance between {pos_0} and {value_pos}: {distance:.2f}")

    invalid_parse: str = "abc,def,ghi"
    print(f"\nParsing invalid coordinates: \"{invalid_parse}\"")
    try:
        parse_value: tuple = parse_pos(invalid_parse)
    except ValueError as e:
        print(f"Error parsing coordinates: {e}")
        print(f"Error details - Type: ValueError, Args: {e.args}\n")

    print("Unpacking demonstration:")
    print(f"Player at x={x2}, y={y2}, z={z2}")
    print(f"Coordinates: X={value_pos[0]}, Y={value_pos[1]}, Z={value_pos[2]}")


if __name__ == "__main__":
    main()
