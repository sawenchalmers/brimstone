"""moves all .ghuser files in this folder to dist/brimstone_[version] as indicated and zips them for delivery"""

import argparse
import os
import shutil

def main(args):
	version = args.version
	if not version:
		return
	target_dir = f"./dist/brimstone_{version}"
	os.mkdir(target_dir)
	for file in os.listdir("."):
		if file.endswith(".ghuser"):
			shutil.move(f"./{file}", f"{target_dir}/{file}")
		elif file == f"brimstone_{version}.gh":
			shutil.copy(f"./{file}", f"{target_dir}/{file}")
	for file in os.listdir("./dist_template"):
		shutil.copy(f"./dist_template/{file}", f"{target_dir}/{file}")
	shutil.make_archive(target_dir, "zip", target_dir)


if __name__ == '__main__':
	arg_parser = argparse.ArgumentParser()
	arg_parser.add_argument("-v", "--version", help="string representing the version")
	main(args = arg_parser.parse_args())
