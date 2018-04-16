"""
*   Module Name: ConfigHandle
*   Module Purpose: Handles the creation and reading of the config file
"""
import os.path


class Config:
    conf = {}
    #prey_ids = []
    config_file = None
    config_name = "admin.cfg"

    def __init__(self):
        #Check if config file has been initialzed & create the file
        if(self.config_file == None):
            self.CreateConfig()
            if(self.config_file.name == self.config_name):
                self.GetConfig()
                self.config_file.close()

    #Create the config file
    def CreateConfig(self):
        print("Creating")
        if (not os.path.exists(self.config_name)):
            self.config_file = open(self.config_name, "w+")
            self.config_file.write("[SQL]\nDatabaseURI;:;mysql+mysqlconnector://root:ThreeCupsOfCoffee123!@@localhost/Uniwards\n[Config]\nDEBUG;:;True\ndo_we_need_logs;:;True")
            self.config_file.flush()
        else:
             self.config_file = open(self.config_name, "r")

    #Read and parse the config file
    def GetConfig(self):
        lines = self.config_file.read().splitlines()
        for line in lines:
            if line.startswith('['):
                continue

            print("Line: " + line)
            split_line = line.split(";:;")
            '''
            if ("," in split_line[0]):
                split_ids = split_line[1].split(",")
                for id in split_ids:
                    self.prey_ids.append(id)
                    print(id)
            else:
            '''
            print(split_line)
            self.conf[split_line[0]] = split_line[1]