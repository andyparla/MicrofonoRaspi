from jproperties import Properties

class LeerPropertyClass():

    @staticmethod
    def getPropertyValue(property_name: str):
        configs = Properties()
        with open('../resources/config.properties', 'rb') as read_prop:
            configs.load(read_prop)
        return configs.get(property_name).data
