# _Challenge 1_ 
-
Introduction
---
---
This ARM Template is used to create a 3-tier architecture on Microsoft Azure. We are creating 3 VM's
1) Front End Layer
2) Back End Layer
3) Database Layer

This ARM Template will create multiple resources (i.e. V.M., NSG, NIC, Public IP, Availability Set, etc.) to set up whole infrastructure 
for a 3-tier application.

We created multiple NSG in this template so that only required ports should be open. For Example, we don't need to RDP in front end layer, so we will block RDP port, and we need to open internet and https port for the same we will create the policy in ARM template to open port 443 for front end layer.







# _Challenge 2_ 
-
Introduction
---
---
This function is to get the metadata from the aws portal for each individual ec2 instance. 

By this we can fetch the metadata in two ways:
1) We will fetch whole metadata in json object format. 
To fetch the whole metadata we need to run
   
    ``python get_metadata.py -o all``


2) We will fetch single metadata just by entering the key. Suppose we want to get the "ami-id" data from the instance. To get this 
we need to run 
   
    `python get_metadata.py -o key -k ami-id`





# _Challenge 3_ 
-
Introduction
---
---
This function is to get value from the nested object. In this function we will pass the two arguments:
1) Object
2) Key

We have the nested object in which we have given a key and for that key we have to find the value from that nested object.

To run this we need to run 

`python main.py -o "{'x':{'y':{'z':'a'}}}" -k "x/y/z"`

By running this command we will get output as shown below:

`2021-03-26 01:55:30 INFO     ===> data : {'x': {'y': {'z': 'a'}}} 
2021-03-26 01:55:30 INFO     ===> key_input_list : ['x', 'y', 'z']
2021-03-26 01:55:30 INFO     ===> output : a`


We also created some unit test cases for the same that you can find in `unitTest.py` file. It 
consists of multiple unit test cases scenario for challenge 3.  
