import PyPDF2
My_file = PyPDF2.PdfFileReader("2019-algen.pdf")
Pagenumber = My_file.getNumPages()
page_ze = My_file.getPage(0)
content1 = page_ze.extractText()
content2 = content1.replace("Results", "\nResults")
content2 = content2.replace("Centre No:  ", " \n\nCentre No: ")
content2 = content2.replace("Regist", "\nRegist")
content2 = content2.replace("% Passed : ", "\n%Passed : ")
content2 = content2.replace(", Passed : ", "\nPassed : ")
content2 = content2.replace("Sanctioned : ", "\nSanction : ")
content2 = content2.replace("Sat for 2 or more Subjects:", "\nSat for 2 or more Subjects:")
content2 = content2.replace("Passed In 5 Subjects: ", " \n\nPassed In 5 Subjects: ")
content2 = content2.replace("Passed In 4 Subjects: ", " \n\nPassed In 4 Subjects: ")
content2 = content2.replace("Passed In 3 Subjects: ", " \n\nPassed In 3 Subjects: ")
content2 = content2.replace("Passed In 2 Subjects: ", " \n\nPassed In 2 Subjects: ")
content2 = content2.replace("(", "\n")
content2 = content2.replace(")", ". ")
print(content2)
