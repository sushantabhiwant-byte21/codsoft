import customtkinter as ctk
from task_manager import TaskManager

class ToDoApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("To-Do List")
        self.geometry("500x600")
        self.minsize(400, 500)
        
        # Configure appearance
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("blue")

        self.task_manager = TaskManager()

        self.setup_ui()
        self.load_tasks_to_ui()

    def setup_ui(self):
        # Configure grid layout
        self.grid_rowconfigure(1, weight=1)
        self.grid_columnconfigure(0, weight=1)

        # Title Label
        self.title_label = ctk.CTkLabel(self, text="My Tasks", font=ctk.CTkFont(size=24, weight="bold"))
        self.title_label.grid(row=0, column=0, padx=20, pady=(20, 10), sticky="w")

        # Scrollable Frame for Tasks
        self.tasks_frame = ctk.CTkScrollableFrame(self)
        self.tasks_frame.grid(row=1, column=0, padx=20, pady=10, sticky="nsew")
        
        # This dictionary will hold the UI elements for each task so we can interact with them
        self.task_widgets = {}

        # Input Area Frame
        self.input_frame = ctk.CTkFrame(self)
        self.input_frame.grid(row=2, column=0, padx=20, pady=(10, 20), sticky="ew")
        self.input_frame.grid_columnconfigure(0, weight=1)

        self.task_entry = ctk.CTkEntry(self.input_frame, placeholder_text="Enter a new task...")
        self.task_entry.grid(row=0, column=0, padx=(10, 10), pady=10, sticky="ew")
        self.task_entry.bind("<Return>", lambda event: self.add_task())

        self.add_btn = ctk.CTkButton(self.input_frame, text="Add Task", width=100, command=self.add_task)
        self.add_btn.grid(row=0, column=1, padx=(0, 10), pady=10)

    def load_tasks_to_ui(self):
        # Clear existing widgets
        for widgets in self.task_widgets.values():
            for widget in widgets.values():
                widget.destroy()
        self.task_widgets.clear()

        # Load from manager
        tasks = self.task_manager.get_tasks()
        for task in tasks:
            self.create_task_widget(task)

    def create_task_widget(self, task):
        task_id = task["id"]
        
        # Frame for individual task
        task_frame = ctk.CTkFrame(self.tasks_frame, fg_color="transparent")
        task_frame.pack(fill="x", pady=5)
        task_frame.grid_columnconfigure(1, weight=1)

        # Checkbox
        checkbox_var = ctk.BooleanVar(value=task["completed"])
        checkbox = ctk.CTkCheckBox(
            task_frame, 
            text="", 
            variable=checkbox_var, 
            width=20,
            command=lambda: self.toggle_task(task_id, checkbox_var.get())
        )
        checkbox.grid(row=0, column=0, padx=(0, 10), pady=5)

        # Task Description Label
        font_kwargs = {"size": 14}
        if task["completed"]:
            font_kwargs["overstrike"] = True
            text_color = "gray"
        else:
            text_color = "white"
            
        desc_label = ctk.CTkLabel(
            task_frame, 
            text=task["description"], 
            font=ctk.CTkFont(**font_kwargs),
            text_color=text_color,
            anchor="w"
        )
        desc_label.grid(row=0, column=1, sticky="ew", pady=5)

        # Delete Button
        delete_btn = ctk.CTkButton(
            task_frame, 
            text="×", 
            width=30, 
            fg_color="#ff5555", 
            hover_color="#ff3333",
            command=lambda: self.delete_task(task_id)
        )
        delete_btn.grid(row=0, column=2, padx=(10, 0), pady=5)

        self.task_widgets[task_id] = {
            "frame": task_frame,
            "checkbox": checkbox,
            "label": desc_label,
            "delete_btn": delete_btn
        }

    def add_task(self):
        description = self.task_entry.get().strip()
        if description:
            task = self.task_manager.add_task(description)
            self.create_task_widget(task)
            self.task_entry.delete(0, 'end')

    def toggle_task(self, task_id, is_completed):
        self.task_manager.update_task_status(task_id, is_completed)
        self.load_tasks_to_ui()  # Reload to apply strikethrough/color changes

    def delete_task(self, task_id):
        self.task_manager.delete_task(task_id)
        if task_id in self.task_widgets:
            widgets = self.task_widgets.pop(task_id)
            widgets["frame"].destroy()

if __name__ == "__main__":
    app = ToDoApp()
    app.mainloop()
