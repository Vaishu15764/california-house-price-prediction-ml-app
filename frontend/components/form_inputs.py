import streamlit as st

def user_form():
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.markdown("### 🏡 Enter House Features")

    col1, col2 = st.columns(2)

    with col1:
        MedInc = st.number_input("Median Income")
        HouseAge = st.number_input("House Age")
        AveRooms = st.number_input("Average Rooms")
        AveBedrms = st.number_input("Average Bedrooms")

    with col2:
        Population = st.number_input("Population")
        AveOccup = st.number_input("Average Occupancy")
        Longitude = st.number_input("Longitude")   # Only 7th feature now

    st.markdown('</div>', unsafe_allow_html=True)

    return {
        "MedInc": MedInc,
        "HouseAge": HouseAge,
        "AveRooms": AveRooms,
        "AveBedrms": AveBedrms,
        "Population": Population,
        "AveOccup": AveOccup,
        "Longitude": Longitude
    }
