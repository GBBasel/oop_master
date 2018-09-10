infoGrades = []
infoGrades.append(5.5)
print infoGrades
infoGrades.append(5)
print infoGrades
infoGrades.append(5.5)
print infoGrades
infoGrades.append(6)
print infoGrades
count = 0
for note in infoGrades:
    count += note
print "Average: " + str(count / len(infoGrades))

#len() gibt die Länge der Liste zurück
#+=: c += a is equivalent to c = c + a (https://www.tutorialspoint.com/python/python_basic_operators.htm)
#str() konvertiert eine Nummer in einen String. 
