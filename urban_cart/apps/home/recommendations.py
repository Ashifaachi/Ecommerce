# import pandas as pd
# import numpy as np
# from sklearn.metrics.pairwise import cosine_similarity
# from sklearn.feature_extraction.text import TfidfVectorizer
# import os 

# # Load dataset
# # DATA_PATH = "urban_cart/apps/home/data/cleaned_data.csv"
# # df = pd.read_csv(DATA_PATH)
# BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# DATA_PATH = os.path.join(BASE_DIR, 'home', 'data', 'cleaned_data.csv')

# df = pd.read_csv(DATA_PATH)

# # Ensure required columns exist
# df = df[['name', 'ratings', 'no_of_ratings', 'main_category', 'sub_category']]

# # Create 'tags' column
# df['tags'] = df['main_category'] + " " + df['sub_category']


# # --- Content-Based Filtering ---
# def content_based_recommendations(item_name, top_n=10):
#     if item_name not in df['name'].values:
#         return pd.DataFrame()  # Return empty if product not found
    
#     # Vectorize product tags
#     tfidf_vectorizer = TfidfVectorizer(stop_words='english')
#     tfidf_matrix = tfidf_vectorizer.fit_transform(df['tags'])
    
#     # Compute cosine similarity
#     cosine_sim = cosine_similarity(tfidf_matrix, tfidf_matrix)
    
#     # Find index of item
#     item_idx = df[df['name'] == item_name].index[0]
    
#     # Get similar items
#     similar_items = list(enumerate(cosine_sim[item_idx]))
#     similar_items = sorted(similar_items, key=lambda x: x[1], reverse=True)[1:top_n+1]
    
#     # Get recommended product names
#     recommended_indices = [i[0] for i in similar_items]
#     return df.iloc[recommended_indices][['name', 'ratings', 'no_of_ratings']]


# # --- Collaborative Filtering ---
# def collaborative_filtering_recommendations(user_id, top_n=10):
#     ratings_df = df.pivot_table(index='user_id', columns='name', values='ratings', fill_value=0)
    
#     if user_id not in ratings_df.index:
#         return pd.DataFrame()  # Return empty if user not found
    
#     user_sim = cosine_similarity(ratings_df)
#     user_idx = list(ratings_df.index).index(user_id)
    
#     # Get similar users
#     similar_users = list(enumerate(user_sim[user_idx]))
#     similar_users = sorted(similar_users, key=lambda x: x[1], reverse=True)[1:top_n+1]
    
#     # Get recommended products
#     recommended_items = []
#     for idx, _ in similar_users:
#         rated_products = ratings_df.iloc[idx]
#         recommended_items.extend(rated_products[rated_products > 0].index.tolist())
    
#     return df[df['name'].isin(recommended_items)][['name', 'ratings', 'no_of_ratings']].head(top_n)


# # --- Hybrid Recommendation ---
# def hybrid_recommendations(user_id, item_name, top_n=10):
#     content_recs = content_based_recommendations(item_name, top_n)
#     collab_recs = collaborative_filtering_recommendations(user_id, top_n)
    
#     hybrid_recs = pd.concat([content_recs, collab_recs]).drop_duplicates()
#     return hybrid_recs.head(top_n)
# import pandas as pd
# import numpy as np
# from sklearn.metrics.pairwise import cosine_similarity
# from sklearn.feature_extraction.text import TfidfVectorizer
# import os

# # Load product data
# BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# PRODUCT_PATH = os.path.join(BASE_DIR, 'home', 'data', 'cleaned_data.csv')
# df = pd.read_csv(PRODUCT_PATH)

# # Load user ratings data
# RATINGS_PATH = os.path.join(BASE_DIR, 'home', 'data', 'ratings_data.csv')
# ratings_df = pd.read_csv(RATINGS_PATH)

# # Ensure required columns exist
# df = df[['name', 'ratings', 'no_of_ratings', 'main_category', 'sub_category']]
# df['tags'] = df['main_category'] + " " + df['sub_category']

# # --- Content-Based Filtering ---
# def content_based_recommendations(item_name, top_n=10):
#     if item_name not in df['name'].values:
#         return pd.DataFrame()  # Return empty if product not found
    
#     # Vectorize product tags
#     tfidf_vectorizer = TfidfVectorizer(stop_words='english')
#     tfidf_matrix = tfidf_vectorizer.fit_transform(df['tags'])
    
#     # Compute cosine similarity
#     cosine_sim = cosine_similarity(tfidf_matrix, tfidf_matrix)
    
