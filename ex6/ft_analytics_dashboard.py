#!/usr/bin/env python3

from typing import Any


def get_data() -> dict[Any, Any]:
    return ({
        "players": {
            "alice": {
                "level": 41,
                "total_score": 2824,
                "sessions_played": 13,
                "favorite_mode": "ranked",
                "achievements_count": 5,
            },
            "bob": {
                "level": 16,
                "total_score": 4657,
                "sessions_played": 27,
                "favorite_mode": "ranked",
                "achievements_count": 2,
            },
            "charlie": {
                "level": 44,
                "total_score": 9935,
                "sessions_played": 21,
                "favorite_mode": "ranked",
                "achievements_count": 7,
            },
            "diana": {
                "level": 3,
                "total_score": 1488,
                "sessions_played": 21,
                "favorite_mode": "casual",
                "achievements_count": 4,
            },
            "eve": {
                "level": 33,
                "total_score": 1434,
                "sessions_played": 81,
                "favorite_mode": "casual",
                "achievements_count": 7,
            },
            "frank": {
                "level": 15,
                "total_score": 8359,
                "sessions_played": 85,
                "favorite_mode": "competitive",
                "achievements_count": 1,
            },
        },
        "sessions": [
            {
                "player": "bob",
                "duration_minutes": 94,
                "score": 1831,
                "mode": "competitive",
                "completed": False,
            },
            {
                "player": "bob",
                "duration_minutes": 32,
                "score": 1478,
                "mode": "casual",
                "completed": True,
            },
            {
                "player": "diana",
                "duration_minutes": 17,
                "score": 1570,
                "mode": "competitive",
                "completed": False,
            },
            {
                "player": "alice",
                "duration_minutes": 98,
                "score": 1981,
                "mode": "ranked",
                "completed": True,
            },
            {
                "player": "diana",
                "duration_minutes": 15,
                "score": 2361,
                "mode": "competitive",
                "completed": False,
            },
            {
                "player": "eve",
                "duration_minutes": 29,
                "score": 2985,
                "mode": "casual",
                "completed": True,
            },
            {
                "player": "frank",
                "duration_minutes": 34,
                "score": 1285,
                "mode": "casual",
                "completed": True,
            },
            {
                "player": "alice",
                "duration_minutes": 53,
                "score": 1238,
                "mode": "competitive",
                "completed": False,
            },
            {
                "player": "bob",
                "duration_minutes": 52,
                "score": 1555,
                "mode": "casual",
                "completed": False,
            },
            {
                "player": "frank",
                "duration_minutes": 92,
                "score": 2754,
                "mode": "casual",
                "completed": True,
            },
            {
                "player": "eve",
                "duration_minutes": 98,
                "score": 1102,
                "mode": "casual",
                "completed": False,
            },
            {
                "player": "diana",
                "duration_minutes": 39,
                "score": 2721,
                "mode": "ranked",
                "completed": True,
            },
            {
                "player": "frank",
                "duration_minutes": 46,
                "score": 329,
                "mode": "casual",
                "completed": True,
            },
            {
                "player": "charlie",
                "duration_minutes": 56,
                "score": 1196,
                "mode": "casual",
                "completed": True,
            },
            {
                "player": "eve",
                "duration_minutes": 117,
                "score": 1388,
                "mode": "casual",
                "completed": False,
            },
            {
                "player": "diana",
                "duration_minutes": 118,
                "score": 2733,
                "mode": "competitive",
                "completed": True,
            },
            {
                "player": "charlie",
                "duration_minutes": 22,
                "score": 1110,
                "mode": "ranked",
                "completed": False,
            },
            {
                "player": "frank",
                "duration_minutes": 79,
                "score": 1854,
                "mode": "ranked",
                "completed": False,
            },
            {
                "player": "charlie",
                "duration_minutes": 33,
                "score": 666,
                "mode": "ranked",
                "completed": False,
            },
            {
                "player": "alice",
                "duration_minutes": 101,
                "score": 292,
                "mode": "casual",
                "completed": True,
            },
            {
                "player": "frank",
                "duration_minutes": 25,
                "score": 2887,
                "mode": "competitive",
                "completed": True,
            },
            {
                "player": "diana",
                "duration_minutes": 53,
                "score": 2540,
                "mode": "competitive",
                "completed": False,
            },
            {
                "player": "eve",
                "duration_minutes": 115,
                "score": 147,
                "mode": "ranked",
                "completed": True,
            },
            {
                "player": "frank",
                "duration_minutes": 118,
                "score": 2299,
                "mode": "competitive",
                "completed": False,
            },
            {
                "player": "alice",
                "duration_minutes": 42,
                "score": 1880,
                "mode": "casual",
                "completed": False,
            },
            {
                "player": "alice",
                "duration_minutes": 97,
                "score": 1178,
                "mode": "ranked",
                "completed": True,
            },
            {
                "player": "eve",
                "duration_minutes": 18,
                "score": 2661,
                "mode": "competitive",
                "completed": True,
            },
            {
                "player": "bob",
                "duration_minutes": 52,
                "score": 761,
                "mode": "ranked",
                "completed": True,
            },
            {
                "player": "eve",
                "duration_minutes": 46,
                "score": 2101,
                "mode": "casual",
                "completed": True,
            },
            {
                "player": "charlie",
                "duration_minutes": 117,
                "score": 1359,
                "mode": "casual",
                "completed": True,
            },
        ],
        "game_modes": ["casual", "competitive", "ranked"],
        "achievements": [
            "first_blood",
            "level_master",
            "speed_runner",
            "treasure_seeker",
            "boss_hunter",
            "pixel_perfect",
            "combo_king",
            "explorer",
        ],
    })


