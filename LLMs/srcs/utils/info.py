import pandas as pd
from transformers import AutoModelForCausalLM, AutoTokenizer
from sqlalchemy import create_engine

def LLM_List():
    llm_list = [
        'Algebra'
    ]
    return llm_list


def LLM_Description(llm, info_type):
    if llm == 'Algebra':
        if info_type == 'skills':
            return ['Algebra', 'Algebric debate', 'Algebric creativity']
        elif info_type == 'model':
            return 'gpt2'


def GetModel(llm):
    if llm == 'Algebra':
        model = AutoModelForCausalLM.from_pretrained('gpt2')
        tokenizer = AutoTokenizer.from_pretrained('gpt2')
    return model, tokenizer


#def GetTrainingData(llm):
#    skills_list = LLM_Description(llm, skills)
#    for skill in skills_list:
#        #faire requete vers db et recuperer les tables correspondante
#    return  database 