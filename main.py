import curses

def main(stdscr):
    curses.curs_set(0)  # Cursor visibility off
    stdscr.clear()

    while True:
        stdscr.addstr(0, 0, "Menyu:")
        stdscr.addstr(1, 0, "1. Boshlash")
        stdscr.addstr(2, 0, "2. Chiqish")
        stdscr.refresh()

        c = stdscr.getch()
        if c == ord('1'):
            stdscr.clear()
            stdscr.addstr(0, 0, "Boshlash")
            stdscr.refresh()
            curses.napms(2000)  # 2 sekund ichida menyu qaytadi
        elif c == ord('2'):
            stdscr.clear()
            stdscr.addstr(0, 0, "Chiqish")
            stdscr.refresh()
            curses.napms(2000)  # 2 sekund ichida menyu qaytadi
        elif c == ord('q'):
            break

curses.wrapper(main)
