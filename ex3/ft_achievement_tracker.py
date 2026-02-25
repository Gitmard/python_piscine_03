#!/usr/bin/env python3

class Player:
    __static_last_id = 0
    __id: int
    __name: str
    __achievements: set[str]

    def __init__(self, name: str):
        self.__id = Player.__static_last_id + 1
        Player.__static_last_id += 1
        self.set_name(name)
        self.set_achievements(set())

    def get_id(self) -> int:
        return self.__id

    def get_name(self):
        return self.__name

    def get_achievements(self):
        return self.__achievements

    def set_name(self, name: str) -> None:
        self.__name = name

    def set_achievements(self, achievements: set[str]):
        self.__achievements = achievements

    def has_achievement(self, achievement: str):
        return achievement in self.get_achievements()

    def add_achievement(self, achievement: str):
        self.get_achievements().add(achievement)


class AchievementsManager:
    __players: list[Player]

    def __init__(
        self,
        players: list[Player] = None,
    ):
        if players is None:
            players = []
        self.set_players(players)

    def get_players(self) -> list[Player]:
        return self.__players

    def set_players(self, players: list[Player]) -> None:
        self.__players = players

    def create_player(self, name: str) -> Player:
        new_player = Player(name)
        self.get_players().append(new_player)
        return new_player

    def get_player(self, id: int):
        for player in self.get_players():
            if (player.get_id() == id):
                return player
        raise ValueError(f"Error: No player has id {id}")

    def unite_achievements(self) -> set[str]:
        first_player = self.get_players()[0]
        players = self.get_players()[1:]
        united_achievements: set[str] = set(
            first_player.get_achievements()
        )
        for player in players:
            united_achievements |= player.get_achievements()
        return united_achievements

    def intersect_achievements(self) -> set[str]:
        first_player = self.get_players()[0]
        players = self.get_players()[1:]
        common_achievements: set[str] = set(
            first_player.get_achievements()
        )
        for player in players:
            common_achievements &= player.get_achievements()
        return common_achievements

    def differentiate_achievements(self) -> set[str]:
        first_player = self.get_players()[0]
        players = self.get_players()[1:]
        differentiated_achievements: set[str] = set(
            first_player.get_achievements()
        )
        for player in players:
            differentiated_achievements -= player.get_achievements()
        return differentiated_achievements

    def get_rare_achievements(self) -> set[str]:
        found_achievements = set()
        rare_achievements = set()
        for player in self.get_players():
            for achievement in player.get_achievements():
                if achievement not in found_achievements:
                    found_achievements.add(achievement)
                    rare_achievements.add(achievement)
                elif achievement in rare_achievements:
                    rare_achievements.remove(achievement)
        return rare_achievements

    def get_unique_achievements(
        self,
        player1: Player,
        player2: Player
    ) -> set[str]:
        return player1.get_achievements() - player2.get_achievements()


def give_achievements(player: Player, achievements: list[str]):
    for achievement in achievements:
        if achievement not in player.get_achievements():
            player.get_achievements().add(achievement)
        else:
            print(
                f"Warning: player {player.get_name()}",
                f"already has achievement {achievement}"
            )


def main():
    print("=== Achievement Tracker System ===\n")

    alices_achievements = [
        'first_kill',
        'level_10',
        'treasure_hunter',
        'speed_demon'
    ]
    bobs_achievements = [
        'first_kill',
        'level_10',
        'boss_slayer',
        'collector'
    ]
    charlies_achievements = [
        'level_10',
        'treasure_hunter',
        'boss_slayer',
        'speed_demon',
        'perfectionist'
    ]
    achievements_manager = AchievementsManager()
    alice = achievements_manager.create_player("Alice")
    give_achievements(alice, alices_achievements)
    bob = achievements_manager.create_player("Bob")
    give_achievements(bob, bobs_achievements)
    charlie = achievements_manager.create_player("Charlie")
    give_achievements(charlie, charlies_achievements)

    for player in achievements_manager.get_players():
        print(
            f"Player {player.get_name()}",
            f"achievements: {player.get_achievements()}"
        )

    print("\n=== Achievement Analytics ===")
    unique_achievements = achievements_manager.unite_achievements()
    print(
        "All unique achievements:",
        f"{unique_achievements}"
    )
    print(f"Total unique achievements: {len(unique_achievements)}")

    print(
        "\nCommon to all players:",
        f"{achievements_manager.intersect_achievements()}"
    )
    print(
        "Rare achievements (1 player):",
        f"{achievements_manager.get_rare_achievements()}"
    )

    print(
        "\nAlice vs Bob common:",
        f"{alice.get_achievements().intersection(bob.get_achievements())}"
    )
    print(
        "Alice unique:",
        f"{achievements_manager.get_unique_achievements(alice, bob)}"
    )
    print(
        "Bob unique:",
        f"{achievements_manager.get_unique_achievements(bob, alice)}"
    )


if __name__ == "__main__":
    main()
