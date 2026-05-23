import streamlit as st
import pandas as pd
from archobj import arcobj

def listObj(objCol, type_id, arcStyle, col1, col2):
    with col2:
        obj_documents = objCol.find({"type_id": type_id}).sort("objName", 1)
        obj_doc_list = list(obj_documents)
        df = pd.DataFrame(obj_doc_list)
        df_lim = df.iloc[:, 1:2]
        with st.container(border=True, width="content"):
            st.write("**Виберіть архітектурний об'єкт:**")
            sel = st.dataframe(df_lim, selection_mode="single-row", on_select="rerun",
                    width="content", height="content")
        sel_rows = sel["selection"]["rows"]
        if len(sel_rows) > 0:
            sel_row = sel_rows[0]
            sel_obj = obj_doc_list[sel_row]
            obj_name = sel_obj.get("objName")
            obj_id = sel_obj.get("_id")
            with col1:
                st.markdown("""<h1 style="text-align: center; color: red; font-family:
                    'Times New Roman', Times, serif;font-size:30px;">""" + obj_name + "</h1>",
                            unsafe_allow_html=True)
                arcobj(sel_obj, arcStyle, col1, col2)