def get_score_category(score) -> str:
    return "high" if score >= 2000 else "medium" if score >= 1000 else "low"


def main() -> None:
    data: dict[Any, Any] = get_data()
    print("=== Game Analytics Dashboard ===")

    print("\n=== List Comprehension Examples ===")

    players: dict[str, dict[str, int | str]] | None = data.get("players")
    sessions: list[dict[str, str | int]] | None = data.get("sessions")
    achievements: list[str] | None = data.get("achievements")
    assert (
        players is not None
        and sessions is not None
        and achievements is not None
    )

    high_score_players = (
        [player_name for player_name, player_data in players.items() if (
            player_data.get("total_score") is not None
            and player_data.get("total_score") > 2000
        )]
    )
    print(f"High scores (>2000): {high_score_players}")

    scores_doubled: list[int] = ([
        player_data.get("total_score") * 2 for player_data in players.values()
    ])
    print(f"Scores doubled: {scores_doubled}")

    active_players: list[str] = list(dict.fromkeys(
        session.get("player")
        for session in sessions
        if not session.get("completed")
    ))
    print(f"Active players: {active_players}")

    print("\n=== Dict Comprehension Examples ===")

    player_scores = dict(
        (player_name, player_data.get("total_score"))
        for player_name, player_data in players.items()
    )
    print(f"Player scores: {player_scores}")

    categories = ["high", "medium", "low"]
    score_categories = {
        category: sum(1 for session in data["sessions"] if (
            get_score_category(session["score"]) == category)
        )
        for category in categories
    }
    print(f"Score categories: {score_categories}")

    achievement_counts = {
        player: data["players"][player]["achievements_count"]
        for player in data["players"]
        if player in active_players
    }
    print(f"Achievement counts: {achievement_counts}")

    print("\n=== Set Comprehension Examples ===")

    unique_players = set(
        player_name
        for player_name in players.keys()
    )
    print(f"Unique players: {unique_players}")

    unique_achievements = set(
        achievement for achievement in achievements
    )
    print(f"Unique achievements: {unique_achievements}")

    # Normally, this would be the active regions
    # But since their isnt any region in the provided data
    # We use the game modes instead
    active_game_modes = set(
        session.get("mode")
        for session in sessions
        if not session.get("completed")
    )
    print(f"Active game modes: {active_game_modes}")

    print("\n==== Combined Analysis ===")
    print(f"Total players: {len(players)}")
    print(f"Total unique achievements: {len(achievements)}")

    average_score = sum(
        [session.get("score") for session in sessions]
    ) / len(sessions)
    print(f"Average score: {average_score:.1f}")

    top_performer = max([
            (player_name, player_data)
            for player_name, player_data in players.items()
    ])
    print(
        f"Top performer: {top_performer[0]}",
        f"({top_performer[1].get('total_score')} points,",
        f"{top_performer[1].get('achievements_count')} achievement(s))"
    )


if __name__ == "__main__":
    main()
