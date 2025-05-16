import click
from service.json_service import read_json_file, store_data_in_json


def add_new_company():
    company_data_file_name = "companies.json"
    print("📨 Enter email details:")
    company_name = input("🏢 Company Name: ").strip()
    email = input("📧 To Email Address: ").strip()
    cc_input  = input("📋 CC (optional, comma-separated): ").strip()
    subject = input("📝 Subject: ").strip()
    print("💬 Cover Letter (end with a blank line):")

    cc_list = [addr.strip() for addr in cc_input.split(",") if addr.strip()] if cc_input else []

    cover_letter = click.edit()
    if cover_letter is None:
        cover_letter = ""
    print(cover_letter)


    companies = read_json_file(company_data_file_name)
    data = {
        "id": len(companies),
        "company_name": company_name,
        "email": email,
        "cc": cc_list,
        "subject": subject,
        "cover_letter": cover_letter,
        "status": True,
    }


    companies.append(data)
    store_data_in_json(company_data_file_name, companies)