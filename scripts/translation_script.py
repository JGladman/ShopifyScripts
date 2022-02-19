import pandas as pd

items = pd.read_csv(
    r"/home/jacobg/Documents/Code/ShopifyScripts/spreadsheets/The_Natural_Store_translations_Feb-17-2022.csv"
)

items.to_excel("unformatted.xlsx")

translated_values = pd.read_excel(
    r"/home/jacobg/Documents/Code/ShopifyScripts/spreadsheets/Website document .xlsx"
)


def translate(row):
    # Translate collections
    # if row["Type"] == "COLLECTION":
    #     print("COLLECTION")

    # Translate product names
    if row["Type"] == "PRODUCT" and row["Field"] == "title":
        value = translated_values.loc[
            translated_values["Product Name"] == row["Default content"]
        ]
        if value["Product Name (FR)"].iloc[0]:
            row["Translated content"] = value["Product Name (FR)"].iloc[0]
    if row["Default content"] == "Brand Description":
        row["Translated content"] = "Description de la Marque"
    elif (
        row["Default content"]
        == "Brand Name: {{ product.metafields.my_fields.brand_name.value }}"
    ):
        row[
            "Translated content"
        ] = "Marque: {{ product.metafields.my_fields.brand_name.value }}"
    elif (
        row["Default content"] == "Size: {{ product.metafields.my_fields.size.value }}"
    ):
        row[
            "Translated content"
        ] = "Taille: {{ product.metafields.my_fields.size.value }}"
    elif row["Default content"] == "Product Description":
        row["Translated content"] = "Description du Produit"
    elif row["Default content"] == "Ingredients":
        row["Translated content"] = "Ingrédients"
    elif row["Default content"] == "Product Information":
        row["Translated content"] = "Information Produit"
    elif (
        row["Default content"]
        == "<p>Country of Origin: {{ product.metafields.my_fields.country_of_origin.value }}</p><p></p><p>Product ID Number 1: {{ product.metafields.my_fields.product_id_1.value }}</p><p></p><p>Product ID Number 2: {{ product.metafields.my_fields.product_id_2.value }}</p><p></p><p>(Can dynamically render DIN/NPN if present on product. Missing for most)</p>"
    ):
        row[
            "Translated content"
        ] = "<p>Pays d'origine: {{ product.metafields.my_fields.country_of_origin.value }}</p><p></p><p>Numéro d'identification du produit 1: {{ product.metafields.my_fields.product_id_1.value }}</p><p></p><p>Numéro d'identification du produit 2: {{ product.metafields.my_fields.product_id_2.value }}</p><p></p><p>(Can dynamically render DIN/NPN if present on product. Missing for most)</p>"
    # Translate Metafields
    return row


# for column in translated_values:
#     if "FR" in column:
#         print(column)

items = items.apply(translate, axis=1)

items.to_excel("formatted_translations.xlsx", index=False)
items.to_csv("formatted_translations.csv", index=False)

print("Complete")
