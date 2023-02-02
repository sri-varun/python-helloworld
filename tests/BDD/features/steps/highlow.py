from behave import given, when, then
import requests
import random
import traceback
import json

@given(u'I pass number less than 100')
def step_impl(context):
    try:
        context.number = random.randint(0,1000)
        print(context.number)
        data1 = {"value":context.number}
        headers = {
        'Content-Type':  'application/json',
        'Accept':  'application/json'
        }
        context.hlresponse = requests.post('http://localhost:9001/highlow',data=json.dumps(data1),headers=headers)
    except:
        traceback.print_exc()

@when(u'I get a success response code')
def step_impl(context):
    assert context.hlresponse.status_code == 200

@then(u'I validate the low scenario')
def step_impl(context):
    valuelow = context.hlresponse.json().get("value")
    if context.number > 100:
        assert valuelow == "1"
    else:
        assert valuelow == "0"

@when(u'I pass invalid data')
def step_impl(context):
    try:
        data1 = {"value":"test:*"}
        headers = {
        'Content-Type':  'application/json',
        'Accept':  'application/json'
        }
        context.hlresponse = requests.post('http://localhost:9001/highlow',data=json.dumps(data1),headers=headers)
    except:
        traceback.print_exc()

@then(u'I validate get invalid response')
def step_impl(context):
    invali_ddata = context.hlresponse.text
    assert invali_ddata == "error"




