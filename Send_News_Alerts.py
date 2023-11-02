import streamlit as st
import requests
import json

st.set_page_config(
    page_title="Send News Alerts",
    page_icon="👋",
)


st.sidebar.success("Powered by Innovation Foundry")
st.title("CSend News Alerts")

msg= st.text_input("Type your Message.")
subscribers = st.text_input("Enter your 11-digit phone numbers (947XXXXXXXX) with seperated commas.", )



submit = st.button("Send")

if submit:
    #create group
    payload = {
    "typing_time": 0,
    "to": "94711486601",
    "body": "testr"
    }
    headers = {
        "accept": "application/json",
        "content-type": "application/json",
        "authorization": "Bearer ab9fNNPC51r8pbwW8FUuRaNv3x1SaGsK"
    }

    response = requests.post(url, json=payload, headers=headers)
    print(response.text)
    data = json.loads(response.text)

    print(data['group_id'])
    #add admin as a member
    url2 = "https://gate.whapi.cloud/groups/"+data['group_id']+"/participants"

    print(url2)

    payload2 = { "participants": [admin] }
    headers2 = {
        "accept": "application/json",
        "content-type": "application/json",
        "authorization": "Bearer ab9fNNPC51r8pbwW8FUuRaNv3x1SaGsK"
    }

    response = requests.post(url2, json=payload2, headers=headers2)
    print(response.text)
    #make admin
    url = "https://gate.whapi.cloud/groups/"+data['group_id']+"/admins"

    payload = { "participants": [admin] }
    headers = {
        "accept": "application/json",
        "content-type": "application/json",
        "authorization": "Bearer ab9fNNPC51r8pbwW8FUuRaNv3x1SaGsK"
    }

    response = requests.patch(url, json=payload, headers=headers)

    print(response.text)
    st.write("Congratulations! "+data['group_id']+" is created successfully. (Please Copy given group id.)")

