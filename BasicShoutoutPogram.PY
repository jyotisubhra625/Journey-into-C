'''WAP a pogram to pronounce list of names using win 32 API.
If you are given a list l as follows:
l= [Frank,Harry,Leo]
Your pogram should show
Shoutout to Frank
Shoutout to Harry
Shoutout to Leo
'''

import win32com.client as win

speaker=win.Dispatch("SAPI.SpVoice")
list=["Frank","Harry","Deba Boba","Saggy","Simpu","Bhola"]
for l in list:
    print(f"Shoutout to {l}")
    speaker.Speak("Shoutout to " + l)

