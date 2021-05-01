"""
        mustext format file

        * ETR based (...)

        * first line must be [[format name]], e.g. [[mustext default]]  > plusieurs formats possibles
            transformer le nom en un module mustext_default

        * parsingtools:
                "lexicon_entry_prefix"
                "text_segment_prefix"

        * markers:
                :marker: N
                :marker: Acc

        * lexicon:
                 ----|-NO SPACE HERE-|------|-------------------|-----------------------...
                 \\s*|text variant(s)| \\s+ | lexicon key       | lexicon value
                     |               |      |                   |
                 MAND|   OPTIONAL    |MANDAT|   OPTIONAL        |    MANDATORY
                     |               |      |                   | (unspecified format)
                     |               |      |                   |
                 ----|---------------|------|-------------------|-----------------------...
                @     (a+b)                   <ǣdre|rapidement>  [adverbe] "rapidement"

        * text segment:
                      |-------NO SPACE HERE----------|---------------------------...
                  \\s*|text refer.|text variant(s)   | \\s+ | text
                      |           |                  |      |
                  OPTI| MANDATORY |    OPTIONAL      |MANDAT| MANDATORY
                      |           |                  |      | (unspecified format)
                      |-----------|------------------|------|--------------------...
                ::     Beowulf.245-Beowulf.246(a+b+c)

        * text segment translation/translitteration/commentary
                      |-------NO SPACE HERE----------|---------------------------...
                  \\s*|text refer.|text variant(s)   | \\s+ | data
                      |           |                  |      |
                  OPTI| OPTIONAL  |    OPTIONAL      |MANDAT| MANDATORY
                      |           |                  |      | (unspecified format)
                      |-----------|------------------|------|--------------------...
                ==     Beowulf.245-Beowulf.246(a+b+c)
                ~~     Beowulf.245-Beowulf.246(a+b+c)
                **     Beowulf.245-Beowulf.246;Beowulf.250(a+b+c)

        * text segment note
                      |-------NO SPACE HERE----------|---------------------------...
                -     Beowulf.245-Beowulf.246(a+b+c)   key : value
"""

from rich import print as rprint
import musamusa_etr.etr

import musamusa_etr.aboutproject as musamusaetr_aboutproject
import musamusa_errors.aboutproject as musamusaerrors_aboutproject
import musamusa_fal.aboutproject as musamusafal_aboutproject
import musamusa_atext.aboutproject as musamusaatext_aboutproject

rprint("--- example #0 : version and dependencies ---")
rprint("Working with package musamusa_etr v."+musamusaetr_aboutproject.__version__)
rprint("Working with package musamusa_fal v."+musamusafal_aboutproject.__version__)
rprint("Working with package musamusa_errors v."+musamusaerrors_aboutproject.__version__)
rprint("Working with package musamusa_atext v."+musamusaatext_aboutproject.__version__)


class MusTextFile:
    def __init__(self):
        self.etr = musamusa_etr.etr.ETR()

    def read(self,
             filename: str):
        yield from self.etr.read(filename)


MUS = MusTextFile()
for etr_line in MUS.read("musamusa_etr/examples/1.txt"):
    print(etr_line, MUS.etr.read_tags)
