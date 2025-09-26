import customtkinter as ctk
from models import DatabaseManager
from controllers import Controller

# Import all view classes
from views.home_view import HomeView
from views.pet_list_view import PetListView
from views.service_list_view import ServiceListView
from views.settings_view import SettingsView
from views.adoption_flow import AdoptionFlowView
from views.booking_flow import BookingFlowView


class App(ctk.CTk):
    """
    Main application window for OnlyPets.
    """
    def __init__(self):
        super().__init__()

        self.db_manager = DatabaseManager()
        self.db_manager.init_db()

        self.title("OnlyPets")
        self.geometry("1280x800")
        self.minsize(960, 720)

        ctk.set_appearance_mode("Dark")
        ctk.set_default_color_theme("blue")

        self.controller = Controller(self)

        # --- Main Layout ---
        self.grid_rowconfigure(1, weight=1)
        self.grid_columnconfigure(0, weight=1)

        # --- Header / Navigation Frame ---
        self.header_frame = ctk.CTkFrame(self, height=60, corner_radius=0, fg_color=("#F0F0F0", "#1E1E1E"))
        self.header_frame.grid(row=0, column=0, sticky="ew", padx=10, pady=10)

        app_title = ctk.CTkLabel(self.header_frame, text="OnlyPets", font=ctk.CTkFont(size=24, weight="bold"), text_color="#F26B38")
        app_title.pack(side="left", padx=20)

        nav_buttons = {
            "Home": "HomeView",
            "Adopt Pets": "PetListView",
            "Book Services": "ServiceListView",
            "Settings": "SettingsView"
        }

        for text, frame_name in nav_buttons.items():
            button = ctk.CTkButton(self.header_frame, text=text,
                                   command=lambda fn=frame_name: self.controller.show_frame(fn),
                                   fg_color="transparent",
                                   hover_color=("#D3D3D3", "#333333"),
                                   font=ctk.CTkFont(size=14))
            button.pack(side="left", padx=10)

        # --- Container for view frames ---
        container = ctk.CTkFrame(self, fg_color="transparent")
        container.grid(row=1, column=0, sticky="nsew", padx=10, pady=(0, 10))
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        # Initialize all frames
        view_classes = (HomeView, PetListView, ServiceListView, SettingsView, AdoptionFlowView, BookingFlowView)
        for F in view_classes:
            page_name = F.__name__
            frame = F(parent=container, controller=self.controller)
            self.frames[page_name] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.controller.show_frame("HomeView")


if __name__ == "__main__":
    app = App()
    app.mainloop()

