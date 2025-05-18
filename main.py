from utils.extract import scrape_page
from utils.transform import transform_data
from utils.load import save_to_csv, save_to_postgresql, save_to_sheet

BASE_URL = "https://fashion-studio.dicoding.dev/"

def main():
    all_products = []

    print("Memulai scraping halaman utama...")
    try:
        products = scrape_page(url=f"{BASE_URL}")
        all_products.extend(products)
    except Exception as e:
        print(f"Gagal scraping halaman utama: {e}")

    # Scrape halaman 2 sampai 50
    for page_number in range(2, 51):
        page_url = f"{BASE_URL}/page{page_number}"
        print(f"Scraping halaman {page_number}...")
        try:
            products = scrape_page(url=page_url)
            all_products.extend(products)
        except Exception as e:
            print(f"Gagal scraping halaman {page_number}: {e}")

    if not all_products:
        print("Tidak ada produk yang berhasil di-scrape. Program dihentikan.")
        return

    print(f"Total produk yang didapat: {len(all_products)}")

    # Transform data
    df = transform_data(all_products)
    if df.empty:
        print("Data hasil transformasi kosong. Program dihentikan.")
        return

    print("Data berhasil ditransformasi:")
    print(df.head())

    # Simpan ke CSV
    save_to_csv(df)

    # Simpan ke PostgreSQL
    save_to_postgresql(df)
    
    # Simpan ke Google Sheet
    save_to_sheet(df, 'Scraped-Products-Submisson-Faris')

if __name__ == '__main__':
    main()
