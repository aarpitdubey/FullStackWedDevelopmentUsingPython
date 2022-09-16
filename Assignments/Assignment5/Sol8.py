# 8. Write a python script to use IN operator to display the data present in the list

ineuron_courses = ['DSA for FAANG preparation with Python', 'Full Stack Data Analytics', 'Full Stack Data Analytics', 'Cyber Security Masters', 'Full Stack Web Development using Python']
# print(type(ineuron_courses))

print('Full Stack Data Analytics' in ineuron_courses) # True

for course in ineuron_courses:
    print(course in ineuron_courses) 
    # All True if all data of list 'ineuron_courses'  are present in the list. 
    
# I further use the the return value (bool) of IN operator to display the data using a for loop

# for course in ineuron_courses:
#     print(str(ineuron_courses.index(course)+1) + ". "+course)
    


    