import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from lxml import html
from traceback import print_exc


def get_jumbo_products(url: str) -> list:
    try:
        chrome_options = Options()
        chrome_options.add_argument("--headless=new")
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-dev-shm-usage")
        chrome_options.add_argument("--disable-gpu")
        chrome_options.add_argument("--disable-extensions")
        chrome_options.add_argument("--disable-infobars")
        chrome_options.add_argument("--disable-browser-side-navigation")
        chrome_options.add_argument("--disable-features=NetworkService")
        chrome_options.add_argument("--disable-features=VizDisplayCompositor")
        chrome_options.add_argument("--disable-dev-tools")
        chrome_options.add_argument("--no-default-browser-check")
        chrome_options.add_argument("--no-first-run")
        #chrome_options.add_argument("--window-size=1920,1080")
        chrome_options.add_argument(
            "user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
        )
        driver_path = ChromeDriverManager().install()
        service = Service(executable_path=driver_path)
        driver = webdriver.Chrome(service=service, options=chrome_options)
        driver.get(url)
        # soft scroll
        scroll_position = 0
        for _ in range(25):
            step = 150
            scroll_position += step
            driver.execute_script(f"window.scrollTo(0, {scroll_position});")
            time.sleep(0.5)

        tree = html.fromstring(driver.page_source)
        html_products = tree.xpath("//article")
        products = []

        for product in html_products[:15]:
            name = product.xpath(
                ".//*[@class='vtex-product-summary-2-x-productBrand vtex-product-summary-2-x-brandName t-body']"
            )[0]
            price = product.xpath(
                ".//*[@class='tiendasjumboqaio-jumbo-minicart-2-x-price']"
            )[0]
            promo_price = product.xpath(
                ".//*[contains(text(), 'Paga')]/following-sibling::*[1]"
            )
            products.append(
                {
                    "name": name.text,
                    "price": price.text,
                    "promo_price": (
                        promo_price[0].text_content() if promo_price else None
                    ),
                }
            )
        return products

    except Exception:
        print_exc()
        return []

    finally:
        print("Cleaning up...")
        driver.quit()
