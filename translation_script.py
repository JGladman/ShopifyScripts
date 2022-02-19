import pandas as pd

items = pd.read_csv(
    r"/home/jacobg/Documents/Code/ShopifyScripts/The_Natural_Store_translations_Feb-17-2022.csv"
)

translated_items = items.dropna(subset=["Default content"])

translated_items = translated_items[translated_items["Translated content"].isna()]

translated_values = pd.read_excel(
    r"/home/jacobg/Documents/Code/ShopifyScripts/Website document .xlsx"
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
        row["Translated content"] = value["Product Name (FR)"]
    return row


# for column in translated_values:
#     if "FR" in column:
#         print(column)

translated_items = translated_items.apply(translate, axis=1)

translated_items.to_excel("formatted_translations.xlsx", index=False)

print("Complete")
