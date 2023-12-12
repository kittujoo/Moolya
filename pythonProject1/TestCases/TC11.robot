*** Settings ***
Documentation     Simple example using SeleniumLibrary.
Library           SeleniumLibrary

*** Variables ***
${LOGIN URL}      http://www.google.com
#${BROWSER}        Chrome
@{BROWSERS}=        Firefox      Chrome      Edge
# Firefox Chrome Edge

*** Test Cases ***
Valid Login
    Open Browser To Login Page

#    [Teardown]    Close Browser

*** Keywords ***
Open Browser To Login Page
    FOR     ${BROWSER}      IN      @{BROWSERS}
        Open Browser    ${LOGIN URL}    ${BROWSER}
        Title Should Be    Google
        Close Browser
    END
