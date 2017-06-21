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
        sentdictionary = {"pos":0,"neg":0}#,"neu":0}
        for line in file.readlines():
            #print(line)
            #print(analyzer.polarity_scores(line)["pos"])
            #print(analyzer.polarity_scores(line)["neg"])
            
            
            sentdictionary["pos"] = sentdictionary["pos"] + analyzer.polarity_scores(line)["pos"]
            sentdictionary["neg"] = sentdictionary["neg"] + analyzer.polarity_scores(line)["neg"]
        

        sent_value = max(sentdictionary.items(), key=operator.itemgetter(1))[0]
        valuelist.append(sent_value)
    print([valuelist.count("pos"),valuelist.count("neg")])
    
    
def main():
    sentimentbysents("pos")
    sentimentbysents("neg")
    #add
main()
