import sys, glob, os, codecs

if len(sys.argv) < 3:
	print('I need photos collection directory' \
		' and new photos directory.')
	exit()

photos_collection_dir = sys.argv[1]
new_photos_dir = sys.argv[2]

collection = {}

for filepath in glob.iglob( \
		os.path.join(photos_collection_dir, '**\\*.jpg'), \
		recursive=True):
	filename = os.path.basename(filepath)
	
	if filename in collection:
		collection[filename].append(filepath)
	else:
		collection[filename] = [filepath]
		
found = []
not_found = []

search_path = os.path.join(new_photos_dir, '**\\*.JPG')
print(search_path)
		
for filepath in glob.iglob(search_path, recursive=True):
	filename = os.path.basename(filepath)
	
	if filename in collection:
		found.append((filepath, collection[filename]))
	else:
		f = filepath.encode('utf8', 'replace')
		print(f)
		not_found.append(filepath)
		
print(str(len(found)) + ' files found.')
print(str(len(not_found)) + ' files not found.')