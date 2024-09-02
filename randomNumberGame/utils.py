import math
import random
import curses
import time
import sys
# Ok
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True


# Ok
def get_divisibility_hint(number):
    divisors = [2, 3, 5, 7]
    valid_divisors = [d for d in divisors if number % d == 0]
    if valid_divisors:
        return f"divisible by {random.choice(valid_divisors)}"
    return "not divisible by 2, 3, 5, or 7"


def get_hint(number):
    hints = [
        "even" if number % 2 == 0 else "odd",
        "prime" if is_prime(number) else "not prime",
        get_divisibility_hint(number),
        f"{'greater' if number > 50 else 'less'} than 50"
    ]
    return random.choice(hints)


def display_time(seconds):
    minutes, secs = divmod(int(seconds), 60)
    return f"{minutes:02d}:{secs:02d}"


def finish_game(stdscr, lostORwin, *args):
    stdscr.clear()

    # Define the message to be displayed
    jafar = "Total score: " + str(args)

    # Define messages with color pairs
    messages = [
        ("Congratulations!", 1),
        ("You've completed the game!", 2),
        ("Thanks for playing!", 3),
        (jafar, 11),
        ("Press any key to exit...", 4)
    ]

    # Check if the game was won or lost
    if lostORwin == "win":
        # Display the messages with colors
        for idx, (message, color) in enumerate(messages):
            y = curses.LINES // 2 - len(messages) // 2 + idx
            x = (curses.COLS - len(message)) // 2
            stdscr.attron(curses.color_pair(color))
            stdscr.addstr(y, x, message)
            stdscr.attroff(curses.color_pair(color))
            stdscr.refresh()
            time.sleep(1)
        # Wait for user input before exiting
        stdscr.getch()
        sys.exit()
        # Clean up and restore terminal settings (automatically done by curses.wrapper)
        # curses.endwin()

    else:
        # Display a different message if the game was lost
        lostMessage = "Not everything is a lesson Ryan, sometimes you just fail"
        y = curses.LINES // 2
        x = (curses.COLS -
             len(lostMessage)) // 2
        stdscr.addstr(
            y, x, lostMessage)
        stdscr.refresh()
        time.sleep(2)
        stdscr.getch()
        sys.exit()

    
