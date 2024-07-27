import streamlit as st

import pathlib
import polars as pl


def prepare_car_reviews_data(data_path: pathlib.Path, vehicle_years: list[int] = [2017]):
    """Prepare the car reviews dataset for ChromaDB"""

    # Define the schema to ensure proper data types are enforced
    dtypes = {
        "": pl.Int64,
        "Review_Date": pl.Utf8,
        "Author_Name": pl.Utf8,
        "Vehicle_Title": pl.Utf8,
        "Review_Title": pl.Utf8,
        "Review": pl.Utf8,
        "Rating": pl.Float64,
    }

    # Scan the car reviews dataset(s)
    car_reviews = pl.scan_csv(data_path, dtypes=dtypes)


    # Extract the vehicle title and year as new columns
    # Filter on selected years
    car_review_db_data = (
        car_reviews.with_columns(
            [
                (
                    pl.col("Vehicle_Title")
                    .str.split(by=" ")
                    .list.get(0)
                    .cast(pl.Int64)
                ).alias("Vehicle_Year"),
                (pl.col("Vehicle_Title").str.split(by=" ").list.get(1)).alias(
                    "Vehicle_Model"
                ),
            ]
        )
        .filter(pl.col("Vehicle_Year").is_in(vehicle_years))
        .select(
            [
                "Review_Title",
                "Review",
                "Rating",
                "Vehicle_Year",
                "Vehicle_Model",
            ]
        )
        .sort(["Vehicle_Model", "Rating"])
        .collect()
    )
    st.text(car_review_db_data)
    st.text(car_review_db_data.shape)

    # Create ids, documents, and metadatas data in the format chromadb expects
    ids = [f"review{i}" for i in range(car_review_db_data.shape[0])]
    st.text(ids)
    documents = car_review_db_data["Review"].to_list()
    st.text(documents[2])
    metadatas = car_review_db_data.drop("Review").to_dicts()
    st.text(metadatas[2])

    return {"ids": ids, "documents": documents, "metadatas": metadatas}

def st_summary():
    st.markdown("In your car.py script, prepare_car_reviews_data() accepts the path to the car reviews dataset and a list of vehicle years to filter on, and it returns a dictionary with the review data properly formatted for ChromaDB. You can include different vehicle years, but keep in mind that the more years you include, the longer it’ll take to build the collection. By default, you’re only including vehicles from 2017.")
    st.markdown("In this block, you import prepare_car_reviews_data() from car.py, store the path to the raw review csv datasets, and create chroma_car_reviews_dict, which stores the reviews in a ChromaDB-compatible format. You then display the ID, document text, and metadata associated with one of the reviews.")
    # st.image("./data/images/featureengineering.png")
