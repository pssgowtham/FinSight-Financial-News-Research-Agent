# Env loading, NLTK setup

import os
from dotenv import load_dotenv
import nltk

def setup_environment():
    load_dotenv()
    nltk.download("punkt")
    nltk.download("punkt_tab")
    nltk.download("averaged_perceptron_tagger_eng")
