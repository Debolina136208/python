class batch:
    def __init__(self):
        self.batchId=""
        self.batchCourseName=""
        self.batchFacultyName=""
        self.batchStudents=""

    def setBatchId(self,batchId):
        self.batchId=batchId
    def getBatchId(self):
        return self.batchId

    def setBatchCourseName(self,batchCourseName):
        self.batchCourseName=batchCourseName
    def getBatchCourseName(self):
        return self.batchCourseName

    def setBatchFacultyName(self,batchFacultyName):
        self.batchFacultyName=batchFacultyName
    def getBatchFacultyName(self):
        return self.batchFacultyName

    def setBatchStudents(self,batchStudents):
        self.batchStudents=batchStudents
    def getBatchStudents(self):
        return self.batchStudents
