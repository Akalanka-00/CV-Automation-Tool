import getpass
from service.json_service import create_json_files, store_data_in_json


def configure():
    configure_json_file_name = "configure.json"
    version = "1.0.0"
    create_json_files()

    email = input("Enter your email: ")
    password = getpass.getpass("Enter your app password: ")
    cv_filename = input("Enter the name of your CV file (e.g., resume.pdf): ")

    store_data_in_json(configure_json_file_name, {"version": version, "email": email, "password": password, "cv_name": cv_filename})
    print("Application configured successfully!\n")

