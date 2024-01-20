import requests
url = 'https://script.googleusercontent.com/macros/echo?user_content_key=gDXDN6BGmuIiD1cPT33m2WU1gjiWkVK-p7PPjPiGbBpPSj3e8nUL7xia3u61E4kwWh1-0PySJFQL-kCbIhnLgD1deptCzzkom5_BxDlH2jW0nuo2oDemN9CCS2h10ox_1xSncGQajx_ryfhECjZEnCaVp0CmChaBTtltHpOv3KL5xkQ45_4XoTFzK_KFFw1QJqjq-U3D5-fM53G8eCK34l7qGerMCjyRlUdsOb1k7DcsblFMU1GF7tz9Jw9Md8uu&lib=MYuB66jlF_R_bHdKmf6d4rIrEEQWGsqde'
response = requests.get(url=url)
data_from_net = response.json()
# print(data_from_net)
financial = data_from_net['financial']

total_budget = 0
q_ty_large_family = 0
q_ty_families = 0
q_ty_women = 0
for people in financial:
    if people['large_family'] == True and people['age'] > 35:
        budget = people['monthly_budget']
        total_budget += budget
    if people['large_family'] == True:
            large_family = people['large_family']
            q_ty_large_family += large_family
    if people['loan_expenses_per_month'] > people['monthly_budget']:
        family = 1
        q_ty_families += family
    if people['gender'] =='w' and people['own_house'] == True:
        women = 1
        q_ty_women += women

print(f'{total_budget=}')
print(f'{q_ty_large_family=}')
print(f'{q_ty_families=}')
print(f'{q_ty_women=}')
