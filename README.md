## 🩺 Healthcare Statement Classification with NLP & Machine Learning
This is a prototype that uses **Natural Language Processing** (NLP) feature extraction and **Machine learning** (ML) to analyze health related statements and predict whether they are **Reliable**  ✅ or **Misleading** ❌

The application is deployed using Streamlit and powered by a Logistic Regression classifier trained on TF-IDF text features.

TF-IDF: Term Fequency-Inverse Document Frequency


## ✨ Features

- 📋 Healthcare statement classification
- 🤖 Model- Trained a Logistic Regression model using TF-IDF text features for accurate classification
- 💻 Web Interface- Interactive Streamlit web application
- ⚡ Instant predictions

## 📂 Project Structure

```
Healthcare-Statement-Classification/
│
├── images/
│   ├── reliable_classification.png
│   ├── misleading_classification.png
│   └── workflow.png
│
├── models/
│   ├── healthcare_lr_model.pkl
│   └── tfidf_vectorizer.pkl
│
├── Healthcare_Statements_Classification.ipynb
├── README.md
├── app.py
├── healthcare_statements.csv
├── predicted_examples.csv
└── requirements.txt
```

## 🚀 Installation Steps
Clone this repo:
```bash
git clone https://github.com/Ibitoye07/Healthcare-Statement-Classification.git
```
Move into the project directory:

```bash
cd Healthcare-Statement-Classification
```
Install dependencies:

```bash
pip install -r requirements.txt
```
## ▶️ Running the App
### Run locally:
```bash
streamlit run app.py
```

### Live Demo

🌐 **Try the deployed application here:**

https://healthcare-statement-classification.streamlit.app/

## 🌐 Usage
1. Copy the link to your browser
2. Type a sentence like:

   ```"Regular blood pressure checks help detect hypertension early"```

   or


   ```"Eating only ginger and lemon can cure typhoid fever"``` 

4. Hit Analyze and watch the magic happen ✨

   You'll see the verdict !
