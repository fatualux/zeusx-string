import tkinter as tk
from tkinter import ttk, messagebox


class AbsenceRequestApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Absence Request String")

        self.create_widgets()

    def create_widgets(self):
        tk.Label(self.root, text="How many hours?").grid(
            row=1, column=0, padx=(10, 0), pady=(10, 0))
        self.hours_entry = tk.Entry(self.root)
        self.hours_entry.grid(row=2, column=0, padx=(10, 0), pady=(10, 0))

        tk.Label(self.root, text="How many minutes?").grid(
            row=1, column=1, pady=(10, 0))
        self.minutes_entry = tk.Entry(self.root)
        self.minutes_entry.grid(row=2, column=1, pady=(10, 0))

        tk.Label(self.root, text="Start time:").grid(
            row=3, column=0, padx=(20), pady=(20, 0))
        tk.Label(self.root, text="Hours").grid(
            row=4, column=0, pady=(5, 0))
        self.start_hour_entry = tk.Entry(self.root)
        self.start_hour_entry.grid(row=5, column=0, pady=(5, 0))
        tk.Label(self.root, text="Minutes").grid(
            row=4, column=1, pady=(5, 0))
        self.start_minute_entry = tk.Entry(self.root)
        self.start_minute_entry.grid(row=5, column=1, pady=(5, 0))

        tk.Label(self.root, text="End time:").grid(
            row=6, column=0, pady=(20, 0))
        tk.Label(self.root, text="Hours").grid(
            row=7, column=0, pady=(5, 0))
        self.end_hour_entry = tk.Entry(self.root)
        self.end_hour_entry.grid(row=8, column=0, pady=(5, 20))
        tk.Label(self.root, text="Minutes").grid(
            row=7, column=1, pady=(5, 0))
        self.end_minute_entry = tk.Entry(self.root)
        self.end_minute_entry.grid(row=8, column=1, pady=(5, 20))

        tk.Label(self.root, text="Category").grid(
            row=9, column=0, pady=(30, 0))
        self.category_var = tk.StringVar()
        self.category_menu = ttk.Combobox(
            self.root, textvariable=self.category_var, state="readonly")
        self.category_menu['values'] = ["AVA", "PAR", "PK", "PP"]
        self.category_menu.grid(row=9, column=1, padx=(0, 10), pady=(30, 0))
        self.category_menu.bind("<<ComboboxSelected>>",
                                self.update_subcategories)

        tk.Label(self.root, text="Subcategory").grid(
            row=10, column=0, pady=(10, 30))
        self.subcategory_var = tk.StringVar()
        self.subcategory_menu = ttk.Combobox(
            self.root, textvariable=self.subcategory_var, state="readonly")
        self.subcategory_menu.grid(
            row=10, column=1, padx=(0, 10), pady=(10, 30))

        self.result_label = tk.Label(
            self.root,
            text="Waiting for completion...",
            bg="#DDEEDD",
            wraplength=400)
        self.result_label.grid(row=11, column=0, columnspan=2, pady=(5, 10))

        self.copy_button = tk.Button(
            self.root,
            text="Copy to clipboard",
            command=self.copy_to_clipboard)
        self.copy_button.grid(
            row=12, column=0, columnspan=4, padx=(0, 10), pady=(10, 30))

    def update_subcategories(self, _):
        category = self.category_var.get()
        subcategories = {
            "AVA": [
                "FERIE (Terziario -Metalmeccanico)",
                "PERMESSI ROL (Terziario)",
                "PERMESSI EX FESTIVITA' (Terziario)",
                "PERMESSI PAR (Metalmeccanico)"
            ],
            "PAR": [
                "CONGEDO OBBLIGATORIO PADRE_N GIORNO_CF FIGLIO",
                "CONGEDO PARENTALE_CF FIGLIO"
            ],
            "PK": [
                "PERMESSO 104_CF ASSISTITO"
            ],
            "PP": ["PERMESSO ESAME",
                   "PERMESSO STUDIO N ORE TOTALE ORE UTILIZZATE"
                   ]
        }
        self.subcategory_menu['values'] = subcategories.get(category, [])
        self.subcategory_menu.set('')

    def copy_to_clipboard(self):
        start_time = (
            f"{self.start_hour_entry.get()}:{self.start_minute_entry.get()}"
        )
        end_time = (
            f"{self.end_hour_entry.get()}:{self.end_minute_entry.get()}"
        )
        category = self.category_var.get()
        subcategory = self.subcategory_var.get()
        hours = self.hours_entry.get()
        minutes = self.minutes_entry.get()
        hours_start = self.start_hour_entry.get()
        minutes_start = self.start_minute_entry.get()
        hours_end = self.end_hour_entry.get()
        minutes_end = self.end_minute_entry.get()

        if not all([
            hours,
            minutes,
            hours_start,
            minutes_start,
            hours_end,
            minutes_end
        ]):
            messagebox.showwarning(
                "Input Error", "All fields must be filled out.")
            return

        try:
            int(hours)
            int(minutes)
            int(hours_start)
            int(minutes_start)
            int(hours_end)
            int(minutes_end)

            start_minutes = (int(hours_start) * 60) + int(minutes_start)
            end_minutes = (int(hours_end) * 60) + int(minutes_end)
            interval = f"{hours},{minutes}"

            if start_minutes < 0 \
                or end_minutes >= 24*60 \
                    or end_minutes <= start_minutes:
                messagebox.showwarning(
                    "Time Error", "Invalid time values.")
                return

            if int(hours) <= 0 or int(hours) > 8:
                messagebox.showwarning(
                    "Interval Error", "Invalid interval.")
                return

            if int(minutes) < 0 or int(minutes) >= 60:
                messagebox.showwarning(
                    "Interval Error", "Invalid interval.")
                return

        except ValueError:
            messagebox.showwarning(
                "Input Error", "All fields must be numbers.")
            return

        result = (
            f"{interval} ore - "
            f"{category} - {subcategory} - "
            f"{start_time}-{end_time}"
        )

        self.root.clipboard_clear()
        self.root.clipboard_append(result)

        self.result_label.config(text=result, bg="#00FF00")


if __name__ == "__main__":
    root = tk.Tk()
    app = AbsenceRequestApp(root)
    root.mainloop()
