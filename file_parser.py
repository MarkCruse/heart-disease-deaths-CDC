file_prefix = "data-raw/heart_disease2 ("
file_suffix = ").txt"
for file_num in range(42):
    if (file_num == 2) or (file_num == 17):  # skip duplicate sets that were double downloaded
        continue
    file_name = file_prefix + str(file_num) + file_suffix
    fileObj = open(file_name,'r')
    if file_num == 0:
        fileOutObj = open("data/heart_disease_all.csv","w")
        header = 'County,State,County Code,Year,Year Code,Gender,Gender Code,Ten-Year Age Groups,Ten-Year Age Groups Code,Cause of death,Cause of death Code,Deaths,Population,Crude Rate\n'
        fileOutObj.write(header)
    cntr = 0
    for line in fileObj:
        outStr = ""
        if line[1:5] != 'Note':
            if line[1:4] == '---':
                break
            line = line.replace('"', '').strip()    # remove all the quotes
            line = line.replace(' County, ', ',').strip() # remove County
            # lines below remove the odd places where a comma appears in the cause of death field
            line = line.replace(', valve', ' - valve').strip()
            line = line.replace(', un', ' - un').strip()
            line = line.replace(', so', ' - so').strip()
            line = line.replace(', ', ',').strip()  # replace all comma space with comma
            line = line.replace('\t', ',').strip()  # replace all tabs with comma
            # AK,DC,LA,MD,WV,VA are states that have some or no 'County' designation
            outStr =line+'\n'
            fileOutObj.write(outStr)
            cntr += 1
    print(cntr, 'records parsed in dataset: ' + file_name)
fileOutObj.close()
fileObj.close()
