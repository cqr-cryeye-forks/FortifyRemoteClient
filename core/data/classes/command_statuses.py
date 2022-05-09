import enum


class CommandStatus(enum.Enum):
    INFO = 'info'
    DEBUG = 'debug'
    ERROR = 'error'
    FAIL = 'fail'
    SUCCESS = 'success'
    FATAL_ERROR = 'fatal_error'
    ONLINE = 'device_online'
    ALREADY_EXIST = 'Already exist'
    UPDATE_STATUS = 'update_status'
