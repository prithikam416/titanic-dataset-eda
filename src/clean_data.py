"""
clean_data.py - Data Cleaning and Preprocessing for Titanic Dataset
"""

import pandas as pd
import numpy as np

def clean_titanic_data(filepath):
    # Load dataset
    df = pd.read_csv(filepath)
    print(f"[INFO] Loaded Titanic dataset with {df.shape[0]} rows and {df.shape[1]} columns.")
    
    # 1. Handle Missing Values
    # Age: Impute using median age of passengers in the same Pclass (Passenger Class)
    df['Age'] = df.groupby('Pclass')['Age'].transform(lambda x: x.fillna(x.median()))
    
    # Embarked: Fill missing with mode (most frequent port)
    mode_embarked = df['Embarked'].mode()[0]
    df['Embarked'].fillna(mode_embarked, inplace=True)
    
    # Cabin: Drop Cabin column since >77% values are missing
    if 'Cabin' in df.columns:
        df.drop(columns=['Cabin'], inplace=True)
        print("[INFO] Dropped Cabin column due to high proportion of missing values.")
        
    # 2. Feature Engineering
    # Create FamilySize column
    df['FamilySize'] = df['SibSp'] + df['Parch'] + 1
    
    # Create IsAlone column (1 if alone, 0 otherwise)
    df['IsAlone'] = np.where(df['FamilySize'] == 1, 1, 0)
    
    # Extract Titles from Name column (e.g. Mr, Mrs, Miss, Master, Rare)
    def get_title(name):
        title_search = re.search(r' ([A-Za-z]+)\.', name)
        if title_search:
            return title_search.group(1)
        return ""
    
    import re
    df['Title'] = df['Name'].apply(get_title)
    df['Title'] = df['Title'].replace(['Lady', 'Countess','Capt', 'Col','Don', 'Dr', 'Major', 'Rev', 'Sir', 'Jonkheer', 'Dona'], 'Rare')
    df['Title'] = df['Title'].replace('Mlle', 'Miss')
    df['Title'] = df['Title'].replace('Ms', 'Miss')
    df['Title'] = df['Title'].replace('Mme', 'Mrs')
    
    # Save cleaned data to a new CSV file
    output_path = filepath.replace(".csv", "_cleaned.csv")
    df.to_csv(output_path, index=False)
    print(f"[SUCCESS] Cleaned dataset saved to {output_path}")
    return df

if __name__ == "__main__":
    clean_titanic_data("data/titanic.csv")
