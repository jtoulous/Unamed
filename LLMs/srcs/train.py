#from transformers import

from utils.logs import PrintLog, PrintError
from utils.info import LLM_List, GetTrainingData


def train(llm):
    database = GetTrainingData(llm)
    model, tokenizer = GetModel(llm)


if __name__ == '__main__':
    try:
        llm_list = LLM_List()
        for llm in llm_list:
            train(llm)

    except Exception as error:
        PrintError(error)