# Django integration to produce a RESTful interface

* [Adapted from code by Mahdi Ghelichi](https://medium.com/@mahdi04/train-predict-simple-machine-learning-models-with-django-rest-76ce46bf2868)
___

## Status
At the moment this is just a tutorial/demo that I can glom that code onto my own project. Next I should integrate this 
with something more appropriate from the GDELT analysis.

## Files
1. To set up the Django infrastructure if it has never been set up, run `./set_up_django.sh`
2. Then edit the Django code per the Ghelichi article, changing a few names. However, I've done this and placed the 
code in this repo in this same `django_gdelt`.
3. Start the server with `python manage.py renserver`.
4. Access (http://127.0.0.1:8000/train). Paste in this JSON, 
which alas doesn't seem to be pasteable from the article or in his GitHub:
```json5
{
    "model_name": "model_1",
    "n_estimators": 4,
    "criterion": "entropy",
    "min_samples_split": 3
}
```
5. Then likewise access http://127.0.0.1:8000/predict and likewise paste in this JSON.
```json5
[
    {
        "model_name": "model_1",
        "sepal length (cm)": 5.1,
        "sepal width (cm)": 3.5,
        "petal length (cm)": 1.4,
        "petal width (cm)": 0.2
    }
]
```
There seems to be another set of inputs but they're unreadable there; 
even so note that our one prediction dict needs to be sent as a one-item list.  

## Results
Not good on the first try:
```python
AttributeError at /predict/
'str' object has no attribute 'pop'
Request Method:	POST
Request URL:	http://127.0.0.1:8000/predict/
Django Version:	2.1
Exception Type:	AttributeError
Exception Value:	
'str' object has no attribute 'pop'
Exception Location:	/home/philip/code/gdelt-demo/django_gdelt/main_app/views.py in post, line 38
Python Executable:	/home/philip/.virtualenvs/gdelt-demo/bin/python
Python Version:	3.6.6
Python Path:	
['/home/philip/code/gdelt-demo/django_gdelt',
 '/home/philip/.virtualenvs/gdelt-demo/lib/python36.zip',
 '/home/philip/.virtualenvs/gdelt-demo/lib/python3.6',
 '/home/philip/.virtualenvs/gdelt-demo/lib/python3.6/lib-dynload',
 '/usr/lib/python3.6',
 '/home/philip/.virtualenvs/gdelt-demo/lib/python3.6/site-packages']
Server time:	Thu, 28 Mar 2019 19:58:15 +0000
```

Time to troubleshoot!