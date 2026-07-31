# Import Required Libraries
import streamlit as st
import pandas as pd
import joblib
import base64

def add_background(image_file):

    with open(image_file, "rb") as file:
        encoded = base64.b64encode(file.read()).decode()

    st.markdown(
        f"""
        <style>

        .stApp {{
            background-image: url("data:image/png;base64,{encoded}");
            background-size: cover;
            background-position: center;
        }}

        </style>
        """,
        unsafe_allow_html=True
    )


# Load Trained Machine Learning Model

model = joblib.load("student_grade_model.pkl")
feature_names = joblib.load("feature_names.pkl")
add_background("background.png")

# Configure Streamlit Page

# Application Title and Description

st.set_page_config(
    page_title="Student Grade Prediction",
    page_icon="🎓",
    layout="wide"
)

st.title("🎓 Student Grade Prediction System")

st.markdown("""
This application predicts a student's **final grade category**
using a trained **Logistic Regression** machine learning model.

The prediction is intended to help **teachers and school counsellors**
identify students who may require additional academic support.
""")

st.info("""
### 📋 How to Use

1. Complete all student information.

2. Review the academic, family and lifestyle information.

3. Confirm that all information is correct.

4. Click **Predict Grade** to generate the prediction.
""")

# splitting into tabs
st.divider()

tab1, tab2, tab3, tab4 = st.tabs(
    [
        "👤 Student",
        "📚 Academic",
        "👨‍👩‍👧 Family",
        "🏠 Lifestyle"
    ]
)

# Student Information Section

with tab1:

    st.subheader("👤 Student Information")

    age = st.slider(
        "Age",
        15,
        22,
        17
    )

    sex = st.selectbox(
        "Gender",
        [
            "Female",
            "Male"
        ]
    )

    school = st.selectbox(
        "School",
        [
            "Gabriel Pereira (GP)",
            "Mousinho da Silveira (MS)"
        ]
    )

    address = st.selectbox(
        "Living Area",
        [
            "Urban",
            "Rural"
        ]
    )
# Academic Information Section

with tab2:

        st.subheader("📚 Academic Information")

        traveltime = st.selectbox(
        "Travel Time to School",
        [
            "<15 minutes",
            "15-30 minutes",
            "30-60 minutes",
            ">60 minutes"
        ]
    )


        studytime = st.selectbox(
        "Weekly Study Time",
        [
            "<2 hours",
            "2-5 hours",
            "5-10 hours",
            ">10 hours"
        ]
    )


        failures = st.selectbox(
            "Past Class Failures",
            [0,1,2,3]
        )


        absences = st.slider(
            "Number of Absences",
            min_value=0,
            max_value=32,
            value=5,
            help="Maximum value is based on the training dataset."
        )
        G2 = st.slider(
            "Second Period Grade (G2)",
            0,
            20,
            12
        )
# Family Background Section

with tab3:

        st.subheader("👨‍👩‍👧 Family Background")

        Medu = st.selectbox(
        "Mother's Education",
        [
            "None",
            "Primary School",
            "Lower Secondary",
            "Upper Secondary",
            "Higher Education"
        ]
    )

        Fedu = st.selectbox(
        "Father's Education",
        [
            "None",
            "Primary School",
            "Lower Secondary",
            "Upper Secondary",
            "Higher Education"
        ]
    )

        Mjob = st.selectbox(
            "Mother's Occupation",
            [
                "At Home",
                "Health Care",
                "Services",
                "Teacher",
                "Other"
            ]
        )

        Fjob = st.selectbox(
            "Father's Occupation",
            [
                "At Home",
                "Health Care",
                "Services",
                "Teacher",
                "Other"
            ]
        )

        guardian = st.selectbox(
            "Primary Guardian",
            [
                "Mother",
                "Father",
                "Other"
            ]
        )

        famsize = st.selectbox(
            "Family Size",
            [
                "3 or fewer",
                "More than 3"
            ]
        )

        Pstatus = st.selectbox(
            "Parents Living Together",
            [
                "Yes",
                "No"
            ]
        )

        famrel = st.selectbox(
            "Family Relationship Quality",
            [
                "Very Poor",
                "Poor",
                "Average",
                "Good",
                "Excellent"
            ]
        )
 # Lifestyle & Support Section
       
