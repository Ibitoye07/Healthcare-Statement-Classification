import streamlit as st
import joblib

# load the saved vectorizer and the trained model
vectorizer = joblib.load('tfidf_vectorizer.pkl')
model = joblib.load('healthcare_lr_model.pkl')

st.title('Healthcare Statement Analysis Prototype', text_alignment = 'center')
user_input = st.text_area('Enter a healthcare statement:')

# button
if st.button('Analyze', type ='primary', width= 'content'):
    if user_input.strip():
        X_new = vectorizer.transform([user_input])
        prediction = model.predict(X_new)[0]

        # Display results
        st.write("### Result")
        st.write(f"Healthcare Statement: {user_input}")
        st.write(f"Response: {prediction}")

    else:
        st.warning('Please enter a healthcare statement.')
