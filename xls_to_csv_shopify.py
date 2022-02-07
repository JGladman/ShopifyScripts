import pandas as pd

products = pd.read_excel(r'/home/jacobg/Documents/Code/ShopifyScripts/Website document .xlsx')

numProducts = products.shape[0]
numColumns = products.shape[1]

"Header,Vendor,Published,Variant Inventory Quantity,Variant Inventory Policy,Variant Fulfillment Service,Variant Price,Variant Requires Shipping,Variant Taxable,Variant Grams,Variant Weight Unit,Status,Option1 Name,Option1 Value"


def squish(row):
  print(row)
  header_string = "Handle,Title,Body (HTML),Vendor,Standardized Product Type,Custom Product Type,Tags,Published,Option1 Name,Option1 Value,Option2 Name,Option2 Value,Option3 Name,Option3 Value,Variant SKU,Variant Grams,Variant Inventory Tracker,Variant Inventory Qty,Variant Inventory Policy,Variant Fulfillment Service,Variant Price,Variant Compare At Price,Variant Requires Shipping,Variant Taxable,Variant Barcode,Image Src,Image Position,Image Alt Text,Gift Card,SEO Title,SEO Description,Google Shopping / Google Product Category,Google Shopping / Gender,Google Shopping / Age Group,Google Shopping / MPN,Google Shopping / AdWords Grouping,Google Shopping / AdWords Labels,Google Shopping / Condition,Google Shopping / Custom Product,Google Shopping / Custom Label 0,Google Shopping / Custom Label 1,Google Shopping / Custom Label 2,Google Shopping / Custom Label 3,Google Shopping / Custom Label 4,Variant Image,Variant Weight Unit,Variant Tax Code,Cost per item,Status"
  row["header"] = header_string
  #row.drop(index=0)


  return row

#test = products.apply(squish, axis='columns')


print(products.loc[products["Category SubType"] == 'Other'])