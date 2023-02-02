from behave import given, when, then
import requests

@when(u'I navigate to helloworld url')
def step_impl(context):
    context.response=requests.get('http://localhost:9001')

@then(u'I get a success response code')
def step_impl(context):
    assert context.response.status_code == 200