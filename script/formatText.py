import functionsNakada
import pandas as pd

stateNames1 = [
    'Andhra Pradesh ',
    'Arunachal Pradesh',
    'Assam',
    'Bihar',
    'Chhattisgarh',
    'Delhi',
    'Goa',
    'Gujarat',
    'Haryana',
    'Himachal Pradesh',
    'Jharkhand',
    'Karnataka',
    'Kerala',
    'Madhya Pradesh',
    'Maharashtra',
    'Manipur',
    'Meghalaya',
    'Mizoram',
    'Nagaland',
    'Odisha',
    'Punjab',
    'Rajasthan',
    'Sikkim',
    'Tamil Nadu',
    'Telangana',
    'Tripura',
    'Uttar Pradesh',
    'Uttarakhand',
    'West Bengal',
    'Andaman & N. Island',
    'Chandigarh',
    'Dadra & Nagar Haveli',
    'Jammu & Kashmir',
    'Ladakh',
    'Lakshadweep',
    'Puducherry',
    'All-India'
]

stateNames2 = [
    'Andhra Pradesh',
    'Arunachal Pradesh',
    'Assam',
    'Bihar',
    'Chhattisgarh',
    'Delhi',
    'Goa',
    'Gujarat',
    'Haryana',
    'Himachal Pradesh',
    'Jharkhand',
    'Karnataka',
    'Kerala',
    'Madhya Pradesh',
    'Maharashtra',
    'Manipur',
    'Meghalaya',
    'Mizoram',
    'Nagaland',
    'Odisha',
    'Punjab',
    'Rajasthan',
    'Sikkim',
    'Tamil Nadu',
    'Telangana',
    'Tripura',
    'Uttar Pradesh',
    'Uttarakhand',
    'West Bengal',
    'A & N Islands',
    'Chandigarh',
    'Dadra & Nagar Haveli & Daman &',
    'Dadra & Nagar Haveli',
    'Jammu & Kashmir',
    'Ladakh',
    'Lakshadweep',
    'Puducherry',
    'all-India'
]

source = 'data_original/Final_Report_HCES_2023-24L.pdf'
pages = [80,81,82]
lines = functionsNakada.extractTextFromPDF(source, pages)
# print(lines[81])

data81 = functionsNakada.formatText(lines[81], stateNames1)
colCount81 = len(data81[0])
colNames81 = [f'col{i}' for i in range(1, colCount81+1)]

HHdata81 = pd.DataFrame(data81, columns=colNames81)
print(HHdata81)

print('---------------------------------------')
source = 'data_original/CAMS Report_October_N.pdf'
pages = [80,81,82]
lines = functionsNakada.extractTextFromPDF(source, pages)

data81 = functionsNakada.formatText(lines[81], stateNames2)
colCount81 = len(data81[0])
colNames81 = [f'col{i}' for i in range(1, colCount81+1)]

# print(len(data81))
# for i in range(len(data81)):
#     print('-----------------------------')
#     print(len(data81[i]))
#     print(data81[i][0])

CAMdata81 = pd.DataFrame(data81, columns=colNames81)
print(CAMdata81)
