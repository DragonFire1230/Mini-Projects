import os

print('Easy recovery tool by DragonFire')
print('WARNING: RUN ITS UNDER CMD')
print('WITH ADMINISTRATOR PERMISSIONS')
print()
print('SFC, DISM by Microsoft Corporation')
print()
print('Recovery tools:')
print(' - (1) sfc /scannow')
print(' - (2) DISM /Online /Cleanup-Image /CheckHealth')
print(' - (3) DISM /Online /Cleanup-Image /ScanHealth')
print()
selForRec = input('You select: ')
print('Follow the instructions on the screen')
print()

if selForRec == '1':
	os.system('sfc /scannow')
	input('Done. Press Enter to continue')
if selForRec == '2':
	os.system('DISM /Online /Cleanup-Image /CheckHealth')
	input('Done. Press Enter to continue')
if selForRec == '3':
	os.system('DISM /Online /Cleanup-Image /ScanHealth')
	input('Done. Press Enter to continue')