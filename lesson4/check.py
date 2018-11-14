from docx import Document
import answer
import os
import write
names = [n for n in os.listdir('./答题卡')]
def check(the_name,row_num):
    document = Document('./答题卡/' + the_name)
    tables = document.tables

    #检查sectionA
    table1 = tables[1]
    row = table1.rows[1].cells
    the_answer = answer.section_A
    i = 0
    score1 = 0
    while (i < len(the_answer)):
        if (row[i].text == the_answer[i]):
            score1 += 1
        i += 1
    i = 0
    # print(score1)


    #检查sectionB
    row = table1.rows[3].cells
    the_answer = answer.section_B
    i = 0
    while(i < len(the_answer)):
        if ('(' in the_answer[i]):
            this_answer = ['improvement','improvements','improving']
            if (answer.get_alpha(row[i].text) in this_answer):
                score1 += 1
        elif ('/' in the_answer[i]):
            this_answer = the_answer[i].split('/')
            if (answer.get_alpha(row[i].text) in this_answer):
                score1 += 1
        else:
            if (answer.get_alpha(row[i].text) == the_answer[i]):
                score1 += 1
        i += 1
    i = 0


    #检查task1~2
    score2 = 0
    table2 = tables[2]
    row = table2.rows[1].cells
    the_answer = answer.task
    i = 0
    while (i < len(the_answer)):
        if (row[i].text == the_answer[i]):
            score2 += 2
        i += 2
    i = 0
    # print(score2)


    #检查task3~4
    row = table2.rows[3].cells
    the_answer = answer.task3_4
    i = 0
    while (i < len(the_answer)):
        if (answer.get_alpha(row[i].text) == the_answer[i]):
            score2 += 2
        i += 1
    # print(score2)


    #检查task5
    score3 = 0
    table3 = tables[3]
    column = table3.columns[1].cells
    the_answer = answer.task5
    i = 0
    while (i < len(the_answer)):
        if (answer.get_alpha(column[i].text) == the_answer[i]):
            score3 += 2
        i += 1
    i = 0


    #检查最后一道
    the_answer = answer.last
    table4 = tables[4]
    column = table4.columns[1].cells
    i = 0
    while (i < len(the_answer)):
        if (answer.get_alpha(column[i].text) == the_answer[i]):
            score3 += 2
        i += 1
    i = 0


    #写入成绩
    table0 = tables[0]
    row = table0.rows[1].cells
    row[1].text = str(score1)
    row[2].text = str(score2)
    row[3].text = str(score3)
    row[5].text = str(score1 + score2 + score3)
    document.save('./答题卡/' + the_name)
    print(the_name)
    write.write(row_num,str(score1 + score2 + score3))
    score1 = 0
    score2 = 0
    score3 = 0


i = 1
while (i < len(names) + 1):
    check(names[i-1],i)
    i += 1