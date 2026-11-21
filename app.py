"""Streamlit web interface for Student Performance Analyzer."""
from io import BytesIO
import numpy as np
import pandas as pd
import streamlit as st

SUBJECTS = ["Maths", "Physics", "Chemistry"]
REQUIRED = ["Name", *SUBJECTS]

st.set_page_config(page_title="Student Performance Analyzer", page_icon="📊", layout="wide")

st.title("📊 Student Performance Analyzer")
st.caption("Upload a student marks CSV to calculate results, class statistics and visual summaries.")

with st.sidebar:
    st.header("How to use")
    st.markdown("1. Upload a CSV file.\n2. Check the validation report.\n3. Explore results and charts.\n4. Download the analysed data.")
    st.markdown("**Required columns**")
    st.code("Name, Maths, Physics, Chemistry")
    st.caption("Each subject must contain numeric marks from 0 to 100.")

sample = pd.DataFrame({
    "Name": ["Aman", "Riya", "Karan", "Neha", "Ravi"],
    "Maths": [80, 60, 40, 100, 0],
    "Physics": [70, 65, 35, 100, 0],
    "Chemistry": [90, 70, 50, 100, 0],
})
st.download_button("⬇️ Download sample CSV", sample.to_csv(index=False).encode("utf-8"),
                   file_name="sample_students.csv", mime="text/csv")

uploaded = st.file_uploader("Upload students CSV", type=["csv"])
if uploaded is None:
    st.info("Upload a CSV file or download the sample CSV to get started.")
    st.subheader("Example dataset")
    st.dataframe(sample, use_container_width=True, hide_index=True)
    st.stop()

try:
    raw = pd.read_csv(uploaded)
except (pd.errors.EmptyDataError, pd.errors.ParserError, UnicodeDecodeError):
    st.error("The uploaded file is empty or is not a valid CSV file.")
    st.stop()

missing = [column for column in REQUIRED if column not in raw.columns]
if missing:
    st.error("Missing required column(s): " + ", ".join(missing))
    st.stop()

data = raw[REQUIRED].copy()
data["Name"] = data["Name"].astype("string").str.strip()
for subject in SUBJECTS:
    data[subject] = pd.to_numeric(data[subject], errors="coerce")

valid = data["Name"].notna() & data["Name"].ne("")
for subject in SUBJECTS:
    valid &= data[subject].between(0, 100, inclusive="both")

invalid_rows = data.loc[~valid].copy()
data = data.loc[valid].reset_index(drop=True)

left, right = st.columns(2)
left.metric("Rows received", len(raw))
right.metric("Invalid rows skipped", len(invalid_rows))

if not invalid_rows.empty:
    with st.expander("View invalid rows"):
        st.warning("Rows with blank names, non-numeric marks, or marks outside 0–100 were excluded.")
        st.dataframe(invalid_rows, use_container_width=True, hide_index=True)

if data.empty:
    st.error("No valid student records remain. Correct the CSV and upload it again.")
    st.stop()

data["Total"] = data[SUBJECTS].sum(axis=1)
data["Percentage"] = data["Total"] / len(SUBJECTS)
data["Grade"] = np.select(
    [data["Percentage"] >= 90, data["Percentage"] >= 75,
     data["Percentage"] >= 60, data["Percentage"] >= 40],
    ["A", "B", "C", "D"], default="F"
)

st.divider()
st.subheader("Class overview")
top_percentage = float(data["Percentage"].max())
topper_names = data.loc[data["Percentage"].eq(top_percentage), "Name"].tolist()
m1, m2, m3, m4 = st.columns(4)
m1.metric("Valid students", len(data))
m2.metric("Class average", f"{data['Percentage'].mean():.2f}%")
m3.metric("Highest percentage", f"{top_percentage:.2f}%")
m4.metric("Topper", ", ".join(map(str, topper_names)))

st.subheader("Student results")
st.dataframe(data.style.format({**{s: "{:.0f}" for s in SUBJECTS},
                                "Total": "{:.0f}", "Percentage": "{:.2f}%"}),
             use_container_width=True, hide_index=True)

csv_bytes = data.to_csv(index=False).encode("utf-8")
st.download_button("⬇️ Download analysed results", csv_bytes,
                   file_name="student_analysis_results.csv", mime="text/csv")

st.divider()
st.subheader("Performance analysis")
c1, c2 = st.columns(2)
with c1:
    st.markdown("**Average marks by subject**")
    st.bar_chart(data[SUBJECTS].mean())
with c2:
    st.markdown("**Percentage distribution**")
    histogram = np.histogram(data["Percentage"], bins=[0, 40, 60, 75, 90, 100.0001])
    distribution = pd.DataFrame({"Percentage range": ["0–39.99", "40–59.99", "60–74.99", "75–89.99", "90–100"],
                                 "Students": histogram[0]}).set_index("Percentage range")
    st.bar_chart(distribution)

st.subheader("Class statistics")
stats = pd.DataFrame({
    "Metric": ["Mean percentage", "Median percentage", "Population standard deviation"],
    "Value": [f"{data['Percentage'].mean():.2f}%", f"{data['Percentage'].median():.2f}%",
              f"{data['Percentage'].std(ddof=0):.2f}"]
})
st.dataframe(stats, use_container_width=True, hide_index=True)
st.caption("Grades: A ≥ 90, B ≥ 75, C ≥ 60, D ≥ 40, F < 40. Population standard deviation is used (ddof=0).")
