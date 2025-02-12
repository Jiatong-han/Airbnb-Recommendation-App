import streamlit as st
import tensorflow
import pandas as pd
import numpy as np
import datetime
import plotly.express as px
from PIL import Image
from plotly.subplots import make_subplots
from plotly.offline import init_notebook_mode, iplot
import plotly.graph_objects as go
import plotly.graph_objs as go
import matplotlib.pyplot as plt
from ast import literal_eval


# Settings
st.set_option('deprecation.showPyplotGlobalUse', False)

st.set_page_config(
     page_title="Airbnb User Recommendation System",
     page_icon="A",
     layout="wide",
     initial_sidebar_state="expanded",
)

# Title and introductions
st.title("Airbnb User Recommendation Service 🏡 (Demo)")
st.markdown("Seek your perfect fit here ❤️")

st.sidebar.title("Airbnb User Recommendation Service 🏡")

st.sidebar.subheader("Registered on Airbnb already?")
id = st.sidebar.text_input('Key in your id',key='id',max_chars=10)
if st.sidebar.button('Here we go!'):
     image = Image.open('./sample.png')
     st.image(image, use_column_width=True)

dest = st.selectbox('Where do you want to go?',['Raffles Place, Marina, Cecil','Tanjong Pagar, Chinatown','Tiong Bahru, Alexandra, Queenstown','Mount Faber, Telok Blangah, Harbourfront','Buona Vista, Pasir Panjang, Clementi','Clarke Quay, City Hall','Bugis, Beach Road, Golden Mile','Little India, Farrer Park'],key='dest')
col1,col2 = st.beta_columns(2)
with col1: 
     date_from = st.date_input('From when are you booking?',min_value=datetime.date.today(),key='when1')
with col2:
     date_to = st.date_input('To when are you booking?',min_value=date_from,key='when2')
price = st.slider('What price range do you prefer?',10, 500, value=(50,250),step=10, key='price')
room_type = st.multiselect('What room type do you want?',('Single room','double room','triple room','quad room','queen room','king room'))
sort = st.radio('Sort the result by:',('Ratings','Number of reviews','Number of history bookings'))
host = st.checkbox('Superhost only',key='super')
if st.button('Find me the rooms!!!',key='fireaway'):
     col1,col2 = st.beta_columns(2)
     with col1:
          image = Image.open('./listing.png')
          st.image(image, use_column_width=True)
     with col2:
          df = pd.DataFrame(np.random.randn(4, 2) / [50, 50] + [1.35, 103.82],columns=['lat', 'lon'])
          st.map(df)


with st.sidebar.beta_expander("See explanation"):
     st.markdown('The listing is only for reference. And the filtering criteria are not taken into account for now.') 

# # Read in necessary data
# listings = pd.read_csv('datasets/all_listing.csv')
# customers = pd.read_csv('datasets/customer_record.csv')

# # Aux func
# # def showhighest(styler):
# #      return (styler.highl(**{'text-align': 'right'})
# #                   .format({'conversion': '{:.1%}'}))

# # Recommendation for past customers.
# @st.cache(allow_output_mutation=True, max_entries=10, ttl=3600)
# st.sidebar.subheader("Registered on Airbnb already?")
# customer_id = st.sidebar.text_input('Key in your id',key='id',max_chars=10)
# if st.sidebar.button('Here we go!'):
#      if int(customer_id) not in customers.reviewer_id.to_list():
#           st.sidebar.text('User profile not found. Please key in your preferred options righthandside')
#           pass
#      else:
#           from tensorflow.contrib import predictor

#           export_dir = 'saved_model/'
#           predict_fn = predictor.from_saved_model(export_dir)

#           customer = customers.query('reviewer_id == @customer_id')
#           book_history = customer.listing_id.apply(literal_eval).agg(set).values[0]
#           listings_fil = listings[[id not in book_history for id in listings.listing_id]]

#           for i in customer.columns[2:]:
#                listings_fil.loc[:,i] = customer[i].values[0]
           
#           list_of_feat = listings_fil.columns.to_list()
#           listings_fil = listings_fil[list_of_feat[:-120] + list_of_feat[-10:] + list_of_feat[-120:-10]]

#           predictions = predict_fn(listings_fil.astype({'listing_id':'string','number_of_reviews_ltm':'float64','calculated_host_listings_count':'float64'}))['preference']
          
#           cleaned_pred = [x[0][0] for x in predictions]
#           result_df = pd.DataFrame(cleaned_pred,columns=['prediction'])
#           result_df = result_df.join(listings_fil[['listing_id','price','latitude','longitude']].reset_index())
          
#           col1,col2 = st.beta_columns(2)
#           sorted_id = result_df.sort_values(['prediction'],ascending=False)[['listing_id','prediction','price','latitude','longitude']].reset_index(drop=True)[:20]
          
#           with col1:
#                st.markdown('Hi long time no see! This is your personal recommendation!')
#                st.dataframe(sorted_id.format({'price': "${:0<3.0f}", 'latitude': '{:+.1f}', 'longitude': '{:+.1f}'}).style.highlight_min(subset=['price'], axis=0, color='blue').set_precision(3).set_table_styles([{'selector': 'tr:hover',
#                                                                                                                                       'props': [('background-color', '#ff0000')]}]))
#           with col2:
#                lat_lon = sorted_id[['latitude','longitude']]
#                st.map(lat_lon)
               
          


          
          
     
     
# dest = st.selectbox('Where do you want to go?',['Raffles Place, Marina, Cecil','Tanjong Pagar, Chinatown','Tiong Bahru, Alexandra, Queenstown','Mount Faber, Telok Blangah, Harbourfront','Buona Vista, Pasir Panjang, Clementi','Clarke Quay, City Hall','Bugis, Beach Road, Golden Mile','Little India, Farrer Park'],key='dest')
# col1,col2 = st.beta_columns(2)
# with col1: 
#      date_from = st.date_input('From when are you booking?',min_value=datetime.date.today(),key='when1')
# with col2:
#      date_to = st.date_input('To when are you booking?',min_value=date_from,key='when2')
# price = st.slider('What price range do you prefer?',10, 500, value=(50,250),step=10, key='price')
# room_type = st.multiselect('What room type do you want?',('Single room','double room','triple room','quad room','queen room','king room'))
# sort = st.radio('Sort the result by:',('Ratings','Number of reviews','Number of history bookings'))
# host = st.checkbox('Superhost only',key='super')
# if st.button('Find me the rooms!!!',key='fireaway'):
#      col1,col2 = st.beta_columns(2)
#      with col1:
#           image = Image.open('./listing.png')
#           st.image(image, use_column_width=True)
#      with col2:
#           df = pd.DataFrame(np.random.randn(1000, 2) / [50, 50] + [1.35, 103.82],columns=['lat', 'lon'])
#           st.map(df)


# with st.sidebar.beta_expander("See explanation"):
#      st.markdown('The listing is only for reference. And the filtering criteria are not taken into account for now.') 
                 





