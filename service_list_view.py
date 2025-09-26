import customtkinter as ctk
from utils import load_image

class ServiceListView(ctk.CTkFrame):
    """
    Displays a list of available pet services.
    """
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        self.services_data = []

        self.grid_rowconfigure(1, weight=1)
        self.grid_columnconfigure(0, weight=1)

        # --- Top Filter/Search Frame ---
        filter_frame = ctk.CTkFrame(self)
        filter_frame.grid(row=0, column=0, sticky="ew", padx=10, pady=10)

        search_entry = ctk.CTkEntry(filter_frame, placeholder_text="Search services...")
        search_entry.pack(side="left", padx=10, pady=10, fill="x", expand=True)

        # --- Scrollable Service Cards Frame ---
        self.scrollable_frame = ctk.CTkScrollableFrame(self, label_text="Our Services")
        self.scrollable_frame.grid(row=1, column=0, sticky="nsew", padx=10, pady=10)

    def on_show(self):
        self.load_services()

    def load_services(self):
        for widget in self.scrollable_frame.winfo_children():
            widget.destroy()

        self.services_data = self.controller.db_manager.get_services()

        row, col = 0, 0
        for i, service in enumerate(self.services_data):
            service_info = {'id': service[0], 'name': service[1], 'description': service[2], 'price': service[3], 'image_path': service[4]}
            card = self.create_service_card(self.scrollable_frame, service_info)
            card.grid(row=row, column=col, padx=10, pady=10, sticky="nsew")

            col += 1
            if col > 3:
                col = 0
                row += 1

    def create_service_card(self, parent, service_info):
        card = ctk.CTkFrame(parent, corner_radius=10, border_width=1)

        img = load_image(service_info['image_path'], size=(200, 150))
        img_label = ctk.CTkLabel(card, image=img, text="")
        img_label.pack(pady=(10, 5))

        name_label = ctk.CTkLabel(card, text=service_info['name'], font=ctk.CTkFont(size=18, weight="bold"))
        name_label.pack(pady=5)

        price_label = ctk.CTkLabel(card, text=f"${service_info['price']:.2f}", text_color="gray", font=ctk.CTkFont(size=14))
        price_label.pack(pady=5)

        book_button = ctk.CTkButton(card, text="Book Now",
                                    command=lambda s=service_info: self.controller.start_booking_flow(s))
        book_button.pack(pady=10, padx=10, fill="x")

        return card
