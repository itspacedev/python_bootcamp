from amazon_helper import get_product_price

PRICE_LIMIT = 70

product_url = input("What product you want to check?: ").strip()

price = get_product_price(product_url)
if price <= PRICE_LIMIT:
    print(f"It is time to buy your favourite product. Its current price is: {price}")
else:
    print(f"Let's check the product price later because we cannot afford it right now =(")


