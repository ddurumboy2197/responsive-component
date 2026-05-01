import tkinter as tk

class ResponsiveComponent:
    def __init__(self, master):
        self.master = master
        self.frame = tk.Frame(self.master)
        self.frame.pack(fill="both", expand=True)

        self.label = tk.Label(self.frame, text="Responsive Label")
        self.label.pack(fill="x")

        self.button = tk.Button(self.frame, text="Responsive Button")
        self.button.pack(fill="x")

        self.entry = tk.Entry(self.frame)
        self.entry.pack(fill="x")

        self.scrollbar = tk.Scrollbar(self.frame)
        self.scrollbar.pack(side="right", fill="y")

        self.text_area = tk.Text(self.frame, yscrollcommand=self.scrollbar.set)
        self.text_area.pack(side="left", fill="both", expand=True)

        self.scrollbar.config(command=self.text_area.yview)

    def make_responsive(self):
        self.frame.grid_columnconfigure(0, weight=1)
        self.frame.grid_columnconfigure(1, weight=0)
        self.frame.grid_rowconfigure(0, weight=1)

        self.label.grid(row=0, column=0, sticky="nsew")
        self.button.grid(row=1, column=0, sticky="ew")
        self.entry.grid(row=2, column=0, sticky="ew")
        self.text_area.grid(row=3, column=0, sticky="nsew")
        self.scrollbar.grid(row=3, column=1, sticky="ns")

root = tk.Tk()
component = ResponsiveComponent(root)
component.make_responsive()
root.mainloop()
