def list_comprehension() -> None:
    print("=== List Comprehension Examples ===")
    players = [{"name": "alice", "score": 2300, "active": True},
               {"name": "bob", "score": 1800, "active": True},
               {"name": "charlie", "score": 2150, "active": True},
               {"name": "diana", "score": 2050, "active": False}]

    high_scorers = [p["name"] for p in players if p["score"] > 2000]
    scores_doubled = [p["score"] * 2 for p in players]
    active_players = [p["name"] for p in players if p["active"] is True]

    print(f"High scorers (>2000): {high_scorers}")
    print(f"Score doubled: {scores_doubled}")
    print(f"Active players: {active_players}")


players = {
        'alice': {
            'score': 2300,
            'active': True,
            'region': 'north',
            'achievements': {
                'first_kill',
                'level_10',
                'boss_slayer',
                'player_killer'
            }
        },
        'charlie': {
            'score': 2150,
            'active': True,
            'region': 'east',
            'achievements': {'level_10', 'speed_runner', 'blade_runner'}
        },
        'bob': {
            'score': 1800,
            'active': True,
            'region': 'east',
            'achievements': {'first_kill', 'collector'}
        },
        'diana': {
            'score': 1450,
            'active': False,
            'region': 'central',
            'achievements': {'boss_slayer', 'collector'}
        },
        'eve': {
            'score': 1200,
            'active': True,
            'region': 'west',
            'achievements': {'first_kill'}
        }
}


def dict_comprehension() -> None:
    player_score = {key: data["score"] for key, data in players.items()}
    score_cat = {
        'high': len(
            [
                data["score"]
                for data in players.values()
                if data["score"] > 2000
            ]
        ),
        'medium': len(
            [
                data["score"]
                for data in players.values()
                if 1500 < data["score"] <= 2000
            ]
        ),
        'low': len(
            [
                data["score"]
                for data in players.values()
                if data["score"] <= 1500
            ]
        )
    }
    ach_count = {
        key: len(data['achievements']) for key, data in players.items()
    }
    print(f"Player scores: {player_score}")
    print(score_cat)
    print(ach_count)


def set_comprehension() -> None:
    unique_player = {name for name in players.keys()}
    unique_ach = {achievements
                  for data in players.values()
                  for achievements in data["achievements"]}
    unique_active_region = {data["region"]
                            for data in players.values()
                            if data["active"] is True}
    print(f"Unique players: {unique_player}")
    print(f"Unique achievements: {unique_ach}")
    print(f"Active regions: {unique_active_region}")


def combined_analysis() -> None:
    total_players = len(players)
    total_unique_achievements = len(
        {
            achievement
            for data in players.values()
            for achievement in data["achievements"]
        }
    )
    average_score = sum(data["score"]
                        for data in players.values()) / total_players

    # Trouver le top performer sans lambda
    top_score = -1
    top_player_name = ""
    for name, data in players.items():
        if data["score"] > top_score:
            top_score = data["score"]
            top_player_name = name
    top_achievements = len(players[top_player_name]["achievements"])

    print(f"Total players: {total_players}")
    print(f"Total unique achievements: {total_unique_achievements}")
    print(f"Average score: {average_score}")
    print(
        f"Top performer: {top_player_name} ({top_score} points, "
        f"{top_achievements} achievements)"
    )


def main() -> None:
    print("=== Game Analytics Dashboard ===\n")

    list_comprehension()

    print("\n=== Dict Comprehension Examples ===")

    dict_comprehension()

    print("\n=== Set Comprehension Examples ===")

    set_comprehension()

    print("\n=== Combined Analysis ===")

    combined_analysis()


if __name__ == "__main__":
    main()