#     # Find index of item
#     item_idx = df[df['name'] == item_name].index[0]
    
#     # Get similar items
#     similar_items = list(enumerate(cosine_sim[item_idx]))
#     similar_items = sorted(similar_items, key=lambda x: x[1], reverse=True)[1:top_n+1]
    
#     # Get recommended product names
#     recommended_indices = [i[0] for i in similar_items]
#     return df.iloc[recommended_indices][['name', 'ratings', 'no_of_ratings']]


# # --- Collaborative Filtering ---
# def collaborative_filtering_recommendations(user_id, top_n=10):
#     # Pivot ratings data to create user-item matrix
#     ratings_matrix = ratings_df.pivot_table(index='user_id', columns='product_name', values='ratings', fill_value=0)
    
#     if user_id not in ratings_matrix.index:
#         return pd.DataFrame()  # Return empty if user not found
    
#     user_sim = cosine_similarity(ratings_matrix)
#     user_idx = list(ratings_matrix.index).index(user_id)
    
#     # Get similar users
#     similar_users = list(enumerate(user_sim[user_idx]))
#     similar_users = sorted(similar_users, key=lambda x: x[1], reverse=True)[1:top_n+1]
    
#     # Get recommended products
#     recommended_items = []
#     for idx, _ in similar_users:
#         rated_products = ratings_matrix.iloc[idx]
#         recommended_items.extend(rated_products[rated_products > 0].index.tolist())
    
#     return df[df['name'].isin(recommended_items)][['name', 'ratings', 'no_of_ratings']].head(top_n)


# # --- Hybrid Recommendation ---
# def hybrid_recommendations(user_id, item_name, top_n=10):
#     content_recs = content_based_recommendations(item_name, top_n)
#     collab_recs = collaborative_filtering_recommendations(user_id, top_n)
    
#     hybrid_recs = pd.concat([content_recs, collab_recs]).drop_duplicates()
#     return hybrid_recs.head(top_n)



# def content_based_recommendations(item_name, top_n=10):
#     if item_name not in df['name'].values:
#         return pd.DataFrame()  # Return empty if product not found
    
#     # Vectorize product tags
#     tfidf_vectorizer = TfidfVectorizer(stop_words='english')
#     tfidf_matrix = tfidf_vectorizer.fit_transform(df['tags'])
    
#     # Find index of item
#     item_idx = df[df['name'] == item_name].index[0]
    
#     # Compute cosine similarity for just this item with all other items
#     cosine_sim = cosine_similarity(tfidf_matrix[item_idx], tfidf_matrix)
    
#     # Get similar items (excluding the input item itself)
#     similar_items = list(enumerate(cosine_sim[0]))
#     similar_items = sorted(similar_items, key=lambda x: x[1], reverse=True)[1:top_n+1]
    
#     # Get recommended product names
#     recommended_indices = [i[0] for i in similar_items]
#     return df.iloc[recommended_indices][['name', 'ratings', 'no_of_ratings']]
# def content_based_recommendations(item_name, top_n=10):
#     if item_name not in df['name'].values:
#         print(f"Item {item_name} not found in the dataset.")
#         return pd.DataFrame()  # Return empty if product not found
    
#     # Vectorize product tags
#     tfidf_vectorizer = TfidfVectorizer(stop_words='english')
#     tfidf_matrix = tfidf_vectorizer.fit_transform(df['tags'])
    
#     # Find index of item
#     item_idx = df[df['name'] == item_name].index[0]
    
#     # Compute cosine similarity for just this item with all other items
#     cosine_sim = cosine_similarity(tfidf_matrix[item_idx], tfidf_matrix)
    
#     # Get similar items (excluding the input item itself)
#     similar_items = list(enumerate(cosine_sim[0]))
#     similar_items = sorted(similar_items, key=lambda x: x[1], reverse=True)[1:top_n+1]
    
#     # Get recommended product names
#     recommended_indices = [i[0] for i in similar_items]
#     print(f"Recommended Indices: {recommended_indices}")  # Debugging line
    
#     return df.iloc[recommended_indices][['name', 'ratings', 'no_of_ratings']]

# def content_based_recommendations(item_name, top_n=10):
#     if item_name not in df['name'].values:
#         print(f"Item {item_name} not found in the dataset.")
#         return []  # Return an empty list if the product is not found
    
#     # Vectorize product tags
#     tfidf_vectorizer = TfidfVectorizer(stop_words='english')
#     tfidf_matrix = tfidf_vectorizer.fit_transform(df['tags'])
    
