 opinion_pulse – Sentiment Analysis Web App

opinionpulse is a Sentiment Analysis Application that classifies user text into Positive, Negative using Natural Language Processing (NLP) techniques.
It combines Flask (backend API), a creative frontend, and an ML model for an end-to-end solution.

---

 Features

  Sentiment Classification: Detects Positive, Negative, Neutral from text input
  Interactive Frontend: Beautiful UI built with HTML, CSS, and JS
  Flask REST API: Backend to handle predictions
  Machine Learning Model: Trained on sentiment dataset using NLP
  Seamless Integration: Frontend ↔ Backend communication via API
  Deployment Ready

---

Tech Stack

Frontend HTML, CSS, JavaScript
Backend: Python, Flask
ML/NLP: scikit-learn, nltk / text preprocessing
Version Control*: Git & GitHub

---

Project Structure


sentiment_api/
│── static/            # CSS, JS files  
│── templates/         # HTML files  
│── model/             # Trained ML model  
│── app.py             # Flask backend  
│── requirements.txt   # Dependencies  
│── README.md          # Documentation  


---

 Installation & Setup

Clone the repo

bash
git clone https://github.com/RachanaShetty93/opinion_pulse
cd opinion_pulse


Create virtual environment & activate it

bash
python -m venv venv
venv\Scripts\activate     # Windows
source venv/bin/activate  # Mac/Linux


Install dependencies

bash
pip install -r requirements.txt


Run the Flask server

bash
python app.py


Access in browser


http://127.0.0.1:5000


---


 Future Improvements

* Add support for multilingual sentiment analysis 
* Improve accuracy with deep learning models (LSTM / BERT) 
* Deploy on *Heroku / Render / AWS* for public access 

---

 Contributing

Contributions are welcome! Feel free to fork the repo and submit pull requests.

---

 Contact

Developed by Rachana
Reach me at: rachanashetty935@gmail.com
LinkedIn: www.linkedin.com/in/rachanashettyb26a

