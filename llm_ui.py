import tkinter as tk
from tkinter import ttk, StringVar

class LlmUi:
    def __init__(self, title: str = "LLM - Tester") -> None:
        self.root = tk.Tk()
        self.root.title(title)
        self.root.geometry("500x500")
        self.text_entry = self.create_text_entry()

    def create_text_entry(self) -> ttk.Entry:
        text_entry = ttk.Entry(self.root, width=30)
        text_entry.grid(column=2, row=1, sticky=(tk.W, tk.E))
        text_entry.focus()
        return text_entry

    def set_process_button(self) -> None:
        ttk.Button(self.root, text="Process", command=self.process_text).grid(column=2, row=2, sticky=tk.W)

    def set_labels(self) -> None:
        ttk.Label(self.root, text="Text").grid(column=1, row=1, sticky=tk.W)
        ttk.Label(self.root, text="Result").grid(column=1, row=3, sticky=tk.W)

    def set_padding(self) -> None:
        for child in self.root.winfo_children():
            child.grid_configure(padx=5, pady=5)

    def set_binding(self) -> None:
        self.root.bind('<Return>', self.process_text)

    def process_text(self, *args) -> None:
        text = str(self.text_entry.get())

        #insert text into text widget
        text_widget = self.root.grid_slaves(row=60, column=2)[0]
        text_widget.configure(state='normal')
        text_widget.delete("1.0", tk.END)
        text_widget.insert(tk.END, text)
        text_widget.configure(state='disabled')

    
    def set_text_widget(self) -> None:
        text_widget = tk.Text(self.root, width=30, height=60, state='disabled')
        text_widget.grid(column=2, row=60, sticky=(tk.W, tk.E))
        text_widget.bind("<2>", lambda event: text_widget.focus_set())
        # add scrollbar to text widget
        scrollbar = ttk.Scrollbar(self.root, orient=tk.VERTICAL, command=text_widget.yview)
        scrollbar.grid(column=3, row=60, sticky=(tk.N, tk.S))
        text_widget['yscrollcommand'] = scrollbar.set


    def setup_ui(self) -> None:
        #self.set_result_label()
        self.set_process_button()
        self.set_labels()
        self.set_padding()
        self.set_binding()
        self.set_text_widget()


        self.root.rowconfigure(60, weight=1)
        self.root.columnconfigure(2, weight=1)
        self.root.mainloop()
    
    def run(self) -> None:
        self.setup_ui()

if __name__ == "__main__":
    ui = LlmUi()
    ui.run()