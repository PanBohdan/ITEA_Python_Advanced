test_range = range(100)
test_list = []
for j in test_range:
    if j % 2 == 0:
        test_list.append(j)
print(test_list)
#  створити словник з 5 країн і їх столиць
country_dict = {
    'Ukraine': 'Kyiv',
    'Germany': 'Berlin',
    'France': 'Paris',
    'Slovakia': 'Bratislava',
    'USA': 'Washington, D.C.'

}
#  створити список з довільної кількості країн
country_list = ['Angola', 'Argentina', 'Bolivia', 'Belgium',
                'Netherlands', 'Italy', 'Mongolia', 'India',
                'Pakistan', 'Bangladesh', 'Vietnam', 'Cambodia',
                'Mexico', 'Iran', 'Iraq', 'Poland',
                'Lithuania', 'Latvia', 'Estonia', 'Bulgaria',
                'Greece', 'Turkey', 'Egypt', 'France',
                'South Africa', 'Ukraine', 'USA', 'Germany']

for j in country_list:
    if country_dict.get(j):
        print(f'{country_dict[j]} is a capital of {j}')
