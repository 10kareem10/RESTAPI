import flask
from flask import request, jsonify

app = flask.Flask(__name__)
app.config["DEBUG"] = True

countries = [
    {'id':0,
     'name': 'Afghanistan',
     'capital': 'Kabul',
     'population': 27657145,
     'alpha2code': 'AF'},
    {'id':1,
     'name': 'Algeria',
     'capital': 'Algiers',
     'population': 40400000,
     'alpha2code': 'DZ'},
    {'id':2,
     'name': 'Angola',
     'capital': 'Luanda',
     'population': 25868000,
     'alpha2code': 'AO'}
]


@app.route('/', methods=['GET'])
def home():
    return "<h1>Distant countries Archive</h1><p>This site is a prototype API for countries data.</p>"

@app.route('/api/v1/resources/countries/all', methods=['GET'])
def api_all():
    return jsonify(countries)

@app.route('/api/v1/resources/countries', methods=['GET'])
def api_id():
    if 'id' in request.args:
        id = int(request.args['id'])
    else:
        return "Error: No id field provided. Please specify an id."
    results = []

    saveFile = open('id.txt', 'a')
    for country in countries:
        if country['id'] == id:
            results.append(country)
            saveFile.write(str(results))
            saveFile.close()
    return jsonify(results)

@app.route('/api/v1/resources/countries/population', methods=['GET'])
def api_population():
    if 'population' in request.args:
        population = int(request.args['population'])
    else:
        return "Error: No population field provided. Please specify a population ."
    results = []

    saveFile = open('population.txt', 'a')
    for country in countries:
        if country['population'] == population:
            results.append(country)
            saveFile.write(str(results))
            saveFile.close()
    return jsonify(results)

@app.route('/api/v1/resources/countries/capital', methods=['GET'])
def api_capital():
    if 'capital' in request.args:
        capital = str(request.args['capital'])
    else:
        return "Error: No capital field provided. Please specify a capital."
    results = []

    saveFile = open('capitals.txt', 'a')
    for country in countries:
        if country['capital'] == capital:
            results.append(country)
            saveFile.write(str(results))
            saveFile.close()
    return jsonify(results)

@app.route('/api/v1/resources/countries/name', methods=['GET'])
def api_name():

    if 'name' in request.args:
        name = str(request.args['name'])
    else:
        return "Error: No name field provided. Please specify a name."
    results = []

    saveFile = open('names.txt', 'a')
    for country in countries:
        if country['name'] == name:
            results.append(country)
            saveFile.write(str(results))
            saveFile.close()
    return jsonify(results)


app.run()

