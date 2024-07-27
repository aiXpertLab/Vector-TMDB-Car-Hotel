import streamlit as st, os, time, csv, pickle, pandas as pd, json
from streamlit_extras.stateful_button import button
from utils import st_def, tmdb, mypinecone
st_def.st_logo(title='🎥 Film Search', page_title="👋 Pinecone!", slogan='The better way to search for films')
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
TMDB_API_KEY    = os.environ.get('TMDB_API_KEY')
OPENAI_API_KEY  = os.environ.get('OPENAI_API_KEY')
PINECONE_API_KEY= os.environ.get('PINECONE_API_KEY')
CSV_HEADER = ['Title', 'Runtime (minutes)', 'Language', 'Overview','Release Year', 'Genre', 'Keywords','Actors', 'Directors', 'Stream', 'Buy', 'Rent', 'Production Companies']
YEAR = '2024'
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
tab1, tab2, tab3, tab4, tab5, tab6, tab7, tab8 = st.tabs(["🔰Saving ids", "➡️CSV", "🍍Combine CSV", "🪻To Pinecone",  "Vector🎍", "Retrieval➡️", "Q&A➡️", "Evaluation🏅"])
with tab1:
    if button("Retrieve and Save", key="button1"):
        ids = tmdb.get_id_list(TMDB_API_KEY, YEAR)
        st.write(type(ids))
        with open('./data/TMDB/ids.pickle','wb') as f: pickle.dump(ids, f)

with tab2:
    if not os.path.exists('./data/TMDB/ids.pickle'):st.info('no ids pickle existed.')
    else:
        with open('./data/TMDB/ids.pickle', 'rb') as f:ids = pickle.load(f)

    if button("Write to csv", key="button2"):tmdb.write_ids_csv(ids, YEAR, CSV_HEADER, TMDB_API_KEY)
    st.success('in data/csv')

with tab3:
    if button("Combine CSV", key="button3"):
        with open('./config.json') as f: config = json.load(f)

        beginning_year = config["years"][0]
        ending_year = config["years"][-1]

        dfs = [pd.read_csv(f'data/TMDB/csv/{year}_movie_collection_data.csv')
               for year in range(beginning_year, ending_year + 1)]

        # Combine the dataframes
        combined_df = pd.concat(dfs)

        combined_df.to_csv('./data/TMDB/csv/full_movie_collection_data.csv', index=False)
