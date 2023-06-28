import streamlit as st
from PIL import Image
import base64
import pandas as pd
import pickle
from sklearn.ensemble import RandomForestClassifier
import numpy as np
from clf import predict

# st.write("Welcome to lim fong web page!!!")
# st.write("This is the wavelet cyclegan")

#st.set_page_config(page_title="My webpage", page_icon = ":tada", layout='wide')

def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

def add_bg_from_local(image_file):
    with open(image_file, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read())
    st.markdown(
    f"""
    <style>
    .stApp {{
        background-image: url(data:image/{"png"};base64,{encoded_string.decode()});
        background-size: cover
    }}
    </style>
    """,
    unsafe_allow_html=True
    )
local_css("C:/Users/Lim Fong/Documents/streamlit/style/style.css")

st.markdown('<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">', unsafe_allow_html=True)

st.markdown("""
<nav class="navbar fixed-top navbar-expand-lg navbar-dark" style="background-color: #3498DB;">
  <a class="navbar-brand" href=" https://github.com/AsherTeo?tab=repositories" target="_blank">Asher</a>
  <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
    <span class="navbar-toggler-icon"></span>
  </button>
  <div class="collapse navbar-collapse" id="navbarNav">
    <ul class="navbar-nav">
      <li class="nav-item active">
        <a class="nav-link disabled" href="#">Home <span class="sr-only">(current)</span></a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="https://github.com/AsherTeo?tab=repositories" target="_blank">Github</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="https://www.youtube.com/channel/UCfkOiINc9QsSGipE-gDDumQ" target="_blank">Youtube</a>
      </li>
    </ul>
  </div>
</nav>
""", unsafe_allow_html=True)

animation_symbol = "❄"

st.markdown(
    f"""
    <div class="snowflake">{animation_symbol}</div>
    <div class="snowflake">{animation_symbol}</div>
    <div class="snowflake">{animation_symbol}</div>
    <div class="snowflake">{animation_symbol}</div>
    <div class="snowflake">{animation_symbol}</div>
    <div class="snowflake">{animation_symbol}</div>
    <div class="snowflake">{animation_symbol}</div>
    <div class="snowflake">{animation_symbol}</div>
    <div class="snowflake">{animation_symbol}</div>
    """,
    unsafe_allow_html=True,
)


#add_bg_from_local('C:/Users/User/Desktop/streamlit/blueprint.jpg')  

img_1 = Image.open('C:/Users/Lim Fong/Documents/streamlit/cat1.jpg')
img_2 = Image.open('C:/Users/Lim Fong/Documents/streamlit/network1.PNG')

img_1 = img_1.resize((600,300))
img_2 = img_2.resize((600,300))

gif_1 = open("C:/Users/Lim Fong/Documents/streamlit/cat.gif", "rb")
contents = gif_1.read()
data_url = base64.b64encode(contents).decode("utf-8")
gif_1.close()

with st.container():
    st.subheader("Hi, I am Lim Fong :wave:")
    st.title("Welcome to my website!!!")
    st.write("I specialist in computer vision task such as image processing, classification, image translation and many more!!!")
    st.write("[To learn more] https://github.com/AsherTeo?tab=repositories")
    st.markdown(f'<img src="data:image/gif;base64,{data_url}" alt="cat gif">',
                unsafe_allow_html=True,
                )
 
with st.container():
    st.write('--')
    st.header('This is the Resnet 101 architecture')
    image_column, text_column = st.columns((2,1))
    with image_column:
       st.image(img_2)

    st.header('Cat classication')
    st.write('##')
    
       #st.image(img_1)

st.sidebar.header('User Input Features')
file_up = st.sidebar.file_uploader("Upload an image", type="jpg")

if file_up is not None:
    image = Image.open(file_up)
    st.image(image, caption='Uploaded Image.', use_column_width=True)
    st.write("")
    st.write("Just a second...")
    labels = predict(file_up)

    # print out the top 5 prediction labels with scores
    for i in labels:
        st.write("Prediction (index, name)", i[0], ",   Score: ", i[1])

with st.container():
    st.write('---')
    st.header('Contact Me!')
    st.write("##")

# Documention: https://formsubmit.co/ !!! CHANGE EMAIL ADDRESS !!!
    contact_form = """
    <form action="https://formsubmit.co/limfong1994@gmail.com" method="POST">
        <input type="hidden" name="_captcha" value="false">
        <input type="text" name="name" placeholder="Your name" required>
        <input type="email" name="email" placeholder="Your email" required>
        <textarea name="message" placeholder="Your message here" required></textarea>
        <button type="submit">Send</button>
    </form>
    """
    left_column, right_column = st.columns(2)
    with left_column:
        st.markdown(contact_form, unsafe_allow_html=True)
    with right_column:
        st.empty()

# st.sidebar.markdown("""
# [Example CSV input file](https://raw.githubusercontent.com/dataprofessor/data/master/penguins_example.csv)
# """)

# uploaded_file = st.sidebar.file_uploader("Upload your input CSV file", type=["csv"])
# if uploaded_file is not None:
#     input_df = pd.read_csv(uploaded_file)
# else:
#     def user_input_features():
#         island = st.sidebar.selectbox('Island',('Biscoe','Dream','Torgersen'))
#         sex = st.sidebar.selectbox('Sex',('male','female'))
#         bill_length_mm = st.sidebar.slider('Bill length (mm)', 32.1,59.6,43.9)
#         bill_depth_mm = st.sidebar.slider('Bill depth (mm)', 13.1,21.5,17.2)
#         flipper_length_mm = st.sidebar.slider('Flipper length (mm)', 172.0,231.0,201.0)
#         body_mass_g = st.sidebar.slider('Body mass (g)', 2700.0,6300.0,4207.0)
#         data = {'island': island,
#                 'bill_length_mm': bill_length_mm,
#                 'bill_depth_mm': bill_depth_mm,
#                 'flipper_length_mm': flipper_length_mm,
#                 'body_mass_g': body_mass_g,
#                 'sex': sex}
#         features = pd.DataFrame(data, index=[0])
#         return features
#     input_df = user_input_features()

# penguins_raw = pd.read_csv('penguins_cleaned.csv')
# penguins = penguins_raw.drop(columns=['species'])
# df = pd.concat([input_df,penguins],axis=0)

# # Encoding of ordinal features
# # https://www.kaggle.com/pratik1120/penguin-dataset-eda-classification-and-clustering
# encode = ['sex','island']
# for col in encode:
#     dummy = pd.get_dummies(df[col], prefix=col)
#     df = pd.concat([df,dummy], axis=1)
#     del df[col]
# df = df[:1] # Selects only the first row (the user input data)

# # Displays the user input features
# st.subheader('User Input features')

# if uploaded_file is not None:
#     st.write(df)
# else:
#     st.write('Awaiting CSV file to be uploaded. Currently using example input parameters (shown below).')
#     st.write(df)

# # Reads in saved classification model
# load_clf = pickle.load(open('penguins_clf.pkl', 'rb'))

# # Apply model to make predictions
# prediction = load_clf.predict(df)
# prediction_proba = load_clf.predict_proba(df)


# st.subheader('Prediction')
# penguins_species = np.array(['Adelie','Chinstrap','Gentoo'])
# st.write(penguins_species[prediction])

# st.subheader('Prediction Probability')
# st.write(prediction_proba)

    