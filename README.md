
# Interview Transcription Analysis

This script is prepared to enable the analysis of interview transcripts via AI-based computational linguistic methods such as topic modeling, sentiment scores, and topic analysis based on the most frequent words and their weights in the dataset.

## Data Description
The dataset contains qualitative textual data gathered from interviews, where participants and post-participants of a digital citizen participation campaign. The dataset consists of the transcription of 20 interviews that are conducted in a 2 months period. Yet, it is possible to use the scripts in any interview datasets, regardless of the domain knowledge.

## Citation
Please include the following citation if you are interested in using the provided scripts:

Ataman, Cem, Pieter Herthogs, Bige Tuncer, and Simon Perrault. 2022. "Multi-Criteria Decision Making in Digital Participation: A Framework to Evaluate Participation in Urban Design Processes". In *Co-creating the Future: Inclusion in and through Design - Proceedings of the 40th Conference on Education and Research in Computer Aided Architectural Design in Europe (eCAADe)*, 401–410, Ghent, Belgium.

## How to use the code
It is recommended to follow the order of these three steps when executing the code:

Run the **data_cleaning.py** file to preprocess the data.
Next, execute **sentiment_analysis.py** to perform sentiment analysis on the preprocessed data.
Finally, run **LDA_topic_modeling.py**, **topic_analysis.py**, or **BerTopic_Model.py** to facilitate further analysis based on the preprocessed data and the results of sentiment analysis.

The final step can be adjusted based on the investigation you would like to conduct. Please ensure to replace the file paths with your own dataset.

### Folders & Scripts
- Data
    - include your datasets as .docx or .txt files.
- Results = all the final visuals and files will be saved here
- Scripts = forder for all the scripts
    - *data_cleaning.py* : preprocessing the textual data
    - *topic_analysis.py* : determining the most frequent words based on final data and visualize them in a bar-chart
    - *sentiment_analysis.py* : calculating sentiment scores of each document (interviewee)
    - *LDA_topic_model.py* : formulating LDA topic model based on final data
    - *BerTopic_Model.py* : formulating BerTopic model based on final data & utilizing various visualizations
