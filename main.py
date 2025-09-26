import customtkinter as ctk
from views.home_view import HomeView
from models import DatabaseManager
from controllers import Controller

class App(ctk.CTk):
    """
    Main application window for OnlyPets.
    """
    def __init__(self):
        super().__init__()

        # Initialize the database
        self.db_manager = DatabaseManager()
        self.db_manager.init_db()

        self.title("OnlyPets")
        self.geometry("1200x800")
        self.minsize(800, 600)

        # Set the theme
        ctk.set_appearance_mode("Dark")
        ctk.set_default_color_theme("blue")

        # Initialize the controller
        self.controller = Controller(self)

        # Create a container for frames
        container = ctk.CTkFrame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        # Initialize frames
        for F in (HomeView,): # Add other views here later
            page_name = F.__name__
            frame = F(parent=container, controller=self.controller)
            self.frames[page_name] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.controller.show_frame("HomeView")

if __name__ == "__main__":
    app = App()
    app.mainloop()
