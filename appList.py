import win32gui
import win32process
import psutil

def getWindowList() -> list[tuple[int, str, str]]:
    application_list = []

    def enum_window_callback(hwnd, extra):
        if win32gui.IsWindowVisible(hwnd) and win32gui.GetWindowText(hwnd).strip():
            _, pid = win32process.GetWindowThreadProcessId(hwnd)
            exe = psutil.Process(pid).name()
            name = win32gui.GetWindowText(hwnd)

            application_list.append((pid, exe, name))

    win32gui.EnumWindows(enum_window_callback, None)

    return application_list

if __name__ == "__main__":
    print(f"{"PID":<10} | {"Process":<30} | Name\n")
    for i in getWindowList():
        print(f"{i[0]:<10} | {i[1]:<30} | {i[2]}")