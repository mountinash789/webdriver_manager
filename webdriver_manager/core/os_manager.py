import platform
import sys


class OSType(object):
    LINUX = "linux"
    MAC = "mac"
    WIN = "win"


class OperationSystemManager(object):

    @staticmethod
    def os_name():
        pl = sys.platform
        if pl == "linux" or pl == "linux2":
            return OSType.LINUX
        elif pl == "darwin":
            return OSType.MAC
        elif pl == "win32":
            return OSType.WIN

    @staticmethod
    def os_architecture():
        if platform.machine().endswith("64"):
            return 64
        else:
            return 32

    def os_type(self):
        return f"{self.os_name()}{self.os_architecture()}"

    @staticmethod
    def is_arch(os_sys_type):
        if '_m1' in os_sys_type:
            return True
        return platform.processor() != 'i386'

    @staticmethod
    def is_mac_os(os_sys_type):
        return OSType.MAC in os_sys_type
