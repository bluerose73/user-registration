from dataclasses import dataclass

@dataclass
class User:
    """Class representing a user holding bananas."""

    banana_cnt: int
    username: str


def register_user(date: str, user: User) -> None:
    """Register a user."""
    print(f"Registering user {user.username} with {user.banana_cnt} bananas on {date}.")