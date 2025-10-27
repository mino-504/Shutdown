import os
import tkinter as tk
from tkinter import messagebox

version = "v0.1"

def shutdown_in(hours):
    seconds = hours * 3600
    os.system(f"shutdown /s /f /t {seconds}")
    messagebox.showinfo("예약 완료", f"{hours}시간 후에 컴퓨터가 자동으로 종료됩니다.")

def cancel_shutdown():
    os.system("shutdown /a")
    messagebox.showinfo("취소 완료", "예약된 종료가 취소되었습니다.")

# GUI 설정
root = tk.Tk()
root.title("자동 종료 타이머")
root.geometry("300x250")

tk.Label(root, text="자동 종료 타이머", font=("맑은 고딕", 14, "bold")).pack(pady=10)

frame = tk.Frame(root)
frame.pack(pady=5)

tk.Button(frame, text="1시간 뒤 종료", command=lambda: shutdown_in(1), width=15).grid(row=0, column=0, padx=5, pady=5)
tk.Button(frame, text="2시간 뒤 종료", command=lambda: shutdown_in(2), width=15).grid(row=1, column=0, padx=5, pady=5)
tk.Button(frame, text="3시간 뒤 종료", command=lambda: shutdown_in(3), width=15).grid(row=2, column=0, padx=5, pady=5)
tk.Button(frame, text="취소하기", command=cancel_shutdown, width=15, fg="red").grid(row=3, column=0, padx=5, pady=15)

root.mainloop()
