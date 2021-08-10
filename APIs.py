import json
import requests

envFile = 'env.json'


def initialize_env(env):
    with open(envFile) as f:
        data = json.load(f)
        hostname = data[env]['hostname']
        port = data[env]['port']
        organizations = data[env]['organizations']
        environments = data[env]['environments']
    return (hostname, organizations, environments)


def api_get_kvm_org(env, kvm_name):
    data = initialize_env(env)
    url = 'http://' + data[0] + '/v1/organizations/' + data[1] + '/environments/' + data[2] + '/keyvaluemaps/' + kvm_name
    print(url)
    response = http_req(url)
    return response

def list_of_kvm(env):
    data = initialize_env(env)
    url = 'http://' + data[0] + '/v1/organizations/' + data[1] + '/environments/' + data[2] + '/keyvaluemaps'
    response = http_req(url)
    return response


def http_req(url):
    try:
        r = requests.get(url, auth=('<Email>', '<PWD>'), timeout=(20, 20))
        print(r.raise_for_status())
        response = r.json()
    except requests.exceptions.HTTPError as errh:
        print(r.status_code)
        return "An Http Error occurred:" + repr(errh)
    except requests.exceptions.ConnectionError as errc:
        return "An Error Connecting to the API occurred:" + repr(errc)
    except requests.exceptions.Timeout as errt:
        return "A Timeout Error occurred:" + repr(errt)
    except requests.exceptions.RequestException as err:
        return "An Unknown Error occurred" + repr(err)
    return response
