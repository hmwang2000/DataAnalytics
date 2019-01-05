import pandas as pd

print("-----------get_option(param)------------")
print ("display.max_rows = ", pd.get_option("display.max_rows"))
print ("display.max_columns = ", pd.get_option("display.max_columns"))

print("-----------set_option(param,value)------------")
print ("before set display.max_rows = ", pd.get_option("display.max_rows"))
pd.set_option("display.max_rows",80)
print ("after set display.max_rows = ", pd.get_option("display.max_rows"))

print ("before set display.max_columns = ", pd.get_option("display.max_columns"))
pd.set_option("display.max_columns",32)
print ("after set display.max_columns = ", pd.get_option("display.max_columns"))

print("-----------reset_option(param)------------")
pd.set_option("display.max_rows",32)
print ("after set display.max_rows = ", pd.get_option("display.max_rows"))
pd.reset_option("display.max_rows")
print ("reset display.max_rows = ", pd.get_option("display.max_rows"))

print("-----------describe_option(param)------------")
pd.describe_option("display.max_rows")

print("-----------option_context()------------")
with pd.option_context("display.max_rows",10):
   print(pd.get_option("display.max_rows"))
   print(pd.get_option("display.max_rows"))

