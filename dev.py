import urllib.parse

from tableau_api_lib import TableauServerConnection
from tableau_api_lib.utils import querying, flatten_dict_column
import pandas as pd

desired_width=320

pd.set_option('display.width', desired_width)

from urllib import parse

#Please mention your personal_access_token_name and personal_access_token_secret below
config = {
    'tableau_online': {
        'server': 'https://us-west-2b.online.tableau.com',
        'api_version': '3.22',
        'personal_access_token_name': 'pp',
        'personal_access_token_secret': '/PPZuxVlTKmFheVtYnMcuQ==:3fwsDWWefHAvmu8Yq4Q8YxTvPAoTfIMh',
        'site_name': 'motivepeopleanalytics',
        'site_url': 'motivepeopleanalytics'
    }
}

conn = TableauServerConnection(config, env='tableau_online')
conn.sign_in()

#print(conn.sign_in())

views_df = querying.get_views_dataframe(conn)
views_df.head()

#print(views_df.head())

views_df = flatten_dict_column(views_df, keys=["name", "id"], col_name="workbook")
view_df = views_df[["workbook_name", "name", "id"]]

#print(view_df.head())

#You can replace "360 Report Generator Test" with the name of a workbook you have uploaded online
relevant_views_df = view_df[view_df["name"] == "Manager Feedback Results"]

relevant_views_df.head()

#print('hello')
print(relevant_views_df.head())

#When you will print above, you will get ids for specific tabs in your workbook, you can mention the one which is the main viz below
pdf_view_id = '8a9961ee-ac72-41bd-9047-b1c0a4fcdee0'

employee_id = urllib.parse.quote("id")
#print(employee_id)




#print(type(view_png_image.content))
#print(view_png_image)


file_path = "ids.txt"
with open(file_path, 'r') as file:
    ids = [line.strip() for line in file.readlines()]

for id in ids:
    print("Processing ID:", id)
    employee_id_filter = urllib.parse.quote(id)
    #print(employee_id_filter)
    customer_url_params = {
        "employee_id_filter": f"vf_{employee_id}={employee_id_filter}"
    }
    #print(customer_url_params)
    view_png_image = conn.query_view_image(view_id=pdf_view_id, parameter_dict=customer_url_params)
    with open(id + '.png','wb') as file:
        #print('in here')
        file.write(view_png_image.content)
        file.close()





