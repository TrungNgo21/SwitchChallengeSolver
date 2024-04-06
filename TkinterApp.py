import tkinter as tk

from SwitchSolver import SwitchSolver


class Application(tk.Tk):
    top_layer = []
    bottom_layer = []
    branches = []

    def __init__(self):
        super().__init__()

        self.title("Form Application")

        self.label_font = ("Helvetica", 24)
        self.entry_font = ("Helvetica", 24)
        self.button_font = ("Helvetica", 24)

        self.T_image = tk.PhotoImage(file="images/circle.png")
        self.V_image = tk.PhotoImage(file="images/square.png")
        self.TG_image = tk.PhotoImage(file="images/triangle.png")
        self.C_image = tk.PhotoImage(file="images/plus.png")


        self.initial_label = tk.Label(self, text="Initial:", font=self.label_font)
        self.initial_label.grid(row=0, column=0)
        self.initial_entry = tk.Entry(self, font=self.entry_font, width=40)
        self.initial_entry.grid(row=0, column=1)

        self.operator_label = tk.Label(self, text="Operators:", font=self.label_font)
        self.operator_label.grid(row=1, column=0)
        self.operator_entry = tk.Entry(self, font=self.entry_font, width=40)
        self.operator_entry.grid(row=1, column=1)

        self.result_label = tk.Label(self, text="Results:", font=self.label_font)
        self.result_label.grid(row=2, column=0)
        self.result_entry = tk.Entry(self, font=self.entry_font, width=40)
        self.result_entry.grid(row=2, column=1)

        self.combination_label = tk.Label(self, text="Combinations:", font=self.label_font)
        self.combination_label.grid(row=3, column=0)
        self.combination_entry = tk.Entry(self, font=self.entry_font, width=40)
        self.combination_entry.grid(row=3, column=1)

        self.T_button_initial = tk.Button(self, image=self.T_image,
                                          command=lambda: self.update_field(self.initial_entry, "T"))
        self.T_button_initial.grid(row=0, column=2)

        self.V_button_initial = tk.Button(self, image=self.V_image,
                                          command=lambda: self.update_field(self.initial_entry, "V"))
        self.V_button_initial.grid(row=0, column=3)

        self.TG_button_initial = tk.Button(self, image=self.TG_image,
                                           command=lambda: self.update_field(self.initial_entry, "TG"))
        self.TG_button_initial.grid(row=0, column=4)

        self.C_button_initial = tk.Button(self, image=self.C_image,
                                          command=lambda: self.update_field(self.initial_entry, "C"))
        self.C_button_initial.grid(row=0, column=5)

        self.C_button_initial = tk.Button(self, text="Reset", font=self.button_font,
                                          command=lambda: self.reset_field(self.initial_entry))
        self.C_button_initial.grid(row=0, column=6)

        self.T_button_result = tk.Button(self, image=self.T_image,
                                         command=lambda: self.update_field(self.result_entry, "T"))
        self.T_button_result.grid(row=2, column=2)

        self.V_button_result = tk.Button(self, image=self.V_image,
                                         command=lambda: self.update_field(self.result_entry, "V"))
        self.V_button_result.grid(row=2, column=3)

        self.TG_button_result = tk.Button(self, image=self.TG_image,
                                          command=lambda: self.update_field(self.result_entry, "TG"))
        self.TG_button_result.grid(row=2, column=4)

        self.C_button_result = tk.Button(self, image=self.C_image,
                                         command=lambda: self.update_field(self.result_entry, "C"))
        self.C_button_result.grid(row=2, column=5)

        self.C_button_initial = tk.Button(self, text="Reset", font=self.button_font,
                                          command=lambda: self.reset_field(self.result_entry))
        self.C_button_initial.grid(row=2, column=6)

        self.submit_button = tk.Button(self, text="Submit", font=self.button_font, command=self.submit_form)
        self.submit_button.grid(row=4, column=0)

        self.reset_button = tk.Button(self, text="Reset", font=self.button_font, command=self.reset_form)
        self.reset_button.grid(row=4, column=1)

    def update_field(self, entry, value):
        current_value = entry.get().strip()
        if current_value:
            values = current_value.split()
            if value not in values:
                entry.insert(tk.END, " " + value)
        else:
            entry.insert(tk.END, value)

    def submit_form(self):
        initial = self.initial_entry.get()
        self.top_layer = initial.strip().split(" ")
        print(self.top_layer)
        operators = self.operator_entry.get()
        self.branches = self.create_branches_lst(operators.strip())
        print(self.branches)

        results = self.result_entry.get()
        self.bottom_layer = results.strip().split(" ")
        print(self.bottom_layer)

        solver = SwitchSolver(self.branches, self.top_layer, self.bottom_layer)
        combine = solver.choose_branch()
        combine_result = ', '.join(str(x) for x in combine)
        self.combination_entry.delete(0, tk.END)
        self.combination_entry.insert(tk.END, combine_result)
        print("Form submitted:")
        print(f"Initial: {initial}")
        print(f"Operators: {operators}")
        print(f"Results: {results}")
        print(f"Combinations: {combine}")

    def reset_form(self):
        self.initial_entry.delete(0, tk.END)
        self.operator_entry.delete(0, tk.END)
        self.result_entry.delete(0, tk.END)
        self.combination_entry.delete(0, tk.END)

    def reset_field(self, entry):
        entry.delete(0, tk.END)

    def create_branches_lst(self, branches_str):
        branches_str_lst = branches_str.split(" ")
        for index, branche_str in enumerate(branches_str_lst):
            int_list = [int(x) for x in branche_str.split("-")]
            branches_str_lst[index] = int_list
        return branches_str_lst


if __name__ == "__main__":
    app = Application()
    app.mainloop()
