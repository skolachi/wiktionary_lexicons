import argparse
import json
import sys

def extract_dictionary(jsonfile,outfile,lang):
	with open(jsonfile,encoding='utf-8') as f1:
		with open(outfile,'w',encoding='utf-8') as f2:
			for line in f1:
				entry = json.loads(line.strip())
				if entry['lang_code'] == lang:
					word = entry['word']
					meaning = ''
					if 'senses' in entry.keys():
						for s in entry['senses']:
							if 'glosses' in s.keys():
								meaning = s['glosses'][0]
								#meaning = '|'.join(s['glosses'])
								break
					if 'sounds' in entry.keys():
						for s in entry['sounds']:
							if "tags" in s.keys():
								if "ipa" in s.keys():
									f2.write('%s\t%s\t%s\t%s\t%s\n'%(word,s["ipa"],"ipa",'|'.join(s["tags"]),meaning))
								if "enpr" in s.keys():
									f2.write('%s\t%s\t%s\t%s\t%s\n'%(word,s["enpr"],"enpr",'|'.join(s["tags"]),meaning))
							else:
								if "ipa" in s.keys():
									f2.write('%s\t%s\t%s\t%s\n'%(word,s["ipa"],"ipa",meaning))
								if "enpr" in s.keys():
									f2.write('%s\t%s\t%s\t%s\n'%(word,s["enpr"],"enpr",meaning))


def main():
	parser = argparse.ArgumentParser(description='Extraction pronunciation dictionary from Wiktionary datafile')
	parser.add_argument("--lang",help='Language',choices=['de','en','es','fr','it'],required=True)
	parser.add_argument("--jsonfile",help='Path to wiktextract json output',default='/data/nfs/datasets/speech/es/englishnativisation/englishlexicon/kaikki.org-dictionary-all.json')
	parser.add_argument("--outfile",help='Extracted dictionary written to this file',default='dictionary.tsv')
	args = parser.parse_args()
	extract_dictionary(args.jsonfile, args.outfile, args.lang)

if __name__ == "__main__":
	main()
