import tkinter as tk


class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.timer_label = tk.Label(self, text="0")
        self.timer_label.pack(side="top")

        self.start_button = tk.Button(self)
        self.start_button["text"] = "Start"
        self.start_button["command"] = self.start_timer
        self.start_button.pack(side="left")

        self.stop_button = tk.Button(self)
        self.stop_button["text"] = "Stop"
        self.stop_button["command"] = self.stop_timer
        self.stop_button.pack(side="right")

    def start_timer(self):
        self.timer_label.after(1000, self.update_timer)

    def stop_timer(self):
        self.timer_label.after_cancel(self.update_timer)

    def update_timer(self):
        current_time = int(self.timer_label["text"])
        current_time += 1
        self.timer_label["text"] = str(current_time)
        self.timer_label.after(1000, self.update_timer)

if __name__ == '__main__':
    # root = tk.Tk()
    # app = Application(master=root)
    # app.mainloop()
    root = tk.Tk()  # create root window
    root.title("Taps To Case")  # title of the GUI window
    root.maxsize(1280, 720)  # specify the max size the window can expand to
    root.config(bg="skyblue")  # specify background color

    # Create left and right frames
    left_frame = tk.Frame(root, width=200, height=400, bg='grey')
    left_frame.grid(row=0, column=0, padx=10, pady=5)

    right_frame = tk.Frame(root, width=650, height=400, bg='grey')
    right_frame.grid(row=0, column=1, padx=10, pady=5)

    # Create frames and labels in left_frame
    tk.Label(left_frame, text="Original Image").grid(row=0, column=0, padx=5, pady=5)

    # load image to be "edited"
    image = tk.PhotoImage(file="C:/r/TapsToCase/app/Photo.png")
    image_sub1 = image.subsample(16, 16)  # resize image using subsample
    image_sub2 = image.subsample(4, 4)  # resize image using subsample

    tk.Label(left_frame, image=image_sub1).grid(row=1, column=0, padx=5, pady=5)

    # Display image in right_frame
    tk.Label(right_frame, image=image_sub2).grid(row=0,column=0, padx=5, pady=5)

    # Create tool bar frame
    tool_bar = tk.Frame(left_frame, width=180, height=185)
    tool_bar.grid(row=2, column=0, padx=5, pady=5)

    # Example labels that serve as placeholders for other widgets
    tk.Label(tool_bar, text="Tools", relief=tk.RAISED).grid(row=0, column=0, padx=5, pady=3, ipadx=10)  # ipadx is padding inside the Label widget
    tk.Label(tool_bar, text="Filters", relief=tk.RAISED).grid(row=0, column=1, padx=5, pady=3, ipadx=10)

    # Example labels that could be displayed under the "Tool" menu
    tk.Label(tool_bar, text="Select").grid(row=1, column=0, padx=5, pady=5)
    tk.Label(tool_bar, text="Crop").grid(row=2, column=0, padx=5, pady=5)
    tk.Label(tool_bar, text="Rotate & Flip").grid(row=3, column=0, padx=5, pady=5)
    tk.Label(tool_bar, text="Resize").grid(row=4, column=0, padx=5, pady=5)
    tk.Label(tool_bar, text="Exposure").grid(row=5, column=0, padx=5, pady=5)
    root.mainloop()
