import random
import string
import pathlib
import os
class FileIOUtility(object):
    def CreateRandomFile(FileName,FilePath,FileSize,NumberOfFiles=1,FileExtension=".txt"):
        pathlib.Path(FilePath).mkdir(parents=True, exist_ok=True) 
        FileLocationList = list();
        for Counter in range(NumberOfFiles):
            FileLocation = FilePath+"\\"+FileName+"_"+str(Counter)+FileExtension;
            FileLocationList.append(FileLocation);
            with open(FileLocation, 'wb') as fout: 
                Data = os.urandom(FileSize)
                Data = ''.join(random.choice(string.ascii_letters) for _ in range(FileSize))
                fout.write(Data.encode('utf-8'))
                #fout.write(Data)
        return FileLocationList;
            