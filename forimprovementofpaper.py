import nltk.sentiment
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import operator


def main():
    analyzer = SentimentIntensityAnalyzer()
    string1 = "danny elfman's score has a nice primitive feel, but jerry goldsmith's 1968 tour de force score is a real classic. "
    string2 = "a mechanical failure strikes the military base that commands the bombers"
    sentdictionary = {"pos":0,"neg":0,"compound": 0}
    for word in string2.split():
        print(word, "POS: ", analyzer.polarity_scores(word)["pos"])
        print(word, "NEG: ", analyzer.polarity_scores(word)["neg"])
        print(word, "COMP: ", analyzer.polarity_scores(word)["compound"])
        sentdictionary["pos"] = sentdictionary["pos"] + analyzer.polarity_scores(word)["pos"]
        sentdictionary["neg"] = sentdictionary["neg"] + analyzer.polarity_scores(word)["neg"]
        sentdictionary["compound"] = sentdictionary["compound"] + analyzer.polarity_scores(word)["compound"]

    print(sentdictionary)
    
main()
