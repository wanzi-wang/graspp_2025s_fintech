import os
import pandas as pd
from pandas.io.stata import StataReader
import fitz


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


def listVariable(state_dir, return_file):
    # Directory containing your .dta files
    all_vars = []

    for filename in os.listdir(state_dir):
        if filename.endswith('.dta'):
            filepath = os.path.join(state_dir, filename)
            with StataReader(filepath) as reader:
                # Variable labels
                var_labels = reader.variable_labels()
                # Data label (label for the whole dataset)
                data_label = reader.data_label  # May be empty string if not set
                for var, label in var_labels.items():
                    all_vars.append({
                        'file': filename,
                        'data_label': data_label,
                        'variable': var,
                        'variable_label': label
                    })

    # Create DataFrame
    result_df = pd.DataFrame(all_vars)

    # Display or export
    print(result_df)
    result_df.to_csv(return_file, index=False)

    return True

def extractUniqueValue(df, col):
    return df[col].unique()

def extractTextFromPDF(source, pages):
    res = {}
    doc = fitz.open(source)
    for num in pages:
        res[num]=doc.load_page(num).get_text()
    return res


def extractTextFromPDF2(sourceNum, pages):
    match sourceNum:
        case 1: source = 'data_original/CAMS Report_October_N.pdf'
        case 2: source = 'data_original/Final_Report_HCES_2023-24L.pdf'
        case _: source = "none"
    if source != "none":
        return extractTextFromPDF(source, pages)
    else:
        print('select 1 for digital access, 2 for houshold status')
        return False

def formatText(myText, stateNames):
    lines = myText.strip().split('\n')

    result = []
    current_state = None
    current_numbers = []

    def is_state_name(line):
        res = False
        if line in stateNames:
            res = True
        return res

    def is_number_line(line):
        return all(is_number(part.replace(',', '')) for part in line.split())

    for line in lines:
        line = line.strip()
        if is_state_name(line):
            if current_state and current_numbers:
                result.append([current_state] + current_numbers)
            current_state = line
            current_numbers = []
        elif is_number_line(line):
            numbers = line.split()
            current_numbers.extend(numbers)

    if current_state and current_numbers:
        result.append([current_state] + current_numbers)

    return result

def is_number(string):
    """Check if a string represents a valid number (including decimals)"""
    try:
        float(string)
        return True
    except ValueError:
        return False

def getTableFromPDF(sourceNum, pages):
    match sourceNum:
        case 1: 
            source = 'data_original/CAMS Report_October_N.pdf'
            stateName = stateNames2
        case 2: 
            source = 'data_original/Final_Report_HCES_2023-24L.pdf'
            stateName = stateNames1
        case _: source = "none"
    if source == "none":
        print('select 1 for digital access, 2 for houshold status')
        return False
    else:
        pageContents = extractTextFromPDF(source, pages)
        res = {}
        for i in pages:
            data = formatText(pageContents[i], stateName)
            colCount = len(data[0])
            colNames = [f'col{i}' for i in range(1, colCount+1)]
            df = pd.DataFrame(data, columns=colNames)
            res[i]=df

        return res
    