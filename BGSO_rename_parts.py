# encoding: utf-8
import re
import os
import sys

file_re = re.compile(r"(.*)-(.*)\.pdf")
starts_with_underscore_re = re.compile(r"_(.*)")

def rename_one_folder(source_folder):
	print(f"\n# SOURCE FOLDER: {source_folder}")
	for f in os.listdir(source_folder):
		oldpath = os.path.join(source_folder, f)
		if os.path.isdir(oldpath):
			continue

		if result := re.match(file_re, f):
			newname = f"{result.groups()[1]}-{result.groups()[0]}.pdf"

			oldpath = os.path.join(source_folder, f)
			newpath = os.path.join(source_folder, newname)
			print(newname)
			os.rename(oldpath, newpath)
		elif re.match(starts_with_underscore_re, f):
			print("THIS FILE STARTS WITH AN UNDERSCORE; THE FOLLOWING FILE IS LEFT UNCHANGED: ", f)
		else:
			print("FILE FORMAT NOT RECOGNIZED; THE FOLLOWING FILE HAS HAD AN UNDERSCORE PREPENDED: ", f)
			newname = f"_{f}"

			oldpath = os.path.join(source_folder, f)
			newpath = os.path.join(source_folder, newname)
			print(newname)
			os.rename(oldpath, newpath)

if __name__ == '__main__':
	if len(sys.argv) < 2:
		print("Please provide the name of the folder")
		exit()
	source = sys.argv[1]
	rename_one_folder(source)
