import json

with open('companies.txt') as c_file, open("companies.json", "w") as cj_file:
    data = c_file.readlines()
    companies_profit = {}
    companies_loss = {}
    avr_profit = {}
    for line in data:
        if float(line.split()[2]) >= float(line.split()[3]):
            company = line.split()[0]
            companies_profit[company] = float(line.split()[2]) - float(line.split()[3])
        else:
            company = line.split()[0]
            companies_loss[company] = float(line.split()[2]) - float(line.split()[3])
    p_average = sum(companies_profit.values())/len(companies_profit.values())
    avr_profit['average_profit'] = p_average
    companies_list = [companies_profit, avr_profit, companies_loss]
    json.dump(companies_list, cj_file)
    print(companies_list)
