#!/usr/bin/env/python2

import os, sys, csv
import re
from collections import OrderedDict

variable = ''

def main():
    basedir = sys.argv[0]
    subdir = sys.argv[1]
    subdir_len = len(subdir)
    dirs = []
    dirs_len = []
    final_dirs_out = []

if not args:
	p.print_help()
	sys.exit()

base_dir = validate_basedir(basedir)
sub_dir = validate_subdir(subdir)
dirs = get_dirs(base_dir, sub_dir)
disk_usage = get_disk_usage(dirs)

#Functions

def options_parser():
	parser = OptionParser(description='%prog --output <Option>')

    parser.add_option('-o', '--output',
        	type='string',
		action='store',
		dest='outdir',
		help='Some text here.')
    parser.add_options('-f', '--file',
		type='string',
		action='store',
		dest='outfile',
		help='Some text here.')
    parser.add_options('-d', '--depth',
		type='string',
		action='store',
		dest='depth',
		help='Some text here.')
	(opts, args) = parser.parse_args()
	return (opts, args)

def validate_basedir(topdir):
	topdir = os.norm.normpath(topdir)

def validate_subdir(subdirs):
	subdirs = os.norm.normpath(subdirs)

def get_directories(top,subdir,depth,subdirlength):
	dirname = []
	dirs_list = []
	unique_dirs_list = []
	subdir_len = len(subdir_length)

	dirlist = os.system('find %s -maxdepth %s -type d | grep %s')$(top, depth, subdir).split("\n")

	for x in dirlist:
		loc = x.find(subdir)
		dirs_list = dirs_list.append([0:loc+subdir])

	for y in dirs_list:
		if y not in final_dirs_out:
			final_dirs_out = final_dirs_out.append(y)

	return final_dirs_out
	
def get_disk_usage(dir):
	dirslength = len(dir)
	print ('Getting disk usage for %s directories' % dirslength)
	diskusage = os.system('du -s %s' % dir)
	return diskusage

def csv_output():
	
	
def screen_result():
	

def command(input):
    cmd = p.open(subprocess()
    (output, err) =
    return output[-1:]

if __name__ == '__main__':
	main()
