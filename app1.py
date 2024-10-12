import streamlit as st
import pickle
from PIL import Image
from streamlit_text_rating.st_text_rater import st_text_rater
from streamlit_card import card

def main():
    st.sidebar.markdown('# Main Page')
    st.title(':grey[DIABETES PREDICTION WEB APP]')
    st.info('📌Helps to find chances of developing diabetes!')
    img=Image.open('d.jpg')
    st.image(img,width=550)
    pregnancies=st.text_input('Pregnancies','Type here')
    glucose= st.text_input('Glucose Level', 'Type here')
    blood_pressure = st.text_input('Blood Pressure Level', 'Type here')
    skin_thickness = st.text_input('Skin Thickness Value', 'Type here')
    insulin=st.text_input('Insulin', 'Type here')
    bmi=st.text_input('BMI', 'Type here')
    diabetes_function=st.text_input('Diabetes Pedigree Function', 'Type here')
    age=st.text_input('Age', 'Type here')
    features=[pregnancies,glucose,blood_pressure,skin_thickness,insulin,bmi,diabetes_function,age]
    scaler=pickle.load(open('diabetes_scaler1.sav','rb'))
    model=pickle.load(open('diabetes_model1.sav','rb'))
    pred=st.button("PREDICT",type='primary')
    if pred:
        result=model.predict(scaler.transform([features]))
        if result==0:
            st.write('The person is not diabetic')
        else:
            st.write('The person is diabetic')

    st.info('It is far better to be ahead of a sickness or disease rather than dealing with the treatment of it, so aim to get your health, eating habits, weight, and more in top-notch shape as soon as possible📍')

    hasClicked = card(
        title="Diabetes Facts!",
        text="What you need to know?",
        image="https://www.rappler.com/tachyon/2024/07/diabetes-fast-facts.jpg",
        url="https://www.medstarhealth.org/news-and-publications/news/life-saving-diabetes-facts"
    )
    st.text("🎈")
    for text in ["Is the above information helpful?", "Do you like this model?"]:
        response = st_text_rater(text=text)
main()
