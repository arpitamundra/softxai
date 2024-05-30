# import xml.etree.ElementTree as ET
# import pandas as pd
# import os
#
# def parse_xml(xml_file):
#     tree = ET.parse(xml_file)
#     root = tree.getroot()
#
#     transactions = []
#     def find_element(parent, tag):
#         return parent.find(f".//{tag}").text if parent.find(f".//{tag}") is not None else ''
#
#     for voucher in root.findall('.//VOUCHER'):
#         voucher_type = voucher.find('.//VOUCHERTYPENAME').text
#         if voucher_type == 'Receipt':
#             date = find_element(voucher, 'DATE')
#             transaction_type = find_element(voucher, 'BANKALLOCATIONS.LIST/TRANSFERMODE')
#             vch_no = find_element(voucher, 'VOUCHERNUMBER')
#             ref_no = find_element(voucher, 'BANKALLOCATIONS.LIST/UNIQUEREFERENCENUMBER')
#             ref_type = find_element(voucher, 'BILLALLOCATIONS.LIST/BILLTYPE')
#             ref_date = find_element(voucher, 'BANKALLOCATIONS.LIST/DATE')
#             debtor = find_element(voucher, 'PARTYLEDGERNAME')
#             ref_amount = find_element(voucher, 'BILLALLOCATIONS.LIST/AMOUNT')
#             amount = find_element(voucher, 'ALLLEDGERENTRIES.LIST/AMOUNT')
#             particulars = find_element(voucher, 'ALLLEDGERENTRIES.LIST/LEDGERNAME')
#             vch_type = find_element(voucher, 'VOUCHERTYPENAME')
#             amount_verified = find_element(voucher, 'ALLLEDGERENTRIES.LIST/AMOUNT')
#
#             print(f"Date: {date}")
#             print(f"Transaction Type: {transaction_type}")
#             print(f"Vch No.: {vch_no}")
#             print(f"Ref No.: {ref_no}")
#             print(f"Ref Type: {ref_type}")
#             print(f"Ref Date: {ref_date}")
#             print(f"Debtor: {debtor}")
#             print(f"Ref Amount: {ref_amount}")
#             print(f"Amount: {amount}")
#             print(f"Particulars: {particulars}")
#             print(f"Vch Type: {vch_type}")
#             print(f"Amount Verified: {amount_verified}")
#             print()
#             transactions.append({'Date': date, 'transaction_type': transaction_type,"Vch No.":vch_no,"Ref No.":ref_no,"Ref Type":ref_type,"Ref Date":ref_date,"Debtor":debtor,"Ref Amount":ref_amount, 'Amount': amount,"Particulars":particulars,"Vch Type":vch_type,"Amount Verified":amount_verified})
#
#     return transactions
#
#
# def create_spreadsheet(transactions, output_file):
#     df = pd.DataFrame(transactions)
#     df.to_excel(output_file, index=False)
#
#
# def main():
#     input_file = 'Input.xml'
#     dir_path = '/Users/arpitamundra/Downloads'
#     input_xml = os.path.join(dir_path, input_file)
#     output_excel = 'output.xlsx'
#
#
#     transactions = parse_xml(input_xml)
#
#     create_spreadsheet(transactions, output_excel)
#     print("Spreadsheet created successfully.")
#
#
# if __name__ == "__main__":
#     main()
#
#
# import xml.etree.ElementTree as ET
# import pandas as pd
# import os
#
# def parse_xml(xml_file):
#     tree = ET.parse(xml_file)
#     root = tree.getroot()
#
#     transactions = []
#     def find_element(parent, tag):
#         return parent.find(f".//{tag}").text if parent.find(f".//{tag}") is not None else ''
#
#     for voucher in root.findall('.//VOUCHER'):
#         voucher_type = voucher.find('.//VOUCHERTYPENAME').text
#         if voucher_type == 'Receipt':
#             date = find_element(voucher, 'DATE')
#             transaction_type = find_element(voucher, 'BANKALLOCATIONS.LIST/TRANSFERMODE')
#             vch_no = find_element(voucher, 'VOUCHERNUMBER')
#             ref_no = find_element(voucher, 'BANKALLOCATIONS.LIST/UNIQUEREFERENCENUMBER')
#             ref_type = find_element(voucher, 'BILLALLOCATIONS.LIST/BILLTYPE')
#             ref_date = find_element(voucher, 'BANKALLOCATIONS.LIST/DATE')
#             debtor = find_element(voucher, 'PARTYLEDGERNAME')
#             ref_amount = find_element(voucher, 'BILLALLOCATIONS.LIST/AMOUNT')
#             amount = find_element(voucher, 'ALLLEDGERENTRIES.LIST/AMOUNT')
#             particulars = find_element(voucher, 'ALLLEDGERENTRIES.LIST/LEDGERNAME')
#             vch_type = find_element(voucher, 'VOUCHERTYPENAME')
#             amount_verified = find_element(voucher, 'ALLLEDGERENTRIES.LIST/AMOUNT')
#
#             print(f"Date: {date}")
#             print(f"Transaction Type: {transaction_type}")
#             print(f"Vch No.: {vch_no}")
#             print(f"Ref No.: {ref_no}")
#             print(f"Ref Type: {ref_type}")
#             print(f"Ref Date: {ref_date}")
#             print(f"Debtor: {debtor}")
#             print(f"Ref Amount: {ref_amount}")
#             print(f"Amount: {amount}")
#             print(f"Particulars: {particulars}")
#             print(f"Vch Type: {vch_type}")
#             print(f"Amount Verified: {amount_verified}")
#             print()
#             transactions.append({'Date': date, 'transaction_type': transaction_type,"Vch No.":vch_no,"Ref No.":ref_no,"Ref Type":ref_type,"Ref Date":ref_date,"Debtor":debtor,"Ref Amount":ref_amount, 'Amount': amount,"Particulars":particulars,"Vch Type":vch_type,"Amount Verified":amount_verified})
#
#     return transactions
#
#
# def create_spreadsheet(transactions, output_file):
#     df = pd.DataFrame(transactions)
#     df.to_excel(output_file, index=False)
#
#
# def main():
#     input_file = 'Input.xml'
#     dir_path = '/Users/arpitamundra/Downloads'
#     input_xml = os.path.join(dir_path, input_file)
#     output_excel = 'output.xlsx'
#
#
#     transactions = parse_xml(input_xml)
#
#     create_spreadsheet(transactions, output_excel)
#     print("Spreadsheet created successfully.")
#
#
# if __name__ == "__main__":
#     main()
#
# import xml.etree.ElementTree as ET
#
# input_file = 'Input.xml'
# dir_path = '/Users/arpitamundra/Downloads'
# input_xml = os.path.join(dir_path, input_file)
# tree = ET.parse(input_xml)
# root = tree.getroot()
# transactions = []
#
# # Iterate through each VOUCHER element
# for voucher in root.findall('.//VOUCHER'):
#     # Extract data from the VOUCHER element
#     voucher_type = voucher.find('.//VOUCHERTYPENAME').text
#     if voucher_type == 'Receipt':
#         date = voucher.find('DATE').text
#         vch_type = voucher.find('VOUCHERTYPENAME').text
#         vch_no = voucher.find('VOUCHERNUMBER').text
#         debtor = voucher.find('PARTYLEDGERNAME').text
#         transactions.append({'Date': date, 'transaction_type': "Parent", "Vch No.": vch_no, "Ref No.": "NA",
#                              "Ref Type": "NA", "Ref Date": "NA", "Debtor": debtor, "Ref Amount": "NA",
#                              'Amount': voucher.find('ALLLEDGERENTRIES.LIST/AMOUNT').text, "Particulars": debtor, "Vch Type": vch_type,
#                              "Amount Verified": "Yes"})
#         for ledger_entry in voucher.findall('.//ALLLEDGERENTRIES.LIST'):
#             ledger_name = ledger_entry.find('LEDGERNAME').text
#             amount = ledger_entry.find('AMOUNT').text
#             if ledger_name == debtor:
#                 for allocation in ledger_entry.findall('BILLALLOCATIONS.LIST'):
#                     transactions.append({'Date': date, 'transaction_type': "Child", "Vch No.": vch_no,
#                                          "Ref No.": allocation.find('NAME').text,
#                                          "Ref Type": allocation.find('BILLTYPE').text,
#                                          "Ref Date": " ", "Debtor": debtor,
#                                          "Ref Amount": allocation.find('AMOUNT').text,
#                                          'Amount': "NA", "Particulars": ledger_name, "Vch Type": vch_type,
#                                          "Amount Verified": "NA"})
#         for ledger_entry in voucher.findall('.//ALLLEDGERENTRIES.LIST'):
#             ledger_name = ledger_entry.find('LEDGERNAME').text
#             amount = ledger_entry.find('AMOUNT').text
#             if ledger_name != debtor:
#                 transactions.append({'Date': date, 'transaction_type': "Other", "Vch No.": vch_no,
#                                      "Ref No.": "NA",
#                                      "Ref Type": "NA",
#                                      "Ref Date": "NA", "Debtor": debtor, "Ref Amount": "NA",
#                                      'Amount': amount, "Particulars": ledger_name, "Vch Type": vch_type,
#                                      "Amount Verified": "NA"})
#                 # continue
# for voucher in root.findall('.//VOUCHER'):
#     voucher_type = voucher.find('.//VOUCHERTYPENAME').text
#     if voucher_type == 'Receipt':
#         mix_date = voucher.find('DATE').text
#         # mix_date = find_element(voucher, 'DATE')
#         date = datetime.strptime(mix_date, "%Y%m%d").date()
#         vch_type = voucher.find('VOUCHERTYPENAME').text
#         vch_no = voucher.find('VOUCHERNUMBER').text
#         debtor = voucher.find('PARTYLEDGERNAME').text
#         transactions.append({'Date': date, 'transaction_type': "Parent", "Vch No.": vch_no, "Ref No.": "NA",
#                              "Ref Type": "NA", "Ref Date": "NA", "Debtor": debtor, "Ref Amount": "NA",
#                              'Amount': voucher.find('ALLLEDGERENTRIES.LIST/AMOUNT').text, "Particulars": debtor,
#                              "Vch Type": vch_type,
#                              "Amount Verified": "Yes"})
#
#         for ledger_entry in voucher.findall('.//ALLLEDGERENTRIES.LIST'):
#             ledger_name = ledger_entry.find('LEDGERNAME').text
#             amount = ledger_entry.find('AMOUNT').text
#             if ledger_name == debtor:
#                 for allocation in ledger_entry.findall('BILLALLOCATIONS.LIST'):
#                     transactions.append({'Date': date, 'transaction_type': "Child", "Vch No.": vch_no,
#                                          "Ref No.": allocation.find('NAME').text,
#                                          "Ref Type": allocation.find('BILLTYPE').text,
#                                          "Ref Date": " ", "Debtor": ledger_name,
#                                          "Ref Amount": allocation.find('AMOUNT').text,
#                                          'Amount': "NA", "Particulars": ledger_name, "Vch Type": vch_type,
#                                          "Amount Verified": "NA"})
#         for ledger_entry in voucher.findall('.//ALLLEDGERENTRIES.LIST'):
#             ledger_name = ledger_entry.find('LEDGERNAME').text
#             amount = ledger_entry.find('AMOUNT').text
#             if ledger_name != debtor:
#                 transactions.append({'Date': date, 'transaction_type': "Other", "Vch No.": vch_no,
#                                      "Ref No.": "NA",
#                                      "Ref Type": "NA",
#                                      "Ref Date": "NA", "Debtor": ledger_name, "Ref Amount": "NA",
#                                      'Amount': amount, "Particulars": ledger_name, "Vch Type": vch_type,
#                                      "Amount Verified": "NA"})
#                     # continue
#                 # else:
#                 #     print(f"{date}\tOther\t{vch_no}\tNA\tNA\tNA\t{ledger_name}\tNA\t{amount}\t{ledger_name}\t{vch_type}\tNA")
#
#
# print(transactions)
#
#
# import xml.etree.ElementTree as ET
# import pandas as pd
# import os
# import datetime
# def parse_xml(xml_file):
#     tree = ET.parse(xml_file)
#     root = tree.getroot()
#
#     transactions = []
#
#     for voucher in root.findall('.//VOUCHER'):
#         try:
#             voucher_type = voucher.find('.//VOUCHERTYPENAME').text
#             if voucher_type == 'Receipt':
#                 mix_date = voucher.find('DATE').text
#                 # mix_date = find_element(voucher, 'DATE')
#                 date = datetime.strptime(mix_date, "%Y%m%d").date()
#                 vch_type = voucher.find('VOUCHERTYPENAME').text
#                 vch_no = voucher.find('VOUCHERNUMBER').text
#                 debtor = voucher.find('PARTYLEDGERNAME').text
#                 transactions.append({'Date': date, 'transaction_type': "Parent", "Vch No.": vch_no, "Ref No.": "NA",
#                                      "Ref Type": "NA", "Ref Date": "NA", "Debtor": debtor, "Ref Amount": "NA",
#                                      'Amount': voucher.find('ALLLEDGERENTRIES.LIST/AMOUNT').text, "Particulars": debtor,
#                                      "Vch Type": vch_type,
#                                      "Amount Verified": "Yes"})
#
#                 for ledger_entry in voucher.findall('.//ALLLEDGERENTRIES.LIST'):
#                     ledger_name = ledger_entry.find('LEDGERNAME').text
#                     amount = ledger_entry.find('AMOUNT').text
#                     if ledger_name == debtor:
#                         for allocation in ledger_entry.findall('BILLALLOCATIONS.LIST'):
#                             transactions.append({'Date': date, 'transaction_type': "Child", "Vch No.": vch_no,
#                                                  "Ref No.": allocation.find('NAME').text,
#                                                  "Ref Type": allocation.find('BILLTYPE').text,
#                                                  "Ref Date": " ", "Debtor": ledger_name,
#                                                  "Ref Amount": allocation.find('AMOUNT').text,
#                                                  'Amount': "NA", "Particulars": ledger_name, "Vch Type": vch_type,
#                                                  "Amount Verified": "NA"})
#                 for ledger_entry in voucher.findall('.//ALLLEDGERENTRIES.LIST'):
#                     ledger_name = ledger_entry.find('LEDGERNAME').text
#                     amount = ledger_entry.find('AMOUNT').text
#                     if ledger_name != debtor:
#                         transactions.append({'Date': date, 'transaction_type': "Other", "Vch No.": vch_no,
#                                              "Ref No.": "NA",
#                                              "Ref Type": "NA",
#                                              "Ref Date": "NA", "Debtor": ledger_name, "Ref Amount": "NA",
#                                              'Amount': amount, "Particulars": ledger_name, "Vch Type": vch_type,
#                                              "Amount Verified": "NA"})
#         except Exception as e:
#             print(f"Error processing voucher: {e}")
#
#     return transactions
#
#
# def create_spreadsheet(transactions, output_file):
#     df = pd.DataFrame(transactions)
#     df.to_excel(output_file, index=False)
#     print(f"Spreadsheet created successfully at: {output_file}")
#
#
# def main():
#     input_file = 'Input.xml'
#     dir_path = '/Users/arpitamundra/Downloads'
#     input_xml = os.path.join(dir_path, input_file)
#     output_excel = 'output.xlsx'
#
#     try:
#         transactions = parse_xml(input_xml)
#         create_spreadsheet(transactions, output_excel)
#     except Exception as e:
#         print(f"An error occurred: {e}")
#
#
# if __name__ == "__main__":
#     main()
# import pandas as pd
#
# # Assuming the data is in a spreadsheet named 'census_data.xlsx'
# # and the sheet name is 'Sheet1'
# df = pd.read_excel('TownwiseCensus.xls', sheet_name='Sheet1')
#
# # Filter out rows with errors (female literacy > 100% or total females = 0)
# df = df[ (df['Female Literacy Percentage'] <= 100) & (df['Total Females'] > 0)]
#
# # Assuming 'Village' indicates a village and 'TOWN' indicates a town
# df_filtered = df[df['VILLAGE'] == 'VILLAGE']
#
# # Assuming 'Total Households' indicates the number of households
# df_filtered = df_filtered[df_filtered['Total Households'] >= 200]
#
# # Calculate the percentage of literate females per C.D. Block
# df_grouped = df_filtered.groupby('CD BLOCK')['Female Literates'].sum() / df_filtered.groupby('CD BLOCK')['Total Females'].sum() * 100
#
# # Get the C.D. Block code with the highest percentage
# block_code = df_grouped.idxmax()
#
# # Print the C.D. Block Code
# print(block_code)


