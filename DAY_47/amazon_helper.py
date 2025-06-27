import requests
from bs4 import BeautifulSoup


def get_product_price(product_url: str):
    """
    Tries to get the current price for a product
    PS: For educational purposes only
    """
    response = requests.get(
        url=product_url,
        headers={
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Safari/537.36"
        }
    )
    contents = response.text

    # Parse html
    soup = BeautifulSoup(contents, "html.parser")

    price = 0.0

    # Get price tags
    price_tag = soup.select_one(selector="span.a-offscreen")
    if price_tag is not None:
        price = float(price_tag.getText().split("£")[1])

    return price
