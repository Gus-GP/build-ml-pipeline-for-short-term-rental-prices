#!/usr/bin/env python
"""
Download from W&B the raw dataset and apply some basic data cleaning, exporting the result to a new artifact

Author: Udacity
Modified by: Gustavo Grinsteins
Modified Date: 06/30/2023
"""
import argparse
import logging
import wandb
import pandas as pd


logging.basicConfig(level=logging.INFO, format="%(asctime)-15s %(message)s")
logger = logging.getLogger()


def go(args):
    """
    Basic cleaning procedure for the ML pipeline

    Arguments:
        args (argparse): contains the information for the arguments defined in MLproject
    Return:
        Nothing
    """

    run = wandb.init(job_type="basic_cleaning")
    run.config.update(args)

    # Download input artifact. This will also log that this script is using this
    # particular version of the artifact
    artifact_local_path = run.use_artifact(args.input_artifact).file()

    ######################
    # YOUR CODE HERE     #
    ######################

    logger.info("Reading CSV Data into Pandas Dataframe")
    df = pd.read_csv(artifact_local_path)

    logger.info(f"Dropping outliers. Price range: [{args.min_price},{args.max_price}]")
    min_price = args.min_price
    max_price = args.max_price
    idx = df['price'].between(min_price, max_price)
    df = df[idx].copy()

    logger.info("Convert last_review columns from string to datetime")
    df['last_review'] = pd.to_datetime(df['last_review'])

    logger.info("Drop rows in the dataset that are not in the proper geolocation")
    idx = df['longitude'].between(-74.25, -73.50) & df['latitude'].between(40.5, 41.2)
    df = df[idx].copy()
    
    logger.info("Creating 'clean_sample.csv' file output")
    df.to_csv("clean_sample.csv", index=False)
    
    logger.info("Uploading 'clean_sample.csv' artifact to data store")
    artifact = wandb.Artifact(
        args.output_artifact,
        type=args.output_type,
        description=args.output_description,
    )
    artifact.add_file("clean_sample.csv")
    run.log_artifact(artifact)
    
    run.finish()
    logger.info("Run Finished Successfully!")


if __name__ == "__main__":
    """
    Entry point for thr Basic Cleaning pipeline step

    Arguments:
        None
    Return:
        Nothing
    """

    parser = argparse.ArgumentParser(description="A very basic data cleaning")


    parser.add_argument(
        "--input_artifact", 
        type=str,
        help="Name of Input Artifact",
        required=True
    )

    parser.add_argument(
        "--output_artifact", 
        type=str,
        help="Name of Output Artifact",
        required=True
    )

    parser.add_argument(
        "--output_type", 
        type=str,
        help="The type for the output artifact",
        required=True
    )

    parser.add_argument(
        "--output_description", 
        type=str,
        help="description for the output artifact",
        required=True
    )

    parser.add_argument(
        "--min_price", 
        type=float,
        help="Minimum Price",
        required=True
    )

    parser.add_argument(
        "--max_price", 
        type=float,
        help="Maximum Price",
        required=True
    )


    args = parser.parse_args()

    go(args)
