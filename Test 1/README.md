# Product JSON Cleaner

## Description

Welcome! This project is a demonstration of back-end web scraping skills. The main objective is to extract and format specific attributes from a JSON file and output the results into a clean CSV file.

## Task

Write a Python script that extracts the following properties from the `custom_attributes` node of a JSON file:

- `allergens`
- `sku`
- `vegan`
- `kosher`
- `organic`
- `vegetarian`
- `gluten_free`
- `lactose_free`
- `package_quantity`
- `unit_size`
- `net_weight`

## Input

A JSON file hosted at:

```
https://storage.googleapis.com/resources-prod-shelftia/scrapers-prueba/product.json
```

This file contains a list of product entries, each with a `custom_attributes` object that holds the relevant properties.

## Expected Output

A CSV file with each row corresponding to a product, and columns representing the attributes listed above.

Sample output:

```
https://storage.googleapis.com/resources-prod-shelftia/scrapers-prueba/output-product.csv
```

## How to Run

1. Clone the repository.
2. Make sure Python 3.7+ is installed.
3. Install dependencies (if any).
4. Run the script:
   ```bash
   python script.py
   ```

This will download the JSON file, extract the relevant data, and create a CSV file named `output-product.csv`.

## Notes

- Make sure to handle missing or null values gracefully.
- Output CSV should be UTF-8 encoded and use commas as delimiters.

## License

MIT