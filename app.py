import streamlit as st
import requests
import json

def main():
    st.title("API Frontend - POST-GET Debugger")
    url_API =st.text_input("inserisci url dell'api","http://localhost:8000/predict")
    rd = st.number_input("R&D",0,1000000,73721)
    adm = st.number_input("Administration",0,1000000,121344)
    mrk = st.number_input("Marketing Spend",0,1000000,211025)

    ############## GET REQUEST #################
    if st.button("Predict with GET"):
        url = url_API
        url2 = f"?rd={rd}&adm={adm}&mrk={mrk}"
        link = url+url2
        st.write('"{}"'.format(link))
        response = requests.get(link)
        result =response.json()
        st.success(f"The result is: {result['prediction']}")

    ############## POST REQUEST #################
    if st.button("Predict with POST"):
        url = url_API
        response =requests.post(url,
                                headers={"Content-Type": "application/json"},
                                data = json.dumps({
                                                   "rd":rd,
                                                   "adm":adm,
                                                   "mrk":mrk,
                                                   })
                                )
        result =response.json()
        st.success(f"The result is: {result['prediction']}")

if __name__ == '__main__':
    main()