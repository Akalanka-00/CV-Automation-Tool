from service.json_service import store_data_in_json
import click

def add_default_cover_letter():
    subject = input("Enter your email subject: ").strip()
    print("💬 Your default text editor will open. Write your cover letter and save it.")

    cover_letter = click.edit()
    if cover_letter is None:
        cover_letter = ""

    data = {"subject": subject, "cover_letter": cover_letter.strip()}
    store_data_in_json("default_cover_letter.json", data)
    print("✅ Successfully added default cover letter!\n")
