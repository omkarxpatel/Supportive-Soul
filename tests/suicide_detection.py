import os
import torch
from transformers import AutoTokenizer, AutoModelForSequenceClassification

# try: 
#     os.chdir("/content/drive/MyDrive/BT4222 Project")
#     print("Directory changed")
# except OSError:
#     print("Error: Can't change the Current Working Directory")


def load_suicide_tokenizer_and_model(tokenizer="google/electra-base-discriminator", model="Models/electra"):
    """Load tokenizer and model instance for suicide text detection model."""

    suicide_tokenizer = AutoTokenizer.from_pretrained(tokenizer)
    suicide_model = AutoModelForSequenceClassification.from_pretrained(model)

    return suicide_tokenizer, suicide_model

# Initialise suicide detection tokenizer and model
suicide_tokenizer, suicide_model = load_suicide_tokenizer_and_model()

def check_intent(text):
    """Check if suicidal intent is present in text"""

    global suicide_tokenizer, suicide_model

    tokenised_text = suicide_tokenizer.encode_plus(text, return_tensors="pt")

    logits = suicide_model(**tokenised_text)[0]

    prediction = round(torch.softmax(logits, dim=1).tolist()[0][1])

    return prediction

print(check_intent("How are you?"))