import pandas as pd

# Assumptions:
# 1. The Excel file contains columns for C.D. Block code, village name, total households, total females, and female literacy percentage.
# 2. We are only interested in villages with at least 200 households.
# 3. We will ignore rows where the female literacy percentage is more than 100% or the total number of females is 0.

# Load the Excel file
file_path = "/Users/arpitamundra/PycharmProjects/python practice /Book 7.xlsx"
data = pd.read_excel(file_path)

# Filter out rows with less than 200 households and errors in data
filtered_data = data[(data['No of Households'] >= 200) &
                     (data['Literates Population Female'] <= 100) &
                     (data['Total Population Female'] > 0)]

# Calculate the percentage of literate rural females for each C.D. Block
filtered_data['Literate Rural Female Percentage'] = (filtered_data['Total Population Female'] *
                                                      filtered_data['Literates Population Female'] / 100) / filtered_data['No of Households'] * 100

# Find the C.D. Block code with the highest percentage of literate rural females
# highest_literate_rural_female_block = filtered_data.loc[filtered_data['Literate Rural Female Percentage'].idxmax(), 'CD Block_Code']
if not filtered_data.empty:
    # Find the C.D. Block code with the highest percentage of literate rural females
    highest_literate_rural_female_block = filtered_data.loc[filtered_data['Literate Rural Female Percentage'].idxmax(), 'CD Block_Code']
    print(highest_literate_rural_female_block) # Output: CID_Block_Code
