from random import randint


def generate_birthdays(num_people: int) -> list[int]:
    """
    Generates a random birthday for each person.

    Each birthday is represented by a number between 1 and 365.
    Returns a list containing one birthday for each person.
    """
    birthdays = [randint(1, 365) for _ in range(num_people)]

    return birthdays


def find_matches(birthdays: list[int]) -> dict[int, list[int]]:
    """
    Finds people who share the same birthday.

    Returns a dictionary where:
    - The key is the shared birthday.
    - The value is a list of person indexes who have that birthday.

    Only birthdays shared by at least two people are included.
    """
    birthday_groups = {}

    for person_index, birthday in enumerate(birthdays):
        if birthday not in birthday_groups:
            birthday_groups[birthday] = []

        birthday_groups[birthday].append(person_index)

    matches = {
        birthday: people
        for birthday, people in birthday_groups.items()
        if len(people) >= 2
    }

    return matches