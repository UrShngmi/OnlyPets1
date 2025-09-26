import customtkinter as ctk
from tkcalendar import Calendar

class BookingFlowView(ctk.CTkFrame):
    """
    A multi-step form for booking a service.
    """
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        self.service_info = None

        self.label = ctk.CTkLabel(self, text="Service Booking", font=ctk.CTkFont(size=24, weight="bold"))
        self.label.pack(pady=20, padx=20)
        
        self.info_label = ctk.CTkLabel(self, text="", font=ctk.CTkFont(size=16))
        self.info_label.pack(pady=10)

        # Placeholder for calendar and form
        # Note: tkcalendar is not a customtkinter widget, so its styling might differ.
        # A custom-styled calendar would be a larger project.
        cal = Calendar(self, selectmode='day', year=2025, month=9, day=26)
        cal.pack(pady=20)
        
        submit_button = ctk.CTkButton(self, text="Confirm Booking")
        submit_button.pack(pady=20)

    def set_service_info(self, service_info):
        """Receives service info when the flow starts."""
        self.service_info = service_info
        self.info_label.configure(text=f"Booking: {self.service_info['name']} for ${self.service_info['price']:.2f}")
