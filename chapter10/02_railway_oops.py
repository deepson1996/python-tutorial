
class RailwayForm:
    formType = "RailwayForm"
    def printData(self):
        print(f"name is {self.name} \ntrain is {self.train}")

harrysApplication = RailwayForm()

harrysApplication.name = "Harry"
harrysApplication.train = "Rajdhani Express"

harrysApplication.printData()

