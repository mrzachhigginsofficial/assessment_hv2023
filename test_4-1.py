import pandas as pd

def test_duplicate_claim_ids():
   df = pd.read_csv('data\\sample_claims.csv', na_filter=False).convert_dtypes(infer_objects=True)
   duplicates = df[df.duplicated(['claim_id'], keep=False)]   
   assert len(duplicates) == 0, "There are duplicate claim ID's."