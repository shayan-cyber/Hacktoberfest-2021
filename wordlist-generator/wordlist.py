import itertools
import time
import sys


print("#"*46)
print("{:>30}".format("Wordlist Generator"))
print("{:>40}".format("Original by Suraj Singh in Python2"))
print("{:>42}".format("Rewritten into Python3 by theDreamer911"))
print("#"*46)

print("")
chars = input("[+] Enter all words combination :>> ")
l = int(input("[+] Enter minimum length of words :>> "))
k = l
j = int(input("[+] Enter maximum length of words :>> "))
n = j+1
mtl = len(chars)
p = []
zt = input("[+] Enter the output name :>> ")
for ltp in range(k, n):
    ans = mtl**ltp
    p.append(ans)
tline = sum(p)

print("")
print("#"*46)
print("[+] Numbers of total lines:", tline)
input("[*] Press enter to start generate")
print("#"*46)

print("")
print("Please wait")
time1 = time.asctime()
start = time.time()
print("")

psd = open(zt, 'a')
for i in range(k, n):
    r = i * 100/n
    l = str(r) + ' percent'
    sys.stdout.write('\r%s' % l)
    sys.stdout.flush()
    psd.flush()
    for xs in itertools.product(chars, repeat=i):
        psd.write("".join(xs)+'\n')
psd.flush()
psd.close()
print("")
sys.stdout.write("Done successfully")

print("")
print("")
print("#"*46)
print("{:>30}".format("Process Report"))
print("#"*46)
print("")
print("[+] Process Started:", time1)
end = time.time()
print("[+] Process Completed:", time.asctime())
total_time = end - start
print("[+] Total Time consumed:", total_time)
rate = tline/total_time
print("[+] Rate of words generating per seconds:", round(rate, 2))

print("[*] Ended Successfully")
input("[*] Press enter for exit")
