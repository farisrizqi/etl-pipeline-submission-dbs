from sqlalchemy import create_engine
import pandas as pd
import gspread
from oauth2client.service_account import ServiceAccountCredentials

def save_to_csv(df: pd.DataFrame, filename='products.csv'):
    df.to_csv(filename, index=False)
    print(f"Data disimpan ke file {filename}")

def save_to_postgresql(df, table_name='products'):
    try:
        username = 'postgres'
        password = 'rizqiawan'
        host = 'localhost'
        port = '5432'
        database = 'scrape_db'

        connection_string = f"postgresql://{username}:{password}@{host}:{port}/{database}"
        engine = create_engine(connection_string)

        df.to_sql(table_name, engine, if_exists='replace', index=False)
        print(f"Data berhasil disimpan ke tabel '{table_name}' di PostgreSQL.")
    except Exception as e:
        print(f"Error menyimpan data ke PostgreSQL: {e}")
        

def save_to_sheet(df, sheet_name='Scraped-Products-Submisson-Faris'):
    try:
        # Scope untuk Google Sheets dan Drive API
        scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]

        # Load credentials dari file JSON
        creds = ServiceAccountCredentials.from_json_keyfile_name('service_account_credentials.json', scope)

        # Authorize
        client = gspread.authorize(creds)

        # Buat Spreadsheet baru
        sheet = client.create(sheet_name)

        # Share spreadsheet agar bisa diakses oleh siapa pun dengan link (sebagai EDITOR)
        sheet.share(None, perm_type='anyone', role='writer')

        # Buka worksheet pertama
        worksheet = sheet.get_worksheet(0)

        # Convert DataFrame ke list of lists
        data = [df.columns.tolist()] + df.values.tolist()

        # Update ke Google Sheet
        worksheet.update(data)

        print(f"Data berhasil disimpan ke Google Sheets: {sheet.url}")
    
    except Exception as e:
        print(f"Error menyimpan ke Google Sheets: {e}")