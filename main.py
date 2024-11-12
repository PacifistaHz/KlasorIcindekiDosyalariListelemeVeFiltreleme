from os import listdir
from os.path import isfile, join
import glob

klasor=r"C:/Users/alfa/PycharmProjects/WriteOdd/pythonProject"

pyUzantiliDosyalar=glob.glob(klasor+"/*.py")
print(pyUzantiliDosyalar)

for f in listdir(klasor):
    if isfile(f):
        print(f)

dosyalarTumu=[f for f in listdir(klasor) if isfile(join(klasor, f))]
print(dosyalarTumu)