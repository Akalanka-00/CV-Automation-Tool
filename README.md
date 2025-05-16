# CV Submission Tool

This application allows you to efficiently send your CV to multiple companies at once with customized cover letters.

## Getting Started

### Prerequisites
- Python installed on your system
- Gmail account (for sending emails)
- Your CV file in PDF format

### Installation

1. Clone or download this repository to your local machine
2. Install required dependencies:
   ```
   pip install -r requirements.txt
   ```

## Usage

### Initial Setup

1. Place your CV file (PDF format) in the `data` folder of the application
2. Open Command Prompt (CMD) and navigate to the application directory
3. Run the main application:
   ```
   python main.py
   ```
4. Click on the "Configure" button in the main interface

### Email Configuration

1. Enter your Gmail address in the provided field
2. Enter your App Password (not your regular Gmail password)
   - To create an App Password:
     - Visit https://myaccount.google.com/apppasswords
     - Sign in with your Google account
     - Select "Mail" as the app and your device
     - Click "Generate" and use the 16-character password
3. Click "Save" to store your email configuration

### Cover Letter Setup

1. Navigate to te main menu.
2. Click on "Add Default Cover Letter"
3. Type or paste your default cover letter template
4. You can use the following placeholders in your cover letter:
   - `{company}` - Will be replaced with the company name
5. Save and close text editor to store your default cover letter

### Company Import

1. From the main menu, select "Import Companies"
2. Prepare a CSV file with the following columns:
   - `company` - Company name
   - `email` - Primary recipient email
   - `cc` - Carbon copy email addresses (optional)
   - `subject` - Email subject line
   - `cover_letter` - Custom cover letter for this company (optional)
3. Click "Import Data from csv" and select your CSV file


## Support

If you encounter any issues or have questions, please reach out to the application support team.

## License

This tool is provided for personal use only.