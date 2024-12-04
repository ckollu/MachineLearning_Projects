Project Walkaway:

Stakeholders: Movie Producers/Directors
Business Problem: To determine whether the current plot of a movie is identical to that of past films. This can help improve creativity and attract a wider audience.

Algorithms Involved: TF-IDF, Word2Vec, GloVe, Universal Sentence Encoder.

The project began with web scraping data from the IMDb Top 1000 movies, including movie names, cast, director, and year of release, and scraped movie plots from Wikipedia using the BeautifulSoup library.

Initially, exploratory data analysis (EDA) was performed to clean and organize the data for use. Natural language processing (NLP) algorithms such as Word2Vec and GloVe were used to calculate the frequency of common words as vectors. Additionally, the pre-trained Universal Sentence Encoder from Google was employed to track the performance of the results.

Next, the performance of Word2Vec, GloVe, and the Universal Sentence Encoder was compared using performance metrics to identify which model outperformed the others. Based on the observations, it was found that the Universal Sentence Encoder outperformed the traditional models like Word2Vec and GloVe.

Finally, a graphical user interface was developed using Streamlit, and the Universal Sentence Encoder model was deployed.
