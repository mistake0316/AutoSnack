from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import utils
import logging
# default_header_map ={
#   "name"  : "姓名",  
#   "count" : "數量",  
#   "url" : "連結",    
#   "item name" : "商品名稱",
# } 

Change_Current_Count_Format = """
document.getElementById("ButtonContainer").getElementsByTagName("select")[0].value = {:d}
"""
Buy_This_Page = """
var button = document.getElementById("ButtonContainer").getElementsByTagName("button")[0];
return button.click()
"""


def go_process(execel_file_path):
  driverPCHome = webdriver.Chrome()
  

  all_purchase = utils.get_all_urls(execel_file_path)
  for a_purchase in all_purchase:
    url = a_purchase["url"]
    count = a_purchase["count"]
    print(a_purchase)
    # import pdb;pdb.set_trace()
    try:
      if not isinstance(url, str):
        raise Exception(f"url is not string :{a_purchase}")
      
      
      driverPCHome.get(url)
#      import pdb;pdb.set_trace()
      select = driverPCHome.execute_script(Change_Current_Count_Format.format(int(count)))
      buy = driverPCHome.execute_script(Buy_This_Page)
      try:
        alert = driverPCHome.switch_to.alert
        alert.accept()
        logging.info(f"alert happen, while purchase item:\n'\t'{a_purchase}")
      except:
        pass
      time.sleep(5)
    except Exception as e:
      logging.info(e)
  return driverPCHome
  
#  driverPCHome.close()

if __name__ == "__main__":
  logging.basicConfig(filename="log.txt",
                  level=logging.INFO,
                  filemode="w")
  driver = go_process("Sheet.xlsx")
# exit(1)
#  import pdb;pdb.set_trace() 
