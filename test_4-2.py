import pandas as pd

def test_empty_diagnosis_codes():
   df = pd.read_csv('data\\sample_claims.csv', na_filter=False).convert_dtypes(infer_objects=True)
   duplicates = df[df['diagnosis_codes'].isnull() | (df['diagnosis_codes'] == "")]   
   assert len(duplicates) == 0, "There are claims with empty/null diagnosis codes."