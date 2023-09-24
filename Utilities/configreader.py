from configparser import ConfigParser

def readconfig(section,key):
    config=ConfigParser()
    config.read("..//ConfigFile//Conf.ini")
    return config.get(section,key)

