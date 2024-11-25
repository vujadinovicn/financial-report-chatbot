import pandas as pd

coverpage_use_cols = ["ACCESSION_NUMBER", "REPORTCALENDARORQUARTER", 'FILINGMANAGER_NAME', 'FILINGMANAGER_STREET1', 'FILINGMANAGER_STREET2', 'FILINGMANAGER_CITY', 'FILINGMANAGER_STATEORCOUNTRY', 'FILINGMANAGER_ZIPCODE']
coverpage = pd.read_csv("COVERPAGE.tsv", usecols=coverpage_use_cols,
                        header = 0,delimiter='\t', dtype={'FIGI': str, 'PUTCALL': str, "OTHERMANAGER": str})
coverpage = coverpage.rename(columns={'FILINGMANAGER_NAME': 'managerName', 'REPORTCALENDARORQUARTER': 'reportCalendarOrQuarter'})
coverpage['managerAddress'] = coverpage[
    ['FILINGMANAGER_STREET1', 'FILINGMANAGER_STREET2',
     'FILINGMANAGER_CITY', 'FILINGMANAGER_STATEORCOUNTRY',
     'FILINGMANAGER_ZIPCODE']
].fillna('').apply(lambda row: ', '.join([val for val in row if val]), axis=1)
coverpage.drop(['FILINGMANAGER_STREET1', 'FILINGMANAGER_STREET2', 'FILINGMANAGER_CITY', 'FILINGMANAGER_STATEORCOUNTRY', 'FILINGMANAGER_ZIPCODE'], axis=1, inplace=True)

infotable_use_cols = ["ACCESSION_NUMBER", 'CUSIP', "VALUE", "SSHPRNAMT", "NAMEOFISSUER"]
infotable = pd.read_csv("INFOTABLE.tsv", usecols=infotable_use_cols,
                        header = 0,delimiter='\t', dtype={'ACCESSION_NUMBER': str, "CUSIP": str})
infotable = infotable.rename(columns={"CUSIP": "cusip", "VALUE": "value", "SSHPRNAMT": "shares", "NAMEOFISSUER": "companyName"})

infotable['cusip6'] = infotable['cusip'].str[:6]

other_manager_cols = ["ACCESSION_NUMBER", "CIK"]
other_manager = pd.read_csv("OTHERMANAGER.tsv", usecols=other_manager_cols,
                        header = 0,delimiter='\t', dtype={'ACCESSION_NUMBER': str, 'CIK': str})
other_manager = other_manager.rename(columns={"CIK": "managerCik"})

other_manager2 = pd.read_csv("OTHERMANAGER2.tsv", usecols=other_manager_cols,
                        header = 0,delimiter='\t', dtype={'ACCESSION_NUMBER': str, 'CIK': str})
other_manager2 = other_manager2.rename(columns={"CIK": "managerCik"})

other_manager = pd.concat([other_manager, other_manager2], ignore_index=True)

other_manager['source'] = other_manager.apply(
    lambda row: f"https://sec.gov/Archives/edgar/data/{row['managerCik']}/{row['ACCESSION_NUMBER']}.txt", axis=1
)
# row = other_manager.iloc[0]  # Get the first row
# url = f"https://sec.gov/Archives/edgar/data/{row['managerCik']}/{row['ACCESSION_NUMBER']}.txt"
# print(url)
# print(other_manager["source"])

companies_cols = ["CUSIP", "CIK"]
companies = pd.read_csv("data/company_metadata.tsv", usecols=companies_cols,
                        header = 0,delimiter='\t', dtype={'CUSIP': str, 'CIK': str})
companies = companies.rename(columns={"CUSIP": "cusip"})

result = pd.merge(companies, infotable, on='cusip', how='left')
# result = pd.merge(result, other_manager, on='ACCESSION_NUMBER', how='left')
result = pd.merge(result, coverpage, on='ACCESSION_NUMBER', how='left')
# print(result["source"])
result.to_csv('all_merged_tables.tsv', sep='\t', index=False, encoding='utf-8')

# nan_counts = result.isna().sum()

# Display columns with NaN values and their counts
# print(nan_counts[nan_counts > 0])
# print(result["source"])

print(result.head())


# matching_columns = []
# for column in result.columns:
#     if result[column].astype(str).str.contains('ROYAL BANK PLAZA,', case=False, na=False).any():
#         matching_columns.append(column)
# print(matching_columns)
# if result["managerAddress"].astype(str).str.contains('ROYAL BANK PLAZA,', case=False, na=False).any():
#     print("YES")
# b = pd.read_csv("file1.csv").astype(basestring)
#
# merged= a.merge(b, on='objectID',how='outer')
#
# merged.to_csv("output.csv", index=False)