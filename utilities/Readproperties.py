import configparser

config=configparser.RawConfigParser()
config.read(".\\Configuration\\Configu.ini")


class Readconfig:
    @staticmethod
    def readappli_url():
        url=config.get('common info','base_url')
        return url

    @staticmethod
    def readusername():
        uname=config.read('common info','username')
        return uname

    @staticmethod
    def readpassword():
        pas=config.read('common info','password')
        return pas



