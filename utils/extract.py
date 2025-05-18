import requests
from bs4 import BeautifulSoup
from datetime import datetime

def scrape_page(url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
    }
    response = requests.get(url, headers=headers)

    if response.status_code != 200:
        print(f"Gagal mengakses halaman: {url}")
        return []

    soup = BeautifulSoup(response.text, 'html.parser')
    product_cards = soup.find_all("div", class_="collection-card")
    results = []

    if not product_cards:
        print("Tidak ada produk yang ditemukan.")
        return []

    for card in product_cards:
        try:
            title = card.find("h3", class_="product-title").text.strip()
        except AttributeError:
            title = "Unknown Product"

        # Ambil elemen harga dari span class="price"
        price_span = card.find("span", class_="price")
        price_text = price_span.text.strip() if price_span else "Price Unavailable"

        # Ambil semua info dalam <p>
        info_paragraphs = card.find_all("p", style=lambda s: s and "font-size" in s)
        info_dict = {}
        for p in info_paragraphs:
            text = p.text.strip()
            if "Rating:" in text:
                info_dict['rating'] = text.replace("rating:", "").strip()
            elif "Colors" in text:
                info_dict['colors'] = text.strip()
            elif "Size:" in text:
                info_dict['size'] = text.replace("size:", "").strip()
            elif "Gender:" in text:
                info_dict['gender'] = text.replace("gender:", "").strip()

        product_data = {
            "title": title,
            "price": price_text,
            "rating": info_dict.get("rating", "N/A"),
            "colors": info_dict.get("colors", "N/A"),
            "size": info_dict.get("size", "N/A"),
            "gender": info_dict.get("gender", "N/A"),   
            "timestamp": datetime.now().isoformat()
        }
        results.append(product_data)

    return results


# Contoh penggunaan
if __name__ == "__main__":
    url = "https://fashion-studio.dicoding.dev/page2"  # Ganti dengan URL asli
    products = scrape_page(url)
    for product in products:
        print(product)
