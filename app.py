import streamlit as st
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import matplotlib.pyplot as plt

# Initialize Analyzer
analyzer = SentimentIntensityAnalyzer()

# App Title
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

    results = {}

    # Aspect-wise Sentiment
    for aspect in aspects:

        if aspect in review.lower():

            score = analyzer.polarity_scores(review)

            compound = score['compound']

            if compound >= 0.05:
                sentiment = "Positive"

            elif compound <= -0.05:
                sentiment = "Negative"

            else:
                sentiment = "Neutral"

            results[aspect] = sentiment

    # Show Results
    st.subheader("Aspect Wise Sentiment")

    if results:

        for aspect, sentiment in results.items():

            st.write(f"✅ {aspect.capitalize()} : {sentiment}")

    else:

        st.write("No aspects found.")

    # Count Sentiments
    positive = list(results.values()).count("Positive")
    negative = list(results.values()).count("Negative")
    neutral = list(results.values()).count("Neutral")

    # Pie Chart
    labels = []
    values = []

    if positive > 0:
        labels.append("Positive")
        values.append(positive)

    if negative > 0:
        labels.append("Negative")
        values.append(negative)

    if neutral > 0:
        labels.append("Neutral")
        values.append(neutral)

    # Plot Pie Chart
    fig, ax = plt.subplots(figsize=(5, 5))

    ax.pie(
        values,
        labels=labels,
        autopct='%1.1f%%'
    )

    ax.set_title("Sentiment Distribution")

    st.pyplot(fig)
