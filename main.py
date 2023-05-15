from bs4 import BeautifulSoup

with open('home.html', 'r') as html_file: #defines the filename we are opening and then parsing over, and the 'r' defines the READ method of parsing.
    content = html_file.read() #the function that actually reads the file

    soup = BeautifulSoup(content, 'lxml') #calls an instance of the Beautiful Soup Library, usues the content variable to get the filename of the file to be used, and lxml is the parser method for the file. 
    
    # courses_html_tags = soup.find_all('h5') #uses the find_all method on the file being read, and passes in the h5 argument as the target of the search.
    # for course in courses_html_tags:
    #     print(course.text) #this function parses over all h5 elements in the html file, and prints only the text rather than the entire lines of html.
    
    course_cards = soup.find_all('div', class_='card') #must add an underscore to class_ because class is a built-in method of Python.
    for course in course_cards:
        course_name = course.h5.text #grabs the text from the h5 tag as each course is iterated over, in order.
        course_price = course.a.text.split()[-1] #grabs the text from the a tags, and splits it on the white space between words. then grabs the last element in the text, which is the actual number(s).
        
        print(f'{course_name} costs {course_price}')
    
       
    