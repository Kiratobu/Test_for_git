from time import time
from functools import wraps

def test_time(func):
    @wraps(func)
    
    def wrapper(*args,**kwargs):
        start = time()
        act = func(*args,*kwargs)
        end = time()-start
        print(end)
        return act
    return wrapper

candidates = [
 {"name": "Vasya",  
 "scores": {"math": 58, "russian_language": 62, "computer_science": 48}, 
 "extra_scores":0},
 {"name": "Fedya",  
 "scores": {"math": 33, "russian_language": 85, "computer_science": 42},  
 "extra_scores":2},
 {"name": "Petya",  
 "scores": {"math": 92, "russian_language": 33, "computer_science": 36},  
 "extra_scores":1},
 {"name": "Bron",  
 "scores": {"math": 85, "russian_language": 79, "computer_science": 90},  
 "extra_scores":3},
 {"name": "Chelo",  
 "scores": {"math": 92, "russian_language": 80, "computer_science": 88},  
 "extra_scores":1},
 {"name": "Roni",  
 "scores": {"math": 80, "russian_language": 95, "computer_science": 79},  
 "extra_scores":3},
]

import operator

def find_top_20(candidates):
    '''Возвращает топ-20 студентов по итоговым баллам, включая дополнительные баллы и профильные предметы'''
    top_students = []
    for candidate in candidates:
        candidate['total_score'] =  candidate['scores']['math'] + \
                                    candidate['scores']['russian_language']+\
                                    candidate['scores']['computer_science']+\
                                    candidate['extra_scores']
        candidate['profile_total_score'] = candidate['scores']['math']+\
                                           candidate['scores']['computer_science']
    sorted_students_list = sorted(candidates, key=operator.itemgetter('total_score','profile_total_score'))
    for student in sorted_students_list:
        top_students.append(student['name'])
    return top_students[-1:-21:-1]

print(find_top_20(candidates))



names = ["Vasya","Alice","Petya","Jenny","Fedya","Viola","Mark","Chris","Margo"]
birthday_years = [1962,1995,2000,None,None,None,None,1998,2001]
genders = ["Male","Female","Male","Female","Male",None,None,None,None]


def get_inductees (names, birthday_years, genders):
    '''Функция сортирует студентов на военнообязанных и студентов по которым
       невозможно точно установить попадают они в список или нет'''
    passed_students = []
    unknown_students = []
    for index_genders, gender in enumerate(genders):
        if  gender=='Male' and birthday_years[index_genders] != None \
            and 1991 <=birthday_years[index_genders]<=2003:
            passed_students.append(names[index_genders])
        elif gender==None and birthday_years[index_genders]== None or \
             gender=='Male' and birthday_years[index_genders]==None or \
             gender==None and birthday_years[index_genders] != None and \
             1991 <=birthday_years[index_genders]<=2003:
             unknown_students.append(names[index_genders])

    return( f'Студенты годные для службы{passed_students}', 
            f'Студенты с неполной информацией{unknown_students}')
        





def get_inductees_1(names, birthday_years, genders):
    students = []
    passed_students = []
    unknown_students = []
    arguments = ['name', 'birthday_year', 'gender']
    zipped_info = list(zip(names,birthday_years,genders))
    for info in zipped_info:
        students.append(dict(zip(arguments,info)))
    for data in students:
        if  data['birthday_year']==None and data['gender'] == None or \
            data['birthday_year']==None and data['gender'] == 'Male' or \
            data['birthday_year']!=None and 1991<=data['birthday_year']<=2003 and data['gender'] ==None:
            unknown_students.append(data['name'])
        elif data['birthday_year']!=None and 1991<=data['birthday_year']<=2003 and data['gender'] =='Male':
            passed_students.append(data['name'])
            
    return( f'Студенты годные для службы{passed_students}', 
            f'Студенты с неполной информацией{unknown_students}')

# get_inductees_1(names,birthday_years,genders)
print(get_inductees(names,birthday_years,genders))

 

know_english = ["Vasya","Jimmy","Max","Peter","Eric","Zoi","Felix"]
sportsmen = ["Don","Peter","Eric","Jimmy","Mark"]
more_than_20_years = ["Peter","Julie","Jimmy","Mark","Max"]

def find_athlets(know_english, sportsmen, more_than_20_years):
    '''Возвращает список атлетов, подходящих под критерии отбора'''
    athlets = []
    for name in know_english:
        if name in sportsmen and name in more_than_20_years:
            athlets.append(name)
    return athlets

print(find_athlets(know_english, sportsmen, more_than_20_years))




students_avg_scores = {'Max': 4.964, 'Eric': 4.962, 'Peter': 4.923, 'Mark': 4.957, 'Julie': 4.95, 'Jimmy': 4.973, 'Felix': 4.937, 'Vasya': 4.911, 'Don': 4.936, 'Zoi': 4.937}

import operator
import openpyxl

def make_report_about_top3(students_list):
    '''Сохраняет данные топ-3 студентов в Excel файле и возвращает его название'''
    sorted_tuples = sorted(students_list.items(), key=operator.itemgetter(1))
    top_3 = sorted_tuples[-1:-4:-1]

    book = openpyxl.Workbook()
    book.remove(book.active)
    sheet = book.create_sheet('Топ-3', 0)

    for student in top_3:
        sheet.append(student)
    
    sheet.insert_rows(0)
    sheet['A1'].value = 'Имя'
    sheet['B1'].value = 'Средний балл'

    sheet.column_dimensions['B'].width = 15
   
    file_name = 'students.xlsx'
    book.save(file_name)
    return(f'Данные студентов сохранены в файле {file_name}')

make_report_about_top3(students_avg_scores)