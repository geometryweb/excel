import streamlit as st
import pandas as pd
import time

st.title("엑셀, CSV파일 뷰어")
file = st.file_uploader("파일을 업로드하기(csv, 엑셀 문서(excel)", type = ["csv", "xls", "xlsx"])


if file is not None:
    extension = file.name.split(".")[-1].lower()
    time.sleep(3)
    
    try:
        if extension == "csv":
            df = pd.read_csv(file)
        elif extension in ["xls", "xlsx"]:
            df = pd.read_excel(file, engine = "openpyxl")

        st.dataframe(df, hide_index = True)
        
    except Exception as e:
        st.error(f"파일을 읽는중 오류가 발생했습니다. 오류 내용: {e}")
        
            
    