import csv
import tkinter as tk
from tkinter import filedialog

from service.json_service import read_json_file, store_data_in_json


def select_csv_file():
    root = tk.Tk()
    root.withdraw()  # Hide the main window
    company_data_file_name = "companies.json"

    existing_companies = read_json_file(company_data_file_name)

    file_path = filedialog.askopenfilename(
        title="Select a CSV file",
        filetypes=[("CSV files", "*.csv"), ("All files", "*.*")]
    )

    companies = []
    for company in existing_companies:
        companies.append(company)
    if file_path:
        with open(file_path, newline='', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            start_index = len(existing_companies)
            for idx, row in enumerate(reader):
                company_name = row.get("Company", "").strip()
                email = row.get("Email", "").strip()
                cc_raw = row.get("CC", "").strip()
                cc_list = [cc.strip() for cc in cc_raw.split(",") if cc.strip()]
                subject = row.get("Subject", "").strip()
                cover_letter = row.get("Cover Letter", "").strip()

                data = {
                    "id": start_index+idx,
                    "company_name": company_name,
                    "email": email,
                    "cc": cc_list,
                    "subject": subject,
                    "cover_letter": cover_letter,
                    "status": True,
                }
                companies.append(data)

        print(f"\n✅ Parsed {len(companies)-len(existing_companies)} companies successfully.")
        store_data_in_json(company_data_file_name, companies)
    else:
        print("❌ No file selected.")
        return None

