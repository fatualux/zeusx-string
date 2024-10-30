import tkinter as tk
from tkinter import ttk
from tkinter import messagebox


class AbsenceRequestApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Absence Request")

        self.create_widgets()

    def create_widgets(self):
        tk.Label(self.root, text="How many hours?").grid(
            row=0, column=0, pady=(10, 0))
        self.hours_entry = tk.Entry(self.root)
        self.hours_entry.grid(row=0, column=1, pady=(10, 0))

        tk.Label(self.root, text="Interval?").grid(
            row=1, column=0, pady=(10, 0))
        self.start_time_entry = tk.Entry(self.root)
        self.start_time_entry.grid(row=1, column=1, pady=(10, 0))
        self.end_time_entry = tk.Entry(self.root)
        self.end_time_entry.grid(row=1, column=2, pady=(10, 0))

        tk.Label(self.root, text="Category").grid(
            row=2, column=0, pady=(10, 0))
        self.category_var = tk.StringVar()
        self.category_menu = ttk.Combobox(
            self.root, textvariable=self.category_var, state="readonly")
        self.category_menu['values'] = ["AVA", "PAR", "PK", "PP"]
        self.category_menu.grid(row=2, column=1, pady=(10, 0))
        self.category_menu.bind("<<ComboboxSelected>>",
                                self.update_subcategories)

        tk.Label(self.root, text="Subcategory").grid(
            row=3, column=0, pady=(10, 0))
        self.subcategory_var = tk.StringVar()
        self.subcategory_menu = ttk.Combobox(
            self.root, textvariable=self.subcategory_var, state="readonly")
        self.subcategory_menu.grid(row=3, column=1, pady=(10, 0))

        self.copy_button = tk.Button(
            self.root, text="Copy to clipboard", command=self.copy_to_clipboard)
        self.copy_button.grid(row=4, column=0, columnspan=3, pady=(10, 10))

    def update_subcategories(self, event):
        category = self.category_var.get()
        subcategories = {
            "AVA": ["FERIE (Terziario -Metalmeccanico)", "PERMESSI ROL (Terziario)", "PERMESSI EX FESTIVITA' (Terziario)", "PERMESSI PAR (Metalmeccanico)"],
            "PAR": ["CONGEDO OBBLIGATORIO PADRE_N GIORNO_CF FIGLIO", "CONGEDO PARENTALE_CF FIGLIO"],
            "PK": ["PERMESSO 104_CF ASSISTITO"],
            "PP": ["PERMESSO ESAME", "PERMESSO STUDIO N ORE TOTALE ORE UTILIZZATE"]
        }
        self.subcategory_menu['values'] = subcategories.get(category, [])
        self.subcategory_menu.set('')

    def copy_to_clipboard(self):
        hours = self.hours_entry.get()
        start_time = self.start_time_entry.get()
        end_time = self.end_time_entry.get()
        category = self.category_var.get()
        subcategory = self.subcategory_var.get()

        if not all([hours, start_time, end_time, category, subcategory]):
            messagebox.showwarning(
                "Input Error", "All fields must be filled out.")
            return

        result = f"{hours} ore - {category} - {subcategory} - {start_time}-{end_time}"
        self.root.clipboard_clear()
        self.root.clipboard_append(result)
        messagebox.showinfo("Success", "Text copied to clipboard!")


if __name__ == "__main__":
    root = tk.Tk()
    app = AbsenceRequestApp(root)
    root.mainloop()
