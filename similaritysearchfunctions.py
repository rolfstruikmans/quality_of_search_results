#these methods are used to calculate the relevance or quality of a query vector in a vector space
#this python-file can be changed into a Class that implements the langchain Vector Store Base Class interface and augments it with the 
#function similarity_search_with_quality_by_vector()

import pandas as pd
import numpy as np

def similarity_search_with_quality_by_vector(query_vector, vector_store, vector_dataframe, num_results=5, omit_first=False):
  search_results_df = get_nearest_neighbors(query_vector, num_results, vector_store)
  #added at 2024-08-04. If the query_vector is in the vector space you do not want to have it in the search results
  if omit_first:
    search_results_df = search_results_df.drop(0)
    search_results_df = search_results_df.reset_index(drop=True)

  nn_id_scores = [get_nn_score_by_id(vector_id, vector_store, vector_dataframe) for vector_id in search_results_df.id]
  nn_id_scores_df = pd.DataFrame(nn_id_scores, columns=['nn_id','nn_score'])
  search_results_df['nn_id'] = nn_id_scores_df.nn_id #add column with nn_ids to search_results_df

  search_results_df['nn_score'] = nn_id_scores_df.nn_score #add column with nn_scores to search_results_df
  search_results_df['nn_distance'] = np.sqrt(search_results_df.nn_score) #add distance column that calculates the actual distances from the nn_score
  # ratio of nn_distance/distance
  qualities = [get_quality(row.distance, row.nn_distance) for index, row in search_results_df.iterrows()]
  # ratio of nn_distance/distances_mean
  mean = search_results_df.distance.mean()
  qualities_mean = [get_quality(mean, row.nn_distance) for index, row in search_results_df.iterrows()]
  # ratio of nn_distance/distances_median
  median = search_results_df.distance.median()
  qualities_median = [get_quality(median, row.nn_distance) for index, row in search_results_df.iterrows()]
  # ratio of nn_distance/distances_max
  max = search_results_df.distance.max()
  qualities_max = [get_quality(max, row.nn_distance) for index, row in search_results_df.iterrows()]

  search_results_df['quality'] = qualities
  search_results_df['quality_mean'] = qualities_mean
  search_results_df['quality_median'] = qualities_median
  search_results_df['quality_max'] = qualities_max
  return search_results_df

# function that takes query_vector and returns dataframe with index, score of NNs
def get_nearest_neighbors(query_vector, num_results, vector_store):
  #search similar documents by vector with .similarity_search_with_score_by_vector()
  search_results = vector_store.similarity_search_with_score_by_vector(query_vector, k=num_results)
  #turn search_results into a list of (id, score) tuples
  res = [(int(doc.page_content), score) for doc, score in search_results]
  #turn list of (id, score) tuples into a dataframe
  res_df = pd.DataFrame(res, columns=['id', 'score'])
  #add distance column that calculates the actual distances from the score
  res_df['distance'] = np.sqrt(res_df.score)
  return res_df
  
# get vector by id
def get_vector_by_id(id, df):
  return df.loc[df.id == id, ['x','y']].squeeze().to_list()  
  
def get_quality(distance_0, distance_1):
  #score_0: distance/mean_distance/median/distance/max_distance from query_vector to the vector you want to calculate the quality for
  #score_1: distance of vector you want to calculate the quality for to its nearest neighbor
  if distance_1 > distance_0: # this can happen when the query vector is not in the vector store and closer to its NN than the nearest neighbor of the NN
    return 1.0
  return distance_1/distance_0

def get_nn_score_by_id(vector_id, vector_store, vector_dataframe):
  vector = get_vector_by_id(vector_id, vector_dataframe)
  search_results = vector_store.similarity_search_with_score_by_vector(vector, k=2)
  nn_id = int(search_results[1][0].page_content)
  nn_score = search_results[1][1] # first search result is the vector itself, so we want the score of the second search result
  return nn_id, nn_score  
  
# takes a dataframe returned from function similarity_search_with_quality_by_vector() as argument and returns a kind of relevance number of the query_vector.
def get_relevance(df, kind = 'distance'):
  if kind == 'distance':
    return df.quality.mean()
  if kind == 'mean':
    return df.quality_mean.mean()
  if kind == 'median':
    return df.quality_median.mean()
  if kind == 'max':
    return df.quality_max.mean()  