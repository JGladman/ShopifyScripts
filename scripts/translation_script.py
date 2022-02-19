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
    # Translate Metafields
    return row


# for column in translated_values:
#     if "FR" in column:
#         print(column)

items = items.apply(translate, axis=1)

items.to_excel("formatted_translations.xlsx", index=False)
items.to_csv("formatted_translations.csv", index=False)

print("Complete")
