
import pandas as pd
import os
from os  import getcwd
import pickle
from flask import Flask, render_template, request
from prod_customer_functions import similar_prods, recommend_prod_cust, most_popular_table, top_sell_table, cust_most_popular_table, cust_top_sell_table

app = Flask(__name__)
directory = getcwd()

prod_ranking_model = pickle.load(open(os.path.join(directory,'pickles/prod_ranking_model.pkl'),'rb'))
cust_prod_ranking_model = pickle.load(open(os.path.join(directory,'pickles/cust_prod_ranking_model.pkl'),'rb'))
cust_correlation_model = pickle.load(open(os.path.join(directory,'pickles/cust_correlation_model.pkl'),'rb'))
prod_correlation_model = pickle.load(open(os.path.join(directory,'pickles/prod_correlation_model.pkl'),'rb'))


def view1(str1,str2):
        prod_price=str2
        prod_name = str(str1).upper()
        if prod_name in prod_ranking_model['Product'].unique():
            prod_price = similar_prods(prod_name)
            return render_template('prod_view.html',prod=prod_name,price=prod_price,exists='y')
   
   
@app.route("/funcall(str1,str2)")
def funcall(str1,str2):
    view1(str1,str2)

@app.route("/products/<prod>")
def products(prod):
    print(prod)
    return view1(prod)
   
@app.route("/")
def home():
    most_popular_table()
    top_sell_table() 
    return render_template('home.html')


@app.route("/login")
def login():
    most_popular_table()
    cust_name = str(request.args.get('name')).upper()
    if cust_name in cust_prod_ranking_model['Party'].unique():
        cust_most_popular_table(cust_name)
        cust_top_sell_table(cust_name)
        recommend_prod_cust(cust_name)
        return render_template('cust_home.html',name=cust_name,new='n')
    else:
        return render_template('cust_home.html',name=cust_name,new='y')

    
@app.route("/view")
def view():
    prod_name = str(request.args.get('prod')).upper()
    
    if prod_name in prod_ranking_model['Product'].unique():
        prod_price = similar_prods(prod_name)
        return render_template('prod_view.html',prod=prod_name,price=prod_price,exists='y')
    else:
        return render_template('prod_view.html',prod=prod_name,exists='n')


def view1(prod_name): 
    if prod_name in prod_ranking_model['Product'].unique():
        prod_price = similar_prods(prod_name)
        return render_template('prod_view.html',prod=prod_name,price=prod_price,exists='y')
    else:
        return render_template('prod_view.html',prod=prod_name,exists='n')


if __name__ == "__main__":
    app.run(debug=True)


