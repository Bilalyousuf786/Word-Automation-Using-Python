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

doc.render(my_context)
doc.save("generated_doc.docx")