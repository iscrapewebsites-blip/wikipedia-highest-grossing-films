# import get_page # on import script run
from lxml import html
import time

time.sleep(5)
page = ''
with open('data.html', 'r', encoding='utf-8') as f:
     page = f.read()

# again nobody cares about how you get there.. people care about the output/result

tree = html.fromstring(page)
elem = tree.xpath('//div/table[contains(@class, "sortable")]/tbody/tr')

header = elem[0].text_content().strip().split('\n\n')
elem  = elem[1:] # skip header

data = []
for e in elem:
     row = e.text_content().strip().split('\n\n')
     data.append(row)

# writing to excel file
from openpyxl import Workbook
from openpyxl.styles import Font
wb = Workbook()
ws = wb.active

# I don't want the last field
header = header[:-1]

ws.append(header)
# setting header bold
for cell in ws['1']:
     cell.font = Font(bold=True)

# I don't want the last field so [:-1]
for row in data:
     ws.append(row[:-1])

wb.save('top_movies.xlsx')