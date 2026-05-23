import streamlit as st
import pandas as pd
from use_db import create_client, use_collections
from objList import listObj


st.set_page_config(layout="wide")
st.markdown("""<h1 style="text-align: center; color: blue; font-family: 
    'Times New Roman', Times, serif;font-size:60px;">Архітектура середньовічного Львова</h1>""",
    unsafe_allow_html=True)

col1, col2 = st.columns(2)

with col1:
    client = create_client()
    collections = use_collections(client)
    typeCol = collections["Type"]
    objCol = collections["Obj"]
    arcStyle = collections["Style"]

    # type_documents = typeCol.find({"norm": "1"}).sort("typeName", 1)
    type_documents = typeCol.find({}).sort("typeName", 1)
    type_doc_list = list(type_documents)
    df = pd.DataFrame(type_doc_list)
    df_lim = df.iloc[:, 1:2]
    with st.container(border=True, width="content"):
        st.write("**Виберіть тип архітектурних об'єктів:**")
        sel = st.dataframe(df_lim, selection_mode="single-row", on_select="rerun",
                width="content", height="content")
    sel_rows = sel["selection"]["rows"]
    if len(sel_rows) > 0:
        sel_row = sel_rows[0]
        sel_type = type_doc_list[sel_row]
        arcType = sel_type.get("typeName")
        type_id = sel_type.get("_id")
        with col2:
            st.markdown("""<h1 style="text-align: center; color: green; font-family: 
                'Times New Roman', Times, serif;font-size:40px;">""" + arcType+ "</h1>",
                        unsafe_allow_html=True)
            listObj(objCol, type_id, arcStyle, col1, col2)
