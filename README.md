
# 🛒 Product Recommendation System

🚀 **Live Demo**: [Click here to view the deployed app](https://products-recommendation-system-r1sz.onrender.com/)

**Mini Project - B.Tech 3rd Year (2022)**  
Developed using Machine Learning and Flask  
By: Bh. Jaya Krishna Sri
Guide: Ms. D. Dakshayani  

---

## 📌 About the Project

This is a **Product Recommendation System** developed as part of my **B.Tech 3rd year mini project (2022)**.  
The system uses customer purchase history over 2.5 years to recommend:

- 🔝 **Top 10 most popular products**
- 👤 **Customer-specific frequently purchased products**
- 👥 **Personalized product recommendations** based on user similarities
- 🛍️ **Related product suggestions** using item similarity


## 🧠 Tech Stack

- Python 3.10.7  
- Flask (Web framework)  
- Pandas, NumPy, Scikit-learn  
- Jupyter Notebook (Google Colab)  
- Pickle (for model serialization)  
- HTML/CSS  
- VS Code (IDE)

---

## 📂 Dataset

Sales transaction data for the years:
- `Sales Transactions-2017.csv`  
- `Sales Transactions-2018.csv`  
- `Sales Transactions-2019.csv`  

---

## 🧾 Program Files

| File | Description |
|------|-------------|
| `PGM-1 - Data_Cleaning.ipynb` | Cleans and preprocesses raw sales data |
| `PGM-2 - Product_Ranking.ipynb` | Identifies top-selling and most popular products |
| `PGM-3 - Customer-Product-Ranking.ipynb` | Extracts frequently purchased items per customer |
| `PGM-4 - Recommend_Products_to_Customer.ipynb` | Recommends products using customer-to-customer correlation |
| `PGM-5 - Recommend_Similar_Products.ipynb` | Suggests similar products based on item-item correlation |
| `Flask.ipynb` | Integrates all functionalities into a Flask web server |

Generated models:
- `prod_ranking_model.pkl`
- `cust_prod_ranking_model.pkl`
- `cust_correlation_model.pkl`
- `prod_correlation_model.pkl`

---

## 🧩 Features

### 📌 General Capabilities
- Predicts **Top 10 popular products**
- Recommends products based on **individual customer history**
- Suggests **similar products** to the currently viewed product

### 🔍 Popularity-Based Recommendation (Most Frequently Purchased Items)
- Products with high number of orders are considered most frequently purchased.
- To find the most popular items, the system factors in the number of customers as well:
  
  **Weighted No_of_Orders (W)** = `O × (C / M)`  
  - `O` = Number of Orders  
  - `C` = Number of Customers who purchased the product  
  - `M` = Maximum number of customers across all products  

---

## 👤 Customer-Based Recommendation

- Shows **most frequently purchased products** for a specific customer.
- Uses **Spearman correlation** to find similar customers.
- Recommends products based on **customer-to-customer similarity**.

---

## 🧾 Item-Based Recommendation

- Recommends products that are **frequently bought together**.
- Uses **item-item purchase history correlation** to identify and suggest related products.

---
![image](https://github.com/user-attachments/assets/75ecec83-692e-4a31-8ce1-5ff584ba6da9)
![image](https://github.com/user-attachments/assets/1f9d944d-c538-456d-8fdd-76056892569e)
![image](https://github.com/user-attachments/assets/4fe3557a-a58d-4d19-abf5-0712359ebf5c)




## 🔗 References
> 📝 **Reference:** This project was inspired by and built upon ideas presented in the following video:  
> 🔗 [About the Project – YouTube](https://youtu.be/0FCxHEc_e8Q)  
> I have taken reference from this video which provides an understanding of the project, and have made additional changes and enhancements. Full credit goes to the original creator for the concept and initial walkthrough.
- [Project Overview – YouTube](https://youtu.be/0FCxHEc_e8Q)
- [Literature Review - ResearchGate](https://www.researchgate.net/publication/353757917_Product_Recommendation_System_A_Systematic_Literature_Review)
- [Amazon Recommender System Paper](https://www.cs.umd.edu/~samir/498/AmazonRecommendations.pdf)
- [TDS: EDA Techniques](https://towardsdatascience.com/exploratory-data-analysis-8fc1cb20fd15)

---

## 💡 Future Scope

- Integrate login/authentication
- Add real-time update support
- Cloud deployment with Docker or Render
- Hybrid recommendation: collaborative + content-based

---

## 👨‍💻 Developed By

Team-47  
- Bh. Jaya Krishna Sri (19071A12C6)  
- P. Srujana (19071A12G1)  
- Sk. Afreen (19071A12G8)  
- G. Shivani (20075A1215)

---

## 📜 License

This project is intended for academic learning and demonstration only.
