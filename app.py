import streamlit as st
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

analyzer = SentimentIntensityAnalyzer()

st.title("Aspect Based Sentiment Analysis")

review = st.text_input("Enter Review")

aspects = [
    "battery",
    "camera",
    "display",
    "sound",
    "performance",
    "design",
    "price",
    "storage",
    "processor",
    "speaker"
]

if st.button("Analyze"):
    
    found = []

    for aspect in aspects:
        if aspect in review.lower():
            found.append(aspect)

    score = analyzer.polarity_scores(review)

    compound = score['compound']

    if compound >= 0.05:
        sentiment = "Positive"

    elif compound <= -0.05:
        sentiment = "Negative"

    else:
        sentiment = "Neutral"

    st.write("### Aspects Found:", found)
    st.write("### Sentiment:", sentiment)
