from studentSchedular import studentSchedular

class Admin:
    def showMenu(self):
        self.StudentSchedular=studentSchedular()
        while (True):
            print("Choose from the menu below")
            print("1. Add Student")
            print("2. Show Students")
            print("3. Add Course")
            print("4. Add Faculty")
            print("5. Add Batch")

        x=input("Enter your choice")

        if (x == 1):
            while (True):
                rollNo = input("enter roll no")
                if (self.studentScheduler.validate(rollNo)):
                    continue
                else:
                    break
            name = input("enter name")
            noCourses = input("Enter the number of courses you want to attend")
            courses = []
            for num in range(0, noCourses):
                course = input("Enter the course name")
                courses.append(course)
            self.studentScheduler.addStudent(rollNo, name, courses)

        elif (x == 2):
            self.studentScheduler.showAllStudents()

        elif (x == 3):
            courseName = input("Enter the name of the course")
            self.studentScheduler.addCourse(courseName)

        elif (x == 4):
            facultyName = input("Enter the name of the faculty")
            facultyId = input("Enter the Id of the faculty")
            noCourses = input("Enter the number of courses of the faculty")
            print
            "Enter the names of the courses"
            facultyCourses = []
            for num in range(0, noCourses):
                facultyCourse = input()
                facultyCourses.append(facultyCourse)
            self.studentScheduler.addFaculty(facultyId, facultyName, facultyCourses)

        elif (x == 5):
            batchId = input("enter the batch Id")
            batchCourseName = input("enter the batch Course Name")
            batchFacultyName = input("enter the batch Faculty Name")
            self.studentScheduler.showAllStudents()
            numStudents = input("Enter the number of students you want to add from the above list")
            batchStudents = {}
            for num in range(0, numStudents):
                rollNo = input("Enter the roll number")
                batchStudents.update({rollNo: self.studentScheduler.getStudentByRollNo(rollNo)})
            self.studentScheduler.addBatch(batchId, batchCourseName, batchFacultyName, batchStudents)

        elif (x == 6):
            rollNo = input("Enter the rollNo")
            self.studentScheduler.getStudentByRollNo(rollNo)

        elif (x == 7):
            batchId = input("Enter the batch Id")
            self.studentScheduler.getBatchDetailsByBatchId(batchId)

        elif (x == 8):
            rollNo = input("Enter the rollNo")
            self.studentScheduler.getBatchDetailsByRollNo(rollNo)

        elif (x == 9):
            exit(0)


admin=Admin()
admin.showMenu()

