import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

st.set_page_config(page_title="Student Performance Analyzer", page_icon="🎓", layout="wide")
st.title("🎓 Student Performance Analyzer")
st.write("Upload student marks or use the sample dataset to view results and class statistics.")

uploaded_file = st.file_uploader("Upload CSV (optional)", type=["csv"])
data = pd.read_csv(uploaded_file) if uploaded_file is not None else pd.read_csv("students.csv")

required = ["Name", "Maths", "Physics", "Chemistry"]
if not all(column in data.columns for column in required):
    st.error("CSV must contain Name, Maths, Physics and Chemistry columns.")
    st.stop()

for subject in ["Maths", "Physics", "Chemistry"]:
    data[subject] = pd.to_numeric(data[subject], errors="coerce")

invalid = data[data[["Maths", "Physics", "Chemistry"]].isna().any(axis=1)]
for _, row in invalid.iterrows():
    st.warning("Invalid marks for " + str(row["Name"]) + ". Row skipped.")

data = data.dropna()
if data.empty:
    st.error("No valid student rows are available.")
    st.stop()

data["Total"] = data["Maths"] + data["Physics"] + data["Chemistry"]
data["Percentage"] = data["Total"] / 3

grades = []
for percentage in data["Percentage"]:
    if percentage >= 90:
        grades.append("A")
    elif percentage >= 75:
        grades.append("B")
    elif percentage >= 60:
        grades.append("C")
    elif percentage >= 40:
        grades.append("D")
    else:
        grades.append("F")
data["Grade"] = grades

st.header("Student Results")
display_data = data.copy()
display_data["Percentage"] = display_data["Percentage"].map(lambda x: format(x, ".2f") + "%")
st.dataframe(display_data, use_container_width=True, hide_index=True)

mean = np.mean(data["Percentage"])
median = np.median(data["Percentage"])
std = np.std(data["Percentage"])
highest = data["Percentage"].max()
toppers = data[data["Percentage"] == highest]["Name"].astype(str).tolist()

st.header("Class Statistics")
c1, c2, c3, c4 = st.columns(4)
c1.metric("Mean %", format(mean, ".2f"))
c2.metric("Median %", format(median, ".2f"))
c3.metric("Std Dev", format(std, ".2f"))
c4.metric("Topper", ", ".join(toppers), format(highest, ".2f") + "%")

averages = [data["Maths"].mean(), data["Physics"].mean(), data["Chemistry"].mean()]
left, right = st.columns(2)
with left:
    st.subheader("Subject-wise Average")
    fig1, ax1 = plt.subplots()
    ax1.bar(["Maths", "Physics", "Chemistry"], averages)
    ax1.set_ylabel("Average Marks")
    st.pyplot(fig1)
with right:
    st.subheader("Percentage Distribution")
    fig2, ax2 = plt.subplots()
    ax2.hist(data["Percentage"])
    ax2.set_xlabel("Percentage")
    ax2.set_ylabel("Number of Students")
    st.pyplot(fig2)