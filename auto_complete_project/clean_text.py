import nltk
import re
import string
from nltk.corpus import stopwords
nltk.download("stopwords")

def clean_text(text):

    text = text.lower()

    # Removing punctuations
    text_wo_punctuation = re.sub(f"[{re.escape(string.punctuation)}]", "", text)

    # Putting each word in an array
    list_text = text_wo_punctuation.split()

    # Loading the portuguese stopwords
    stopdwords_ = set(stopwords.words("portuguese"))

    text_clean = [word_ for word_ in list_text if word_ not in stopdwords_]
    text_clean = set(text_clean)
    text_clean = list(text_clean)

    return text_clean
