import streamlit as st
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

analyzer = SentimentIntensityAnalyzer()

st.title("Aspect Based Sentiment Analysis")

review = st.text_area("Enter Review")

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

    sentences = review.split("but")

    results = {}

    for sentence in sentences:

        for aspect in aspects:

            if aspect in sentence.lower():

                score = analyzer.polarity_scores(sentence)

                compound = score['compound']

                if compound >= 0.05:
                    sentiment = "Positive 😊"

                elif compound <= -0.05:
                    sentiment = "Negative 😔"

                else:
                    sentiment = "Neutral 😐"

                results[aspect] = sentiment

    st.subheader("Aspect Wise Sentiment")

    for aspect, sentiment in results.items():
        st.write(f"{aspect.title()} → {sentiment}")
