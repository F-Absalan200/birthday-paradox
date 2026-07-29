from random import randint

def birthday_paradox(num_people: int) -> bool:
    """
    Simulates the birthday paradox for a given number of people.
    Returns True if at least two people share the same birthday.
    """
    birthdays = [randint(1, 365) for _ in range(num_people)]
    seen = set()

    for b in birthdays:
        if b in seen:
            return True
        seen.add(b)

    return False


def examination(people: int, trials: int) -> float:
    """
    Runs multiple trials of the birthday paradox simulation.
    Returns the percentage of trials where a match occurred.
    """
    same = 0

    for _ in range(trials):
        if birthday_paradox(people):
            same += 1

    return (same / trials) * 100

