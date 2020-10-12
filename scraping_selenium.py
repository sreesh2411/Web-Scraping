from selenium import webdriver


PATH=r"C:\Users\SREESH\Downloads\chromedriver_win32\chromedriver.exe"
browser = webdriver.Chrome(PATH)
browser.get('https://stackoverflow.com/questions?sort=votes')

title = browser.find_element_by_css_selector('h1').text

questions = browser.find_elements_by_css_selector('.question-summary')
for question in questions:
    question_title = question.find_element_by_css_selector('.summary h3 a').text
    question_excerpt =  question.find_element_by_css_selector('.summary .excerpt').text
    question_votes = question.find_element_by_css_selector('.stats .vote .votes .vote-count-post').text

    print("%s\n%s\n%s votes \n-------------- \n" % (question_title, question_excerpt, question_votes))