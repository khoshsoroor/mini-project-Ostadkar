Feature: login
I want to login to my github

Scenario: login to github
  Given send my "username" with "mahsa.khoshsoroor@gmail.com"
  And send my "password" with "0014429543mMm"
  And call login api
  Then login should be successful


Scenario: starring a repository
  Given send "owner" as "aloetesting"
  And send "repo" as "aloe"
  Then Call starring repo api
  And check Response if this repository is starred

Scenario: collaborator repository
  Given send "collabo" as "koterpillar"
  Then Call collaborate api
  And Response if user is a collaborator



