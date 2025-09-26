import customtkinter as ctk

class AdoptionFlowView(ctk.CTkFrame):
    """
    A multi-step form for the pet adoption process.
    """
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        self.pet_info = None

        self.label = ctk.CTkLabel(self, text="Adoption Flow", font=ctk.CTkFont(size=24, weight="bold"))
        self.label.pack(pady=20, padx=20)
        
        self.info_label = ctk.CTkLabel(self, text="", font=ctk.CTkFont(size=16))
        self.info_label.pack(pady=10)
        
        # Placeholder for form fields
        form_frame = ctk.CTkFrame(self)
        form_frame.pack(pady=20, padx=20, fill="x")

        ctk.CTkLabel(form_frame, text="Full Name:").pack(anchor="w", padx=10)
        ctk.CTkEntry(form_frame).pack(fill="x", padx=10, pady=5)
        
        ctk.CTkLabel(form_frame, text="Address:").pack(anchor="w", padx=10, pady=(10,0))
        ctk.CTkEntry(form_frame).pack(fill="x", padx=10, pady=5)

        submit_button = ctk.CTkButton(self, text="Submit Application")
        submit_button.pack(pady=20)


    def set_pet_info(self, pet_info):
        """Receives pet info when the flow starts."""
        self.pet_info = pet_info
        self.info_label.configure(text=f"Adoption Application for: {self.pet_info['name']}")
