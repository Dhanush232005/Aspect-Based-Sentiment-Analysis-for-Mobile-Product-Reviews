import streamlit as st
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import streamlit as st
import plotly.express as px
import pandas as pd
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
        import plotly.express as px
import pandas as pd

sentiment_values = list(results.values())

positive = sentiment_values.count("Positive 😊")
negative = sentiment_values.count("Negative 😔")
neutral = sentiment_values.count("Neutral 😐")

data = pd.DataFrame({
    "Sentiment": ["Positive", "Negative", "Neutral"],
    "Count": [positive, negative, neutral]
})

fig = px.pie(
    data,
    names="Sentiment",
    values="Count",
    title="Sentiment Distribution"
)

st.plotly_chart(fig)
