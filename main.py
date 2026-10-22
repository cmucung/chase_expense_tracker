from fastapi import FastAPI, UploadFile, File
import pandas as pd  

app = FastAPI()

@app.post("/upload")
def upload(file: UploadFile = File(...)):
    df = pd.read_csv(file.file, index_col=False)
    return {"rows": len(df), "columns": list(df.columns)}