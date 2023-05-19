# from requests_html import HTMLSession

# url = "https://apps.shopline.com/sort/?type=0&currentPage="

# s = HTMLSession()
# r =s.get(url)
# r.html.render(sleep=1)

# apps = r.html.xpath('//*[@class= "_applist_content_warp_1wuz5_1"]')
# print(apps)
import pandas as pd


# Create a list with multiple lines or indices
my_list = ['Line 1', 'Line 2', 'Line 3']

# Create a new DataFrame with a single cell
df = pd.DataFrame({'Lines': [" ".join(my_list)]})

# Export the DataFrame to an Excel file
df.to_excel('output.xlsx', index=False)