from pywinauto.application import Application

app=Application("win32").start('Notepad.exe')
dlg=app.UntitledNotepad
dlg_act=dlg.wait('visible')