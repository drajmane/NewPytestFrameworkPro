import os
import pytest
from selenium import webdriver

@pytest.fixture
def setup(browser):
    if browser=='Chrome':
        driver=webdriver.Chrome()
    elif browser=='Firefox':
        driver=webdriver.Firefox()
    elif browser=='Edge':
        driver=webdriver.Edge()
    return driver



def pytest_addoption(parser):
    parser.addoption("--browser")

@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser")

