*** Settings ***
Documentation     Simple example using SeleniumLibrary.
Library           SeleniumLibrary

*** Test Cases ***
Demotest
        Open Browser    http://www.google.com       chrome
        Close Browser
