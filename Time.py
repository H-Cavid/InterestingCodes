import time
start=time.time()
print(time.time())#komputer texnologiyalarina 1970-de etiibaren 0 saat 0deq,0saniye qoyulub,o vaxtdan sayir.
print(time.asctime())#komputerde olan indiki vaxti sorusursan.
print(time.gmtime())#Qrinvic Mean Time-nen saati sorusursan
now=time.gmtime()
now=time.asctime(now)
stop=time.time()
print(stop-start)
#print(now[3:6])#Tuple-dan istifade ederek istediyimizi ekrana cixaririq