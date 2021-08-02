import pandas as pd
from pathlib import Path

DIRECTORY = r'C:\Users\devineg\Desktop\FedEx POD'
WORKBOOK = 'Book5.xlsx'

file = Path(DIRECTORY) / WORKBOOK
df = pd.read_excel(file, usecols=[0, 1])

invoices = df['Invoice #'].values
numbers = df['Fed Ex Tracking #'].values

for invoice, tracking in zip(invoices, numbers):
    print(invoice, tracking)