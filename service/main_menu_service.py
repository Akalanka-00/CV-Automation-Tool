import questionary
import sys

from service.company_service import add_new_company
from service.configuration_service import configure
from service.cover_letter_service import add_default_cover_letter
from service.csv_service import select_csv_file
from service.cv_send_service import send_cvs
from service.md_service import open_md_in_browser

choices = [
    "Configure",
    "Add default cover letter",
    "Add new Company",
    "Import Data from csv",

    "Delete Company",
    "Change company status",
    "Send Cvs",
    "Instructions",

    "Exit"
]

def get_choices():
    return choices

def open_main_menu():

    choice = questionary.select(
        "Choose an option:",
        choices=choices,
    ).ask()

    print(f"\nYou selected: {choice}")

    if choice == choices[0]:
        configure()

    if choice == choices[1]:
        add_default_cover_letter()

    elif choice == choices[2]:
        add_new_company()

    elif choice == choices[3]:
        select_csv_file()

    elif choice == choices[4]:
        print(choices[4])

    elif choice == choices[5]:
        print(choices[5])

    elif choice == choices[6]:
        send_cvs()

    elif choice == choices[7]:
        open_md_in_browser()

    elif choice == choices[8]:
        sys.exit()