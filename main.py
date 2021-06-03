import requests
import hashlib

def pwned(password):
  passwd_bin = password.encode()

  hash = hashlib.sha1(passwd_bin).hexdigest().upper()
  print("Your password hash is", hash)
  hashHead = hash[:5]
  hashTail = hash[5:]

  r = requests.get("https://api.pwnedpasswords.com/range/"+hash[:5])
  rlist = r.text.split()

  flag = True
  for i in rlist:
    if i[:len(hashTail)] == hashTail:
      return i[len(hashTail)+1:]
  return 0



type = input("Enter 'f' to use file input and 'y' for individual tests:")

#filetype
if type == 'f' or type == 'F':
  input, output = "input", "output"
  fout = open(output, 'a')
  with open(input, "r") as fin:
    while True:
      i = fin.readline()
      if i!='':
        fout.write(i[:-1] + " : " + pwned(i[:-1]) + '\n')
      else:
        break
  fout.close()

#StdIN
else:
  while True:
    passwd = input("Enter Password:")
    print("Your password was pwned "+pwned(passwd)+" times")
    print()
