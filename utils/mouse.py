import curses
from curses import wrapper

# mourse state
MOUSE_STATE = {
    curses.BUTTON1_CLICKED: "BUTTON1_CLICKED",
    curses.BUTTON1_DOUBLE_CLICKED: "BUTTON1_DOUBLE_CLICKED",
    curses.BUTTON1_TRIPLE_CLICKED: "BUTTON1_TRIPLE_CLICKED",
    curses.BUTTON1_PRESSED: "BUTTON1_PRESSED",
    curses.BUTTON1_RELEASED: "BUTTON1_RELEASED",
    curses.BUTTON2_CLICKED: "BUTTON2_CLICKED",
    curses.BUTTON2_DOUBLE_CLICKED: "BUTTON2_DOUBLE_CLICKED",
    curses.BUTTON2_TRIPLE_CLICKED: "BUTTON2_TRIPLE_CLICKED",
    curses.BUTTON2_PRESSED: "BUTTON2_PRESSED",
    curses.BUTTON2_RELEASED: "BUTTON2_RELEASED",
    curses.BUTTON3_CLICKED: "BUTTON3_CLICKED",
    curses.BUTTON3_DOUBLE_CLICKED: "BUTTON3_DOUBLE_CLICKED",
    curses.BUTTON3_TRIPLE_CLICKED: "BUTTON3_TRIPLE_CLICKED",
    curses.BUTTON3_PRESSED: "BUTTON3_PRESSED",
    curses.BUTTON3_RELEASED: "BUTTON3_RELEASED",
    curses.BUTTON4_CLICKED: "BUTTON4_CLICKED",
    curses.BUTTON4_DOUBLE_CLICKED: "BUTTON4_DOUBLE_CLICKED",
    curses.BUTTON4_TRIPLE_CLICKED: "BUTTON4_TRIPLE_CLICKED",
    curses.BUTTON4_PRESSED: "BUTTON4_PRESSED", # 滾輪
    curses.BUTTON4_RELEASED: "BUTTON4_RELEASED",
    curses.BUTTON_ALT: "BUTTON_ALT",
    curses.BUTTON_CTRL: "BUTTON_CTRL",
    curses.BUTTON_SHIFT: "BUTTON_SHIFT",
    curses.REPORT_MOUSE_POSITION: "REPORT_MOUSE_POSITION", # 滾輪，button5 似乎無法使用
}

def main(stdscr: curses.window):
    stdscr.clear()
    stdscr.refresh()


    # Set the mouse events to be reported, and return a tuple (availmask, oldmask)
    curses.mousemask(curses.ALL_MOUSE_EVENTS | curses.REPORT_MOUSE_POSITION)

    stdscr.addstr(0, 0, "Click anywhere to see mouse event details. Press 'q' to exit.")
    stdscr.refresh()

    # show mouse events
    while True:
        key = stdscr.getkey()
        if key == "q":
            break
        elif key == "KEY_MOUSE":
            try:
                _, mx, my, _, bstate = curses.getmouse()
                stdscr.clear()
                stdscr.addstr(0, 0, "Click anywhere to see mouse event details. Press 'q' to exit.")
                stdscr.addstr(2, 0, f"Mouse Event at ({mx}, {my}) with state {MOUSE_STATE.get(bstate, 'UNKNOWN')}")
                stdscr.refresh()
            except curses.error:
                # Ignore errors from getmouse
                pass


if __name__ == "__main__":
    wrapper(main)
