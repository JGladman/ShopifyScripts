import pandas as pd

products = pd.read_excel(
    r'/home/jacobg/Documents/Code/ShopifyScripts/Website document .xlsx')

numProducts = products.shape[0]
numColumns = products.shape[1]

formatted_products = pd.DataFrame(columns=[
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
    'Metafield: my_fields.dosage [multi_line_text_field]',
    'Metafield: my_fields.ingredients [single_line_text_field]',
    'Metafield: my_fields.product_id_1 [single_line_text_field]',
    'Metafield: my_fields.product_id_2 [single_line_text_field]',
    'Metafield: my_fields.brand_description [single_line_text_field]'
    'Metafield: my_fields.din [single_line_text_field]',
    'Metafield: my_fields.allergens [multi_line_text_field]',
    'Metafield: my_fields.product_description [single_line_text_field]'
])


def compile_badges(columns, row):
    badges = ""

    for column in columns:
        if row[column] == "Y":
            badges = badges + column + "\r\n"

    return badges


def compile_descriptions(columns, row):
    descriptions = ""

    for column in columns:
        if type(row[column]) is str:
            if len(row[column]) > 0:
                descriptions = descriptions + str(row[column]) + "\r\n"
                #descriptions = descriptions + row[column] + ","

    return descriptions


def compile_allergens(columns, row):
    allergens = ""

    contains = "Contains: "
    may_contain = "May Contain: "

    for column in columns:
        if row[column] == "Y":
            contains = contains + column.replace("Contains", "") + "\r\n"
        elif row[column] == "M":
            may_contain = may_contain + \
                column.replace("Contains", "") + "\r\n"

    allergens = contains + "\r\n\r\n" + may_contain

    return allergens


def format(row):
    row["Command"] = "MERGE"
    row["Title"] = row["Product Name"]
    row["Body HTML"] = row["Description"]
    row['Vendor'] = row['Brand']

    # tags_str = row["Category Type"].replace(
    #     ",", "") + ", " + row["Category SubType"].replace(",", "")

    row["Tags"] = row["Category Type"].replace(
        ",", "") + ", " + row["Category SubType"].replace(",", "")
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
    row["Variant Inventory Qty"] = 15
    row["Metafield: my_fields.brand_name [single_line_text_field]"] = row["Brand"]

    #size_str = str(row["Product Size"]) + str(row["UOM"])

    row["Metafield: my_fields.size [single_line_text_field]"] = str(
        row["Product Size"]) + str(row["UOM"])

    # badges = compile_badges(["Canadian", "Organic", "GMO Free", "Vegetarian", "Vegan",
    #                         "Fair Trade", "Kosher", "Halal", "Gluten Free", "Bcorp Certified"], row)

    row["Metafield: my_fields.badges [multi_line_text_field]"] = compile_badges(["Canadian", "Organic", "GMO Free", "Vegetarian", "Vegan",
                                                                                 "Fair Trade", "Kosher", "Halal", "Gluten Free", "Bcorp Certified"], row)
    row["Metafield: my_fields.description2 [multi_line_text_field]"] = compile_descriptions(
        ["Key Product Features 1", "Key Product Features 2", "Key Product Features 3", "Key Product Features 4", "Key Product Features 5"], row)
    row["Metafield: my_fields.dosage [multi_line_text_field]"] = row["Recommended Dosage"]
    row["Metafield: my_fields.ingredients [single_line_text_field]"] = row["Ingredients"]
    row["Metafield: my_fields.product_id_1 [single_line_text_field]"] = row["Unit UPC"]
    row["Metafield: my_fields.product_id_2 [single_line_text_field]"] = row["Stock ID"]
    row["Metafield: my_fields.brand_description [multi_line_text_field]"] = row["Brand Description"]
    row["Metafield: my_fields.din [single_line_text_field]"] = row["DIN/NPN"]
    row["Metafield: my_fields.allergens [multi_line_text_field]"] = compile_allergens([
        "Contains Egg", "Contains Dairy", "Contains Mustard", "Contains Peanuts", "Contains Seafood", "Contains Sesame", "Contains Soy", "Contains Sulfites", "Contains Tree Nuts", "Contains Wheat Gluten"
    ], row)
    row["Metafield: my_fields.product_description [single_line_text_field]"] = row["Description"]
    row["Metafield: my_fields.country_of_origin [single_line_text_field]"] = row["Country of Origin"]

    row = row.filter(['Stock ID',
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
                      'Metafield: my_fields.dosage [multi_line_text_field]',
                      'Metafield: my_fields.ingredients [single_line_text_field]',
                      'Metafield: my_fields.product_id_1 [single_line_text_field]',
                      'Metafield: my_fields.product_id_2 [single_line_text_field]',
                      "Metafield: my_fields.brand_description [multi_line_text_field]",
                      'Metafield: my_fields.din [single_line_text_field]',
                      'Metafield: my_fields.allergens [multi_line_text_field]',
                      'Metafield: my_fields.product_description [single_line_text_field]',
                      "Metafield: my_fields.country_of_origin [single_line_text_field]"])

    return row


formatted_products = products.apply(format, axis=1)

formatted_products.set_index('Stock ID', inplace=True)

print(products.iloc[0])

formatted_products.head(10).to_excel(
    "formatted_products.xlsx", sheet_name="Products", index=False)
