from ..app import app
from flask import render_template, request
import pandas as pd
import requests
from io import StringIO

def data_from_gouv():
    url = 'https://www.data.gouv.fr/storage/f/2014-05-06T19-39-42/auto-ecole-resultats.csv'
    response = requests.get(url)
    donnees = pd.read_csv(StringIO(response.text), encoding='ISO-8859-1')
    return donnees

donnees = data_from_gouv()

@app.route("/")
def accueil():
    offset = int(request.args.get('offset', 0))
    limit = 50
    from_value = offset * limit

    subset_data = donnees.iloc[from_value: from_value + limit]

    table_html = subset_data.to_html(classes='table table-striped', index=False)

    return render_template("/home.html", table=table_html, offset=offset)
