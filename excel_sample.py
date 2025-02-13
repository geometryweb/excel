import pandas as pd
import streamlit as st
import os
st.markdown("""
            <style>
            
            /*.e14lo1l1.st-emotion-cache-jl9d4a.ex0cdmw0 */
            /*.st-emotion-cache-1ba8tjn.e1d5ycv523 */
            /*.e14lo1l1.st-emotion-cache-jl9d4a.ex0cdmw0 */
            .e1fexwmo1.st-emotion-cache-jl9d4a.ex0cdmw0 {
                display: none;
                visibility: hidden;
            }   
            </style>
            """, unsafe_allow_html=True)

df = pd.read_excel(
        io= "pages/sample.xlsx",        
        sheet_name= "통계",
        header= 0,  
        usecols="A:H",
        engine= "openpyxl",
).dropna()
st.dataframe(df)

secret_token = os.getenv("SECRET_TOKEN")

# 앱에서 시크릿 사용하기
st.write(f"Token: {secret_token}")

st.write("1")