import customtkinter as ctk
from utils import load_image

class HomeView(ctk.CTkFrame):
    """
    The home screen of the OnlyPets application.
    """
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller

        self.configure(fg_color=("#FFFFFF", "#1B1A1D"))

        # Main content frame
        main_content = ctk.CTkFrame(self, fg_color="transparent")
        main_content.pack(pady=60, padx=60, fill="both", expand=True)

        # Left side content (Welcome Text)
        left_frame = ctk.CTkFrame(main_content, fg_color="transparent")
        left_frame.pack(side="left", fill="both", expand=True, padx=(0, 20))

        welcome_label = ctk.CTkLabel(left_frame, text="WELCOME,",
                                     font=ctk.CTkFont(family="Helvetica", size=72, weight="bold"))
        welcome_label.pack(anchor="w", pady=(20,0))

        guest_label = ctk.CTkLabel(left_frame, text="Guest User!",
                                   font=ctk.CTkFont(family="Helvetica", size=72, weight="bold"),
                                   text_color="#F26B38")
        guest_label.pack(anchor="w")

        sub_text = ctk.CTkLabel(left_frame,
                                text="Find your new best friend and\ngive them a forever home, while\nwe care for all your pet's needs",
                                font=ctk.CTkFont(family="Helvetica", size=18),
                                text_color=("#333333", "#A9A9A9"),
                                justify="left")
        sub_text.pack(anchor="w", pady=20)

        make_friend_button = ctk.CTkButton(left_frame, text="Make a friend",
                                           command=lambda: controller.show_frame("PetListView"),
                                           font=ctk.CTkFont(family="Helvetica", size=16, weight="bold"),
                                           fg_color="#F26B38",
                                           hover_color="#D95F30",
                                           text_color="#FFFFFF",
                                           corner_radius=20,
                                           height=50,
                                           width=200)
        make_friend_button.pack(anchor="w", pady=20)

        # Right side content (Image)
        right_frame = ctk.CTkFrame(main_content, fg_color="transparent")
        right_frame.pack(side="right", fill="both", expand=True)

        self.pet_image = load_image("assets/pets/home_pets.png", (600, 500))

        image_label = ctk.CTkLabel(right_frame, image=self.pet_image, text="")
        image_label.pack(expand=True)

