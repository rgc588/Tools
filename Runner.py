from selenium import webdriver
import shutil

#shutil.rmtree("C:\\1myGames", ignore_errors=True)

driver = webdriver.Chrome(".\\chromedriver\\lib\\chromedriver\\chromedriver.exe")
driver.get("http://hqswqadb02/ATAutoExecutionNewDB/TaskList.aspx?drillDownLevel=0&release=R375_WS_Combined_Automation_Run5&type=AutomationNotRanDetails&projectID=1152&qScoreID=3308&taskOwner=Chen%20Gong")

elements = driver.find_elements_by_xpath("//table[@id='GridData']/tbody/tr")

print len(elements)

# for element in elements:
#     state = element.find_element_by_xpath("td[4]")
#     if state.text == "NOTSUPPORTED":
#         checkbox = element.find_element_by_xpath("td[1]/input")
#         checkbox.click()
#
# na_btn = driver.find_element_by_xpath("//input[@name='btnNATasks']")
# na_btn.click()

# for element in elements:
#     state = element.find_element_by_xpath("td[4]")
#     error = element.find_element_by_xpath("td[5]")
#     if state.text == "NOTRUN" and error.text == "DriverInstall_WindowsErrorCode":
#         file_path = element.find_element_by_xpath("td[3]/a").get_attribute("href")[5:]
#         print file_path
#         log = ""
#         with open(file_path + "/Debug/dbgout.log", 'r') as f:
#             log = f.read()
#         f.close()
#         if "error: 2108" in log:
#             checkbox = element.find_element_by_xpath("td[1]/input")
#             checkbox.click()

for element in elements:
    state = element.find_element_by_xpath("td[4]")
    error = element.find_element_by_xpath("td[5]")
    #if state.text == "" and error.text == "":
    file_path = element.find_element_by_xpath("td[3]/a").get_attribute("href")[5:]
    print file_path
    log = ""
    with open(file_path + "/Debug/dbgout.log", 'r') as f:
        log = f.read()
    f.close()
    if '''error: 2120''' in log:
        checkbox = element.find_element_by_xpath("td[1]/input")
        checkbox.click()

# attach bug
att_bug_btn = driver.find_element_by_xpath("//input[@name='btnAddBugs']")
att_bug_btn.click()

print driver.title
att_bug_btn = driver.find_element_by_xpath("//input[@name='btnAddBugs']")
print len(driver.window_handles)

driver.switch_to.window(driver.window_handles[1])

bug_id = driver.find_element_by_xpath("//input[@name='txtBugID']")
bug_id.clear()
bug_id.send_keys("1753354")

task_state = driver.find_element_by_xpath("//td[@id='cboTaskState_TextBox']")
task_state.click()
gate = driver.find_element_by_xpath("//div[@id='cboTaskState_DropDownContent']/div[@id='cboTaskState_item_1']")
gate.click()

add = driver.find_element_by_xpath("//a[@id='addButton']")
add.click()

#wait for success
#success = driver.find_element_by_xpath("//span[@lblFeedback]")

print "end"