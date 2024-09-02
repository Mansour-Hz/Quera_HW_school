import random
import time
import curses
import threading
from utils import *


def update_timer(stdscr, time_limit, stop_event):
    start_time = time.time()
    while not stop_event.is_set():
        
        elapsed_time = time.time() - start_time
        remaining_time = max(0, time_limit - elapsed_time)
        
        if(remaining_time < 10):
            stdscr.addstr(0, 1, 
                          f"Time remaining: {display_time(remaining_time)}",
                                                     curses.color_pair(1))
        else:
            stdscr.addstr(0, 1, f"Time remaining: {display_time(remaining_time)}",
                                                     curses.color_pair(2))
        
        stdscr.refresh()
        if remaining_time <= 0:
            break
        time.sleep(0.2)


def get_user_input(stdscr, prompt, y, x):
    curses.noecho()  # Disable automatic echoing of characters
    stdscr.addstr(y, x, prompt)
    input_win = curses.newwin(1, 20, y, x + len(prompt))
    input_win.keypad(1)
    input_str = ""
    while True:
        try:
            char = input_win.get_wch()
            if isinstance(char, str) and ord(char) == 10:  # Enter key
                break
            elif isinstance(char, int) and char in (curses.KEY_BACKSPACE, 127):  # Backspace
                if input_str:
                    input_str = input_str[:-1]
                    input_win.clear()
                    input_win.addstr(0, 0, input_str)
            elif isinstance(char, str) and char.isdigit():
                input_str += char
                input_win.addstr(char)
            input_win.refresh()
        except curses.error:
            pass
    return input_str


def play_round(stdscr, difficulty):
    if difficulty == 1:
        lower, upper = 1, 50
        time_limit = 60
    elif difficulty == 2:
        lower, upper = 1, 100
        time_limit = 90
    else:
        lower, upper = 1, 200
        time_limit = 120

    number = random.randint(lower, upper)
    guesses = 0

    stdscr.clear()
    stdscr.addstr(0, 1, f"Time remaining: {display_time(time_limit)}")
    stdscr.addstr(1, 1, f"Guesses made: {guesses}")
    stdscr.addstr(2, 1, f"Guess a number between {lower} and {upper}")
    stdscr.refresh()

    stop_event = threading.Event()
    timer_thread = threading.Thread(
        target=update_timer, args=(stdscr, time_limit, stop_event))
    timer_thread.start()

    start_time = time.time()

    while True:
        if time.time() - start_time >= time_limit:
            stop_event.set()
            return 0

        guess_str = get_user_input(stdscr, "Enter your guess: ", 4, 1)
        if not guess_str:
            continue

        try:
            guess = int(guess_str)
            guesses += 1

            stdscr.addstr(1, 1, f"Guesses made: {guesses}")

            if guess < number:
                stdscr.addstr(6, 1, f"Higher than {guess_str}!")
            elif guess > number:
                stdscr.addstr(6, 1, f"Lower than {guess_str}!")
            else:
                stop_event.set()
                time_taken = time.time() - start_time
                message = f"Congratulations! You guessed the number in {
                    guesses} attempts and {time_taken:.2f} seconds."
                stdscr.refresh()
                stageScore = max(
                    0, int((time_limit - time_taken) * 10 + (upper - lower) / guesses))
                return message, stageScore

            if guesses % 5 == 0:
                stdscr.addstr(7, 1, f"Hint: The number is {get_hint(number)}.")

            stdscr.move(4, 19)  # Move cursor back to input position
            stdscr.clrtoeol()  # Clear the line
            stdscr.refresh()

        except ValueError:
            stdscr.addstr(6, 1, "Please enter a valid number.")
            stdscr.refresh()


def play_game(stdscr):
    stdscr.clear()
    total_score = 0
    for stage in range(1, 4):
        stdscr.addstr(0, 1, f"--- Stage {stage} ---", curses.color_pair(1))
        stdscr.refresh()
        time.sleep(2)
        message, score = play_round(stdscr, stage)
        if score == 0:
            finish_game(stdscr, "lost")
        total_score += score
        stdscr.clear() # Test
        if (stage!=4):
            stdscr.addstr(3, 1, message, curses.color_pair(3))
            stdscr.addstr(4, 1, f"Stage score: {score}", curses.color_pair(12))
            stdscr.addstr(5, 1, f"Total score: {total_score}", curses.color_pair(19))
        stdscr.refresh()
        time.sleep(2)

    # stdscr.addstr(11, 1,"Game completed! Final score: {total_score}")
    finish_game(stdscr, "win", total_score)



def main(stdscr):
    curses.curs_set(0)  # Hide the cursor
    stdscr.clear()
    if not curses.has_colors():
        stdscr.addstr(0, 0, "Your terminal does not support colors.")
    else:
        curses.start_color()
        curses.init_pair(1, curses.COLOR_RED, curses.COLOR_BLACK)
        curses.init_pair(2, curses.COLOR_GREEN, curses.COLOR_BLACK)
        curses.init_pair(3, curses.COLOR_YELLOW, curses.COLOR_BLACK)
        curses.init_pair(4, curses.COLOR_BLUE, curses.COLOR_BLACK)
        curses.init_pair(5, curses.COLOR_MAGENTA, curses.COLOR_BLACK)
        curses.init_pair(6, curses.COLOR_CYAN, curses.COLOR_BLACK)
        curses.init_pair(7, curses.COLOR_WHITE, curses.COLOR_BLACK)
        curses.init_pair(8, curses.COLOR_RED, curses.COLOR_YELLOW)
        curses.init_pair(9, curses.COLOR_GREEN, curses.COLOR_CYAN)
        curses.init_pair(10, curses.COLOR_YELLOW, curses.COLOR_BLUE)
        curses.init_pair(11, curses.COLOR_BLUE, curses.COLOR_MAGENTA)
        curses.init_pair(12, curses.COLOR_MAGENTA, curses.COLOR_GREEN)
        curses.init_pair(13, curses.COLOR_CYAN, curses.COLOR_RED)
    stdscr.clear()
    stdscr.addstr(
        0, 1, "Welcome to the Advanced Number Guessing Game!", curses.color_pair(2))

    stdscr.refresh()
    time.sleep(2)
    play_game(stdscr)


if __name__ == "__main__":
    curses.wrapper(main)