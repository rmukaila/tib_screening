Research problem extraction with NLP
This repository is a proof of concept of topic modeling/ key phrase extraction / topic identification 
in Natural Language Processing (NLP)

Here for brevity and time limitation, I tried to accomplish the whole task
using keyBERT (https://github.com/MaartenGr/KeyBERT#embeddings).

#How keyBERT works:



#Workflow of the task


#RESULTS
In the following table (TABLE 1), I displayed 19 selected predicted phrases and their coresponding actual phrases
  
 #TABLE 1 :Predicted (extracted) Keyphrases/research problem phrase VS actual key phrases/research problem phrase
![alt text](https://github.com/rmukaila/tib_screening/blob/master/actualANDextractedKeyPhrase.png)

#From the TABLE 1, it is clear that the model is performing quite bad but 
not too bad for an out-of-the-box model pending hyperparameter tuning. Also in
the subsequent table, it is evident for some datapoints that much of the 
wrong predictions are coming from wrong assignment of cosine similarity values.







TABLE 2: Actual research problem phrase as column names and all predicted/extracted phrases
          and their cosine similarity values as items in the columns.
![alt text](https://github.com/rmukaila/tib_screening/blob/master/possiblePredictions_vs_actuals.png)



In table two the system did have correct predictions in it's list of extracted phrases
but for some reason, the system assigned a lower cosine similarity value to such phrases 
and instead gave the highest cosine similarity to wrong phrases. This is gives some 
promise that with some tunning, I could get the system to a good improvement on it's 
performance.

#REFERENCES:
https://towardsdatascience.com/enhancing-keybert-keyword-extraction-results-with-keyphrasevectorizers-3796fa93f4db

https://github.com/MaartenGr/KeyBERT#embeddings
