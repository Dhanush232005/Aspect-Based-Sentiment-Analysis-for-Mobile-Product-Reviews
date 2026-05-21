from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

analyzer = SentimentIntensityAnalyzer()

review = input("Enter Review: ")

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

print("\nAspects Found:", found)
print("Sentiment:", sentiment)