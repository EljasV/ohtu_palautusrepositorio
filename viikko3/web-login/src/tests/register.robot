*** Settings ***
Resource  resource.robot
Suite Setup  Open And Configure Browser
Suite Teardown  Close Browser
Test Setup  Start Register Test Environment

*** Keywords ***
Start Register Test Environment
     Reset Application
     Go To Register Page

Set Username
    [Arguments]  ${username}
    Input Text  username  ${username}

Set Password
    [Arguments]  ${password}
    Input Text  password  ${password}

Set Password Confirmation
    [Arguments]  ${password_confirmation}
    Input Text  password_confirmation  ${password_confirmation}

Registration Should Fail With Message
    [Arguments]  ${message}
    Register Page Should Be Open
    Page Should Contain  ${message}

Submit Credentials
    Click Button  Register

*** Test Cases ***

Register With Valid Username And Password
    Set Username  kalle
    Set Password  kalle123
    Set Password Confirmation  kalle123
    Submit Credentials
    Title Should Be  Welcome to Ohtu Application!

Register With Too Short Username And Valid Password
    Set Username  ka
    Set Password  kalle123
    Set Password Confirmation  kalle123
    Submit Credentials
    Registration Should Fail With Message  Username must be at least 3 characters long.


Register With Valid Username And Invalid Password
    Set Username  kalle
    Set Password  kalle
    Set Password Confirmation  kalle
    Submit Credentials
    Registration Should Fail With Message  Password must be at least 8 characters long.

Register With Nonmatching Password And Password Confirmation
    Set Username  kalle
    Set Password  kalle123
    Set Password Confirmation  kalle234
    Submit Credentials
    Registration Should Fail With Message  Password and password confirmation must be same.

Login After Successful Registration
    Set Username  kalle
    Set Password  kalle123
    Set Password Confirmation  kalle123
    Submit Credentials
    Go To Login Page
    Set Username  kalle
    Set Password  kalle123
    Click Button  Login
    Main Page Should Be Open

Login After Failed Registration
    Set Username  kalle
    Set Password  kalle123
    Set Password Confirmation  kalle124
    Submit Credentials
    Go To Login Page
    Set Username  kalle
    Set Password  kalle123
    Click Button  Login
    Login Page Should Be Open
    Page Should Contain  Invalid username or password




