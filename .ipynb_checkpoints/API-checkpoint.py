import nlpcloud
def ner(text,entity):
    client = nlpcloud.Client("finetuned-llama-3-70b", "d9b35acc835d0374457be6bc91f4e0e755221594", gpu=True)
    response=client.entities(text,entity)
    return response

def sentiment_analysis(text):

    client = nlpcloud.Client("distilbert-base-uncased-emotion", "d9b35acc835d0374457be6bc91f4e0e755221594", gpu=False)
    response=client.sentiment(text)
    return response

def summary(text):

    client = nlpcloud.Client("finetuned-llama-3-70b", "d9b35acc835d0374457be6bc91f4e0e755221594", gpu=True)
    response=client.summarization(text,size="small")
    return response