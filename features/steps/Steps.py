from features import call
from aloe import step, world, before

@before.all
def clear(*args):
    world.cred = dict()
########login scenario#######################
@step(r'send my "(username|password)" with "(.*)"')
def get_username_from_feature_file(self, key, value):
    world.cred.update({key: value})

@step(r'call login api')
def call_login_api_with_credentials(self):
    res = call.login_api_call(world.cred['username'], world.cred['password'])
    world.cred.update({'result': res.status_code})

@step(r'login should be successful')
def check_status_code(self):
    assert world.cred['result'] == 200

################check starring repository scenario################
@step(r'send "(owner|repo)" as "(.*)"')
def get_repo_info( self, key , value):
    world.cred.update({key: value})

@step(r'call starring repo api')
def call_api(self):
    res = call.stargazers_api_call(world.cred['owner'],world.cred['repo'],world.cred['username'], world.cred['password'])
    world.cred.update({'result' : res.status_code})


@step(r'check Response if this repository is starred')
def check_response_star(self):
    assert world.cred['result'] == 204




#########check collaborator scenario
@step(r'send "(collabo)" as "(.*)"')
def get_info(self, key , value):
    world.cred.update({key: value})


@step(r'call collaborate api')
def call_collab_api(self):
    res = call.collabo_api_call(world.cred['owner'],world.cred['repo'],world.cred['collabo'], world.cred['username'], world.cred['password'] )
    world.cred.update({'result': res.status_code})

@step(r'Response if user is a collaborator')
def check_response_coll(self):
    assert world.cred['result'] == 204
