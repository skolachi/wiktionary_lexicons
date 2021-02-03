Multilingual Pronunciation lexicons extracted from Wiktionary

Sudheer Kolachina
21/1/2021

This repo contains scripts to parse the Wiktionary data json extracted using wiktextract package. 
These pronunciation lexicons can be useful in building ASR / TTS systems.

I downloaded extracted json file from https://kaikki.org/dictionary/All%20languages%20combined/kaikki.org-dictionary-all.json.bz2.

The main extraction script is extract\_dictionary.py.\
Usage: 
python3 extract\_dictionary.py --lang de,en,es,fr,it --jsonfile jsonfile --outfile langcode\_dictionary.tsv

Output tsv file contains fields- word, transcription, phone set, locale (accent), word meaning

Two kinds of transcriptions found:
1. IPA
2. EnPr

To do: convert these to arpabet or festival phone set or other options. 

Steps-
1. Extract json file- 
bzip2 -d kaikki.org-dictionary-all.json.bz2

2. Split the json file into smaller files.
split -l 100000 kaikki.org-dictionary-all.json wikt

(Data files not included)

3. Create language specific extraction commands for each of the smaller json files. 
de\_dictionary\_commands
en\_dictionary\_commands
es\_dictionary\_commands
fr\_dictionary\_commands
it\_dictionary\_commands

4. bash extract\_dictionary.sh language-specific-commandsfile (en\_dictionary\_commands)

5. cat wikt*.tsv > lang_dictionary.tsv

Statistics-\
German	54850 de_dictionary.tsv\
English	162495 en_dictionary.tsv\
Spanish	156076 es_dictionary.tsv\
French	73579 fr_dictionary.tsv\
Italian	26854 it_dictionary.tsv
