from unittest import TestCase
from unittest import mock
from flask import request

class Test(TestCase):
    def test_api_capital(self):
        line = 'http://127.0.0.1:5000/api/v1/resources/countries/capital?capital=Algiers'
        stringToMatch = '?capital=Algiers'
        if stringToMatch in line:
            matchedline={'id':1,
                         'name':'Algeria',
                         'capital':'Algiers',
                         'population':40400000,
                         'alpha2code':'DZ'}
        actual=matchedline
        expected={'id':1,
                  'name':'Algeria',
                  'capital':'Algiers',
                  'population':40400000,
                  'alpha2code':'DZ'}
        self.assertEqual(expected,actual,msg=True)

    def test_api_capital2(self):
        line = 'http://127.0.0.1:5000/api/v1/resources/countries/capital?capital=Algiers'
        stringToMatch = '?capital=Algiers'
        if stringToMatch in line:
            matchedline = {'id': 1,
                           'name': 'Algeria',
                           'capital': 'Algiers',
                           'population': 40400000,
                           'alpha2code': 'DZ'}
        actual = matchedline
        expected = {'id':2,
     'name':'Angola',
     'capital':'Luanda',
     'population':25868000,
     'alpha2code':'AO'}
        self.assertEqual(expected, actual, msg=False)

    def test_api_name(self):

        line = 'http://127.0.0.1:5000/api/v1/resources/countries/name?name=Algeria'
        stringToMatch = '?name=Algeria'
        if stringToMatch in line:
            matchedline={'id':1,
                         'name':'Algeria',
                         'capital':'Algiers',
                         'population':40400000,
                         'alpha2code':'DZ'}
        actual=matchedline
        expected={'id':1,
                  'name':'Algeria',
                  'capital':'Algiers',
                  'population':40400000,
                  'alpha2code':'DZ'}
        self.assertEqual(expected,actual,msg=True)

    def test_api_population(self):

        line = 'http://127.0.0.1:5000/api/v1/resources/countries/population?population=40400000'
        stringToMatch = '?population=40400000'
        if stringToMatch in line:
            matchedline={'id':1,
                         'name':'Algeria',
                         'capital':'Algiers',
                         'population':40400000,
                         'alpha2code':'DZ'}
        actual=matchedline
        expected={'id':1,
                  'name':'Algeria',
                  'capital':'Algiers',
                  'population':40400000,
                  'alpha2code':'DZ'}
        self.assertEqual(expected,actual,msg=True)

    def test_api_population2(self):

        line = 'http://127.0.0.1:5000/api/v1/resources/countries/population?population=27657145'
        stringToMatch = '?population=27657145'
        if stringToMatch in line:
            matchedline = {'id':0,
     'name':'Afghanistan',
     'capital':'Kabul',
     'population':27657145,
     'alpha2code':'AF'}
        actual = matchedline
        expected = {'id': 1,
                    'name': 'Algeria',
                    'capital': 'Algiers',
                    'population': 40400000,
                    'alpha2code': 'DZ'}
        self.assertEqual(expected, actual, msg=False)

    def test_api_population3(self):

        line = 'http://127.0.0.1:5000/api/v1/resources/countries/population?population=27657145'
        stringToMatch = '?population=27657145'
        if stringToMatch in line:
            matchedline = {'id':0,
     'name':'Afghanistan',
     'capital':'Kabul',
     'population':27657145,
     'alpha2code':'AF'}
        actual = matchedline
        expected = {'id':0,
     'name':'Afghanistan',
     'capital':'Kabul',
     'population':27657145,
     'alpha2code':'AF'}
        self.assertEqual(expected, actual, msg=True)









