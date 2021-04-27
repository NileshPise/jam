import jamspell

corrector = jamspell.TSpellCorrector()
corrector.LoadLangModel('en.bin')

corrector.GetCandidates(['ok','cherken'], 1)
