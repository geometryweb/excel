import pandas as pd
import streamlit as st

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