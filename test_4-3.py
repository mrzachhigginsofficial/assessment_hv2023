import pandas as pd

def test_invalid_diagnosis_codes():
   df_claims = pd.read_csv('data\\sample_claims.csv', na_filter=False).convert_dtypes(infer_objects=True)
   df_codes_icd10 = pd.read_csv('data\\valid_icd_10_codes.csv', na_filter=False).astype({'code': 'string'})   
   
   df = (df_claims
      .assign(row_number=range(len(df_claims)))
      .assign(diagnosis_codes=df_claims['diagnosis_codes'].str.split('^'))
      .explode('diagnosis_codes')
      .merge(df_codes_icd10, left_on='diagnosis_codes', right_on='code', how='left', indicator=True))
   
   assert len(df[df['code'].isnull()]) == 0, "Invalid diagnosis codes detected. Does not exist in icd10 codes extract."
   