from views.auth_dialog import AuthDialog

class Controller:
    """
    Handles navigation, authentication, and application state.
    """
    def __init__(self, app):
        self.app = app
        self.db_manager = app.db_manager
        self.current_user = None

    def show_frame(self, page_name):
        """
        Shows a frame for the given page name.
        """
        frame = self.app.frames[page_name]
        # Refresh data if the view has a refresh method
        if hasattr(frame, 'on_show'):
            frame.on_show()
        frame.tkraise()

    def show_auth_dialog(self):
        """
        Displays the authentication dialog.
        """
        # The dialog will handle its own logic and call controller.login/signup
        AuthDialog(self.app, self)

    def login(self, username, password):
        """
        Handles the login logic. Returns True on success, False on failure.
        """
        if self.db_manager.verify_user(username, password):
            self.current_user = username
            print(f"User '{self.current_user}' logged in.")
            return True
        print(f"Failed login attempt for user '{username}'.")
        return False

    def signup(self, username, password):
        """
        Handles the signup logic. Returns True on success, False if user exists.
        """
        if self.db_manager.add_user(username, password):
            print(f"User '{username}' created successfully.")
            return True
        print(f"Signup failed: Username '{username}' already exists.")
        return False

    def logout(self):
        """
        Logs the current user out.
        """
        print(f"User '{self.current_user}' logged out.")
        self.current_user = None

    def start_adoption_flow(self, pet_info):
        """
        Starts the adoption process for a specific pet.
        """
        if not self.current_user:
            self.show_auth_dialog()
            return

        print(f"Starting adoption flow for {pet_info['name']} for user {self.current_user}")
        adoption_view = self.app.frames["AdoptionFlowView"]
        adoption_view.set_pet_info(pet_info)
        self.show_frame("AdoptionFlowView")

    def start_booking_flow(self, service_info):
        """
        Starts the booking process for a specific service.
        """
        if not self.current_user:
            self.show_auth_dialog()
            return
            
        print(f"Starting booking flow for {service_info['name']} for user {self.current_user}")
        booking_view = self.app.frames["BookingFlowView"]
        booking_view.set_service_info(service_info)
        self.show_frame("BookingFlowView")

