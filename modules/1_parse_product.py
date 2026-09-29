"""
This is the main file responsible for collecting product data. In a larger project, it would be reasonable to split the
 logic into several files and use classes, but for this task that would be unnecessary overengineering.

The main function is `get_data`, which parses the HTML and collects all required product information.

`get_characteristics` is responsible for collecting data from the product's Characteristics section.

`get_page` sends a GET request to the website and returns the HTML content of the page.

 To run the project you need to enter the command - `python ..\modules\1_parse_product.py`

"""


from load_django import *
from parser_app.models import Product

import requests
from bs4 import BeautifulSoup

URL = "https://brain.com.ua/ukr/Mobilniy_telefon_Apple_iPhone_16_128GB_Black-p1145393.html"


def get_page(url: str) -> str:
    headers = {
        "User-Agency": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:156.0) Gecko/20100101 Firefox/156.0"
    }

    response = requests.get(
        url=url,
        headers=headers,
        timeout=10,
    )

    response.raise_for_status()

    return response.text


def get_characteristics(soup: BeautifulSoup):

    items = soup.find_all("div", class_="br-pr-chr-item")

    dict_of_items = {}

    for item in items:
        container = item.find("div", recursive=False)

        if not container:
            continue

        rows = container.find_all("div", recursive=False)

        for row in rows:
            values = row.find_all("span", recursive=False)

            if len(values) <2:
                continue

            key = values[0].get_text(strip=True)
            value = " ".join(values[1].get_text(" ", strip=True).split())

            dict_of_items[key] = value

    return dict_of_items


def get_data(html) -> dict:
    soup = BeautifulSoup(html, "html.parser")

    product = {}

    characteristics = get_characteristics(soup=soup)

    try:
        product['name'] = soup.find("h1", class_="desktop-only-title").get_text(strip=True)
    except AttributeError:
        product['name'] = None

    try:
        div_price = soup.find("div", class_="br-pr-price main-price-block")
        product['regular_price'] = (div_price.find("span").get_text(strip=True)).replace(" ", "")
    except AttributeError:
        product['regular_price'] = None

    try:
        div_prom_price = soup.find("div", class_="br-pr-price main-price-block")
        product['promotion_price'] = (div_prom_price.find("span", class_="red-price").get_text(strip=True)).replace(" ", "")
    except AttributeError:
        product['promotion_price'] = None

    try:
        product['code'] = soup.find("span", class_="br-pr-code-val").get_text(strip=True)
    except AttributeError:
        product['code'] = None

    try:
        div_rewies = soup.find("div", class_="br-pt-rt-main-mark")
        numb_of_reviews = div_rewies.find("span")
        product['numb_of_reviews'] = (numb_of_reviews.get_text(strip=True))
    except AttributeError:
        product['numb_of_reviews'] = None

    try:
        div_photos = soup.find("div", class_="product-block-top")
        all_photos = div_photos.find_all("img", class_="br-main-img")
        product['photos'] = list(image.get("src") for image in all_photos if image.get("src"))
    except AttributeError:
        product['photos'] = None

    product['storage'] = characteristics.get("Вбудована пам'ять")

    product['manufacturer'] = characteristics.get("Виробник")

    product['display_resolution'] = characteristics.get("Роздільна здатність екрану")

    product['color'] = characteristics.get('Колір')

    try:
        product['product_specification'] = characteristics
    except AttributeError:
        product['product_specification'] = None

    return product


if __name__ == "__main__":
    html = get_page(URL)
    product = get_data(html)

    for key, value in product.items():
        print(f"{key} - {value}", "\n")

    Product.objects.get_or_create(
        name=product["name"],
        color=product["color"],
        storage=product["storage"],
        manufacturer=product["manufacturer"],
        regular_price=product["regular_price"],
        promotion_price=product["promotion_price"],
        photos=product["photos"],
        code=product["code"],
        numb_of_reviews=product["numb_of_reviews"],
        display_resolution=product["display_resolution"],
        product_specification=product["product_specification"]
    )

