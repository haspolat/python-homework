from docx import Document
def get_alpha(x):
    return ''.join(i for i in x if (i.isalpha() or i == '(' or i == ')' or i == '/'))


document = Document("参考答案.docx")
paragraphs = document.paragraphs

#得sectionA答案
paragraph = paragraphs[5].text.strip()
section_A = get_alpha(paragraph)
# print(section_A)


# 得sectionB答案
i = 8      
section_B = []
while (i<12):
    paragraph = paragraphs[i].text.strip()
    mid_list = paragraph.split('.')
    test = []
    for x in mid_list:
        test.append(get_alpha(x))
    test.remove('')
    section_B.extend(test)
    i += 1
# print(section_B)


#得task1~2答案
paragraph = paragraphs[17].text.strip()
task = get_alpha(paragraph)
paragraph = paragraphs[20].text.strip()
task += get_alpha(paragraph)
# print(task)


#得task3答案
i = 23      
task3 = []
while (i<25):
    paragraph = paragraphs[i].text.strip()
    mid_list = paragraph.split('3')
    test = []
    for x in mid_list:
        test.append(get_alpha(x))
    test.remove('')
    task3.extend(test)
    i += 1
task3.remove('')
# print(task3)


#得task4答案
paragraph = paragraphs[27].text.strip()
mid_list = paragraph.split('.')
task4 = []
for x in mid_list:
    task4.append(get_alpha(x))
task4.remove('')
task3.extend(task4)
task3_4 = task3


# 得task5
i = 30      
task5 = []
while (i<32):
    paragraph = paragraphs[i].text.strip()
    mid_list = paragraph.split('.')
    test = []
    for x in mid_list:
        test.append(get_alpha(x))
    test.remove('')
    task5.extend(test)
    i += 1
# print(task5)


#最后一题
paragraph = paragraphs[34].text.strip()
last = get_alpha(paragraph)
# print(last)