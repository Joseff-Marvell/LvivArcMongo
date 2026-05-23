import streamlit as st
import pymongo


def create_client():
    username = st.secrets["mongoDB"]["username"]
    password = st.secrets["mongoDB"]["password"]
    cluster_name = st.secrets["mongoDB"]["cluster_name"]
    uri = "mongodb+srv://" + username + ":" + password + "@" + cluster_name + ".mongodb.net"
    client = pymongo.MongoClient(uri)
    return client
    
def use_collections(client):
    db = client.ArcLviv
    typecol = db.ArcType
    stylecol = db.ArcStyle
    objcol = db.ArcObj
    return {"Obj":objcol, "Type":typecol, "Style":stylecol}

    