# 9. Write a python script to use NOT IN operator to display the data not present in list

ineuron_courses = ['DSA for FAANG preparation with Python', 'Full Stack Data Analytics', 'Full Stack Data Analytics', 'Cyber Security Masters', 'Full Stack Web Development using Python']

courses_not_present = ['Big Data Masters', 'YouTube Mentorship Program By Amresh Bharti Sir', 'C, C++ and DSA in depth with Job Assistance in Hindi', 'Be A DevOps Pro', 'Manual Testing Course']

print('Big Data Masters' not in ineuron_courses) # it'll give True because 'Big Data Masters' is not present in ineuron_courses list.

# Those course which are not present in ineuron_courses gives True as in return value.
for course in courses_not_present:
    print("\n"+course+" is not present in ineuron_courses : "+str(course not in ineuron_courses)+"\n")
    
# Those course which are present in ineuron_courses gives False as in return value.  
for course in ineuron_courses:
     print("\n"+course+" is not present in ineuron_courses : "+str(course not in ineuron_courses)+"\n")
    
    

 


    