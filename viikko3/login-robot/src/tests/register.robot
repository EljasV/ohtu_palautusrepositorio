*** Settings ***
Resource  resource.robot
Test Setup  Input New Command
*** Keywords ***


*** Test Cases ***
Register With Valid Username And Password
    Input Credentials  kalle  kalle123
    Output Should Contain  New user registered

Register With Already Taken Username And Valid Password
    Input Credentials  kalle  kalle123
    Input New Command
    Input Credentials  kalle  kalle123
    Output Should Contain  You must choose an available username.

Register With Too Short Username And Valid Password
    Input Credentials  ka  kalle123
    Output Should Contain  Username must be at least 3 characters long.


Register With Enough Long But Invalid Username And Valid Password
    Input Credentials  ka11e  kalle123
    Output Should Contain  Username must consist only of lower case letters a-z.

Register With Valid Username And Too Short Password
    Input Credentials  kalle  kal123
    Output Should Contain  Password must be at least 8 characters long.

Register With Valid Username And Long Enough Password Containing Only Letters
    Input Credentials  kalle  aaaaaaaa
    Output Should Contain  Password must contain at least one special character or number.

