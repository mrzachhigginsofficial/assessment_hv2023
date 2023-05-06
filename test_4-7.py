import pandas as pd

def test_date_chronological_errors():
   df = pd.read_csv('data\\sample_claims.csv', na_filter=False).convert_dtypes(infer_objects=True)
   df["date_service"] = pd.to_datetime(df["date_service"], errors='coerce')
   df["date_received"] = pd.to_datetime(df["date_received"], errors='coerce')
   
   df = df[(df["date_service"].isnull() == False) | (df["date_received"].isnull() == False)]
   df["out_of_order"] = (df["date_service"] < df["date_received"])
   
   result = len(df[df['out_of_order'] == True])
   assert result == 0, "Date received before service date."
