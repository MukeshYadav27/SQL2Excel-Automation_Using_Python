# utils.py

import os


def clear_screen():
    """
    Clear terminal screen.
    """

    os.system("cls" if os.name == "nt" else "clear")


def print_header(title):
    """
    Display formatted title.
    """

    print("\n" + "=" * 70)

    print(title.center(70))

    print("=" * 70)


def press_enter():
    """
    Pause execution.
    """

    input("\nPress Enter To Continue...")


def validate_time(schedule):
    """
    Validate time format.

    Example:
    11:50 AM
    """

    try:

        time_part, ampm = schedule.strip().upper().split()

        hour, minute = map(int, time_part.split(":"))

        if ampm not in ["AM", "PM"]:

            return False

        if hour < 1 or hour > 12:

            return False

        if minute < 0 or minute > 59:

            return False

        return True

    except:

        return False