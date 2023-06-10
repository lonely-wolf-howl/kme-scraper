import customtkinter

toplevel_window = None  # 전역 변수로 선언합니다.

class ToplevelWindow(customtkinter.CTkToplevel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.title("경고")
        self.geometry("200x100")

        self.label = customtkinter.CTkLabel(self, text="정말로 종료하시겠습니까?")
        self.label.pack(padx=20, pady=20)

        self.button = customtkinter.CTkButton(self, text="예", command=close_all)
        self.button.pack(padx=10, pady=10)

        self.button = customtkinter.CTkButton(self, text="아니오", command=close_toplevel)
        self.button.pack(padx=10, pady=10)

def open_toplevel():
    global toplevel_window

    if toplevel_window is None or not toplevel_window.winfo_exists():
        toplevel_window = ToplevelWindow(root)
        toplevel_window.attributes('-topmost', True) # 추가 창을 항상 맨 위에 표시합니다.
    else:
        toplevel_window.lift() # 이미 존재하는 창을 맨 위로 올립니다.
        toplevel_window.focus() # 추가 창에 초점을 맞춥니다.


def close_toplevel(): # <--- 추가 창을 종료하는 함수입니다.
    if toplevel_window is not None and toplevel_window.winfo_exists():
        toplevel_window.destroy() # 추가 창을 종료합니다.

def close_all(): # <--- 추가 창, 기본 창을 모두 종료하는 함수입니다.
    if toplevel_window is not None and toplevel_window.winfo_exists():
        toplevel_window.destroy()
    root.destroy() # 기본 창을 종료합니다.

root = customtkinter.CTk()
root.geometry("400x200")

button_1 = customtkinter.CTkButton(root, text="open toplevel", command=open_toplevel)
button_1.pack(side="top", padx=10, pady=10)

button_close = customtkinter.CTkButton(root, text="close toplevel", command=close_toplevel)
button_close.pack(side="top", padx=10)

button_close_all = customtkinter.CTkButton(root, text="close all", command=close_all)
button_close_all.pack(side="top", padx=10, pady=10)

root.mainloop()
