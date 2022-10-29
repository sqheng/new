#!/usr/bin/env python
# coding: utf-8

# In[1]:


from flask import Flask


# In[2]:


import joblib


# In[3]:


app = Flask(__name__)
#flask: web development application / framework.
# in every framework you use you need to input the variable
# anything with __xxx__ is a magic number? its like a signature?


# In[4]:


#python theres a decorator function for flask. e.g. app.route?
#For any function you want to run, you need to use a decorator first for the flask to work
#to force it to run first
#A decorator is a design pattern in Python that allows a user to 
#add new functionality to an existing object without modifying its structure. 
# Decorators are usually called before the definition of a function you want to decorate.


# In[5]:


from flask import request, render_template

@app.route("/", methods =["GET","POST"])
def index():
    if request.method =="POST":
        rates = float(request.form.get("rates"))
        print(rates)
        model1 = joblib.load("regression.joblib")
        r1 = model1.predict([[rates]])
        model2 = joblib.load("tree.joblib")
        r2 = model2.predict([[rates]])
        
        return(render_template("index.html",result1=r1,result2=r2))
    else:
        return(render_template("index.html",result1="waiting",result2="waiting"))

        


# In[ ]:


if __name__=="__main__":
    app.run()
    
    #port no. of flask is 5000
#jupiter is 8888


# In[ ]:




