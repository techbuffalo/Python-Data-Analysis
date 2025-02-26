import altair as alt
import pandas as pd
import requests
import streamlit as st
from mitreapi import AttackAPI

url = "https://services.nvd.nist.gov/rest/json/cves/2.0"
page = requests.get(url)
KVEWebData = page.json()

# Extract the 'vulnerabilities' list from the JSON response
vulnerabilities = KVEWebData.get('vulnerabilities', [])

# Create a list to store the extracted data
data_list = []

# Extract relevant information from each vulnerability
for vuln in vulnerabilities:
    cve_data = vuln.get('cve', {})
    data_list.append({
        'id': cve_data.get('id'),
        'published': cve_data.get('published'),
        'lastModified': cve_data.get('lastModified'),
        'description': cve_data.get('descriptions', [{}])[0].get('value', '')
    })

# Create a DataFrame from the extracted data
cisaDF = pd.DataFrame(data_list)

# Display the first few rows of the DataFrame
print(cisaDF.columns())