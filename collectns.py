
menu={'A':'Add Student','B':'Delete Student',
      'C': 'Add Grade to Student','D': 'Calculate Student Avg',
    'E':'Find Max (Students data with the Maximum average)',
      'F':'Replace Grades', 'G':'Exit'}



#menu printing
for key, value in menu.items():
    print('<{}> key to {}'.format(key, value))

#choices

validchoices=[key for key in menu.keys()]

def uinpchk(uinput, choises):
    if uinput.lower() in choises or uinput.upper() in choises:
        return uinput.upper()
    else:
        return 'Invalid choice'

#data init
students = {}
grades = {}

#data manipulations
#students
def addstudent(sname,sid):
    if sid in students.keys():
        print('Student {} with id {} already presented and will be updated to {}'.format(students[sid],sid,sname))
    students.update({sid:sname})
    return students[sid]

def deletestudent(sid):
    #deleteng sid in students and sid in grades if presented
    if sid in students.keys():
        delstud=students.pop(sid)
        if sid in grades.keys():
            grades.pop(sid)
        return 'Student {} was deleted sucessful.\nCurrent students:{}'.format(delstud, students)
    else:
        return 'Student with %s not found' % sid

#grade appending
def addgrade(sid, grade):

    if sid in grades.keys(): #in case of student already have account appending grade to gradelist
        grades[sid].append(float(grade))

    else: #creating account and appending a grade to it
        grades.update({sid:[]})
        grades[sid].append(float(grade))
    return 'Current grades for {} is {}'.format(students[sid],grades[sid])
#searching for average grade
def avgrades(sid, mode):
    if sid in grades.keys():
        grd=grades[sid]
        sumgr=0
        for g in grd:
            sumgr+=g
        avg=float(sumgr/len(grd))
        if mode == 'single':
            return 'Average grade for student {} is {}'.format(students[sid],avg)
        if mode == 'max':
            return avg
#retrieving max grade from all grades
def maxgrades():
    allavgrades={}
    for st in grades:
        allavgrades.update({st:avgrades(st,'max')})
        #searching for max
    maxval=0
    maxid=0
    for m in allavgrades:
        if allavgrades[m] > maxval:
            maxval=allavgrades[m]
            maxid = m
    resultstud = []
    resultstud.append(maxid)
    #additionally checking for students with the same values
    for m in allavgrades:
        if allavgrades[m] == maxval:
            if m not in resultstud:
                resultstud.append(m)
    return "Student(s) with max ({}) grades: {}".format(maxval, [students[r] for r in resultstud])

#change places
def chgrades (stud1,stud2):
    gradestmp=grades[stud1]
    grades[stud1]=grades[stud2]
    grades[stud2]=gradestmp
    return "Grades of {1} now are the grades of {1}".format(students[stud1],students[stud2])
# execution
run = True
while run == True:
    uinp = input('Please choose action: ')
    filtrinp = uinpchk(uinp,validchoices)
    if filtrinp !='Invalid choice':
        print('You choosed %s ' %menu[filtrinp])
    else:
        print('Invalid choice')

    if filtrinp == 'Invalid choice':
        continue

    elif filtrinp == 'A':
        sid = input('Please enter ID ')
        sname = input('Please enter name ')
        print('User %s appended sucessfuly ' %addstudent(sname,sid))

    elif filtrinp=='B':
        sid = input('Please enter ID ')
        print(deletestudent(sid))

    elif filtrinp=='C':
        sid = input('Please enter ID ')
        if sid in students.keys():
            try:
                grade = int(input('Please enter a new grade entry for appending to student %s ' %students[sid]))
                print(addgrade(sid,grade))
            except ValueError:
                print('Error - grade must be a number')
        else:
            print('Student with id %s not found' % sid)

    elif filtrinp=='D':
        sid = input('Please enter students ID for displaying average grade ')
        if sid in grades.keys():
            print(avgrades(sid, 'single'))
        else:
            print('Grades for student with id %s not available' % sid)

    elif filtrinp=='E':
        if len(grades) > 0:
            print(maxgrades())
        else:
            print('Grades data for students is unavailable')
    elif filtrinp=='F':
        print('Please enter two student ids for changing grades with each other')
        stud1=input('Please enter first students ID')
        if stud1 in grades.keys():
            stud2=input('Please enter second students ID')
            if stud2 in grades.keys():
                print(chgrades(stud1,stud2))
            else:
                print('Student with id %s have no grades' %stud2)
        else:
            print('Student with id %s have no grades' % stud1)

    elif filtrinp=='G':
        print('Bye...')
        run=False
    else: #some other value passed filter but not associated with condition
       print('error')


