
#coding:utf-8

class StudentsInfo:
    def __init__(self,sID="1033",sName="LXZ"):
        self.id=sID
        self.name=sName
        self.courseList=[]

    def setID(self,sID):
        self.id=sID
        
    def setName(self,sName):
        self.name=sName

    def selectCourse(self,courseName):
        self.courseList.append(courseName)

    def getPersonalInfo(self):
        return (self.id,self.name)