import os
from openai import OpenAI

THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))
my_file = os.path.join(THIS_FOLDER, 'secrets.txt')
with open(my_file) as f:
    lines = f.readlines()
    gpt_key = lines[1].strip('\n')


class Inference:
    def __init__(self):
        self.openai = OpenAI(api_key=gpt_key)

    def get_main_task_data(self, sentence: str):

        response = self.openai.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {
                "role": "system",
                "content": [
                    {
                    "type": "text",
                    "text": "You will be given a sentence that contains a To Do item, a date, and a class the item is for. Extract the data from the sentence and put it in the format outlined below:\n\n NAME OF ITEM\n DATE\n CLASS NAME\n\nOnly include the final values and omit any quotation marks, white spaces, new lines, commas, etc.\n\nThe following list is a list of the possible classes the item can be for:\nFoundations of Artificial Intelligence, Molecules that Shaped the World, Software Projects\n\nWhen reading the sentence, interpret what class the item may fit under and make the value of  \"CLASS NAME\" the name of that class. If the class name is found, omit it from the NAME OF ITEM value of the item. If the class name is not found, make the CLASS NAME value \"None\".\nIf the date has the name or part of the name of a month, interpret what number month it is and convert it into the \"MM-DD\" format.\nIf the date is the name of a weekday, \"today\", \"td\", \"tomorrow\", or \"tm\" leave it that way.\n"
                    }
                ]
                },
                {
                "role": "user",
                "content": [
                    {
                    "type": "text",
                    "text": sentence
                    }
                ]
                }
            ],
            temperature=0.2,
            max_tokens=280,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0
        )
        return (response.choices[0].message.content)
        
    def get_subtask_data(self, sentence):
        response = self.openai.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {
            "role": "system",
            "content": [
                {
                "text": "You will be given a sentence that contains a To Do item and a date for when the item is due. Extract the data from the sentence and put it in the format outlined below:\n\n NAME OF ITEM\n DATE\n\nOnly include the final values and omit any quotation marks, white spaces, new lines, commas, etc.\n\nIf the date has the name or part of the name of a month, interpret what number month it is and convert it into the \"MM-DD\" format.\nIf the date is the name of a weekday, \"today\", \"td\", \"tomorrow\", or \"tm\" leave it that way.",
                "type": "text"
                }
            ]
            },
            {
            "role": "user",
            "content": [
                {
                "text": sentence,
                "type": "text"
                }
            ]
            }
        ],
        temperature=1,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
        )
        return (response.choices[0].message.content)