import pandas as pd
import numpy as np

default_header_map ={
  "name"  : "姓名",
  "count" : "數量",
  "url" : "連結",
  "item name" : "商品名稱",
}

def get_all_urls(excel_file_path, header_map=None):
  """\
  return list of dicts, each dict has keys 
  """
  ret = []
  
  if not header_map:
    header_map = default_header_map

  SeperateSheet = pd.ExcelFile(excel_file_path)
  SheetNamesArray = SeperateSheet.sheet_names
  for __name in SheetNamesArray:
    df = SeperateSheet.parse(__name)
    parsed_result = parse_one_dataframe(df, header_map)
    ret += parsed_result 
  return ret

def parse_one_dataframe(
      df,
      header_map=None,
      shift=1,
  ):
  ret = []
  for __name in header_map.values():
    if __name not in df.columns:
        return ret

  if not header_map:
    header_map = default_header_map

  keys, column_names = header_map.keys(), header_map.values()
  for _, a_purchase in df.loc[shift:, column_names].iterrows():
    if a_purchase.isnull().min():
      continue
    ret.append(
      dict(zip(keys, a_purchase))
    ) 

  return ret
if __name__ == "__main__":
  print(*get_all_urls("Sheet.xlsx"), sep="\n")
