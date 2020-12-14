#!/usr/bin/env python
# coding: utf-8

# In[1]:


from flask import Flask

# Instantiate the Flask app
app = Flask(__name__)

@app.route('/') # Home directory
def hello():
    return "Hello AI-ML Batch 1 Students. Congratulations to all of you."

# to call use the run()
if __name__== '__main__':
    app.run(debug=True)


# In[ ]:




