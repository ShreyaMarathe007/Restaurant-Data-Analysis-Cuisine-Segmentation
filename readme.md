🍽️ Restaurant Data Analysis Using Cuisine Segmentation

Food delivery and restaurant listing platforms contain large volumes of unstructured cuisine text data that directly influence pricing analysis, customer perception, and cuisine visibility.
Due to inconsistent cuisine labeling, regional economic differences, and popularity bias, meaningful insights are often distorted.

This project addresses the following key challenges:

Regional pricing inequality across cuisines

Perception gap between traditional and modern cuisines

Vote distribution bias by cuisine type

Long-tail cuisine visibility issues

Lack of identification of cuisine signature combinations

Absence of a measurable cuisine diversity metric

🎯 Project Objectives

Structure and clean unorganized cuisine data

Analyze pricing, ratings, and vote patterns across cuisines

Compare Gwalior city restaurants with India-level data

Identify hidden cuisine clusters and combinations

Measure and compare cuisine diversity across regions

Present insights through an interactive Power BI dashboard

🛠️ Tools & Technologies

Python 3.x

Pandas, NumPy – Data cleaning and analysis

Selenium – Web data collection

Scikit-learn – Feature encoding and clustering

Jupyter Notebook – Analysis environment

Power BI Desktop – Data visualization and dashboard creation

📊 Dataset Description

Public restaurant datasets (Zomato-based)

Gwalior city restaurant data

India-level restaurant data

Cuisine information stored as unstructured text

🔄 Project Workflow

Data Collection
Restaurant data collected from datasets and web sources using Selenium.

Data Cleaning & Preprocessing

Handled missing values

Standardized cost and rating fields

Normalized cuisine text

Converted cuisines into list-based format

Feature Engineering

Created cuisine lists per restaurant

Encoded cuisine combinations using MultiLabelBinarizer

Cuisine Segmentation (Unsupervised Learning)

Applied K-Means clustering to identify cuisine signature patterns

Used clusters for analytical segmentation, not prediction

Exploratory Data Analysis (EDA)

Pricing variation across cuisines and cities

Rating vs cost comparison

Vote share vs restaurant share analysis

Long-tail cuisine frequency analysis

Dashboard Creation

Exported cleaned datasets as CSV files

Manually imported data into Power BI

Built an interactive dashboard with KPIs, slicers, and visual comparisons

✅ Problem–Solution Mapping
Problem	Solution Implemented
Regional pricing inequality	City-wise cuisine cost comparison
Traditional vs modern cuisine perception gap	Rating vs pricing analysis
Vote distribution bias	Vote share vs restaurant share comparison
Long-tail cuisine invisibility	Cuisine frequency and dominance analysis
Missing cuisine signatures	Cuisine clustering using K-Means
No diversity measurement	Cuisine Diversity Index comparison

📈 Key Insights

Pricing varies significantly for the same cuisine across regions

Traditional cuisines tend to be under-rated despite competitive pricing

Popular cuisines attract disproportionately high votes

Long-tail cuisines remain underrepresented in listings

Distinct cuisine clusters reveal hidden restaurant positioning

Gwalior and India show measurable differences in cuisine diversity

📊 Power BI Dashboard

The Power BI dashboard includes:

KPIs (Average Cost, Average Rating, Restaurant Count)

Cuisine-wise and city-wise comparisons

Vote share vs restaurant share visualization

Interactive slicers for filtering by cuisine and category

Note: Power BI is used only for visualization. No automated integration with Python scripts was implemented.

🗂️ Project Structure
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

⚙️ Environment Setup

This project uses a Python virtual environment (venv) for dependency management.

python -m venv venv
venv\Scripts\activate   
pip install -r requirements.txt

📦 Requirements

See requirements.txt for the complete list of dependencies.

🧠 Learning Outcomes

Real-world experience with unstructured text data

Practical application of unsupervised learning

Analytical thinking in bias and diversity detection

Dashboard-driven data storytelling

End-to-end data analysis workflow

👩‍💻 Author

Shreya Marathe
Aspiring Data Analyst | Python | Power BI | Data Analytics