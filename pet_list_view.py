import customtkinter as ctk
from utils import load_image

class PetListView(ctk.CTkFrame):
    """
    Displays a searchable and filterable list of pets for adoption.
    """
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        self.pets_data = []

        # Configure grid layout
        self.grid_rowconfigure(1, weight=1)
        self.grid_columnconfigure(0, weight=1)

        # --- Top Filter/Search Frame ---
        filter_frame = ctk.CTkFrame(self)
        filter_frame.grid(row=0, column=0, sticky="ew", padx=10, pady=10)

        search_entry = ctk.CTkEntry(filter_frame, placeholder_text="Search pets...")
        search_entry.pack(side="left", padx=10, pady=10, fill="x", expand=True)

        # --- Scrollable Pet Cards Frame ---
        self.scrollable_frame = ctk.CTkScrollableFrame(self, label_text="Available Pets")
        self.scrollable_frame.grid(row=1, column=0, sticky="nsew", padx=10, pady=10)

    def on_show(self):
        """Called when the frame is raised to the top."""
        self.load_pets()

    def load_pets(self):
        """Loads pet data and creates pet cards."""
        # Clear existing widgets
        for widget in self.scrollable_frame.winfo_children():
            widget.destroy()

        self.pets_data = self.controller.db_manager.get_pets()

        # Create pet cards in a grid
        row, col = 0, 0
        for i, pet in enumerate(self.pets_data):
            pet_info = {'id': pet[0], 'name': pet[1], 'breed': pet[2], 'age': pet[3], 'description': pet[4], 'image_path': pet[6]}
            card = self.create_pet_card(self.scrollable_frame, pet_info)
            card.grid(row=row, column=col, padx=10, pady=10, sticky="nsew")
            
            col += 1
            if col > 3: # 4 cards per row
                col = 0
                row += 1

    def create_pet_card(self, parent, pet_info):
        """Creates a single pet card widget."""
        card = ctk.CTkFrame(parent, corner_radius=10, border_width=1)

        img = load_image(pet_info['image_path'], size=(200, 150))
        img_label = ctk.CTkLabel(card, image=img, text="")
        img_label.pack(pady=(10, 5))

        name_label = ctk.CTkLabel(card, text=pet_info['name'], font=ctk.CTkFont(size=18, weight="bold"))
        name_label.pack(pady=5)

        breed_label = ctk.CTkLabel(card, text=f"{pet_info['breed']}, Age: {pet_info['age']}", text_color="gray")
        breed_label.pack(pady=5)

        adopt_button = ctk.CTkButton(card, text="Adopt Me",
                                     command=lambda p=pet_info: self.controller.start_adoption_flow(p))
        adopt_button.pack(pady=10, padx=10, fill="x")

        return card
