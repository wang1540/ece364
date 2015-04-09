#! /usr/bin/env python3.4

class Experiment:

    def __init__(self, experimentNo=0, experimentDate="", virusName="", unitCount=0, unitCost=0.00):
        self.experimentNumber = int(experimentNo)
        self.experimentDate = str(experimentDate)
        self.virusName = str(virusName)
        self.unitCount = int(unitCount)
        self.unitCost = float(unitCost)
        self.totalCost = round(self.unitCost * self.unitCount, 2)

    def __str__(self):
        return "{:03d}, {}, ${:06.2f}: {}".format(self.experimentNumber, self.experimentDate, self.totalCost, self.virusName)


class Technician:

    def __init__(self, techName="", techID =""):
        self.techName = techName
        self.techID = techID
        self.experiments = {}

    def addExperiment(self, experiment):
        if not isinstance(experiment, Experiment):
            return None
        self.experiments[experiment.experimentNumber] = experiment

    def __str__(self):
        return "{}, {}: {:02d} Experiments".format(self.techID, self.techName, len(self.experiments))

    def generateTechActivity(self):
        result="{}, {}\n".format(self.techID, self.techName)
        temp = [key for key in self.experiments.keys()]
        temp.sort()

        for key in temp:
            experiment = self.experiments[key]
            result += experiment.__str__() + "\n"
        return result

    def loadExperimentsFromFile(self, fileName):
        with open(fileName, 'r') as f:
            lines = f.readlines()
        for l in lines[2:]:
            no, date, name, unit, cost = l.split()
            temp = Experiment(no, date, name, unit, cost[1:])
            self.addExperiment(temp)


class Laboratory:

    def __init__(self, labName=""):
        self.labName = labName
        self.technicians = {}

    def addTechnician(self, technician):
        if not isinstance(technician, Technician):
            return None
        self.technicians[technician.techName] = technician

    def __str__(self):
        temp = []
        result="{}: {:02d} Technicians\n".format(self.labName, len(self.technicians))
        for key in self.technicians.keys():
            technician = self.technicians[key]
            kkey ="".join(technician.techID.split('-'))
            temp += [(kkey, key)]
        temp.sort()

        for T in temp:
            key = T[1]
            technician = self.technicians[key]
            result = result + technician.__str__() + "\n"
        return result[:-1]

    def generateLabActivity(self):
        result = ""
        temp = [key for key in self.technicians.keys()]
        temp.sort()

        for key in temp:
            technician = self.technicians[key]
            result += technician.generateTechActivity() + "\n"
        return result[:-1]











