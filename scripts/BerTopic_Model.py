import matplotlib
import matplotlib.pyplot as plt
from bertopic import BERTopic
from umap import UMAP
import os
import pandas as pd
import numpy as np
import plotly.io as py
from wordcloud import WordCloud
from collections import defaultdict

# Load data
x = open("/Users/cem_ataman/PycharmProjects/Interview_Analysis/data/intermediate_data/final_data.py", "r")
final_data = eval(x.readlines()[0])
x.close()

### Dataframe display settings
desired_width = 520
pd.set_option('display.width', desired_width)
np.set_printoptions(linewidth=desired_width)
pd.set_option('display.max_columns', 10)

# Set the background color to white
matplotlib.rcParams['figure.facecolor'] = 'white'

# Convert non-string elements to strings in the corpus
final_data = [str(doc) for doc in final_data]

# Filter out the empty lists:
final_data = [doc for doc in final_data if doc != '[]']

# Initiate UMAP
umap_model = UMAP(n_neighbors=15,
                  n_components=5,
                  min_dist=0.0,
                  metric='cosine',
                  random_state=100)

# Initiate BERTopic
topic_model = BERTopic(nr_topics="auto", top_n_words=10, umap_model=umap_model, language="english", calculate_probabilities=True)

# Run BERTopic model
topics, probabilities = topic_model.fit_transform(final_data)

# Get topic information
topic_info = topic_model.get_topic_info()
print(topic_info)

# # Get specific topic information
# topic_info_n = topic_model.get_topic(2)
# print(topic_info_n)


# Convert the topic_info dictionary to a DataFrame
topic_info_df = pd.DataFrame(topic_info)

# Specify the path where you want to save the Excel file
excel_file_path = "/Users/cem_ataman/PycharmProjects/Interview_Analysis/results/topic_info.xlsx"

# Save the DataFrame to an Excel file
topic_info_df.to_excel(excel_file_path, index=False)

# Display a message indicating that the file has been saved
print("Topic information has been saved to Excel file:", excel_file_path)


#### USE THE NECESSARY PART IF NECESSARY


# #### Generate the plot for TOPIC BARCHART ---------------------------------------------------
# plot_figure = topic_model.visualize_barchart(top_n_topics=9)
# py.write_html(plot_figure, '/Users/cem_ataman/PycharmProjects/Interview_Analysis/results/topic_barchart.html') # Save to an HTML file

# #### Generate the plot for TOPIC HIERARCHY ---------------------------------------------------
# plot_figure_2 = topic_model.visualize_hierarchy()
# plot_figure_2.update_layout(plot_bgcolor='white')
# py.write_html(plot_figure_2, '/Users/cem_ataman/PycharmProjects/Interview_Analysis/results/topic_hierarchy.html') # Save to an HTML file

# #### Generate the plot for TOPIC SIMILARITY ---------------------------------------------------
# plot_figure_3 = topic_model.visualize_heatmap()
# py.write_html(plot_figure_3, '/Users/cem_ataman/PycharmProjects/Interview_Analysis/results/topic_similarity.html') # Save to an HTML file

# #### Generate the plot for INTERTOPIC DISTANCE MAP ---------------------------------------------------
# plot_figure_4 = topic_model.visualize_topics()
# py.write_html(plot_figure_4, '/Users/cem_ataman/PycharmProjects/Interview_Analysis/results/intertopic_distance_map.html') # Save to an HTML file


# #### Creat wordloud for each topic ---------------------------------------------------

# # Get all topic ids
# topic_ids = list(topic_info["Topic"])
#
# # Create a directory for word clouds if it does not exist
# wordcloud_dir = "/Users/cem_ataman/PycharmProjects/Interview_Analysis/results/word_clouds/"
# os.makedirs(wordcloud_dir, exist_ok=True)
#
# # Create a word cloud for each topic
# for topic_id in topic_ids:
#     if topic_id != -1:  # Ignore the outliner topic which is labeled as -1
#         # Get the words and weights for the topic
#         word_weight_tuples = topic_model.get_topic(topic_id)
#
#         # Convert list of tuples to a dictionary
#         word_weight_dict = {word: weight for word, weight in word_weight_tuples}
#
#         # Create a word cloud
#         wc = WordCloud(width=800, height=400, max_words=200, background_color='white')
#         wordcloud = wc.generate_from_frequencies(word_weight_dict)
#
#         # Save the word cloud image
#         wordcloud.to_file(os.path.join(wordcloud_dir, f"wordcloud_topic_{topic_id}.png"))


# #### Creat one big wordloud from all topics---------------------------------------------------
# # Get all topic ids
# topic_ids = list(topic_info["Topic"])
#
# # Create a dictionary to hold the sum of the weights for each word across all topics
# combined_word_weight_dict = defaultdict(float)
#
# # Sum the weights of the words across all topics
# for topic_id in topic_ids:
#     if topic_id != -1:  # Ignore the outliner topic which is labeled as -1
#         # Get the words and weights for the topic
#         word_weight_tuples = topic_model.get_topic(topic_id)
#
#         # Add the weights to the combined weights
#         for word, weight in word_weight_tuples:
#             combined_word_weight_dict[word] += weight
#
# # Create a word cloud from the combined weights
# wc = WordCloud(width=800, height=400, max_words=200, background_color='white')
# combined_wordcloud = wc.generate_from_frequencies(combined_word_weight_dict)
#
# # Save the combined word cloud image
# combined_wordcloud.to_file("/Users/cem_ataman/PycharmProjects/Interview_Analysis/results/combined_wordcloud.png")

