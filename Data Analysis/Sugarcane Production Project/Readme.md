# 📊 Sugarcane Production Data Analysis

## 📌 Overview
This project analyzes **global sugarcane production data** to uncover trends, top producers, and key insights.  
The dataset contains information about sugarcane production in different countries, including acreage (hectares) and production (tons).  

The project focuses on:
- Cleaning and preprocessing the dataset  
- Exploring production patterns across countries  
- Handling missing values and data inconsistencies  
- Preparing the dataset for meaningful visualizations and insights  

---

## 🗂️ Dataset
- **File Used**: `List of Countries by Sugarcane Production.csv`  
- **Attributes**:  
  - `Country` – Name of the country  
  - `Acreage(Hectare)` – Area under sugarcane cultivation  
  - `Production(Tons)` – Total sugarcane production  

---

## ⚙️ Steps Performed
### 1. Data Loading
- Read the dataset using **pandas**  

### 2. Data Cleaning
- Removed unwanted columns (e.g., `Unnamed: 0`)  
- Fixed numeric formatting in `Production(Tons)`  
- Renamed inconsistent column names  
- Handled missing values using `dropna()`  

### 3. Exploratory Data Analysis (EDA)
- Checked dataset shape and structure  
- Analyzed missing values and unique values  
- Summarized production across countries  

### 4. Visualization (recommended)
- Bar plots of top sugarcane producers  
- Distribution of acreage vs. production  
- Trend comparisons between top countries  

---

## 🛠️ Tech Stack
- **Language**: Python 
- **Libraries**: Pandas, NumPy, Matplotlib, Seaborn  
- **Environment**: Jupyter Notebook  

---

## 📢 Results & Insights

- **Dataset cleaned and prepared for analysis**
- **Identified top sugarcane-producing countries**
- **Structured foundation for visualization and predictive modeling**
