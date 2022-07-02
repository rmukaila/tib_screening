import pandas as pd
from glob import glob
import json


def save_phrase_and_sentence(list_item,saved_items_dict):
    
    """    
    :arguments:
    :list_item : list
    :saved_items_dict : dict
    
    :Saves the research-problem phrase and the respective sentence it came from into a dictionary
    :Note: we are ignoring possible multiple research problem phrases because they are all from same sentence
    :for now this works okay with the current data and goal but should be changed when necessary
    """
    saved_items_dict[list_item[0]]=list_item[-1]["from sentence"]
    
    

def get_preprocessed_data(data_path):
    """
    :arguments:
    :data_path : str
    
    :returns:
    :research_keyPhrase_and_sentence_dict :dict
    :json_counts : int
    
    
    :function:
    :Counts and loops through all the research-problem.josn files of all
    :the research paper folders, extracting one research-problem
    :phrase (there could be many such phrases) and the sentence from which
    :it came from, and save both in one dict (research_keyPhrase_and_sentence_dict)
    :Also count number of research-problem.jsons into json_counts
    
    
    """
    
    path_ = data_path
    json_counts = 0
    # research_problem_json_urls = []
    research_keyPhrase_and_sentence_dict ={}
    for json_path in glob(path_, recursive=False):
    #     for paper_path in glob(domain_path+)

        with open(json_path) as file:
            research_problm = json.load(file)
            research_p = research_problm["has research problem"]

            #Some annotations didn't follow the structure 
            #of the lot (items in some "has research problem" are not in a list object)
            #for those, we handle differently as follows
            if type(research_p[0])==str:
                save_phrase_and_sentence(research_p,research_keyPhrase_and_sentence_dict)
                continue

            for item in research_p:
                research_keyPhrase_and_sentence_dict[item[0]]=item[-1]['from sentence']

        json_counts +=1
    return research_keyPhrase_and_sentence_dict,json_counts
    
    
#Create a list of the keyPhrases with the maximum cosine similarity values
def get_predicted_keyPhrases(all_predictions):
    higherCosineS_keyPhrases = []
    all_keyPhrases = all_predictions
    for item2 in all_keyPhrases:
        max_cosine =0
        max_cosine_phrase = None
        for phrase_tuple in item2:
            if phrase_tuple[1]>max_cosine:
                max_cosine = phrase_tuple[1]
                max_cosine_phrase = phrase_tuple[0]

        higherCosineS_keyPhrases.append(max_cosine_phrase)
        
    return higherCosineS_keyPhrases
    
    
#Code for exploring the data (structure)

# for json_path in glob(training_data_url, recursive=True):
# #     for paper_path in glob(domain_path+)
    
#     with open(json_path) as file:
#         research_problm = json.load(file)
#         research_p = research_problm["has research problem"]
#         for item in research_p:
#             if len(item)>2:
#                 count_dict=0
#                 for x in item:
#                     if type(x) != str:
#                         count_dict +=1
# #                 print("Number of dicts: ",count_dict)#len(item))
#                 if count_dict==0:
#                     print("No dict json: ",json_path)
#                     print("Researh problem phrase item: ",research_p)
# #             try:
# #                 print("sentence: ",item[1]['from sentence'])
# #             except:
# #                 print("Error causative path: ",json_path)
                
# #     print(json_path)
# #     break