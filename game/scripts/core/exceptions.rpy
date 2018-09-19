init python:
    class SummertimeSagaException(Exception):
        def __init__(self, message = "SummertimeSagaException triggered"):
            self.message = message
        
        def __repr__(self):
            return self.message

    class OnSleepException(SummertimeSagaException):
        def __init__(self, message = "OnSleepException triggered"):
            self.message = message
        
        def __repr__(self):
            return self.message

    class FSMException(SummertimeSagaException):
        def __init__(self, message = "FSM Exception Triggered"):
            self.message = message
        
        def __repr__(self):
            return self.message

    class DuplicateStateAddedException(FSMException):
        def __init__(self, message = "Duplicate State added."):
            self.message = message
        
        def __repr__(self):
            return self.message

    class SummertimeSagaInitException(SummertimeSagaException):
        pass

    class OrphanedStateException(FSMException):
        def __init__(self, message = "State Orphaned."):
            self.message = message
        
        def __repr__(self):
            return self.message
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
