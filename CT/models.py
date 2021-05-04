class Command:
    def __init__(self, name, command_id, subgroup=None):
        """This class represents a command that can be sent

        :param name: str, name of the command
        :param command_id:str, numerical identifier
        :param subgroup: str, optional subgroup to group commands together
        """
        self.name = name
        self.command_id = command_id
        self.subgroup = subgroup
        self.parameters = []


class Parameter:
    def __init__(self, name, data_length, datatype=None,
                 units=None, high_limit=None, low_limit=None,
                 conversion=None, bits=False):
        """
        This class represents a parameter that can be sent with a command.

        :param name: str, parameter name
        :param data_length: int, length in bytes
        :param datatype: str, optional data type unsigned int, signed int, float,text
        :param units: str, optional, C, F, V, I, etc
        :param high_limit: str, optional,  top limit on parameters value. Converted based on datatype and conversion
        :param low_limit: str, low limit, optional on parameter value. Converted based on datatype and conversion
        :param conversion: str, optional, conversion defined in conversion.csv. Converts raw values to something meaningful
        :param bits: str, Y or y means in bits, N or n means not in bits. defaults to bytes
        """
        self.name = name
        self.data_length = data_length
        self.datatype = datatype
        self.units = units
        self.high_limit = high_limit
        self.low_limit = low_limit
        self.conversion = conversion
        self.bits = bits



class Telemetry:
    def __init__(self, name, length, subgroup=None,
                 data_type=None, units=None, low_error=None,
                 low_warning=None, high_warning=None, high_error=None,
                 conversion=None, bits=False):
        """
        This class represents a telemetry point from the hardware

        :param name: str, telemetry point name
        :param length: int, length in bytes
        :param subgroup: str, optional way to group telemetry
        :param data_type: str, optional data type unsigned int, signed int, float,text
        :param units: str, optional, C, F, V, I, etc
        :param low_error: str, optional. Converted based on data_type and conversion
        :param low_warning: str, optional. Converted based on data_type and conversion
        :param high_warning: str, optional. Converted based on data_type and conversion
        :param high_error: str, optional. Converted based on data_type and conversion
        :param conversion: str, optional, conversion defined in conversion.csv. Converts raw values to something meaningful
        :param bits: str, Y or y means in bits, N or n means not in bits. defaluts to bytes
        """
        self.name = name
        self.length = length
        self.subgroup = subgroup
        self.data_type = data_type
        self.units = units
        self.low_error = low_error
        self.low_warning = low_warning
        self.high_warning = high_warning
        self.high_error = high_error
        self.conversion = conversion
        self.bits = bits