with tab4:

        st.subheader("🏠 Lifestyle & Support")

        freetime = st.selectbox(
            "Free Time After School",
            [
                "Very Low",
                "Low",
                "Average",
                "High",
                "Very High"
            ]
        )

        goout = st.selectbox(
            "Going Out With Friends",
            [
                "Very Low",
                "Low",
                "Average",
                "High",
                "Very High"
            ]
        )

        health = st.selectbox(
            "Current Health Status",
            [
                "Very Poor",
                "Poor",
                "Average",
                "Good",
                "Excellent"
            ]
        )

        dalc = st.selectbox(
            "Workday Alcohol Consumption",
            [
                "Very Low",
                "Low",
                "Average",
                "High",
                "Very High"
            ]
        )

        walc = st.selectbox(
            "Weekend Alcohol Consumption",
            [
                "Very Low",
                "Low",
                "Average",
                "High",
                "Very High"
            ]
        )

        reason = st.selectbox(
            "Main Reason for Choosing This School",
            [
                "Course",
                "Home",
                "Reputation",
                "Other"
            ]
        )

        schoolsup = st.radio(
            "Receives School Support",
            [
                "Yes",
                "No"
            ],
            horizontal=True
        )

        famsup = st.radio(
            "Receives Family Educational Support",
            [
                "Yes",
                "No"
            ],
            horizontal=True
        )

        paid = st.radio(
            "Attends Extra Paid Classes",
            [
                "Yes",
                "No"
            ],
            horizontal=True
        )

        activities = st.radio(
            "Participates in Extra Activities",
            [
                "Yes",
                "No"
            ],
            horizontal=True
        )

        nursery = st.radio(
            "Attended Nursery School",
            [
                "Yes",
                "No"
            ],
            horizontal=True
        )

        higher = st.radio(
            "Plans to Pursue Higher Education",
            [
                "Yes",
                "No"
            ],
            horizontal=True
        )

        internet = st.radio(
            "Internet Access at Home",
            [
                "Yes",
                "No"
            ],
            horizontal=True
        )

        romantic = st.radio(
            "Currently in a Romantic Relationship",
            [
                "Yes",
                "No"
            ],
            horizontal=True
        )


# Confirm User Inputs


st.divider()

st.subheader("📋 Before Generating the Prediction")

st.info("""
Please ensure that:

- All four sections have been completed.
- The information entered is accurate.
- The student's details have been reviewed before generating the prediction.
""")

confirm = st.checkbox(
    "✅ I confirm that all information entered is complete and accurate."
)

predict = False

if confirm:

    predict = st.button(
        "🎓 Predict Grade",
        use_container_width=True
    )

else:

    st.warning(
        "Please review all sections before generating the prediction."
    )


