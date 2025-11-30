import streamlit as st
import requests

def load_history(api_url):
    st.sidebar.markdown("## 🕘 Prediction History")

    # Load history
    try:
        history = requests.get(f"{api_url}/history").json()
    except:
        history = []

    # Show items
    for item in history:
        st.sidebar.markdown(
            f"""
            <div style="
                background:#ffffff15;
                padding:12px;
                border-radius:10px;
                margin-bottom:10px;">
                <b>Price:</b> {item['prediction']}
            </div>
            """,
            unsafe_allow_html=True
        )

    # ----- Clear History Button -----
    if st.sidebar.button("🗑️ Clear History"):
        try:
            requests.delete(f"{api_url}/history")
            st.sidebar.success("History cleared!")
        except:
            st.sidebar.error("Failed to clear history!")
