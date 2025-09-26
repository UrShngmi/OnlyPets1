class Controller:
    """
    Handles navigation, authentication, and application state.
    """
    def __init__(self, app):
        self.app = app
        self.user = None # To store logged-in user info

    def show_frame(self, page_name):
        """
        Shows a frame for the given page name.
        """
        frame = self.app.frames[page_name]
        frame.tkraise()

    def login(self, username, password):
        """
        Handles the login logic.
        """
        if self.app.db_manager.verify_user(username, password):
            self.user = username
            print(f"User {self.user} logged in.")
            # Here you would typically navigate to a user-specific dashboard
            self.show_frame("HomeView") # For now, just go home
            return True
        return False

    def signup(self, username, password):
        """
        Handles the signup logic.
        """
        if self.app.db_manager.add_user(username, password):
            print(f"User {username} created.")
            return True
        return False

    def logout(self):
        """
        Logs the current user out.
        """
        print(f"User {self.user} logged out.")
        self.user = None
