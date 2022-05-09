import enum


@enum.unique
class ServerCommands(enum.Enum):
    CHECK_STATUS = 'CHECK_STATUS'
    GET_RESULT = 'GET_RESULT'
    RUN_SCAN = 'RUN_SCAN'
    GET_FILE = 'GET_FILE'
    CLEAN_OLD_TARGETS = 'CLEAN_OLD_TARGETS'
    CLEAN_OLD_RESULTS = 'CLEAN_OLD_RESULTS'
