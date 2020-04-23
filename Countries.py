import flask
import os
import pickle
import mmap

from flask import request, jsonify

app = flask.Flask(__name__)
app.config["DEBUG"] = True


countries = [
    {'id':0,
     'name':'Afghanistan',
     'capital':'Kabul',
     'population':27657145,
     'alpha2code':'AF'},
    {'id':1,
     'name':'Algeria',
     'capital':'Algiers',
     'population':40400000,
     'alpha2code':'DZ'},
    {'id':2,
     'name':'Angola',
     'capital':'Luanda',
     'population':25868000,
     'alpha2code':'AO'}
]
def checkall():
    readme=open("all.txt",'r')
    x=[]
    count=0
    all=readme.read()
    readme.close()
    #print(all)
    return all

#checkall()
def get_size(file_path):
    if os.stat(file_path).st_size == 0:
        return False
    else:
        return True
def countlines(fname):
    count = 0
    with open(fname, 'r') as f:
        for line in f:
            count += 1
    print("Total number of lines is:", count)

def write_all():
    results=[]
    saveFile = open('all.txt', 'w')
    results.append(countries)
    saveFile.write(str(results))
    saveFile.write("\n")
    saveFile.close()

def writeid(results=[]):
    saveFile = open('id.txt', 'a')
    saveFile.write(str(results))
    saveFile.write("\n")
    saveFile.close()

def checkid(id):
    stringToMatch = ': '+str(id)
    matchedLine = ''

    # get line
    with open('id.txt', 'r') as file:
        for line in file:
            if stringToMatch in line:
                matchedLine = line
                print(matchedLine)
                return matchedLine
                break

def writepop(results=[]):
    saveFile = open('population.txt', 'a')
    saveFile.write(str(results))
    saveFile.write("\n")
    saveFile.close()

def checkpop(population):
    stringToMatch = ': '+str(population)
    matchedLine = ''

    # get line
    with open('population.txt', 'r') as file:
        for line in file:
            if stringToMatch in line:
                matchedLine = line
                print(matchedLine)
                return matchedLine
                break

def writecap(results=[]):
    saveFile = open('capitals.txt', 'a')
    saveFile.write(str(results))
    saveFile.write("\n")
    saveFile.close()

def checkcap(capital):
    stringToMatch = capital
    matchedLine = ''

    # get line
    with open('capitals.txt', 'r') as file:
        for line in file:
            if stringToMatch in line:
                matchedLine = line
                print(matchedLine)
                return matchedLine
                break

def writename(results=[]):
    saveFile = open('names.txt', 'a')
    saveFile.write(str(results))
    saveFile.write("\n")
    saveFile.close()

def checkname(name):
    stringToMatch = name
    matchedLine = ''

    # get line
    with open('names.txt', 'r') as file:
        for line in file:
            if stringToMatch in line:
                matchedLine = line
                print(matchedLine)
                return matchedLine
                break

#checkid(id)


@app.route('/', methods=['GET'])
def home():
    return "<h1>Distant countries Archive</h1><p>This site is a prototype API for countries data.</p>"

@app.route('/api/v1/resources/countries/all', methods=['GET'])
def api_all():

    if get_size("all.txt")== False:
         write_all()
         return jsonify(countries)
    else:
         print("returned from cache")
         print(checkall())
         return checkall()


@app.route('/api/v1/resources/countries', methods=['GET'])
def api_id():
    if 'id' in request.args:
        id = int(request.args['id'])
    else:
        return "Error: No id field provided. Please specify an id."
    results = []

    if checkid(id) is None:
      for country in countries:
        if country['id'] == id:
            results.append(country)
            writeid(results)
            return jsonify(results)
    else :
         print("returned from cache")
         return checkid(id)

@app.route('/api/v1/resources/countries/population', methods=['GET'])
def api_population():
    if 'population' in request.args:
        population = int(request.args['population'])
    else:
        return "Error: No population field provided. Please specify a population ."
    results = []

    if checkpop(population) is None:
        for country in countries:
            if country['population'] == population:
                results.append(country)
                writepop(results)
                return jsonify(results)
    else:
        print("returned from cache")
        return checkpop(population)

@app.route('/api/v1/resources/countries/capital', methods=['GET'])
def api_capital():
    if 'capital' in request.args:
        capital = str(request.args['capital'])
    else:
        return "Error: No capital field provided. Please specify a capital."
    results = []

    if checkcap(capital) is None:
        for country in countries:
            if country['capital'] == capital:
                results.append(country)
                writecap(results)
                return jsonify(results)
    else:
        print("returned from cache")
        return checkcap(capital)

@app.route('/api/v1/resources/countries/name', methods=['GET'])
def api_name():
    x=True

    if 'name' in request.args:
        name = str(request.args['name'])
        print(request.args)

    else:
        return "Error: No name field provided. Please specify a name."
    results = []

    if checkname(name) is None:
        for country in countries:
            if country['name'] == name:
                results.append(country)
                writename(results)
                return jsonify(results)
    else:
        print("returned from cache")
        return checkname(name)


app.run()

