# 🛒 FastAPI Jumbo Scraper

This project is a FastAPI-based application that exposes an endpoint to scrape product data from [Jumbo Colombia](https://www.jumbocolombia.com) product category pages. It's designed to fetch and return the first 15 products listed on a given URL.

---

## 📁 Project Structure

```
main.py                         # Entry point of the FastAPI application

├── utils/
│   ├── __init__.py             # Package marker
│   └── scrapper.py             # Selenium-based scraping logic

├── routes/
│   ├── __init__.py             # Package marker
│   └── jumbo_products.py       # Route for scraping products

├── requirements.txt            # Project dependencies
└── README.md                   # Project documentation
```

---

## ⚙️ Setup Instructions

1. **Clone the repository:**

   ```bash
   git clone <repository-url>
   cd fastapi-app
   ```

2. **Create a virtual environment:**

   ```bash
   python -m venv venv
   ```

3. **Activate the virtual environment:**

   - **Windows:**
     ```bash
     venv\Scripts\activate
     ```
   - **macOS/Linux:**
     ```bash
     source venv/bin/activate
     ```

4. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

---

## 🚀 Running the App

1. **Start the FastAPI server:**

   ```bash
   uvicorn main:app --reload
   ```

2. **Access the interactive API docs:**
   Open your browser and navigate to:

   ```
   http://127.0.0.1:8000/docs
   ```

---

## 📡 Usage

### POST `/get_jumbo_products/`

Send a `POST` request with a JSON payload containing the target Jumbo category URL.

#### Example Request:

```bash
curl -X POST "http://127.0.0.1:8000/get_jumbo_products/" \
-H "Content-Type: application/json" \
-d '{"url": "https://www.jumbocolombia.com/supermercado/despensa/enlatados-y-conservas"}'
```

#### Example Response:

```json
{
  "url": "https://www.jumbocolombia.com/supermercado/despensa/enlatados-y-conservas",
  "products": [
    {
      "name": "Atún En Aceite Van Camps x 160g x 4und",
      "price": "$ 25.492",
      "promo_price": "$ 20.392"
    },
    {
      "name": "Atún En Aceite Van Camps x 160g x 4und",
      "price": "$ 25.492",
      "promo_price": "$ 20.392"
    }
  ]
}
```

> ⚠️ Only the first 15 products are returned for performance and simplicity.

---

## 📄 License

This project is licensed under the **MIT License**.