#     # Find index of item
#     item_idx = df[df['name'] == item_name].index[0]
    
#     # Compute cosine similarity for just this item with all other items
#     cosine_sim = cosine_similarity(tfidf_matrix[item_idx], tfidf_matrix)
    
#     # Get similar items (excluding the input item itself)
#     similar_items = list(enumerate(cosine_sim[0]))
#     similar_items = sorted(similar_items, key=lambda x: x[1], reverse=True)[1:top_n+1]
    
#     # Get recommended product names
#     recommended_indices = [i[0] for i in similar_items]
#     print(f"Recommended Indices: {recommended_indices}")  # Debugging line
    
#     # Convert the DataFrame to a list of dictionaries
#     recommended_products = df.iloc[recommended_indices][['name', 'ratings', 'no_of_ratings', 'image_url', 'discount_price']].to_dict('records')
    
#     return recommended_products
# def content_based_recommendations(item_name, top_n=10):
#     if item_name not in df['name'].values:
#         print(f"Item {item_name} not found in the dataset.")
#         return []  # Return an empty list if the product is not found
    
#     # Vectorize product tags
#     tfidf_vectorizer = TfidfVectorizer(stop_words='english')
#     tfidf_matrix = tfidf_vectorizer.fit_transform(df['tags'])
    
#     # Find index of item
#     item_idx = df[df['name'] == item_name].index[0]
    
#     # Compute cosine similarity for just this item with all other items
#     cosine_sim = cosine_similarity(tfidf_matrix[item_idx], tfidf_matrix)
    
#     # Get similar items (excluding the input item itself)
#     similar_items = list(enumerate(cosine_sim[0]))
#     similar_items = sorted(similar_items, key=lambda x: x[1], reverse=True)[1:top_n+1]
    
#     # Get recommended product names
#     recommended_indices = [i[0] for i in similar_items]
#     print(f"Recommended Indices: {recommended_indices}")  # Debugging line
    
#     # Convert the DataFrame to a list of dictionaries
#     recommended_products = df.iloc[recommended_indices][['name', 'ratings', 'no_of_ratings', 'image_url', 'discount_price']].to_dict('records')
    
#     print(f"Recommended Products: {recommended_products}")  # Debugging line
#     return recommended_products


# import pandas as pd
# from sklearn.metrics.pairwise import cosine_similarity
# from sklearn.feature_extraction.text import TfidfVectorizer
# import os 
# from apps.cart.models import CartItem
# from apps.payments.models import OrderItem

# # Load dataset
# BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# DATA_PATH = os.path.join(BASE_DIR, 'home', 'data', 'cleaned_data.csv')
# df = pd.read_csv(DATA_PATH)

# # Ensure required columns exist
# df = df[['name', 'ratings', 'no_of_ratings', 'main_category', 'sub_category']]

# # Create 'tags' column
# df['tags'] = df['main_category'] + " " + df['sub_category']



# #Loading packages and libraries

# import pandas as pd
# import numpy as np
# import matplotlib.pyplot as plt
# import seaborn as sns

# from sklearn.metrics.pairwise import cosine_similarity
# from sklearn.feature_extraction.text import TfidfVectorizer

# import os
# from scipy.sparse import coo_matrix
# # Read your dataset
# DATASETS_DIR = 'C:/Users/ACER/OneDrive/Desktop/URBAN CART 3/urban_cart/datasets'
# # Load the CSV files with full path
# casual_shoes = pd.read_csv(os.path.join(DATASETS_DIR, 'Casual Shoes.csv'))
# formal_shoes = pd.read_csv(os.path.join(DATASETS_DIR, 'Formal Shoes.csv'))
# sports_shoes = pd.read_csv(os.path.join(DATASETS_DIR, 'Sports Shoes.csv'))
# shoes = pd.read_csv(os.path.join(DATASETS_DIR, 'Shoes.csv'))
# kids_shoes = pd.read_csv(os.path.join(DATASETS_DIR, 'Kids Shoes.csv'))
# DATASETS = [casual_shoes, formal_shoes, sports_shoes, shoes, kids_shoes]
# for dataset in DATASETS:


