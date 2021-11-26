from nitk.sentiment.vader import SentimentIntensityAnalizer

x="positive"
y="negative"
z="neutral"

sid=SentimentIntensityAnalizer()
resultados=sid.polarity_scores(x)
print(resultados)
