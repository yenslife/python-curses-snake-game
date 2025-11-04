import curses
from curses import wrapper
from curses.textpad import rectangle

from utils.mouse import MOUSE_STATE

# 遊戲常數
GAME_WIN_START_Y = 3
GAME_WIN_START_X = 3
GAME_WIN_HEIGHT = 20
GAME_WIN_WIDTH = 50
GAME_TITLE = "SNAKE GAME"
GAME_AREA_START = (1, 1)
GAME_AREA_END = (GAME_WIN_HEIGHT - 2, GAME_WIN_WIDTH - 2)

# 選單常數
MENU_WIN_START_Y = GAME_WIN_START_Y
MENU_WIN_START_X = GAME_WIN_START_X + GAME_WIN_WIDTH + 2
MENU_WIN_HEIGHT = GAME_WIN_HEIGHT
MENU_WIN_WIDTH = 17
## 按鈕位置 (反過來做，相對底部的概念，這樣之後調整視窗長度都會跟著變)
MENU_RESTART_END = (MENU_WIN_HEIGHT - 2, MENU_WIN_WIDTH - 3)
MENU_RESTART_START = (MENU_RESTART_END[0] - 4, 2)
MENU_PAUSE_END = (MENU_RESTART_START[0] - 1, MENU_WIN_WIDTH - 3)
MENU_PAUSE_START = (MENU_PAUSE_END[0] - 4, 2)


def main(stdscr: curses.window):
    curses.start_color()
    curses.curs_set(0)  # 隱藏游標
    stdscr.clear()
    stdscr.refresh()

    # 讓滑鼠事件會被 report
    curses.mousemask(curses.ALL_MOUSE_EVENTS | curses.REPORT_MOUSE_POSITION)
    click_msg = "Click anywhere to see mouse event details. Press 'q' to exit."
    stdscr.addstr(
        GAME_WIN_START_Y - 2,
        (GAME_WIN_WIDTH + MENU_WIN_WIDTH + 2 - len(click_msg)) // 2,
        click_msg,
    )
    stdscr.refresh()

    # 初始化遊戲視窗
    game_win = curses.newwin(
        GAME_WIN_HEIGHT, GAME_WIN_WIDTH, GAME_WIN_START_Y, GAME_WIN_START_X
    )

    # 繪製遊戲區塊、title
    game_win.box()  # Debug: 先畫個邊框看位置
    rectangle(game_win, *GAME_AREA_START, *GAME_AREA_END)
    game_win.addstr(0, (GAME_WIN_WIDTH - len(GAME_TITLE)) // 2, GAME_TITLE)
    game_win.refresh()

    # 繪製選單區塊、按鈕 (分數、時間、暫停、重新開始區塊，以及一個小動畫區塊)
    menu_win = curses.newwin(
        MENU_WIN_HEIGHT, MENU_WIN_WIDTH, MENU_WIN_START_Y, MENU_WIN_START_X
    )
    menu_win.box()  # Debug: 先畫個邊框看位置
    menu_win.addstr(0, 2, "SCORE: 696")
    menu_win.addstr(1, 2, "TIMER: 06:09")

    # add colored rectangle buttons
    rectangle(menu_win, *MENU_PAUSE_START, *MENU_PAUSE_END)
    curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_MAGENTA)
    menu_win.attron(curses.color_pair(1)) # 按鈕顏色
    menu_win.addstr(
        (MENU_PAUSE_START[0] + MENU_PAUSE_END[0]) // 2,
        (MENU_WIN_WIDTH - len("PAUSE")) // 2,
        "PAUSE",
    )
    menu_win.attroff(curses.color_pair(1)) # 關閉按鈕顏色

    rectangle(menu_win, *MENU_RESTART_START, *MENU_RESTART_END)
    curses.init_pair(2, curses.COLOR_BLACK, curses.COLOR_CYAN)
    menu_win.attron(curses.color_pair(2))
    menu_win.addstr(
        (MENU_RESTART_START[0] + MENU_RESTART_END[0]) // 2,
        (MENU_WIN_WIDTH - len("RESTART")) // 2,
        "RESTART",
    )
    menu_win.attroff(curses.color_pair(2))
    menu_win.refresh()

    # debug 用
    while True:
        key = stdscr.getkey()
        if key == "q":
            break
        elif key == "KEY_MOUSE":
            try:
                _, mx, my, _, bstate = curses.getmouse()
                click_msg = f"Click at ({mx}, {my}) with state {MOUSE_STATE.get(bstate, 'UNKNOWN')}"
                middle_x = (GAME_WIN_WIDTH + MENU_WIN_WIDTH) // 2 - len(
                    click_msg) // 2
                stdscr.addstr(
                    GAME_WIN_START_Y - 1,
                    middle_x,
                    click_msg
                )
                stdscr.refresh()
            except curses.error:
                # Ignore errors from getmouse
                pass


if __name__ == "__main__":
    wrapper(main)
