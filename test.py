# import webvtt
# from googletrans import Translator
# import googletrans

# translator = Translator()
# vtt = webvtt.read('test.vtt')
# transcript = ""

# lines = []
# for line in vtt:
#     lines.extend(line.text.strip().splitlines())

# previous = None
# for line in lines:
#     if line == previous:
#         continue
#     transcript += " " + line
#     previous = line
# translated = translator.translate('test', src='en', dest='vi')

from googletrans import Translator

translator = Translator()


translator.translate('veritas lux mea', src='la')
