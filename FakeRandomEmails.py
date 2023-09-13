import random
import string
import csv

def getcount():
    while True:
        try:
            rownums = int(input("How many fake email addresses?: "))
            return rownums
        except ValueError:
            print("Please enter an integer value")

def makeEmail():
    extensions = ['com', 'net', 'org', 'gov']
    domains = ['gmail', 'yahoo', 'comcast', 'verizon', 'charter', 'hotmail', 'outlook', 'frontier']

    winext = random.choice(extensions)
    windom = random.choice(domains)

    acclen = random.randint(1, 20)

    winacc = ''.join(random.choice(string.ascii_lowercase + string.digits) for _ in range(acclen))

    finale = f"{winacc}@{windom}.{winext}"
    return finale

howmany = getcount()

emailarray = []

print("Creating email addresses...")
print("Progress: ")

for _ in range(howmany):
    emailarray.append(makeEmail())
    print(f"Progress: {len(emailarray)}/{howmany}", end='\r')

print("\nCreation completed.")

filename = input("Name your file: ")

print("Progress: ")

with open(filename, 'w', newline='') as emailfile:
    aa = csv.writer(emailfile)
    for emailaddr in emailarray:
        aa.writerow([emailaddr])
        print(f"Progress: {len(emailarray)}/{howmany}", end='\r')

print(f"File '{filename}' created.")
