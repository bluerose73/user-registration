from dataclasses import dataclass

@dataclass
class User:
    """Class representing a user."""

    username_xyz: str
    banana_cnt: int


def register_user(date: str, user: User) -> None:
    """Register a user."""
    print(f"Registering user {user.username_xyz} with {user.banana_cnt} bananas on {date}.")