# train_data = pd.read_csv(dataset)
# train_data.columns
# train_data.head(2)
# train_data = train_data[['user_id','product_id', 'rating', 'rating_count', 'category', 'product_name', 'img_link', 'about_product']]
# train_data.head(3)
# #Basic operations
# train_data['about_product']
# train_data.shape
# #Getting missing values to identify them
# train_data.isnull().sum()
# # Fill missing values in 'Product Reviews Count' with a default value (e.g., 0)
# train_data.loc[:, 'rating_count'] = train_data['rating_count'].fillna(0)
# #Getting missing values to identify them
# train_data.isnull().sum()
# train_data.duplicated().sum()
# train_data_cleaned = train_data.drop_duplicates(subset=['user_id', 'product_id'])
# train_data_cleaned
# # make columns shorter
# # Define the mapping of current column names to shorter names
# column_name_mapping = {
#     'user_id': 'ID',
#     'product_id': 'ProdID',
#     'rating': 'Rating',
#     'rating_count': 'ReviewCount',
#     'category': 'Category',
#     'product_name': 'Name',
#     'img_link': 'ImageURL',
#     'about_product': 'Description'
# }


# # Rename the columns using the mapping
# train_data.rename(columns=column_name_mapping, inplace=True)
# train_data
# from sklearn.preprocessing import LabelEncoder

# # Initialize LabelEncoder
# le_id = LabelEncoder()
# le_prod = LabelEncoder()

# train_data['ID']= le_id.fit_transform(train_data['ID'])
# train_data['ProdID'] = le_prod.fit_transform(train_data['ProdID'])
# train_data
# train_data.duplicated().sum()
# #EDA (Exploratory Data Analysis)

# # Basic statistics
# num_users = train_data['ID'].nunique()
# num_items = train_data['ProdID'].nunique()
# num_ratings = train_data['Rating'].nunique()

# print(f"Number of unique users: {num_users}")
# print(f"Number of unique items: {num_items}")
# print(f"Number of unique ratings: {num_ratings}")
# # Distribution of interactions
# plt.figure(figsize=(12, 5))
# plt.subplot(1, 2, 1)
# train_data['ID'].value_counts().hist(bins=10, edgecolor='k')
# plt.xlabel('Interactions per User')
# plt.ylabel('Number of Users')
# plt.title('Distribution of Interactions per User')

# plt.subplot(1, 2, 2)
# train_data['ProdID'].value_counts().hist(bins=10, edgecolor='k',color='green')
# plt.xlabel('Interactions per Item')
# plt.ylabel('Number of Items')
# plt.title('Distribution of Interactions per Item')

# plt.tight_layout()
# plt.show()
# # most rated counts
# train_data['Rating'].value_counts().plot(kind='bar',color='Black')
# #Data Cleaning and Tags Creations
# import spacy
# from spacy.lang.en.stop_words import STOP_WORDS

# nlp = spacy.load("en_core_web_sm")

# def clean_and_extract_tags(text):
#     doc = nlp(text.lower())
#     tags = [token.text for token in doc if token.text.isalnum() and token.text not in STOP_WORDS]
#     return ', '.join(tags)

# columns_to_extract_tags_from = ['Description']

# for column in columns_to_extract_tags_from:
#     train_data[column] = train_data[column].apply(clean_and_extract_tags)
# # Replace '|' with ',' in the 'Category' column for all records
# train_data['Category'] = train_data['Category'].str.replace('|', ',')

# train_data
# columns_to_extract_tags = ['Description','Category']

# # Concatenate the cleaned tags from all relevant columns
# train_data['Tags'] = train_data[columns_to_extract_tags].apply(lambda row: ', '.join(row), axis=1)

# # Convert the 'Rating' column to numeric, forcing errors to NaN
# train_data['Rating'] = pd.to_numeric(train_data['Rating'], errors='coerce')
# train_data.to_csv('cleaned_data.csv', index=False)
# from IPython.display import FileLink

# # Provide the link to download the cleaned data file
# FileLink('cleaned_data.csv')

# #Rating Base Recommendations System



# average_ratings =train_data.groupby(['Name','ReviewCount','ImageURL'])['Rating'].mean().reset_index()
# average_ratings.sort_values(by='Rating', ascending=False)
# top_rated_items = average_ratings.sort_values(by='Rating', ascending=False)
# rating_base_recommendation = top_rated_items.head(15)
# rating_base_recommendation
# train_data.head(2)
# #Content Base Recommendation system (User Preferences or Items similarities)
# from sklearn.feature_extraction.text import TfidfVectorizer
# from sklearn.metrics.pairwise import cosine_similarity

