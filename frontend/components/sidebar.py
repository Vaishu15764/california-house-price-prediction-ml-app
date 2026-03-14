import streamlit as st
import requests


def load_history(api_url):

    # -----------------------------
    # MODEL PERFORMANCE
    # -----------------------------
    st.sidebar.markdown("## 📊 Model Performance")

    model_metrics = {
        "Linear Regression": {"R2": 0.609, "MSE": 0.528},
        "Decision Tree": {"R2": 0.435, "MSE": 0.763},
        "Random Forest": {"R2": 0.724, "MSE": 0.373}
    }

    selected_model = st.sidebar.selectbox(
    "Select Model",
    list(model_metrics.keys()),
    key="model_selector_sidebar"
   )

    metrics = model_metrics[selected_model]

    st.sidebar.metric("R² Score", metrics["R2"])
    st.sidebar.metric("MSE", metrics["MSE"])

    st.sidebar.success("🏆 Best Model: Random Forest")

    st.sidebar.markdown("---")

    # -----------------------------
    # PREDICTION HISTORY
    # -----------------------------
    st.sidebar.markdown("## 🕘 Prediction History")

    try:
        history = requests.get(f"{api_url}/history").json()
    except:
        history = []

    # Show items (YOUR ORIGINAL LOGIC)
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