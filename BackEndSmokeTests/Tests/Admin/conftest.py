from datetime import datetime
import json
import sys
import pytest
from py.xml import html
sys.path.append("C:\\Users\\Roy Braish\\Roy Personal\\Appium-Automation-Python\\BackEndSmokeTests")
from SystemPathBackend import System_Path_Backend

# try:from test_pytest_smoke import Variables
from test_pytest_admin import Variables 
# from test_pytest_smoke import Variables

@pytest.mark.hookwrapper
def pytest_runtest_makereport(item, call):
    try:url=Variables.temp_API_URL
    except:url="https://www.google.com"
    
    pytest_html = item.config.pluginmanager.getplugin('html')
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, 'extra', [])
    if report.when == 'call':
        # always add url to report
        extra.append(pytest_html.extras.url(Variables.temp_API_URL))
        xfail = hasattr(report, 'wasxfail')
        if (report.skipped and xfail) or (report.failed and not xfail):
            # only add additional html on failure
            extra.append(pytest_html.extras.html('<div>Additional HTML</div>'))
        report.extra = extra
        
def pytest_html_report_title(report):
    report.title = "Backend Specific Essential APIs!"
    


@pytest.hookimpl(tryfirst=True)
def pytest_sessionfinish(session, exitstatus):
   
    with open("C:\\Users\\Roy Braish\\Roy Personal\\Appium-Automation-Python\\BackendSmokeTests\\temp_json_file.json") as file:
        # Load its content and make a new dictionary
            JSON=json.load(file)  
   
    try:Environment=Variables.Environment
    except:Environment=JSON["Environment"] 
    try:Email=Variables.Email
    except:Email="No email by default"
      
    session.config._metadata["SmartWealth Environment"] = Environment.upper()    
    session.config._metadata["Email"] = "N/A"
    session.config._metadata["Base URL"] = JSON["SW_UAT_URL"]



def pytest_addoption(parser):
    parser.addoption("--env", action="store", default="internal")


def pytest_generate_tests(metafunc):
    # This is called for every test. Only get/set command line arguments
    # if the argument is specified in the list of test "fixturenames".
    option_value = metafunc.config.option.env
    if 'env' in metafunc.fixturenames and option_value is not None:
        metafunc.parametrize("env", [option_value])




@pytest.mark.optionalhook
def pytest_html_results_table_header(cells):
    cells.insert(1, html.th('Description'))
    cells.insert(4, html.th('URL'))
    del cells[2]
    cells.insert(2, html.th('Testcase'))
    cells.pop()

@pytest.mark.optionalhook
def pytest_html_results_table_row(report, cells):
    cells.insert(1, html.td(report.description))
    cells.insert(4, html.td(report.URL))
    del cells[2]
    cells.insert(2, html.td(report.Testcase))
    cells.pop()

    # for cell in cells:
    #     if cell.attr.class_ == "Test":
    #         if hasattr(report, "docstring"):
    #             cell[0] = report.docstring
    #         break

    
@pytest.mark.hookwrapper
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()
    report.description = str(Variables.temp_status_code)
    report.URL=str(Variables.temp_API_URL)
    # report.Test = str("ffff") 
    report.Testcase = str(Variables.temp_test_case)
    # test_fn = item.obj
    # docstring = getattr(test_fn, '__doc__')
    # if docstring:
    #     report.docstring = docstring