# tfidf_vectorizer = TfidfVectorizer(stop_words='english')
# tfidf_matrix_content = tfidf_vectorizer.fit_transform(train_data['Tags'])
# cosine_similarities_content = cosine_similarity(tfidf_matrix_content,tfidf_matrix_content)
# cosine_similarities_content
# train_data['Name'][0]
# item_name = 'Wayona Nylon Braided USB to Lightning Fast Charging and Data Sync Cable Compatible for iPhone 13, 12,11, X, 8, 7, 6, 5, iPad Air, Pro, Mini (3 FT Pack of 1, Grey)'
# item_index = train_data[train_data['Name']==item_name].index[0]
# similar_items = list(enumerate(cosine_similarities_content[item_index]))
# sorted(similar_items, key=lambda x:x[1], reverse=True)
# similar_items = sorted(similar_items, key=lambda x:x[1], reverse=True)
# top_similar_items = similar_items[1:10]

# recommended_items_indics = [x[0] for x in top_similar_items]
# train_data.iloc[recommended_items_indics][['Name','ReviewCount','Rating']]
# #Function To Recommend Products for Content Base

# from sklearn.feature_extraction.text import TfidfVectorizer
# from sklearn.metrics.pairwise import cosine_similarity

# def content_based_recommendations(train_data, item_name, top_n=10):
#     # Check if the item name exists in the training data
#     if item_name not in train_data['Name'].values:
#         print(f"Item '{item_name}' not found in the training data.")
#         return pd.DataFrame()

#     # Create a TF-IDF vectorizer for item descriptions
#     tfidf_vectorizer = TfidfVectorizer(stop_words='english')

#     # Apply TF-IDF vectorization to item descriptions
#     tfidf_matrix_content = tfidf_vectorizer.fit_transform(train_data['Tags'])

#     # Calculate cosine similarity between items based on descriptions
#     cosine_similarities_content = cosine_similarity(tfidf_matrix_content, tfidf_matrix_content)

#     # Find the index of the item
#     item_index = train_data[train_data['Name'] == item_name].index[0]

#     # Get the cosine similarity scores for the item
#     similar_items = list(enumerate(cosine_similarities_content[item_index]))

#     # Sort similar items by similarity score in descending order
#     similar_items = sorted(similar_items, key=lambda x: x[1], reverse=True)

#     # Get the top N most similar items (excluding the item itself)
#     top_similar_items = similar_items[1:top_n+1]

#     # Get the indices of the top similar items
#     recommended_item_indices = [x[0] for x in top_similar_items]

#     # Get the details of the top similar items
#     recommended_items_details = train_data.iloc[recommended_item_indices][['Name', 'ReviewCount', 'ImageURL', 'Rating']]

#     return recommended_items_details
# # Example: Get content-based recommendations for a specific item
# item_name = 'AmazonBasics Flexible Premium HDMI Cable (Black, 4K@60Hz, 18Gbps), 3-Foot'
# content_based_rec = content_based_recommendations(train_data, item_name, top_n=10)

# content_based_rec
# # Example: Get content-based recommendations for a specific item
# item_name = 'LG 80 cm (32 inches) HD Ready Smart LED TV 32LM563BPTC (Dark Iron Gray)'
# content_based_rec = content_based_recommendations(train_data, item_name, top_n=8)

# content_based_rec
# filtered_data = train_data[train_data['ProdID'] == 346]
# train_data
# # Create the User-Item matrix
# user_item_matrix = train_data.pivot_table(index='ID', columns='ProdID', values='Rating', aggfunc='mean').fillna(0)
# user_item_matrix
# user_item_matrix = train_data.pivot_table(index='ID', columns='ProdID', values='Rating',aggfunc='mean').fillna(0).astype(int)
# user_item_matrix
# user_similarity = cosine_similarity(user_item_matrix)
# user_similarity
# target_user_id = 2
# target_user_index = user_item_matrix.index.get_loc(target_user_id)
# user_similarities = user_similarity[target_user_index]
# user_similarities
# similar_user_indices = user_similarities.argsort()[::-1][1:]
# recommend_items = []

# for user_index in similar_user_indices:
#     rated_by_similar_user = user_item_matrix.iloc[user_index]
#     not_rated_by_target_user = (rated_by_similar_user==0) & (user_item_matrix.iloc[target_user_index]==0)
    
#     recommend_items.extend(user_item_matrix.columns[not_rated_by_target_user][:10])

# recommended_items_details = train_data[train_data['ProdID'].isin(recommend_items)][['Name','ReviewCount','ImageURL','Rating']]
# recommended_items_details.head(10)
# def collaborative_filtering_recommendations(train_data, target_user_id, top_n=10):
#     # Create the user-item matrix
#     user_item_matrix = train_data.pivot_table(index='ID', columns='ProdID', values='Rating', aggfunc='mean').fillna(0)

