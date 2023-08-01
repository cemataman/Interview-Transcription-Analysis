import matplotlib.pyplot as plt
from nltk.probability import FreqDist
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
import io

with open("/Users/cem_ataman/PycharmProjects/Interview_Analysis/data/intermediate_data/final_data.py", "r") as f:
    file_contents = f.read()

# Remove the square brackets and single quotes from the file contents
file_contents = file_contents.replace("[", "").replace("]", "").replace("'", "").replace(',',"")

# Tokenize the text into words
words = word_tokenize(file_contents)

stop_words = set(stopwords.words("english"))
stop_words.update(['example', 'see', 'make', 'lot', 'know',
                   'year', 'kind', 'need', 'way', 'thing',
                   'going', 'put', 'right', 'want', 'say',
                   'come', 'use', 'actually', 'think', 'maybe',
                   'able', 'different', 'mean', 'important',
                   'question','understand', 'feel', 'usually',
                   'certain', 'talk', 'point', 'work', 'user',
                   'go', 'well', 'quite'])
filtered_words = [word for word in words if word.lower() not in stop_words]

# Calculate the frequency distribution of the words
fdist = FreqDist(filtered_words)

# Print the most common words and their frequency
for word, frequency in fdist.most_common(20):
    print("{}: {}".format(word, frequency))

# Extract the words and frequencies for the bar plot
common_words, word_freq = zip(*fdist.most_common(20))

# Create a bar plot to visualize the most common words and their frequencies
plt.figure(figsize=(10, 6))
bars = plt.bar(common_words, word_freq, color='yellowgreen', edgecolor='black', linewidth=0.5)
plt.xlabel('Words')
plt.ylabel('Frequency')
# plt.title('Most Common Words and Their Frequencies')
plt.xticks([])  # Remove x-axis ticks and labels
plt.tight_layout()

# Remove the frame around the plot by turning off the spines
ax = plt.gca()
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['bottom'].set_visible(True)
ax.spines['left'].set_visible(True)

# Add reference lines parallel to the x-axis for y-values 50, 100, and 150
plt.axhline(y=50, color='gray', linestyle='--', linewidth=0.5)
plt.axhline(y=100, color='gray', linestyle='--', linewidth=0.5)
plt.axhline(y=150, color='gray', linestyle='--', linewidth=0.5)

# Add the words diagonally on top of each bar
for bar, word, frequency in zip(bars, common_words, word_freq):
    plt.text(bar.get_x() + bar.get_width() / 2, bar.get_height(), word,
             ha='left', va='bottom', rotation=45, fontsize=10, fontweight='bold', color='dimgray')

# Save the plot directly as an image (you can specify the file name and format)
plt.savefig('/Users/cem_ataman/PycharmProjects/Interview_Analysis/results/most_common_words_plot.png')

# Show the plot (optional if you want to see it in the Jupyter Notebook or interactive environment)
plt.show()