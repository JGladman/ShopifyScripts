import pandas as pd

items = pd.read_csv(
    r"/home/jacobg/Documents/Code/ShopifyScripts/spreadsheets/translations/The_Natural_Store_translations_Feb-21-2022.csv"
)

translated_values = pd.read_excel(
    r"/home/jacobg/Documents/Code/ShopifyScripts/spreadsheets/WebsiteDocument2.xlsx",
)


def feature_mapping(desc):
    if type(desc) == str:
        return desc.replace("\r", "").replace("\n", "").replace("_x000D_", "")
    else:
        return desc


translated_values["Description"] = translated_values["Description"].map(feature_mapping)

translated_values["Key Product Features"] = translated_values[
    "Key Product Features"
].map(feature_mapping)

translated_values["Ingredients"] = translated_values["Ingredients"].map(feature_mapping)

translated_values["Recommended Use/ Indications "] = translated_values[
    "Recommended Use/ Indications "
].map(feature_mapping)

print(translated_values["Recommended Use/ Indications (FR)"])


def translate(row):
    # Translate collections
    # if row["Type"] == "COLLECTION":
    #     print("COLLECTION")

    # Product title translations
    if row["Type"] == "PRODUCT" and row["Field"] == "title":
        value = translated_values.loc[
            translated_values["Product Name"] == row["Default content"]
        ]
        if value["Product Name (FR)"].iloc[0]:
            row["Translated content"] = value["Product Name (FR)"].iloc[0]

    # Navbar translations
    elif row["Default content"] == "Home":
        row["Translated content"] = "Maison"
    elif row["Default content"] == "Categories":
        row["Translated content"] = "Catégories"
    elif row["Default content"] == "Brands":
        row["Translated content"] = "Marques"
    elif row["Default content"] == "Our brands":
        row["Translated content"] = "Nos marques"
    elif row["Default content"] == "Our Brands":
        row["Translated content"] = "Nos Marques"
    elif row["Default content"] == "Our categories":
        row["Translated content"] = "Nos catégories"
    elif row["Default content"] == "Our Categories":
        row["Translated content"] = "Nos Catégories"

    # Product page translations
    elif row["Default content"] == "Brand Description":
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
    elif row["Type"] == "METAFIELD" and type(row["Default content"]) == str:
        # Description 1
        desc1 = translated_values.loc[
            translated_values["Description"]
            == row["Default content"].replace("\r", "").replace("\n", "")
        ]["Description (FR)"]

        # Description 2
        desc2 = translated_values.loc[
            translated_values["Key Product Features"]
            == row["Default content"].replace("\r", "").replace("\n", "")
        ]["Key Product Features (FR)"]

        # Ingredients
        ingredients = translated_values.loc[
            translated_values["Ingredients"]
            == row["Default content"].replace("\r", "").replace("\n", "")
        ]["Ingredients (FR)"]

        # Dosage
        dosage = translated_values.loc[
            translated_values["Recommended Use/ Indications "]
            == row["Default content"].replace("\r", "").replace("\n", "")
        ]["Recommended Use/ Indications (FR)"]

        if len(desc1) > 0:
            row["Translated content"] = str(desc1.iloc[0]).replace("_x000D_", "")
        elif len(desc2) > 0:
            row["Translated content"] = str(desc2.iloc[0]).replace("_x000D_", "")
        elif len(ingredients) > 0:
            row["Translated content"] = str(ingredients.iloc[0]).replace("_x000D_", "")
        elif len(dosage) > 0:
            row["Translated content"] = str(dosage.iloc[0]).replace("_x000D_", "")

    return row


items = items.apply(translate, axis=1)

items.to_excel(r"/home/jacobg/Documents/Code/ShopifyScripts/spreadsheets/translations/formatted_translations.xlsx", index=False)
items.to_csv(r"/home/jacobg/Documents/Code/ShopifyScripts/spreadsheets/translations/formatted_translations.csv", index=False)

print("Complete")

# https://thenounproject.com/icon/peanut-4614698/ peanut
# https://thenounproject.com/icon/seeds-2516786/ sesame
# https://thenounproject.com/icon/soy-604524/ soy
# https://thenounproject.com/icon/red-wine-2901625/ sulfites
# https://thenounproject.com/icon/walnut-3413234/ tree nuts