#     # Calculate the user similarity matrix using cosine similarity
#     user_similarity = cosine_similarity(user_item_matrix)

#     # Find the index of the target user in the matrix
#     target_user_index = user_item_matrix.index.get_loc(target_user_id)

#     # Get the similarity scores for the target user
#     user_similarities = user_similarity[target_user_index]

#     # Sort the users by similarity in descending order (excluding the target user)
#     similar_users_indices = user_similarities.argsort()[::-1][1:]

#     # Generate recommendations based on similar users
#     recommended_items = []

#     for user_index in similar_users_indices:
#         # Get items rated by the similar user but not by the target user
#         rated_by_similar_user = user_item_matrix.iloc[user_index]
#         not_rated_by_target_user = (rated_by_similar_user == 0) & (user_item_matrix.iloc[target_user_index] == 0)

#         # Extract the item IDs of recommended items
#         recommended_items.extend(user_item_matrix.columns[not_rated_by_target_user][:top_n])

#     # Get the details of recommended  'ImageURL', 'Rating']]

#     return recommended_items_details.head(10)


# # Example usage
# target_user_id = 2
# top_n = 5
# collaborative_filtering_rec = collaborative_filtering_recommendations(train_data, target_user_id)
# print(f"Top {top_n} recommendations for User {target_user_id}:")
# collaborative_filtering_rec
# # Hybrid Recommendations (Combine Content-Based and Collaborative Filtering)
# def hybrid_recommendations(train_data,target_user_id, item_name, top_n=10):
#     # Get content-based recommendations
#     content_based_rec = content_based_recommendations(train_data,item_name, top_n)

#     # Get collaborative filtering recommendations
#     collaborative_filtering_rec = collaborative_filtering_recommendations(train_data,target_user_id, top_n)
    
#     # Merge and deduplicate the recommendations
#     hybrid_rec = pd.concat([content_based_rec, collaborative_filtering_rec]).drop_duplicates()
    

#     return hybrid_rec.head(10)

# # Example usage: Get hybrid recommendations for a specific user and item
# target_user_id = 12 # Change this to the user_id you want recommendations for
# item_name = "Philips Daily Collection HD2582/00 830-Watt 2-Slice Pop-up Toaster (White)"  
# hybrid_rec = hybrid_recommendations(train_data,target_user_id, item_name, top_n=10)

# print(f"Top 10 Hybrid Recommendations for User {target_user_id} and Item '{item_name}':")
# hybrid_rec


# import pandas as pd
# from sklearn.feature_extraction.text import TfidfVectorizer
# from sklearn.metrics.pairwise import cosine_similarity
# from sklearn.metrics.pairwise import linear_kernel
# import os

# # Load dataset
# BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# DATA_PATH = os.path.join(BASE_DIR, 'home', 'data', 'cleaned_data.csv')
# df = pd.read_csv(DATA_PATH)

# # Ensure relevant columns exist
# df = df[['name', 'tags', 'image', 'link', 'ratings', 'no_of_ratings', 'discount_price', 'actual_price']]

# # Vectorize the 'tags' column for similarity calculation
# tfidf_vectorizer = TfidfVectorizer(stop_words='english')
# tfidf_matrix = tfidf_vectorizer.fit_transform(df['tags'])

# # Compute cosine similarity
# # cosine_sim = cosine_similarity(tfidf_matrix, tfidf_matrix)
# cosine_sim = linear_kernel(tfidf_matrix, tfidf_matrix)
# # Create a function to get similar products
# def get_recommendations(product_name, top_n=6):
#     # Ensure the product exists in the dataset
#     if product_name not in df['name'].values:
#         return []

#     # Find index of the given product
#     idx = df[df['name'] == product_name].index[0]

#     # Get similarity scores for the product
#     sim_scores = list(enumerate(cosine_sim[idx]))

#     # Sort by similarity score
#     sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)[1:top_n+1]

#     # Get the indices of similar products
#     product_indices = [i[0] for i in sim_scores]

#     # Return recommended product details
#     recommended_products = df.iloc[product_indices][['name', 'image', 'link', 'ratings', 'no_of_ratings', 'discount_price', 'actual_price']]
#     return recommended_products.to_dict(orient='records')


# import pandas as pd
# from sklearn.feature_extraction.text import TfidfVectorizer
# from sklearn.metrics.pairwise import linear_kernel
# import os

# # Load dataset
# BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# DATA_PATH = os.path.join(BASE_DIR, 'home', 'data', 'cleaned_data.csv')

