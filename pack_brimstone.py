"""moves all .ghuser files in this folder to dist/brimstone_[version] as indicated and zips them for delivery"""

import argparse
import os
import shutil

def main(args):
	version = args.version
	if not version:
		return
	target_dir = f"./dist/brimstone_{version}"
	try:
		os.mkdir(target_dir)
		for file in os.listdir("."):
			if file.endswith(".ghuser"):
				shutil.move(f"./{file}", f"{target_dir}/{file}")
			elif file == f"brimstone_{version}.gh" or file == "brimstone.py":
				shutil.copy(f"./{file}", f"{target_dir}/{file}")

		for item in os.listdir("./dist_template"):
			print(item)
			if os.path.isfile(item):
				file = item
				shutil.copy(f"./dist_template/{file}", f"{target_dir}/{file}")
			else:
				folder = item
				os.mkdir(f"{target_dir}/{folder}")
				for file in os.listdir(f"./dist_template/{folder}"):
					shutil.copy(f"./dist_template/{folder}/{file}", f"{target_dir}/{folder}/{file}")
		shutil.make_archive(target_dir, "zip", target_dir)
	except:
		# it failed, remove the broken directory
		shutil.rmtree(target_dir)
		zip_file = f"{target_dir}.zip"
		if os.path.isfile(zip_file):
			os.remove(zip_file)
		raise


if __name__ == '__main__':
	arg_parser = argparse.ArgumentParser()
	arg_parser.add_argument("-v", "--version", help="string representing the version")
	main(args = arg_parser.parse_args())
