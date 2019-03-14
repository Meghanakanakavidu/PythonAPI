#!/usr/bin/python
import json
import requests

def main():
 r = requests.get("https://ci.libreoffice.org/view/All/api/json")
 data= r.json()
 array = []
 array_lotb = []
#  array_fir= []

 for i in range(0, len(data['jobs'])):

   x =data['jobs'][i]['name']
   array.append(x)


 for item in array:
   if (item.find('lo_tb') != -1):
     y = item
     array_lotb.append(y)

# print(array_lotb)
# param = "lo_tb_master_win_dbg"
 for item1 in array_lotb:
    array_fir= []
#   url = "https://ci.libreoffice.org/job/"+item1+"/lastCompletedBuild/api/json"
    url = "https://ci.libreoffice.org/job/"+item1+"/api/json"
    res= requests.get(url)
    data_lo = res.json()
 #   for i in range(0,2):
#      z=data_lo['builds'][i]['url']
    z=data_lo['builds']
 # array_fir.append(z)]
    z1=len(z)
#    print(z1)
    if ((z1 < 2)):
      continue
    else:
      for i in range(0,3):
          z2=data_lo['builds'][i]['url']
          array_fir.append(z2)
# print(array_fir)
    s = 0
    t = 0
    for item2 in array_fir:
     url = item2+"/api/json"
     res1= requests.get(url)
     data_fir = res1.json()
 #    print(data_fir)

     if data_fir['result'] == "SUCCESS":
#      continue
       s = s+1
       #print("s has been incremented")
#   else:
#      print(item2)

     elif data_fir['result'] == "FAILURE":
       t = t+1
       #print("entered elif")


     else:
       continue

    if (s>t):
#     continue
      print("{} has more successes ".format(item1))

    else:
      print("{} has more failures".format(item1))












main()

