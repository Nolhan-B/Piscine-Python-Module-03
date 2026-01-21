def main() -> None:
    print("=== Achievement Tracker System ===\n")

    alice: set = {
        "first_kill",
        "level_10",
        "treasure_hunter",
        "speed_demon"
    }

    bob: set = {
        "first_kill",
        "level_10",
        "boss_slayer",
        "collector"
    }

    charlie: set = {
        "level_10",
        "treasure_hunter",
        "boss_slayer",
        "speed_demon",
        "perfectionist"
    }

    print(f"Player alice achievements: {alice}")
    print(f"Player bob achievements: {bob}")
    print(f"Player charlie achievements: {charlie}")

    print("\n=== Achievement Analytics ===")
    all_ach: set = alice.union(bob.union(charlie))
    print(f"All unique achievements: {all_ach}")
    print(f"Total unique achievements: {len(all_ach)}")

    all_own = alice.intersection(bob).intersection(charlie)
    print(f"Common to all players: {all_own}")

    rare_ach: set = set()
    for ach in all_ach:
        count: int = 0
        if ach in alice:
            count += 1
        if ach in bob:
            count += 1
        if ach in charlie:
            count += 1
        if count == 1:
            rare_ach.add(ach)

    print(f"Rare achievements (1 player): {rare_ach}\n")

    print(f"Alice vs Bob common: {alice.intersection(bob)}")
    print(f"Alice unique: {alice.difference(bob)}")
    print(f"Bob unique: {bob.difference(alice)}")


if __name__ == "__main__":
    main()
