import os
from os import listdir
from os.path import isfile, join

import pickle

import matplotlib.pyplot as plt
import matplotlib.image as mpimg

pics_folder = './data/pics/'
labels_file_path = './data/labels.pickle'


key_2_category = {
	'1': 'amazon',
	'2': 'whatsapp',
	'4': 'facebook',
	'8': 'instagram',
	'9': 'linkedin',

	'e': 'email',
	'f': 'food',
	'g': 'workout',
	'h': 'fashion',
	'm': 'music',
	'n': 'news',
	'q': 'quotes',
	's': 'shopping',
	'w': 'weather',

	'o': 'other'
}


def input_2_categorties(input_text):
	'''convert input text into list of categories'''
	cats = [key_2_category[c] for c in input_text]
	return cats


def label_images(pic_paths, labels):
	'''
	pic_paths: 
	labels: dict of lables (pic_name, categories)
	'''

	for i, file in enumerate(pic_paths):

		file_name = file.split('/')[-1]
		if file_name in labels:
			print('skipping ' + file_name + ' (already annotated)')
		else:
			img = mpimg.imread(file)
			plt.imshow(img)
			plt.pause(0.05)

			label = None
			while label is None:
			    try:
			    	input_text = input('input: ')
			    	if input_text == '/':
			    		return labels
			    	label = input_2_categorties(input_text)
			    except:
			    	print('unknow input')
			    	pass
			print(file_name, label)
			labels[file_name] = label    	

	return labels

# load labels
labels = dict()
if os.path.exists(labels_file_path):
	labels = pickle.load(open(labels_file_path, 'rb'))

# load image paths
pic_paths = [join(pics_folder, f) for f in listdir(pics_folder) if isfile(join(pics_folder, f))]	

labels = label_images(pic_paths, labels)

print(labels)

with open(labels_file_path, 'wb') as handle:
	pickle.dump(labels, handle, protocol=pickle.HIGHEST_PROTOCOL)




