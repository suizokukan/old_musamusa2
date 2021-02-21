=============================
= Musamusa text format file =
=============================

-------------------------------
- (default format, version 1) -
-------------------------------
The first real line (nonwithstanding comments or white lines) must be a
"format_name_and_version" line, see above.

Some symbols have a special meaning at the very beginning of a line:
#              | comment
+++            | nested file
:abbreviation: | abbreviation definition    
:flag:         | flag definition
:marker:       | marker definition
@              | glossary line
::             | text segment : text
**             | text segment : comment
==             | text segment : translation
~~             | text segment : transcription
-              | text segment : glossary line
    
###  -  utf8 encoded
###
###  -  empty lines        : lines made of spaces are discarded
###
###  -  comment lines      : lines starting with '#' are discarded
###
###                          → see MUSTEXTFORMATSETTINGS["comment_char"]
###
###  -  ⬂ character        : lines ending with ⬂ are joined to the next line
###
###                          → see MUSTEXTFORMATSETTINGS["tobecontinued_char"]
###
###  -  left-spaces syntax : if True, lines beginning with spaces are joined
###                          to the precedent line.
###
###                          → see MUSTEXTFORMATSETTINGS["allow_leftspaces_syntax"]
###
###  -  nested file        : +++ (=file to be included tag)
###                          the string after +++ will be stripped.
###
###                          it's a relative path based on the parent file,
###                          absolute path IS NOT allowed.
###                          e.g. if the file "directory/myfile.mus" contains the line
###                              +++ subdirectory/mynestedfile.mus
###                          the nested file will be directory/subdirectory/mynestedfile.mus
###
###                          → see MUSTEXTFORMATSETTINGS["filetobeincluded_tag"]

### format_name_and_version line
### [[musamusa]] stands for [[musamusa;format=default;version=1]]
[[musamusa]]
    
### flag definition:
:flag: € : euro

### abbreviation definition:
###   henceforth, every "ᵛⁱ" string will by replaced by "[vi]"
:abbreviation: ᵛⁱ : [vi]   ### 

### markers definition:
###   henceforth, you may use [N], {N} and ⟨word=N⟩ in text segments (see how to use marker)
:marker:            N
    
### glossary entry:
###                    entry                            infos                            content
###                    ---------------- -------------------------------------------- --------------
###                  @ <nārro▨raconter> [verbe|nārro, nārrās, nārrāre, nārrāuī|1C]
@ <se, sē▨ce, le, qui, …> [déterminant+pronom relatif] ⬂
  (1) déterminant démonstratif ⬂
  (2) article défini; au génitif singulier peut avoir le sens de "en échange de quoi" ⬂
      cf e.g. ▶ᴷ⁴ᵃBe0114b ⬂
  (3) pronom relatif. ⬂
  (4) conjonction "þæt : cf <þæt_conj▨que>
    
### text segment:
###        text variant  text reference  text
###        ------------  --------------  --------------------------------------------
###      ::ᴷ⁴ᵃ           (Be.0001)       Hwæt, ᴺwḗ ᴳGār-déna | {gp}in ᴰġḗardágum{/gp}
###

::ᴷ⁴ᵃ    (Be.0001)      Hwæt, ᴺwḗ ᴳGār-déna | {gp}in ᴰġḗardágum{/gp}
==ᴷ⁴ᵃ                   Holà ! Des grands rois danois d'antan
-ᴷ⁴ᵃ                    Hwæt          : <hwæt▨holà>
-ᴷ⁴ᵃ                    wḗ            : <pronom personnel▨je, tu, …> ◖1P◗; unique occurence de wē dans Beowulf
-ᴷ⁴ᵃ                    Gārdéna       : <Gār-Dene▨Danois à la lance> ◖G.pl.◗
-ᴷ⁴ᵃ                    in            : <in▨dans>
-ᴷ⁴ᵃ                    ġḗardágum     : <ġēar-dagas▨des années d'antan> ◖D.pl◗


::ᴷ⁴ᵃ    Be0046         ᴬǣ́nne {gp}ofer ᴬȳ́ðe{/gp} | ᴬúmbọrwésènde.
::ᴷ⁴'ᵃ   Be0046         ᴬǣ́nne {gp}ofer ᴬȳ́ðe{/gp} | ᴬúmbrwésènde.
==                      seul sur les vagues, quand il était enfant.
==ø                     alone, on the waves, when he was a child.
-                       ǣ́nne          : <ān▨un> ◖A.sg.masculin.strong◗
-                       ofer          : <ofer▨au delà de>
-                       ȳ́ðe           : <ȳð▨une vague> ◖A.sg◗
-ᴷ⁴ᵃ                    úmbọrwésènde  : <umbor-wesende▨étant un enfant> ◖strong.A.sg.masculin◗ ⬂
                                        On attendait plutôt la forme úmbọrwésèndne,⬂
                                        cf <non accord entre un adjectif et le mot qu'il qualifie>
-ᴷ⁴'ᵃ                   úmbrwésènde   : <umbor-wesende▨étant un enfant> ◖strong.A.sg.masculin◗ ⬂
                                        On attendait plutôt la forme úmbọrwésèndne,⬂
                                        cf <non accord entre un adjectif et le mot qu'il qualifie>