# df = pd.read_csv(DATA_PATH)

# # Ensure relevant columns exist
# df = df[['name', 'tags', 'image', 'link', 'ratings', 'no_of_ratings', 'discount_price', 'actual_price']].copy()

# # Handle missing values in 'tags' column
# df['tags'] = df['tags'].fillna('')

# # Convert all names to lowercase for case-insensitive matching
# df['name'] = df['name'].str.lower()

# # Vectorize the 'tags' column for similarity calculation
# tfidf_vectorizer = TfidfVectorizer(stop_words='english')
# tfidf_matrix = tfidf_vectorizer.fit_transform(df['tags'])

# # Compute similarity using memory-efficient linear_kernel
# cosine_sim = linear_kernel(tfidf_matrix, tfidf_matrix)

# # Function to get product recommendations
# def get_recommendations(product_name, top_n=6):
#     # Convert input to lowercase for consistent matching
#     product_name = product_name.lower()

#     # Ensure the product exists in the dataset
#     matching_index = df[df['name'] == product_name].first_valid_index()
#     if matching_index is None:
#         return []

#     # Get similarity scores for the product
#     sim_scores = list(enumerate(cosine_sim[matching_index]))

#     # Sort by similarity score, excluding itself (index 0)
#     sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)[1:top_n+1]

#     # Get the indices of similar products
#     product_indices = [i[0] for i in sim_scores]

#     # Return recommended product details
#     recommended_products = df.iloc[product_indices][['name', 'image', 'link', 'ratings', 'no_of_ratings', 'discount_price', 'actual_price']]
#     return recommended_products.to_dict(orient='records')

# # Example usage:
# # recommendations = get_recommendations("Nike Running Shoes")
# # print(recommendations)


# import pandas as pd
# from sklearn.feature_extraction.text import TfidfVectorizer
# from sklearn.neighbors import NearestNeighbors
# import os


# # Load dataset
# BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# DATA_PATH = os.path.join(BASE_DIR, 'home', 'data', 'cleaned_data.csv')

# df = pd.read_csv(DATA_PATH)

# # Ensure relevant columns exist
# df = df[['name', 'tags', 'image', 'link', 'ratings', 'no_of_ratings', 'discount_price', 'actual_price']].copy()

# # Handle missing values in 'tags' column
# df['tags'] = df['tags'].fillna('')

# # Convert all names to lowercase for case-insensitive matching
# df['name'] = df['name'].str.lower()

# # Vectorize the 'tags' column
# tfidf_vectorizer = TfidfVectorizer(stop_words='english')
# tfidf_matrix = tfidf_vectorizer.fit_transform(df['tags'])

# # Use Nearest Neighbors for similarity search (efficient memory usage)
# nn_model = NearestNeighbors(metric='cosine', algorithm='brute')
# nn_model.fit(tfidf_matrix)

# # Function to get product recommendations
# def get_recommendations(product_name, top_n=12):
#     product_name = product_name.lower()
    
#     # Find the product index
#     matching_index = df[df['name'] == product_name].first_valid_index()
#     if matching_index is None:
#         return []

#     # Find top N similar items
#     distances, indices = nn_model.kneighbors(tfidf_matrix[matching_index], n_neighbors=top_n+1)

#     # Get recommended products (excluding itself)
#     product_indices = indices[0][1:]  # Exclude itself (first result)

#     # Return recommended product details
#     recommended_products = df.iloc[product_indices][['name', 'image', 'link', 'ratings', 'no_of_ratings', 'discount_price', 'actual_price']]
#     return recommended_products.to_dict(orient='records')

# # Example usage:
# # recommendations = get_recommendations("Nike Running Shoes")
# # print(recommendations)
# import pandas as pd
# from sklearn.feature_extraction.text import TfidfVectorizer
# from sklearn.neighbors import NearestNeighbors
# import os
# import random


# # Load dataset
# BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# DATA_PATH = os.path.join(BASE_DIR, 'home', 'data', 'cleaned_data.csv')

# df = pd.read_csv(DATA_PATH)

# # Ensure relevant columns exist
# df = df[['name', 'tags', 'image', 'link', 'ratings', 'no_of_ratings', 'discount_price', 'actual_price']].copy()

# # Handle missing values in 'tags' column
# df['tags'] = df['tags'].fillna('')

# # Convert all names to lowercase for case-insensitive matching
# df['name'] = df['name'].str.lower()

# # Vectorize the 'tags' column
# tfidf_vectorizer = TfidfVectorizer(stop_words='english')
# tfidf_matrix = tfidf_vectorizer.fit_transform(df['tags'])

