OnlyPets - Pet Adoption & Services ApplicationThis is a desktop application for browsing and adopting pets, as well as booking pet-related services. It's built with Python, tkinter, and customtkinter.Setup and InstallationPrerequisites: Make sure you have Python 3.10 or newer installed.Create a Virtual Environment (Recommended):python -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
Install Dependencies:pip install customtkinter passlib tkcalendar pillow
How to Run the ApplicationWith your virtual environment activated and dependencies installed, run the main.py file:python main.py
The application will start, automatically creating the data/onlypets.db SQLite database with sample data on its first run.Project StructureOnlyPets/
│
├── main.py
├── models.py
├── controllers.py
├── utils.py
│
├── views/
│   ├── __init__.py
│   ├── home_view.py
│   └── (other view files...)
│
├── assets/
│   ├── pets/
│   └── services/
│
└── data/
    └── (database and json files will be created here)
