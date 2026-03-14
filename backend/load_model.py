import joblib 

def load_model():
    model=joblib.load('backend/california_house_price_model.joblib')
    return model
