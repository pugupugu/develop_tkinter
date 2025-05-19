import tkinter as tk
import webbrowser

def open_naver():
    webbrowser.open("https://www.naver.com")

def open_google():
    webbrowser.open("https://www.google.com")

root = tk.Tk()
root.title("사이트 이동 버튼")
root.geometry("200x100")  # 창 크기 지정

btn_naver = tk.Button(root, text="Naver", command=open_naver)
btn_naver.pack(pady=10)

btn_google = tk.Button(root, text="Google", command=open_google)
btn_google.pack(pady=10)

root.mainloop()