a = """76101   DATTA, N.   16  6.7 74  78  78  72
76101   SIU, J. 12  7.0 98  96  96  88
76101   TREMERYN, K.    91  6.0 92  86  86  88
76101   GLAVAN, .   11  7.2 94  90  90  90
76101   COMMER, C.  15  6.4 92  92  88  90
76101   ZEBROWSKI, M.   38  5.6 84  84  82  82
76101   COOKE, .    12  5.8 92  86  86  82
76101   SEIBERT, S. 10  5.3 92  92  92  92
76101   SCHULDT, D. 39  7.1 90  92  90  88
76101   SHIMMIN, K. 23  7.7 82  80  76  70
76101   GLOVER, G.  39  7.5 92  88  86  88
76101   CLOUD, D.   24  6.8 90  90  92  88
76101   SLATE, E.   17  7.1 96  96  92  88
76101   LAMBERT, M. 30  6.0 84  82  82  82
76101   DAWSON, J.  20  7.1 86  84  84  76
76101   HANBURY, E. 13  8.5 54  60  74  50
76101   MITCHELL, T.    64  7.1 86  88  84  80
76101   KOEPFINGER, C.  35  6.1 68  72  78  70
76101   VAZQUEZ, E. 39  6.6 76  74  78  72
76101   MENNIES, R. 34  6.4 90  92  88  80
76101   LIMING, S.  25  6.4 90  88  86  86
76101   STEFFEN, H. 94  6.3 96  94  94  92
76101   MARCELLINO, W.  51  6.4 82  78  84  76
76101   WISCOMB, A. 55  7.4 90  90  90  84
76101   HAESELIN, D.    54  6.1 90  88  92  88
76101   HAMILTON, K.    42  6.4 96  92  92  88
76101   WILTON, J.  27  7.2 80  78  76  74
76101   NELSON, M.  61  6.4 90  84  84  84
76101   REINEKE, J. 37  5.7 94  94  88  92
76101   TEAGARDEN, A.   72  7.3 82  84  82  76
76101   WIKE, C.    48  6.6 92  88  92  86
76101   LONGINI, A. 13  5.8 82  88  84  78
76101   KLEIN, A.   17  5.7 84  84  76  74
76101   GENTRY, N.  29  7.2 86  86  86  86
76101   DICKSON-LAPRADE, D. 15  6.0 86  88  80  82
76101   MARKOWICZ, D.   45  6.6 72  74  76  66
76101   WETZEL, D.  16  6.7 88  88  88  84
76101   MANDO, J.   17  7.7 88  82  78  82
76101   PHILLIPS, D.    83  6.8 84  84  80  76
76101   KILPATRICK, R.  12  6.8 96  98  92  84
76101   SQUIRES, J. 12  7.8 86  90  88  86"""

#remove all the formatting
a = a.replace('   ',' ').replace('  ',' ').replace(', ','').replace('.','')
courses =  a.split('\n')
data = []
for i in xrange(len(courses)):
    data.append(courses[i].split(' '))
teachersWithRatings = []
for item in data:
    teachersWithRatings.append([item[-1]]  + [item[1]])
teachersWithRatings.sort()
teachers = [(x[1]) for x in teachersWithRatings]
ratings = [int(x[0]) for x in teachersWithRatings]

def mean(array):
    return sum(array) / len(array) * 1.0

def notAValidTeacher(teacher):
    return not( teacher in teachers)

def run():
    print "here are the interp teachers:"
    for name in sorted(teachers): print name
    teacher = raw_input("Enter your interp teacher's name ").upper()
    while(notAValidTeacher(teacher)):
        teacher = raw_input("Not a teacher from the list above, please pick a correct name: ").upper()
    else:
        teacherIndex = teachers.index(teacher)
        teacherScore = ratings[teacherIndex]
        print "Your Teacher: ", teacher
        print "Their score:  ", teacherScore
        print "%s is ranked %d out of %d teachers"  % (teacher, len(ratings) - ratings.index(teacherScore), len(teachers))

run()


