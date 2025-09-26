import customtkinter as ctk

class AuthDialog(ctk.CTkToplevel):
    """
    A modal dialog for user login and signup.
    """
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller

        self.title("Login or Signup")
        self.geometry("400x450")
        self.transient(parent) # Keep on top of the main window
        self.grab_set() # Modal behavior

        self.tab_view = ctk.CTkTabview(self)
        self.tab_view.pack(expand=True, fill="both", padx=20, pady=20)
        self.tab_view.add("Login")
        self.tab_view.add("Signup")

        self.create_login_tab(self.tab_view.tab("Login"))
        self.create_signup_tab(self.tab_view.tab("Signup"))

    def create_login_tab(self, tab):
        """Creates the content for the Login tab."""
        login_frame = ctk.CTkFrame(tab, fg_color="transparent")
        login_frame.pack(expand=True)

        ctk.CTkLabel(login_frame, text="Username").pack(pady=(20, 5))
        self.login_username_entry = ctk.CTkEntry(login_frame)
        self.login_username_entry.pack(pady=5, padx=20)

        ctk.CTkLabel(login_frame, text="Password").pack(pady=(10, 5))
        self.login_password_entry = ctk.CTkEntry(login_frame, show="*")
        self.login_password_entry.pack(pady=5, padx=20)

        self.login_error_label = ctk.CTkLabel(login_frame, text="", text_color="red")
        self.login_error_label.pack(pady=10)

        login_button = ctk.CTkButton(login_frame, text="Login", command=self.handle_login)
        login_button.pack(pady=20, padx=20)

    def create_signup_tab(self, tab):
        """Creates the content for the Signup tab."""
        signup_frame = ctk.CTkFrame(tab, fg_color="transparent")
        signup_frame.pack(expand=True)

        ctk.CTkLabel(signup_frame, text="Username").pack(pady=(20, 5))
        self.signup_username_entry = ctk.CTkEntry(signup_frame)
        self.signup_username_entry.pack(pady=5, padx=20)

        ctk.CTkLabel(signup_frame, text="Password").pack(pady=(10, 5))
        self.signup_password_entry = ctk.CTkEntry(signup_frame, show="*")
        self.signup_password_entry.pack(pady=5, padx=20)
        
        self.signup_error_label = ctk.CTkLabel(signup_frame, text="", text_color="red")
        self.signup_error_label.pack(pady=10)

        signup_button = ctk.CTkButton(signup_frame, text="Sign Up", command=self.handle_signup)
        signup_button.pack(pady=20, padx=20)

    def handle_login(self):
        username = self.login_username_entry.get()
        password = self.login_password_entry.get()
        if self.controller.login(username, password):
            self.destroy() # Close dialog on successful login
        else:
            self.login_error_label.configure(text="Invalid username or password.")

    def handle_signup(self):
        username = self.signup_username_entry.get()
        password = self.signup_password_entry.get()
        if not username or not password:
            self.signup_error_label.configure(text="Username and password cannot be empty.")
            return
            
        if self.controller.signup(username, password):
            # Automatically log in the user after successful signup
            if self.controller.login(username, password):
                self.destroy()
        else:
            self.signup_error_label.configure(text="Username already exists.")
