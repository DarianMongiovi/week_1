def pro_syllable_counter(word):
    word = word.lower().strip(".:,;!?")
    if len(word) <= 3: return 1

    # 1. Handle starting 'y' (make it a consonant for the regex)
    processing_word = word
    if word.startswith('y'):
        processing_word = word[1:]

    # 2. Base count
    syllables = len(re.findall(r'[aeiouy]+', processing_word))

    # 3. Suffix Exceptions
    if word.endswith("e") and not word.endswith(("le", "ee")):
        syllables -= 1
    if word.endswith(("ed", "es")):
        # Only subtract if it's not a 'heavy' ending like -ted or -shes
        if not word.endswith(("ted", "ded", "ces", "ses", "xes", "zes", "ches", "shes")):
            syllables -= 1
    if word.endswith(("que", "gue")):
        syllables -= 1
    if word.endswith("ism"): # prism, schism
        syllables += 1

    # 4. Prefix/Hiatus Exceptions (The 'Adders')
    # These pairs almost always split into two syllables
    add_one = ["ia", "io", "iu", "uo", "oa", "eo", "ao", "ua"]
    for pair in add_one:
        if pair in word:
            syllables += 1

    return max(syllables, 1)
