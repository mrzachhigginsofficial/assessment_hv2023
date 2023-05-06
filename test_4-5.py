import pandas as pd

def test_date_service_parse():
   df = pd.read_csv('data\\sample_claims.csv', na_filter=False).convert_dtypes(infer_objects=True)
   df["date_service"] = pd.to_datetime(df["date_service"], errors='coerce')
   result = len(df[df['date_service'].isnull()])
   assert result == 0, "Invalid service dates have been found. Dates could note be parsed to a valid timestamp."