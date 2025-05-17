import pandas as pd

with open('datasets/column_names.txt') as f:
    column_names = f.read().split(',')

with open('datasets/class_labels.txt') as f:
    class_labels = f.read().split(',')

def clean_csv(csv_path):

    df = pd.read_csv(csv_path)

    # Rename column names to snake_case
    
    df.columns = column_names

    # One-hot encode finding label classes
    
    df['finding_labels'] = df['finding_labels'].str.lower()
    
    for col in class_labels:
        df[col] = df['finding_labels'].apply(lambda x: 1 if col in x else 0)
    
    df.drop('finding_labels', axis=1, inplace=True)

    # Parse ages
    
    df['patient_age'] = df['patient_age'].apply(lambda x: int(x[:-1]) if x.endswith('Y') \
                                                else int(x[:-1]) / 12 if x.endswith('M') else x)
    df['patient_age'] = df['patient_age'].apply(lambda x: 0 if str(x).endswith('D') else x)
    df['patient_age'] = df['patient_age'].astype(int)

    # One-hot encode 'gender'
    
    df['patient_gender_M'] = df['patient_gender'].apply(lambda x: 1 if x == 'M' else 0)
    df['patient_gender_F'] = df['patient_gender'].apply(lambda x: 1 if x == 'F' else 0)
    df.drop('patient_gender', axis=1, inplace=True)

    # One-hot encode 'view_position'
    
    df['view_position_AP'] = df['view_position'].apply(lambda x: 1 if x == 'AP' else 0)
    df['view_position_PA'] = df['view_position'].apply(lambda x: 1 if x == 'PA' else 0)
    df.drop('view_position', axis=1, inplace=True)

    df.to_csv(f"{csv_path}_clean.csv", index=False)