if predict:

   
    # Convert User-Friendly Inputs into Model Values


    # Gender
    sex = "M" if sex == "Male" else "F"

    # School
    school = "MS" if school == "Mousinho da Silveira (MS)" else "GP"

    # Address
    address = "U" if address == "Urban" else "R"

    # Family size
    famsize = "GT3" if famsize == "More than 3" else "LE3"

    # Parents living together
    Pstatus = "T" if Pstatus == "Yes" else "A"

    education_map = {
        "None": 0,
        "Primary School": 1,
        "Lower Secondary": 2,
        "Upper Secondary": 3,
        "Higher Education": 4
    }

    Medu = education_map[Medu]
    Fedu = education_map[Fedu]
    traveltime_map = {
        "<15 minutes": 1,
        "15-30 minutes": 2,
        "30-60 minutes": 3,
        ">60 minutes": 4
    }

    traveltime = traveltime_map[traveltime]

    studytime_map = {
        "<2 hours": 1,
        "2-5 hours": 2,
        "5-10 hours": 3,
        ">10 hours": 4
    }

    studytime = studytime_map[studytime]

    rating_map = {
        "Very Low": 1,
        "Low": 2,
        "Average": 3,
        "High": 4,
        "Very High": 5
    }

    health_map = {
        "Very Poor": 1,
        "Poor": 2,
        "Average": 3,
        "Good": 4,
        "Excellent": 5
    }

    freetime = rating_map[freetime]
    goout = rating_map[goout]

    dalc = rating_map[dalc]
    walc = rating_map[walc]

    health = health_map[health]

    job_map = {
        "At Home": "at_home",
        "Health Care": "health",
        "Services": "services",
        "Teacher": "teacher",
        "Other": "other"
    }

    Mjob = job_map[Mjob]
    Fjob = job_map[Fjob]


    guardian_map = {
        "Mother": "mother",
        "Father": "father",
        "Other": "other"
    }

    guardian = guardian_map[guardian]

    reason_map = {
        "Course": "course",
        "Home": "home",
        "Reputation": "reputation",
        "Other": "other"
    }

    famrel_map = {
    "Very Poor": 1,
    "Poor": 2,
    "Average": 3,
    "Good": 4,
    "Excellent": 5
    }

    famrel = famrel_map[famrel]

    reason = reason_map[reason]

    schoolsup = "yes" if schoolsup == "Yes" else "no"
    famsup = "yes" if famsup == "Yes" else "no"
    paid = "yes" if paid == "Yes" else "no"
    activities = "yes" if activities == "Yes" else "no"
    nursery = "yes" if nursery == "Yes" else "no"
    higher = "yes" if higher == "Yes" else "no"
    internet = "yes" if internet == "Yes" else "no"
    romantic = "yes" if romantic == "Yes" else "no"

    Total_Alcohol = dalc + walc

     # Create Input DataFrame for Prediction

    input_data = pd.DataFrame({

        "age": [age],
        "Medu": [Medu],
        "Fedu": [Fedu],
        "traveltime": [traveltime],
        "studytime": [studytime],
        "failures": [failures],
        "famrel": [famrel],
        "freetime": [freetime],
        "goout": [goout],
        "health": [health],
        "absences": [absences],
        "G2": [G2],

        "school": [school],
        "sex": [sex],
        "address": [address],
        "famsize": [famsize],
        "Pstatus": [Pstatus],

        "Mjob": [Mjob],
        "Fjob": [Fjob],
        "reason": [reason],
        "guardian": [guardian],

        "schoolsup": [schoolsup],
        "famsup": [famsup],
        "paid": [paid],
        "activities": [activities],
        "nursery": [nursery],
        "higher": [higher],
        "internet": [internet],
        "romantic": [romantic],

        "Total_Alcohol": [Total_Alcohol]

    }) 

    # Apply One-Hot Encoding


    input_data = pd.get_dummies(
        input_data,
        drop_first=True
    )  

    # Align Features with Training Dataset


    input_data = input_data.reindex(
        columns=feature_names,
        fill_value=0
    )
    prediction = model.predict(input_data)

    grade_map = {
        0: "A",
        1: "B",
        2: "C",
        3: "D"
    }
# Generate Grade Prediction

    predicted_grade = grade_map[prediction[0]]



    st.divider()
    # Display Prediction Result

    st.subheader("📊 Student Performance Prediction")

    if predicted_grade == "A":
        st.success(f"🎉 Predicted Grade: {predicted_grade}")

        st.markdown("""
    **Performance Level:** Excellent

    **Summary:**  
    The student is predicted to perform at an excellent academic level based on the information provided.

    **Recommendation:**  
    Continue encouraging the student's current study habits and academic engagement to maintain strong performance.
    """)
    elif predicted_grade == "B":
        st.info(f"👍 Predicted Grade: {predicted_grade}")

        st.markdown("""
    **Performance Level:** Good

    **Summary:**  
    The student is predicted to achieve good academic performance.

    **Recommendation:**  
    Continue monitoring the student's progress and encourage consistent revision to further improve performance.
    """)
    elif predicted_grade == "C":
        st.warning(f"📚 Predicted Grade: {predicted_grade}")

        st.markdown("""
    **Performance Level:** Moderate Risk

    **Summary:**  
    The student may require additional academic support to improve performance.

    **Recommendation:**  
    Provide additional guidance, encourage regular study habits, and monitor academic progress more closely.
    """)
    else:
        st.error(f"⚠️ Predicted Grade: {predicted_grade}")

        st.markdown("""
    **Performance Level:** High Risk

    **Summary:**  
    The student is predicted to be at higher academic risk based on the information provided.

    **Recommendation:**  
    Early intervention, closer teacher supervision, and additional academic support are recommended.
    """)