import numpy as np
import nltk
import ssl

try:
    _create_unverified_https_context = ssl._create_unverified_context
except AttributeError:
    pass
else:
    ssl._create_default_https_context = _create_unverified_https_context

nltk.download('stopwords')
nltk.download('punkt')
from nltk.corpus import stopwords
import re
import string
import transformers
import torch
from nltk.tokenize import word_tokenize

def clean_sentence(s):
    """Given a sentence remove its punctuation and stop words"""

    stop_words = set(stopwords.words('english'))
    s = s.translate(str.maketrans('', '', string.punctuation))  # remove punctuation
    tokens = word_tokenize(s)
    cleaned_s = [w for w in tokens if w not in stop_words]  # removing stop-words
    return " ".join(cleaned_s)


def feature_create(data):
    # print("!Data inside the feature extractor\n\n", data)
    data["num_words"] = data["text"].apply(
        lambda s: len(re.findall(r'\w+', s)))  # Count the number of words in the message
    data["message_len"] = data["text"].apply(len)  # get the length of the text message

    data["text"] = data["text"].apply(clean_sentence)

    # Loading pretrained model/tokenizer
    tokenizer = transformers.DistilBertTokenizer.from_pretrained("distilbert-base-uncased")
    model = transformers.DistilBertModel.from_pretrained("distilbert-base-uncased")
    tokenized = data["text"].apply(lambda x: tokenizer.encode(x, add_special_tokens=True))

    max_len = tokenized.apply(len).max()  # get the length of the longest tokenized sentence

    padded = np.array([i + [0] * (max_len - len(i)) for i in
                       tokenized.values])  # padd the rest of the sentence with zeros if the sentence is smaller than the longest sentence

    attention_mask = np.where(padded != 0, 1, 0)

    input_ids = torch.tensor(padded)  # create a torch tensor for the padded sentences
    attention_mask = torch.tensor(attention_mask)  # create a torch tensor for the attention matrix

    with torch.no_grad():
        encoder_hidden_state = model(input_ids, attention_mask=attention_mask)
    X = encoder_hidden_state[0][:, 0, :].numpy()
    X = np.hstack((X, data[["num_words", "message_len"]].to_numpy().reshape(-1,
                                                                            2)))  # addind the the engineered features from the beginning

    # print("output of extractor\n\n", X)
    return X