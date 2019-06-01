import requests
from requests.auth import HTTPBasicAuth

def login_api_call(u, p):
    r = requests.get('https://api.github.com/user', auth=HTTPBasicAuth(
        u, p))
    return r


def stargazers_api_call(owner, repo, u, p):
    starr = requests.get( 'https://api.github.com/user/starred/{owner}/{repo}'.format(owner=owner,repo = repo), auth=HTTPBasicAuth(
        u, p))
    print(starr, starr.url)
    return starr

def collabo_api_call(owner , repo , coll ,u , p):
    collabo = requests.get('https://api.github.com/user/repos/{o}/{r}/collaborators/{coll}'.format(o=owner, r = repo , coll = coll ) , auth=HTTPBasicAuth(
        u, p))
    print(collabo.url)
    return collabo

