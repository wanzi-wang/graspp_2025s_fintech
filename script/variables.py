import os
import pandas as pd
from pandas.io.stata import StataReader

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

state_dir = '/Users/snakada/Library/CloudStorage/GoogleDrive-snakada@g.ecc.u-tokyo.ac.jp/マイドライブ/大学/2025/2025 S1S2 Data Science for Public Policy/dataset/org/household/stata'
returnfile = 'data_processed/householdSurvey_variables.csv'
listVariable(state_dir, returnfile)

state_dir = '/Users/snakada/Library/CloudStorage/GoogleDrive-snakada@g.ecc.u-tokyo.ac.jp/マイドライブ/大学/2025/2025 S1S2 Data Science for Public Policy/dataset/org/mobileAccess'
returnfile = 'data_processed/mobileAccess_variables.csv'
listVariable(state_dir, returnfile)

