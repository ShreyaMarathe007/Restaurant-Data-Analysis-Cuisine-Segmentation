# 🍽️ Restaurant Data Analysis Using Cuisine Segmentation

## 📌 Project Overview
Food delivery and restaurant listing platforms contain large volumes of unstructured cuisine text data that directly influence pricing analysis, customer perception, and cuisine visibility. Due to inconsistent cuisine labeling, regional economic differences, and popularity bias, meaningful insights are often distorted.

This project addresses these challenges through data cleaning, analysis, clustering, and dashboard-driven visualization.

---

## 📝 Problem Statement
The project focuses on solving the following challenges:

- Regional pricing inequality across cuisines  
- Perception gap between traditional and modern cuisines  
- Vote distribution bias by cuisine type  
- Long-tail cuisine visibility issues  
- Lack of identification of cuisine signature combinations  
- Absence of a measurable cuisine diversity metric  

---

## 🎯 Project Objectives
- Structure and clean unorganized cuisine data  
- Analyze pricing, ratings, and vote patterns across cuisines  
- Compare **Gwalior city** restaurants with **India-level** data  
- Identify hidden cuisine clusters and combinations  
- Measure and compare cuisine diversity across regions  
- Present insights through an interactive Power BI dashboard  

---

## 🛠️ Tools & Technologies
- **Python 3.x**
- **Pandas, NumPy** – Data cleaning and analysis  
- **Selenium** – Web data collection  
- **Scikit-learn** – Feature encoding and clustering  
- **Jupyter Notebook** – Analysis environment  
- **Power BI Desktop** – Dashboard creation and visualization  

---

## 📊 Dataset Description
- Public restaurant datasets (Zomato-based)  
- Gwalior city restaurant data  
- India-level restaurant data  
- Cuisine information stored as unstructured text  

---

## 🔄 Project Workflow

### 1️⃣ Data Collection
- Restaurant data collected from datasets and web sources using Selenium  

### 2️⃣ Data Cleaning & Preprocessing
- Handled missing values  
- Standardized cost and rating fields  
- Normalized cuisine text  
- Converted cuisines into list-based format  

### 3️⃣ Feature Engineering
- Created cuisine lists per restaurant  
- Encoded cuisine combinations using `MultiLabelBinarizer`  

### 4️⃣ Exploratory Data Analysis (EDA)
- Pricing variation across cuisines and cities  
- Rating vs cost comparison  
- Vote share vs restaurant share analysis  
- Long-tail cuisine frequency analysis

### 5️⃣ Cuisine Segmentation (Unsupervised Learning)
- Applied **K-Means clustering** to identify cuisine signature patterns  
- Used clusters strictly for analytical segmentation  

### 6️⃣ Dashboard Creation
- Exported cleaned datasets as CSV files  
- Manually imported data into Power BI  
- Built an interactive dashboard with KPIs, slicers, and visual comparisons  

---

## ✅ Problem–Solution Mapping

| Problem | Solution Implemented |
|-------|--------------------|
| Regional pricing inequality | City-wise cuisine cost comparison |
| Traditional vs modern perception gap | Rating vs pricing analysis |
| Vote distribution bias | Vote share vs restaurant share comparison |
| Long-tail cuisine invisibility | Cuisine frequency analysis |
| Missing cuisine signatures | Cuisine clustering using K-Means |
| No cuisine diversity metric | Cuisine Diversity Index comparison |

---

## 📈 Key Insights
- Pricing varies significantly for the same cuisine across regions  
- Traditional cuisines tend to be under-rated despite competitive pricing  
- Popular cuisines attract disproportionately high votes  
- Long-tail cuisines remain underrepresented in listings  
- Distinct cuisine clusters reveal hidden restaurant positioning  
- Gwalior and India show measurable differences in cuisine diversity  

---

## 📊 Power BI Dashboard
The dashboard includes:
- KPIs (Average Cost, Average Rating, Restaurant Count)  
- Cuisine-wise and city-wise comparisons  
- Vote share vs restaurant share visualization  
- Interactive slicers for cuisine and category filtering  

> **Note:** Power BI is used only for visualization. No automated Python integration was implemented.

---

## 🗂️ Project Structure
```text
Restaurant-Data-Analysis-Cuisine-Segmentation
│
├── analysis
│   └── restaurant_analysis.ipynb
├── raw_data
├── cleaned_data
├── scripts
├── dashboard
│   └── Restaurant_Cuisine_Analysis.pbix
├── output
├── problem_statement
│   └── problem_statement.txt
├── requirements.txt
└── README.md
```
## ⚙️ Environment Setup
This project uses a Python virtual environment (`venv`) to manage dependencies and ensure a clean, reproducible setup.
```text
python -m venv venv
venv\Scripts\activate        # On Windows
pip install -r requirements.txt
```

---

## 📦 Requirements

All required Python libraries are listed in the requirements.txt file.
Make sure Python 3.x is installed before running the project.

---

## 🧠 Learning Outcomes

Worked with unstructured cuisine text data

Performed data cleaning and preprocessing using Python

Applied unsupervised learning (K-Means clustering) for cuisine segmentation

Analyzed pricing inequality, popularity bias, and cuisine diversity

Built interactive dashboards for data storytelling using Power BI

---

## 👩‍💻 Author

Shreya Marathe
Aspiring Data Analyst | Python | Power BI | Data Analytics
