import streamlit as st
import joblib

# ---------------- Page Configuration ----------------
st.set_page_config(
    page_title="Healthcare Statement Analysis",
    page_icon="🩺",
    layout="centered"
)

# ---------------- Load Model ----------------
vectorizer = joblib.load("models/tfidf_vectorizer.pkl")
model = joblib.load("models/healthcare_lr_model.pkl")

# ---------------- Custom CSS ----------------
st.markdown("""
<style>

/* Reduce top spacing */
.block-container{
    padding-top:1rem;
    padding-bottom:1rem;
}

/* Title */
.title{
    text-align:center;
    color:#2563EB;
    font-size:34px;
    font-weight:700;
    margin-bottom:0;
}



/* Rounded button */
div.stButton > button{
    background-color: #2563EB !important;
    color: white !important;
    border: none !important;
    border-radius:10px;
    height:3em;
    font-weight:600;
}

/* Rounded text area */
textarea{
    border-radius:10px !important;
}

</style>
""", unsafe_allow_html=True)

# ---------------- Header ----------------
st.markdown("""
<h1 class="title">
🩺 Healthcare Statement Analysis
</h1>
""", unsafe_allow_html=True)


# ---------------- Disclaimer ----------------
st.caption(
    "⚠️ Educational AI prototype. This tool should not replace professional medical advice."
)

# ---------------- Input ----------------
with st.container(border=True):

    st.markdown("**Enter a healthcare statement**")

    user_input = st.text_area(
        "",
        height=100,
        label_visibility="collapsed"
    )

    analyze = st.button(
        "🔍 Analyze Statement",
        type="primary",
        use_container_width=True
    )

# ---------------- Verdict ----------------
if analyze:

    if user_input.strip():

        X_new = vectorizer.transform([user_input])
        response = model.predict(X_new)[0]

        #st.markdown("---")
        st.write("#### Result:")

        col1, col2 = st.columns([3, 1])

        with col1:
            st.markdown("Statement")
            st.write(user_input)

        with col2:
            st.markdown("Verdict")

            if response == "Reliable":
                st.success("✅ Reliable")
            else:
                st.error("❌ Misleading")

    else:
        st.warning("Please enter a healthcare statement.")
