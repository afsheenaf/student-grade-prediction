import streamlit as st
import pandas as pd
import joblib

model = joblib.load("student_grade_model.pkl")
feature_names = joblib.load("feature_names.pkl")

st.set_page_config(
    page_title="Student Grade Prediction",
    page_icon="🎓",
    layout="wide"
)

st.title("🎓 Student Grade Prediction System")

st.markdown("""
This application predicts a student's final grade category using a trained
**Logistic Regression** machine learning model.

Please complete the information below before clicking **Predict Grade**.
""")

st.divider()

left, right = st.columns(2)

with left:

    st.subheader("👤 Student Information")

    age = st.slider(
        "Age",
        min_value=15,
        max_value=22,
        value=17
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

    st.divider()

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
        [
            0,
            1,
            2,
            3
        ]
    )

    absences = st.slider(
        "Number of Absences",
        0,
        100,
        5
    )

    G2 = st.slider(
        "Second Period Grade (G2)",
        0,
        20,
        12,
        help="Enter the student's second-period examination score."
    )

with right:

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

    st.divider()

st.subheader("🏠 Lifestyle & Support")
lifestyle_left, lifestyle_right = st.columns(2)

with lifestyle_left:

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
        "Weekday Alcohol Consumption",
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

with lifestyle_right:

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
            ["Yes", "No"],
            horizontal=True
        )

        famsup = st.radio(
            "Receives Family Educational Support",
            ["Yes", "No"],
            horizontal=True
        )

        paid = st.radio(
            "Attends Extra Paid Classes",
            ["Yes", "No"],
            horizontal=True
        )

        activities = st.radio(
            "Participates in Extra Activities",
            ["Yes", "No"],
            horizontal=True
        )

        nursery = st.radio(
            "Attended Nursery School",
            ["Yes", "No"],
            horizontal=True
        )

        higher = st.radio(
            "Plans to Pursue Higher Education",
            ["Yes", "No"],
            horizontal=True
        )

        internet = st.radio(
            "Internet Access at Home",
            ["Yes", "No"],
            horizontal=True
        )

        romantic = st.radio(
            "Currently in a Romantic Relationship",
            ["Yes", "No"],
            horizontal=True
        )

st.divider()

predict = st.button(
    "🎓 Predict Grade",
    use_container_width=True
)



if predict:

    # -----------------------------
    # Convert user-friendly inputs
    # -----------------------------

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



