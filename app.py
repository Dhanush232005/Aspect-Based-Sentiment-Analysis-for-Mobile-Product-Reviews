import streamlit as st
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import matplotlib.pyplot as plt

# Sentiment Analyzer
analyzer = SentimentIntensityAnalyzer()

# Title
st.title("📱 Aspect Based Sentiment Analysis")

# User Input
review = st.text_area("Enter Mobile Review")

# Aspect List
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

# Analyze Button
if st.button("Analyze"):

    # Find Aspects
    found = []

    for aspect in aspects:
        if aspect in review.lower():
            found.append(aspect)

    # Sentiment Analysis
    score = analyzer.polarity_scores(review)

    compound = score['compound']

    if compound >= 0.05:
        sentiment = "Positive 😊"

    elif compound <= -0.05:
        sentiment = "Negative 😔"

    else:
        sentiment = "Neutral 😐"

    # Results
    st.subheader("Results")

    st.write("### Aspects Found:")
    st.write(found)

    st.write("### Sentiment:")
    st.write(sentiment)

    # Pie Chart Data
    labels = ["Positive", "Negative", "Neutral"]

    if sentiment == "Positive 😊":
        values = [1, 0, 0]

    elif sentiment == "Negative 😔":
        values = [0, 1, 0]

    else:
        values = [0, 0, 1]

    # Create Pie Chart
    fig, ax = plt.subplots()

    ax.pie(
        values,
        labels=labels,
        autopct='%1.1f%%'
    )

    ax.set_title("Sentiment Distribution")

    # Show Chart
    st.pyplot(fig)
