import os
import math

# set file_path
trg_path = '/data/'
trg_name = 'melodyline.csv'
out_name = 'meloline.csv'
trg = trg_path + trg_name
out = trg_path + out_name


class custum_dict(dict):
	def __init__(self):
		super().__init__()
	def __getitem__(self, key):
		try:
			return super().__getitem__(self, key)
		except:
			for k in self.keys():
				if key in k:
					return super().__getitem__(k)
			raise ValueError(f'Cannot get {key} in keys')

def create_melokey():
	with open(out, encoding='utf_8') as f:
		reader = [s.rstrip().split(',') for s in f.readlines()]
	
	header = reader[0]
	bufbuf = custum_dict()
	for j, x in enumerate(reader[1:]):
		buf = {}
		for i, v in enumerate(x):
			buf.setdefault(header[i], v)
		bufbuf.setdefault((buf['itaric'], buf['english']), buf)
	rtn = bufbuf
	return rtn

def get_melo(key_id, sel_bodyname='freq'):
	key_id = key_id.upper()
	sel_bodyname = sel_bodyname.lower()
	return dict_melo[key_id][sel_bodyname]

dict_melo = create_melokey()

class MelodyLine():
	def __init__(self, bpm=60):
		self.bpm = bpm
	
	def Note(self, tone, notesize=(1, 4)):
		f = get_melo(tone)
		size = notesize[0] / notesize[1] * 4
		time = int(round(60_000 / self.bpm * size, 0))
		return {'freq': int(f),
				'length': time}

if __name__ == '__main__':
	exchange_meloline_csv()
	ml = MelodyLine()
	print(get_melo('C4', 'english'))
	
