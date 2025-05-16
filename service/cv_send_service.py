from service.email_service import send_email
from service.json_service import read_json_file


def send_cvs():
    raw_companies = read_json_file("companies.json")
    raw_default_cover_letter = read_json_file("default_cover_letter.json")
    subject = raw_default_cover_letter["subject"]
    cover_letter = raw_default_cover_letter["cover_letter"]
    active_companies = [company for company in raw_companies if company.get("status") is True]


    for company in active_companies:
        if len(company["subject"]) > 0:
            subject = company["subject"]
        if len(company["cover_letter"]) > 0:
            cover_letter = company["cover_letter"]

        subject = subject.replace("{company}", company["company_name"])
        cover_letter = cover_letter.replace("{company}", company["company_name"])
        send_email(company["email"], subject, cover_letter, company["cc"])
