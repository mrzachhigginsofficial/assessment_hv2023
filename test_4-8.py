import pandas as pd

def test_empty_cpt_codes():
   df = pd.read_csv('data\\sample_claims.csv', na_filter=False).convert_dtypes(infer_objects=True)
   duplicates = df[df['procedure_code'].isnull() | (df['procedure_code'] == "")]   
   assert len(duplicates) == 0, "There are claims with empty/null cpt codes."