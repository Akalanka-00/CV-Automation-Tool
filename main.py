from dotenv import load_dotenv

from service.company_service import add_new_company
from service.configuration_service import configure
from service.email_service import send_email
from service.main_menu_service import open_main_menu

if __name__ == "__main__":
    # Load .env file
    load_dotenv()
    cv_name = "Shenal_Akalanka_cv.pdf"
    cv_path = "./data/" + cv_name

    while True:
        open_main_menu()
    # send_email("shenalakalanka513@gmail.com", "Hello world", "This is a test email with attachment", cv_path)



