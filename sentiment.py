import nltk.sentiment
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import operator
#look more for this to get the same numbers as in the demo on: http://text-processing.com/demo/sentiment/

#pip3 install vaderSentiment
def sentimentbysents(posneg):
    analyzer = SentimentIntensityAnalyzer()
    valuelist = []
    for i in range(1,1001):
        name = posneg+str(i)
        file = open("movie_reviews/"+name+".txt")
        sentdictionary = {"pos":0,"neg":0,"compound":0}
        for line in file.readlines():
            #print(line)
            #print(analyzer.polarity_scores(line)["pos"])
            #print(analyzer.polarity_scores(line)["neg"], "\n\n")
            
            
            sentdictionary["pos"] = sentdictionary["pos"] + analyzer.polarity_scores(line)["pos"]
            sentdictionary["neg"] = sentdictionary["neg"] + analyzer.polarity_scores(line)["neg"]
            #sentdictionary["compound"] = sentdictionary["compound"] + analyzer.polarity_scores(line)["compound"]
        

        sent_value = max(sentdictionary.items(), key=operator.itemgetter(1))[0] #when using pos/neg
        #sent_value = "pos" if sentdictionary["compound"]>0 else "neg" #when using compound
            
        valuelist.append(sent_value)
    print([valuelist.count("pos"),valuelist.count("neg")])
    
def sentimentbywords(posneg):
    analyzer = SentimentIntensityAnalyzer()
    valuelist = []
    for i in range(1,1001):
        name = posneg+str(i)
        file = open("movie_reviews/"+name+".txt")
        sentdictionary = {"pos":0,"neg":0,"compound": 0}
        for line in file.readlines():
            for word in line.split():
                sentdictionary["pos"] = sentdictionary["pos"] + analyzer.polarity_scores(word)["pos"]
                sentdictionary["neg"] = sentdictionary["neg"] + analyzer.polarity_scores(word)["neg"]
                sentdictionary["compound"] = sentdictionary["compound"] + analyzer.polarity_scores(line)["compound"]

        #word_value = max(sentdictionary.items(), key=operator.itemgetter(1))[0] #when using pos/neg-scores
        word_value = "pos" if sentdictionary["compound"]>0 else "neg" #when using compound
        valuelist.append(word_value)
    print([valuelist.count("pos"),valuelist.count("neg")])

    
def main():
    #sentimentbysents("pos")
    #sentimentbysents("neg")
    sentimentbywords("pos")
    sentimentbywords("neg")

main()

