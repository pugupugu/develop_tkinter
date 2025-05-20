import tkinter as tk

def change_text():
    current = label.cget("text")
    if current == "여기에 텍스트가 표시됩니다.":
        label.config(text="텍스트가 변경되었습니다!")
    else:
        label.config(text="여기에 텍스트가 표시됩니다.")

root = tk.Tk()
root.title("동적 레이블 예제")
root.geometry("500x200")

label = tk.Label(root, text="여기에 텍스트가 표시됩니다.", font=("Helvetica", 24))
label.pack(pady=10)

button = tk.Button(root, text="텍스트 변경", command=change_text)
button.pack(pady=5)

root.mainloop()