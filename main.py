import FileReader
import MouseController

# Read script
print('# [ Read File ] Start ...')
script_list = FileReader.read_file('Script.txt', 'utf-8')
print('# [ Read File ] End\n')

# Execute script
print('# [ Execute Script ] Start ...')
for scr in script_list:
    if len(scr) == 1:
        MouseController.FunctionDict[scr[0]]()

    elif len(scr) == 2:
        MouseController.FunctionDict[scr[0]](scr[1])

    else:
        MouseController.FunctionDict[scr[0]](scr[1:])

print('# [ Execute Script ] End.\n')
