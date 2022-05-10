import matplotlib.pyplot as plt
import re
from nltk.tokenize import regexp_tokenize,sent_tokenize,word_tokenize
from nlp_utils import get_sample_Santo_Graal
import matplotlib.pyplot as plt

# Split the script into lines: lines
holy_grail = get_sample_Santo_Graal()
lines = holy_grail.split("\n")

# Replace all script lines for speaker
pattern = "[A-Z]{2,}(\s)?(#\d)?([A-Z]{2,})?:"
lines = [re.sub(pattern, '', l) for l in lines]

# Tokenize each line: tokenized_lines
tokenized_lines = [regexp_tokenize(l, "\w+") for l in lines]

# Make a frequency list of lengths: line_num_words
line_num_words = [len(l) for l in tokenized_lines]

# # Plot a histogram of the line lengths
plt.hist(line_num_words)
plt.show()