else:
    print("No data found after filtering.")
# print(highest_literate_rural_female_block)  # Output: CID_Block_Code


# filtered_data = data[data['No of Households'] >= 200]
#
# if not filtered_data.empty:
#     print("Data found after filtering on 'No of Households' >= 200.")
# else:
#     print("No data found after filtering on 'No of Households' >= 200.")


# Converting xls file to xlsx format
import pandas as pd
# Load the Excel file
file_path = "/Users/arpitamundra/PycharmProjects/python practice /Book 7.xlsx"
data = pd.read_excel(file_path)


# Creating Female Literacy Percentage
data['Female Literacy Percentage'] = (data['Literates Population Female'] / data['Total Population Female']) * 100
filtered_data = data[(data['No of Households'] >= 200) & (data['Female Literacy Percentage'] <= 100) & (data['Total Population Female'] > 0) & (data['Total/Rural/Urban'] == "Rural" )]


if not filtered_data.empty:
    highest_literate_rural_female_block = filtered_data.loc[filtered_data['Female Literacy Percentage'].idxmax(), 'CD Block_Code']
    print(highest_literate_rural_female_block)
    print("Data found after filtering on 'No of Households' >= 200 and 'Literates Population Female' <= 100.")
else:
    print("No data found after filtering on 'No of Households' >= 200 and 'Literates Population Female' <= 100.")

# output : 284