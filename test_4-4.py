import pandas as pd

def test_invalid_cpt_codes():
   df_claims = pd.read_csv('data\\sample_claims.csv', na_filter=False).convert_dtypes(infer_objects=True)
   df_codes_cpt = pd.read_csv('data\\valid_cpt_codes.csv', na_filter=False).convert_dtypes(infer_objects=True)
   df_codes_cpt = df_codes_cpt.astype({'code': 'string'})   
   
   df = df_claims.merge(df_codes_cpt, left_on='procedure_code', right_on='code', how='left')
   assert len(df[df['code'].isnull()]) == 0, "Invalid CPT codes detected. Does not exist in CPT codes extract."