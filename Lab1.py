'''
  Carlos Cabada
  CS 2302 - Fall 2018
  Lab Assignment No.1 : Lab1.py
  Date: September 18, 2018
  Instructor: Diego Aguirre
  Purpose: Given a text file containing user, salt values and hashed passwords, generate the equivalent password to each user.

'''

import hashlib


def main():
    minChars = int(3)
    maxChars = int(7)
    user, salts, hash = read_file()
    length = file_len()
    generate_password(user, minChars, maxChars, salts, hash, length)

#Reads text file, Extracts Usernames, Salt Values, and hashes.
def read_file():
    filename = "password_file.txt"
    readfile = open(filename, "r")
    user = []
    salts = []
    hash = []
    with open(filename, mode="r", encoding="utf-8") as file:
        for line in readfile:
            user.append(line.rstrip().split(",")[0])
            salts.append(line.rstrip().split(",")[1])
            hash.append(line.rstrip().split(",")[2])
            #print(user, salts, passwords)
            readfile.close
        return user, salts, hash
#Reads file and counts the lines of the file.
def file_len():
    with open("password_file.txt") as f:
        for i, l in enumerate(f):
            pass
        return i + 1


#Hashes strings using sha256.
def hash_with_sha256(str):
    hash_object = hashlib.sha256(str.encode('utf-8'))
    hex_dig = hash_object.hexdigest()
    return hex_dig

#Adds password to possible passwords list.
def generate_password(username, minChars, maxChars, salts, hash, length):
    passwords = []

    if minChars < maxChars:
        password = gen_possible_password(username, minChars, salts, hash, length)
        passwords.append(password)
        return passwords + generate_password(username, minChars + 1, maxChars, salts, hash, length)
    return -1
#Calls the compare_hashes method to compared the passwords that were passed as parameters.
def gen_possible_password(username, minChars, salts, hash, length):
    password_found = ""
    for j in range(len(hash)):
        for i in range((len(hash)) ** 2):
            i = str(i).format(i).zfill(minChars)
            password_found = compare_hashes(username[j],salts[j],i, hash[j], length)
    return password_found

#Compares the hashes, and determines the passwords of each user.
def compare_hashes(username, salts, password, hash, length):
    newStr = password + salts
    newHash = hash_with_sha256(newStr)
    count = 0
    if newHash == hash:
        count +=1
        print("Username: " + username)
        print("Hash: " + hash)
        print("Hashed value: " + newHash)
        print("Password found: " + password)

        return password
    if count == length:
        print("Done!")
    return -1


main()
