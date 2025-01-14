import meta

for language in meta.languages:
	top = 1000
	forms = set()
	try:
		fh = open(meta.output_dir + "/" + "formlist-" + language + ".txt")
	except Exception:
		print("Couldn't open {}".format("formlist-" + language + ".txt"))
		continue
	for line in fh:
		forms.add(line.strip().lower())

	try:
		output = open(meta.output_dir + "/" + "missing-" + language + ".txt", "w")
	except Exception:
		print("Couldn't open {}".format("missing-" + language + ".txt"))
		continue

	filtered = meta.load_filter(language)

	try:
		fh = open(meta.output_dir + "/" + "wordlist-" + language + ".txt")
	except Exception:
		print("Couldn't open {}".format("wordlist-" + language + ".txt"))
		continue

	output.write("{{lc-head}}\n")
	for line in fh:
		word, _, num = line.strip().rpartition(" ")
		word = word.lower()
		count = int(num)

		if word in forms or word in filtered:
			pass
		else:
			top -= 1
			if top < 0:
				break
			output.write("{{lc-row|" + word + "|" + str(count) + "}}\n")
	output.write("{{lc-foot}}\n")
	output.close()
