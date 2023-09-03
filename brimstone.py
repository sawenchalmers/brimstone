from Grasshopper.Kernel import GH_RuntimeMessageLevel as Message

class globals:
    version = "0.1.4"
    kdb_json_path = "brimstone_data/klimatdatabas_02.04.000.json"

class utils:
    @staticmethod
    def warn(ghenv, message):  
        ghenv.Component.AddRuntimeMessage(Message.Warning, message)

    @staticmethod
    def replace_null(value, default):
        return value if value is not None else default