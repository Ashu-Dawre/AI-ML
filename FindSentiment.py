#!C:\Users\Ethan Hunt\AppData\Local\Programs\Python\Python39\python
import cgi
from azure.ai.textanalytics import TextAnalyticsClient
from azure.core.credentials import AzureKeyCredential

print("Content-Type: text/html")
print()

print("<link rel='stylesheet' href='bootstrap.min.css'>")
print("<div class='container'><br><br>")

print("<table><tr><td>")
print("<img src='cognitive.png' height='200px'>")
print("<td><h1>Sentiment Analysis with <br>Microsoft Azure Cloud Cognitive Services</h1><tr></table>")
print("<hr>")

print("<h5>The document : </h5>")

form=cgi.FieldStorage()
cont=form.getvalue("content")


# use this code if you're using SDK version is 5.0.0

def authenticate_client():
    ta_credential = AzureKeyCredential('0fbe6dcae56e46f48f9750d035f8f086')
    text_analytics_client = TextAnalyticsClient(
            endpoint='https://sohamsentiments.cognitiveservices.ai.azure.com/', 
            credential=ta_credential) 
    return text_analytics_client

client = authenticate_client()


def sentiment_analysis_example(client):

    print("<p style='color:purple'>%s</p>" %cont)

    documents=[]
    documents.append(cont)
    response = client.analyze_sentiment(documents = documents)[0]
    #print("<h4><i>Document Sentiment: {}</i></h4>".format(response.sentiment))

    pos=response.confidence_scores.positive
    neu=response.confidence_scores.neutral
    neg=response.confidence_scores.negative
    sent=None
    if(pos>neu):
        if(pos>neg):
            sent="Positive"
        else:
            sent="Negative"
    else:
        if(neu>neg):
            sent="Neutral"
        else:
            sent="Negative"
    
    print("<h4 style='color:steelblue'><i>General Document Sentiment: {}</i></h4>".format(sent))

    '''
    print("Overall scores: positive={0:.2f}; neutral={1:.2f}; negative={2:.2f} \n".format(
        response.confidence_scores.positive,
        response.confidence_scores.neutral,
        response.confidence_scores.negative,
    ))
    '''
    #client=MongoClient('mongodb://localhost:27017')
    #pip install dnspython
    dic={"sentiment":sent,"positive":pos*100,"neutral":neu*100,"negative":neg*100}
    print("<br><br><h5>")
    print(dic)
    print("</h5>")

    
    print("<a href='TakeReview.html'>Back</a>")



sentiment_analysis_example(client)




print("</div>")


'''
def sentiment_analysis_example(client):

    documents = ["I had the best day of my life. I wish you were there with me."]
    response = client.analyze_sentiment(documents = documents)[0]
    print("Document Sentiment: {}".format(response.sentiment))
    print("Overall scores: positive={0:.2f}; neutral={1:.2f}; negative={2:.2f} \n".format(
        response.confidence_scores.positive,
        response.confidence_scores.neutral,
        response.confidence_scores.negative,
    ))
    for idx, sentence in enumerate(response.sentences):
        print("Sentence: {}".format(sentence.text))
        print("Sentence {} sentiment: {}".format(idx+1, sentence.sentiment))
        print("Sentence score:\nPositive={0:.2f}\nNeutral={1:.2f}\nNegative={2:.2f}\n".format(
            sentence.confidence_scores.positive,
            sentence.confidence_scores.neutral,
            sentence.confidence_scores.negative,
        ))
'''