# # Use Nearest Neighbors for similarity search (efficient memory usage)
# nn_model = NearestNeighbors(metric='cosine', algorithm='brute')
# nn_model.fit(tfidf_matrix)

# # Function to get product recommendations
# def get_recommendations(product_name, top_n=12):
#     # Normalize the product name (in case it's case-sensitive)
#     product_name = product_name.strip().lower()
    
#     # Find the product index
#     matching_index = df[df['name'].str.lower() == product_name].index

#     if matching_index.empty:
#         return []  # Return empty if no match is found

#     # We expect `matching_index` to have one entry, so get the first match
#     matching_index = matching_index[0]

#     # Find top N similar items using KNN model
#     distances, indices = nn_model.kneighbors(tfidf_matrix[matching_index], n_neighbors=top_n + 50)  # Get more neighbors
    
#     # Get recommended products (exclude the original product itself)
#     product_indices = indices[0][1:]  # Exclude itself (first result)
    
#     # Shuffle the product indices to randomize recommendations
#     random.shuffle(product_indices)

#     # Limit the number of recommendations (top N)
#     product_indices = product_indices[:top_n]

#     # Fetch recommended product details based on the indices
#     recommended_products = df.iloc[product_indices][['name', 'image', 'link', 'ratings', 'no_of_ratings', 'discount_price', 'actual_price']]

#     # Return the recommended products as a dictionary
#     return recommended_products.to_dict(orient='records')

# # Example usage:
# # recommendations = get_recommendations("Nike Running Shoes")
# # print(recommendations)

import numpy as np
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.neighbors import NearestNeighbors
from sklearn.metrics.pairwise import cosine_similarity
from apps.admin1.models import Product  # Import your Product model

# 1. Fetch products from the database
def get_product_data():
    products = Product.objects.all().only('id', 'name', 'manufacturer__name', 'main_category__name', 'sub_category__name', 'ratings', 'no_of_ratings', 'discount_price', 'actual_price')
    # Prepare a DataFrame for easy manipulation
    product_data = pd.DataFrame(list(products.values('id', 'name', 'manufacturer__name', 'main_category__name', 'sub_category__name', 'ratings', 'no_of_ratings', 'discount_price', 'actual_price')))
    return product_data

# 2. Prepare the text data for TF-IDF vectorization
def create_tfidf_matrix(product_data):
    # Combine relevant fields into a single text string
    product_data['combined_features'] = product_data['name'] + " " + product_data['manufacturer__name'] + " " + product_data['main_category__name'] + " " + product_data['sub_category__name']
    
    # TF-IDF Vectorization
    tfidf = TfidfVectorizer(stop_words='english')
    tfidf_matrix = tfidf.fit_transform(product_data['combined_features'])
    return tfidf_matrix, product_data

# 3. Build the recommendation model using K-Nearest Neighbors
def build_knn_model(tfidf_matrix, n_neighbors=12):
    model = NearestNeighbors(metric='cosine', algorithm='brute', n_neighbors=n_neighbors, n_jobs=-1)
    model.fit(tfidf_matrix)
    return model

# 4. Get recommendations for a given product
def get_recommendations(product_id, top_n=12):
    product_data = get_product_data()
    tfidf_matrix, product_data = create_tfidf_matrix(product_data)
    
    # Find the index of the product in the product_data DataFrame
    matched_product_data = product_data[product_data['id'] == product_id]
    
    if matched_product_data.empty:
        # If no matching product is found, return an empty list or a default recommendation
        return []

    # Get the index of the product
    product_idx = matched_product_data.index[0]
    
    # Build the KNN model and get recommendations
    model = build_knn_model(tfidf_matrix, n_neighbors=top_n+1)
    distances, indices = model.kneighbors(tfidf_matrix[product_idx], n_neighbors=top_n+1)  # +1 to exclude itself
    
    # Exclude the first recommendation (the product itself)
    recommended_indices = indices[0][1:]
    
    # Fetch the recommended products from the database
    recommended_products = Product.objects.filter(id__in=product_data.iloc[recommended_indices]['id'])
    
    recommended_products_data = [
        {
            'id': product.id,
            'name': product.name,
            'image': product.image_url,
            'site_link': product.site_link,
            'ratings': product.ratings,
            'no_of_ratings': product.no_of_ratings,
            'discount_price': product.discount_price,
            'actual_price': product.actual_price,
        }
        for product in recommended_products
    ]
    
    return recommended_products_data
