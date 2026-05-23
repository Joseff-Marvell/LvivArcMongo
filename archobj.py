import streamlit as st

def arcobj(sel_obj, arcStyle, col1, col2):
    descr = sel_obj.get("descr")
    curaddr = sel_obj.get("curaddr")
    styleid = sel_obj.get("style_id")
    doc = arcStyle.find_one({"_id": styleid})
    if doc is not None:
        styleName = doc["styleName"]
        styleInfo = doc["info"]
    else:
        styleName = ""
        styleInfo = ""
    img = sel_obj.get("image")
    image = "./images/" + img
    with st.container(horizontal=True, horizontal_alignment="center", border=True):
        st.image(image, width=600)
        st.write(descr)
    with col2:
        with st.container(horizontal=False, horizontal_alignment="center",
                border=True, width="content"):
            st.write("Сучасна адреса: " + curaddr)
            if styleName != "":
                st.write("Архітектурний стиль: " + styleName)
            if styleInfo != "":
                st.write("Детальніше. " + styleInfo)