import pandas as pd

products = pd.read_excel(
    r'/home/jacobg/Documents/Code/ShopifyScripts/Website document .xlsx')

numProducts = products.shape[0]
numColumns = products.shape[1]

formattedProducts = pd.DataFrame(columns=[
    'Stock ID',
    'ID',
    'Handle',
    'Command',
    'Title',
    'Body HTML',
    'Vendor',
    'Tags',
    'Tags Command',
    'Status',
    'Published',
    'Published Scope',
    'Gift Card',
    'Row #',
    'Top Row',
    'Image Src',
    'Image Command',
    'Image Position',
    'Image Alt Text',
    'Variant ID',
    'Variant Command',
    'Variant Position',
    'Variant SKU',
    'Variant Price',
    'Variant Requires Shipping',
    'Variant Taxable',
    'Variant Image',
    'Variant Inventory Tracker',
    'Variant Inventory Policy',
    'Variant Fulfillment Service',
    'Variant Inventory Qty',
    'Metafield: my_fields.brand_name [single_line_text_field]',
    'Metafield: my_fields.size [single_line_text_field]',
    'Metafield: my_fields.badges [multi_line_text_field]',
    'Metafield: my_fields.description2 [multi_line_text_field]',
    'Metafield: my_fields.dosage [single_line_text_field]',
    'Metafield: my_fields.ingredients [single_line_text_field]',
    'Metafield: my_fields.product_id_1 [single_line_text_field]',
    'Metafield: my_fields.product_id_2 [single_line_text_field]',
    'Metafield: my_fields.brand_description [single_line_text_field]'
    'Metafield: my_fields.din [single_line_text_field]',
    'Metafield: my_fields.allergens [multi_line_text_field]',
    'Metafield: my_fields.product_description [single_line_text_field]'
])

formattedProducts.set_index('Stock ID', inplace=True)


def format(row):
    row["Command"] = "MERGE"
    row["Title"] = row["Product Name"]
    row["Body HTML"] = row["Description"]
    row['Vendor'] = row['Brand']

    tags_str = row["Category Type"].replace(
        ",", "") + ", " + row["Category SubType"].replace(",", "")

    row["Tags"] = tags_str
    row["Tags Command"] = "REPLACE"
    row["Status"] = "Active"
    row["Published"] = "TRUE"
    row["Published Scope"] = "global"
    row["Gift Card"] = "FALSE"
    row["Row #"] = 1
    row["Top Row"] = "TRUE"
    row["Image Src"] = row["Product Image Link"]
    row["Image Command"] = "MERGE"
    row["Image Position"] = 1
    row["Image Alt Text"] = row["Title"]
    row["Variant Command"] = "MERGE"
    row["Variant Position"] = 1
    row["Variant SKU"] = row["Stock ID"]
    row["Variant Price"] = row["Wholesale Price"]
    row["Variant Requires Ship"] = "TRUE"
    row["Variant Taxable"] = "TRUE"
    row["Variant Image"] = row["Image Src"]
    row["Variant Inventory"] = "shopify"
    row["Variant Inventory Policy"] = "deny"
    row["Variant Fulfillment Service"] = "manual"
    row["Variant Inventory Qty"]

    return row


products = products.apply(format, axis=1)

print(products.iloc[0])


formattedProducts.to_excel("formatted_products.xlsx")
