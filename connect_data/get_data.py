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
                        header = 0,delimiter='\t', dtype={'ACCESSION_NUMBER': str})
infotable = infotable.rename(columns={"CUSIP": "cusip", "VALUE": "value", "SSHPRNAMT": "shares", "NAMEOFISSUER": "companyName"})

infotable['cusip6'] = infotable['cusip'].str[:6]

other_manager_cols = ["ACCESSION_NUMBER", "CIK"]
other_manager = pd.read_csv("OTHERMANAGER.tsv", usecols=other_manager_cols,
                        header = 0,delimiter='\t', dtype={'ACCESSION_NUMBER': str, 'CIK': str})
other_manager = other_manager.rename(columns={"CIK": "managerCik"})

other_manager['source'] = other_manager.apply(
    lambda row: f"https://sec.gov/Archives/edgar/data/{row['managerCik']}%2F{row['ACCESSION_NUMBER']}.txt", axis=1
)
# row = other_manager.iloc[0]  # Get the first row
# url = f"https://sec.gov/Archives/edgar/data/{row['managerCik']}/{row['ACCESSION_NUMBER']}.txt"
# print(url)
# print(other_manager["source"])

result = pd.merge(other_manager, infotable, on='ACCESSION_NUMBER', how='left')
result = pd.merge(result, coverpage, on='ACCESSION_NUMBER', how='outer')



print(result.head())
# print(result["source"])


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