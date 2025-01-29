from docxtpl import DocxTemplate
from datetime import datetime
import pandas as pd

doc = DocxTemplate("template.docx")

job_position = "Jr Customer Support Engineer"
my_phone = "+92324-123456"
my_email = "bilalyousuf@gmail.com"
my_address ="Karachi Pakistan"
today_date = datetime.today().strftime("%d %b, %Y") 
my_name = "Bilal"

# This is a dictionary having key and value
my_context = {
    'job_position' : job_position,
    'my_phone' : my_phone,
    'my_email' : my_email,
    'my_address' : my_address,
    'today_date' : today_date,
    'my_name' : my_name
}

df = pd.read_csv("dummy_data.csv")

for index, row in df.iterrows():
# show each row data from dummy_data.csv file
    #print(index)
# it shows index No. starts from 0
    #print(row)
# it shows each data row wise.

    context = {
        'hiring_manager_name' : row['name'],
        'address' : row['address'],
        'phone_number': row['phone_number'],
        'email': row['email'],
        'job_position' : row['job'],
        'company_name': row['company']
    }
    context.update(my_context)

    doc.render(context)
    doc.save(f"generated_doc_{index}.docx")