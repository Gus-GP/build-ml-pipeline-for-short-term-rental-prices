
# Build an ML Pipeline for Short-Term Rental Prices in NYC

- Project **ML Pipeline for Short-Term Rental Prices in NYC** of ML DevOps Engineer Nanodegree Udacity

## Project Description

Reusable end-to end pipeline for a property management company renting rooms and properties for short periods of 
time on various rental platforms. The goal is to estimate the typical price for a given property based 
on the price of similar properties.

## Link to W&B Project
https://wandb.ai/gusgrinsteins/nyc_airbnb/

## Link to Github repository
https://github.com/Gus-GP/build-ml-pipeline-for-short-term-rental-prices

## Best Model Results

Hyperparameters:
modeling:
  random_forest:
    n_estimators: 100
    max_depth: 15
    min_samples_split: 4
    min_samples_leaf: 3
    criterion: mae
    max_features: 0.5

Data: /components/get_data/data/sample2.csv

### Training & Validation

From W&B Run titled **bumbling-waterfall-30**

* Artifact Model: random_forest_export:v16
* r2 score -> 0.5863
* Mean Absolute Error (MAE): 31.05198

### Testing

From W&B Run titled **iconic-yogurt-22**

* Artifact Model: random_forest_export:v16
* r2 score -> 0.5796
* Mean Absolute Error (MAE): 32.3608

The random_forest_export:v16 model performance is comparable to what was obtained against the validation set.



