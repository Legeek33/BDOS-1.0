import tkinter as tk
from tkinter import scrolledtext

class BDOSApp:
    def __init__(self, root):
        self.root = root
        self.root.title("BDOS")
        self.root.geometry("800x500")
        self.root.configure(bg="black")

        self.output = scrolledtext.ScrolledText(
            root, bg="black", fg="lime", insertbackground="lime",
            font=("Consolas", 12), wrap=tk.WORD
        )
        self.output.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

        self.entry = tk.Entry(
            root, bg="black", fg="lime", insertbackground="lime",
            font=("Consolas", 12)
        )
        self.entry.pack(fill=tk.X, padx=10, pady=(0, 10))
        self.entry.bind("<Return>", self.run_command)

        self.write("BDOS 1.0\nType 'help' for commands.\n")
        self.prompt()

    def write(self, text):
        self.output.insert(tk.END, text)
        self.output.see(tk.END)

    def prompt(self):
        self.write("C:\\> ")

    def run_command(self, event=None):
        cmd = self.entry.get().strip()
        self.entry.delete(0, tk.END)
        self.write(cmd + "\n")

        if cmd == "help":
            self.write("Commands: help, ver, clear, exit\n")
        elif cmd == "ver":
            self.write("BDOS 1.0 (C) Balenger Corp. 2026\n")
        elif cmd == "clear":
            self.output.delete("1.0", tk.END)
        elif cmd == "exit":
            self.root.destroy()
            return
        elif cmd:
            self.write("Unknown command.\n")

        self.prompt()

root = tk.Tk()
app = BDOSApp(root)
root.mainloop()
