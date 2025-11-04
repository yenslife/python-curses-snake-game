import curses
from curses import wrapper

def main(stdscr: curses.window):
    stdscr.clear()
    stdscr.refresh()

    # 讓滑鼠事件會被 report
    curses.mousemask(curses.ALL_MOUSE_EVENTS | curses.REPORT_MOUSE_POSITION)
    stdscr.addstr(0, 0, "Click anywhere to see mouse event details. Press 'q' to exit.")
    stdscr.refresh()

    # 繪製遊戲區塊、title


    # 繪製按鈕 (分數、時間、暫停、重新開始區塊)


if __name__ == "__main__":
    wrapper(main)
