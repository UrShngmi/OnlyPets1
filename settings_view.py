import customtkinter as ctk

class SettingsView(ctk.CTkFrame):
    """
    Application settings page.
    """
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller

        self.grid_columnconfigure(0, weight=1)

        title = ctk.CTkLabel(self, text="Settings", font=ctk.CTkFont(size=24, weight="bold"))
        title.grid(row=0, column=0, padx=20, pady=20, sticky="w")

        # --- Theme Setting ---
        theme_frame = ctk.CTkFrame(self)
        theme_frame.grid(row=1, column=0, padx=20, pady=10, sticky="ew")
        
        theme_label = ctk.CTkLabel(theme_frame, text="Appearance Mode:")
        theme_label.pack(side="left", padx=10, pady=10)

        self.theme_menu = ctk.CTkOptionMenu(theme_frame, values=["Dark", "Light", "System"],
                                            command=self.change_appearance_mode)
        self.theme_menu.pack(side="left", padx=10, pady=10)
        self.theme_menu.set(ctk.get_appearance_mode())

        # --- Clear Cache Setting ---
        cache_frame = ctk.CTkFrame(self)
        cache_frame.grid(row=2, column=0, padx=20, pady=10, sticky="ew")

        cache_label = ctk.CTkLabel(cache_frame, text="Clear local data (e.g., guest wishlist).")
        cache_label.pack(side="left", padx=10, pady=10)
        
        clear_cache_button = ctk.CTkButton(cache_frame, text="Clear Cache", command=self.clear_cache)
        clear_cache_button.pack(side="left", padx=10, pady=10)


    def change_appearance_mode(self, new_mode: str):
        """Changes the application's appearance mode."""
        ctk.set_appearance_mode(new_mode)

    def clear_cache(self):
        """Placeholder for cache clearing logic."""
        print("Cache clearing functionality would be implemented here.")
        # Example: os.remove('data/wishlist.json')
