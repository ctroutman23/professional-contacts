import pandas as pd


# This file automates the process of fitering our professional contacts to certain professions
# (i.e. insurance agents, realtors, etc.)


# Read in contacts csv to pandas df
professional_contacts_df = pd.read_csv("data/Evegreen-Professional-Relationships-List.csv")


# Insurance Contacts
insurance_contacts_df = professional_contacts_df[
  professional_contacts_df['Profession'].str.strip().str.lower() == 'insurance agent'
  ]

# print(insurance_contacts_df)

# write to new csv
insurance_contacts_df.to_csv("data/evergreen_insurance_contacts.csv")


# Realtors
realtor_contacts_df = professional_contacts_df[
    professional_contacts_df['Profession'].str.contains('realtor', case=False, na=False)
]

print(realtor_contacts_df)

# write to new csv
insurance_contacts_df.to_csv("data/evergreen_realtor_contacts.csv")