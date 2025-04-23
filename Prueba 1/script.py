import json
import pandas as pd


# Search custom_attributes node
def find_custom_attributes(data):
    if isinstance(data, dict):
        if data.get("name") == "custom_attributes" and "value" in data:
            return data["value"]
        for key, value in data.items():
            found = find_custom_attributes(value)
            if found:
                return found
    elif isinstance(data, list):
        for item in data:
            found = find_custom_attributes(item)
            if found:
                return found
    return None


# Extract attributes from custom_attributes
def extract_attributes(custom_attributes) -> dict:
    attributes = {}
    for lang, json_str in custom_attributes.items():
        data = json.loads(json_str)
        attributes[lang] = {
            "allergens": ", ".join(
                [a.get("name") for a in data.get("allergens", {}).get("value", [])]
            ),
            "sku": data.get("sku", {}).get("value", None),
            "vegan": data.get("vegan", {}).get("value", None),
            "kosher": data.get("kosher", {}).get("value", None),
            "organic": data.get("organic", {}).get("value", None),
            "vegetarian": data.get("vegetarian", {}).get("value", None),
            "gluten_free": data.get("gluten_free", {}).get("value", None),
            "lactose_free": data.get("lactose_free", {}).get("value", None),
            "package_quantity": data.get("package_quantity", {}).get("value", None),
            "unit_size": data.get("unit_size", {}).get("value", None),
            "net_weight": data.get("net_weight", {}).get("value", None),
        }
    return attributes


def load_json(file_path: str) -> dict:
    with open(file_path, "r", encoding="utf-8") as f:
        return json.load(f)


def save_to_excel(data, output_file):
    df = pd.DataFrame(data).T
    df.to_excel(output_file, index_label="language")


if __name__ == "__main__":
    input_file = "product.json"
    output_excel = "extracted_attributes.xlsx"

    json_data = load_json(input_file)
    custom_attributes = find_custom_attributes(json_data)

    if custom_attributes is not None:
        print("Custom_attributes found.")
        extracted_attributes = extract_attributes(custom_attributes)
        save_to_excel(extracted_attributes, output_excel)
        print(f"Attributes exported successfully to: '{output_excel}'.")
    else:
        print("No se encontró el nodo 'custom_attributes'.")
