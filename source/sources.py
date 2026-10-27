"""Citations for the Society game. Every entry was checked against the linked text (or, where noted, a reference work).

WORKS: key -> (title, year, url to a free full text or the best available page, note)
CITES: (question number, thinker id) -> (work key, locator, chapter url or None)
QUOTES: thinker id -> (work key, locator, url or None)
"""

SE_LEV = "https://standardebooks.org/ebooks/thomas-hobbes/leviathan/text/chapter-{}"
LOCKE_ST = "https://pressbooks.library.torontomu.ca/secondtreatiseofgovernment/chapter/{}/"
SC = "https://www.marxists.org/reference/subject/economics/rousseau/social-contract/ch0{}.htm"
REP = {2: "3.ii", 3: "4.iii", 4: "5.iv", 5: "6.v"}
REPU = lambda b: f"https://classics.mit.edu/Plato/republic.{REP[b]}.html"
POL = {1: "1.one", 3: "3.three", 4: "4.four", 8: "8.eight"}
POLU = lambda b: f"https://web.mit.edu/classics/Aristotle/politics.{POL[b]}.html"
NEU = {2: "https://classics.mit.edu/Aristotle/nicomachaen.2.ii.html", 10: "https://classics.mit.edu/Aristotle/nicomachaen.10.x.html"}
AN = "https://standardebooks.org/ebooks/confucius/analects/james-legge/text/chapter-{}"
WV = "https://www.marxists.org/reference/archive/wollstonecraft-mary/1792/vindication-rights-woman/ch{:02d}.htm"
MF = "https://www.marxists.org/archive/marx/works/1848/communist-manifesto/ch{:02d}.htm"
PR = "https://www.marxists.org/reference/archive/machiavelli/works/prince/ch{}.htm"

WORKS = {
    # Hobbes
    "leviathan": ("Leviathan", "1651", "https://standardebooks.org/ebooks/thomas-hobbes/leviathan", "Free full text"),
    # Locke
    "second_treatise": ("Second Treatise of Government", "1689", "https://pressbooks.library.torontomu.ca/secondtreatiseofgovernment/", "Free full text"),
    "locke_essay": ("An Essay Concerning Human Understanding", "1689", "https://www.gutenberg.org/dirs/1/0/6/1/10615/10615-h/10615-h.htm", "Free full text, vol. 1"),
    # Rousseau
    "social_contract": ("The Social Contract", "1762", "https://www.marxists.org/reference/subject/economics/rousseau/social-contract/index.htm", "Free full text, G. D. H. Cole translation"),
    "inequality": ("Discourse on the Origin of Inequality", "1755", "https://www.marxists.org/reference/subject/economics/rousseau/inequality/ch02.htm", "Free full text"),
    "emile": ("Emile, or On Education", "1762", "https://gutenberg.org/cache/epub/5427/pg5427-images.html", "Free full text, Barbara Foxley translation"),
    # Plato
    "republic": ("The Republic", "c. 375 BCE", "https://classics.mit.edu/Plato/republic.html", "Free full text, Benjamin Jowett translation"),
    "laws": ("Laws", "c. 348 BCE", "https://classics.mit.edu/Plato/laws.html", "Free full text, Benjamin Jowett translation"),
    # Aristotle
    "politics": ("Politics", "c. 350 BCE", "https://web.mit.edu/classics/Aristotle/politics.html", "Free full text, Benjamin Jowett translation"),
    "ethics": ("Nicomachean Ethics", "c. 340 BCE", "https://classics.mit.edu/Aristotle/nicomachaen.html", "Free full text, W. D. Ross translation"),
    # Confucius
    "analects": ("The Analects", "c. 400 BCE (compiled by his students)", "https://standardebooks.org/ebooks/confucius/analects/james-legge", "Free full text, James Legge translation. Passages are numbered book.passage"),
    # Machiavelli
    "prince": ("The Prince", "1513", "https://www.marxists.org/reference/archive/machiavelli/works/prince/index.htm", "Free full text, W. K. Marriott translation"),
    "discourses": ("Discourses on Livy", "c. 1517", "https://gutenberg.org/files/10827/old/10827-h/10827-h.htm", "Free full text, Ninian Hill Thomson translation"),
    # Montesquieu
    "spirit_laws": ("The Spirit of the Laws", "1748", "https://constitutioncenter.org/media/files/6.5_Primary_Source__Montesquieu%2C_The_Spirit_of_the_Laws_%281748%29_.pdf", "Excerpt of Book XI from the National Constitution Center"),
    # Ibn Khaldun
    "muqaddimah": ("The Muqaddimah", "late 1370s", "https://archive.org/details/muqaddimahintrod00ibnk", "Franz Rosenthal translation, abridged by N. J. Dawood. Free to borrow with an Internet Archive account"),
    # Burke
    "reflections": ("Reflections on the Revolution in France", "1790", "https://standardebooks.org/ebooks/edmund-burke/reflections-on-the-revolution-in-france", "Free full text. The book has no chapters, so citations quote a phrase you can search for"),
    # Paine
    "common_sense": ("Common Sense", "1776", "https://www.gutenberg.org/cache/epub/147/pg147-images.html", "Free full text"),
    "rights_of_man": ("Rights of Man", "1791", "https://gutenberg.org/cache/epub/3742/pg3742-images.html", "Free full text"),
    "age_of_reason": ("The Age of Reason", "1794", "https://ushistory.org/PAINE/reason/reason1.htm", "Free full text"),
    # Wollstonecraft
    "vindication": ("A Vindication of the Rights of Woman", "1792", "https://www.marxists.org/reference/archive/wollstonecraft-mary/1792/vindication-rights-woman/", "Free full text"),
    # Mill
    "on_liberty": ("On Liberty", "1859", "https://gutenberg.org/cache/epub/34901/pg34901-images.html", "Free full text"),
    "rep_gov": ("Considerations on Representative Government", "1861", "https://www.gutenberg.org/cache/epub/5669/pg5669-images.html", "Free full text"),
    "utilitarianism": ("Utilitarianism", "1863", "https://www.gutenberg.org/cache/epub/11224/pg11224-images.html", "Free full text"),
    "subjection": ("The Subjection of Women", "1869", "https://gutenberg.org/cache/epub/27083/pg27083-images.html", "Free full text"),
    # Douglass
    "narrative": ("Narrative of the Life of Frederick Douglass", "1845", "https://www.gutenberg.org/cache/epub/23/pg23-images.html", "Free full text"),
    "fourth_july": ("What to the Slave Is the Fourth of July?", "1852 (speech, Rochester, New York)", "https://teachingamericanhistory.org/document/what-to-the-slave-is-the-fourth-of-july/", "Free full text"),
    "self_made": ("Self-Made Men", "1872 (speech)", "https://teachingamericanhistory.org/library/document/self-made-men", "Free full text"),
    "north_star": ("The North Star (his newspaper)", "1847", "https://en.wikipedia.org/wiki/The_North_Star_(anti-slavery_newspaper)", "About the paper and its motto"),
    # Marx
    "manifesto": ("The Communist Manifesto (with Friedrich Engels)", "1848", "https://www.marxists.org/archive/marx/works/1848/communist-manifesto/index.htm", "Free full text"),
    # Gandhi
    "hind_swaraj": ("Hind Swaraj (Indian Home Rule)", "1909", "https://scalar.lehigh.edu/literature-of-colonial-south-asia/mohandas-k-gandhi-indian-home-rule-hind-swaraj-1909-full-text", "Free full text"),
    "constructive": ("Constructive Programme", "1945", "https://www.mkgandhi.org/ebks/construct.pdf", "Free full text (PDF)"),
    # King
    "birmingham": ("Letter from Birmingham Jail", "1963", "https://billofrightsinstitute.org/activities/martin-luther-king-jr-letter-from-birmingham-jail-1963-pdj", "Free full text"),
    "dream": ("I Have a Dream", "1963 (speech, Washington, D.C.)", "https://www.archives.gov/files/press/exhibits/dream-speech.pdf", "Free full text (PDF), National Archives"),
    "where_go": ("Where Do We Go From Here?", "1967 (speech)", "https://wealthandwant.com/docs/King_Where.htm", "Free full text"),
    # Arendt
    "origins_tot": ("The Origins of Totalitarianism", "1951", "https://plato.stanford.edu/entries/arendt/", "Not free online. Look for it in a library. The link is the Stanford Encyclopedia of Philosophy guide"),
    "human_condition": ("The Human Condition", "1958", "https://plato.stanford.edu/entries/arendt/", "Not free online. Look for it in a library. The link is the Stanford Encyclopedia of Philosophy guide"),
    "on_revolution": ("On Revolution", "1963", "https://plato.stanford.edu/entries/arendt/", "Not free online. Look for it in a library. The link is the Stanford Encyclopedia of Philosophy guide"),
    "thinking": ("Thinking and Moral Considerations", "1971 (essay)", "https://plato.stanford.edu/entries/arendt/", "Not free online. The link is the Stanford Encyclopedia of Philosophy guide"),
    # Beauvoir
    "second_sex": ("The Second Sex", "1949", "https://www.marxists.org/reference/subject/ethics/de-beauvoir/2nd-sex/introduction.htm", "Introduction free online. The full book is in libraries"),
    "ambiguity": ("The Ethics of Ambiguity", "1947", "https://www.marxists.org/reference/subject/ethics/de-beauvoir/ambiguity/index.htm", "Free full text"),
    # Rawls
    "theory_justice": ("A Theory of Justice", "1971", "https://plato.stanford.edu/entries/rawls/", "Not free online. Look for it in a library. The link is the Stanford Encyclopedia of Philosophy guide"),
    # Nozick
    "asu": ("Anarchy, State, and Utopia", "1974", "https://plato.stanford.edu/entries/nozick-political/", "Not free online. Look for it in a library. The link is the Stanford Encyclopedia of Philosophy guide"),
}

CITES = {
    # Plato
    (3, "plato"): ("republic", "Book III (education of the guardians)", REPU(3)),
    (4, "plato"): ("republic", "Book III, 414b–415d (the myth of the metals)", REPU(3)),
    (5, "plato"): ("republic", "Book V, 473c–d", REPU(5)),
    (6, "plato"): ("republic", "Book V, 473c–d", REPU(5)),
    (9, "plato"): ("republic", "Book V, 473c–d", REPU(5)),
    (11, "plato"): ("republic", "Book II, 377b–c", REPU(2)),
    (12, "plato"): ("laws", "Book I, 630e–631a", "https://classics.mit.edu/Plato/laws.1.i.html"),
    (17, "plato"): ("republic", "Book III, 414b–415d (the myth of the metals)", REPU(3)),
    (19, "plato"): ("republic", "Book IV, 433a–b", REPU(4)),
    # Aristotle
    (1, "aristotle"): ("politics", "Book I, part 2", POLU(1)),
    (2, "aristotle"): ("ethics", "Book II, ch. 1", NEU[2]),
    (4, "aristotle"): ("politics", "Book VIII, part 1", POLU(8)),
    (6, "aristotle"): ("politics", "Book IV, part 8", POLU(4)),
    (12, "aristotle"): ("ethics", "Book X, ch. 9", NEU[10]),
    (15, "aristotle"): ("politics", "Book IV, part 11", POLU(4)),
    (16, "aristotle"): ("politics", "Book I, part 5", POLU(1)),
    (17, "aristotle"): ("politics", "Book I, part 5", POLU(1)),
    (18, "aristotle"): ("politics", "Book III, part 9", POLU(3)),
    # Confucius
    (1, "confucius"): ("analects", "18.6", AN.format(18)),
    (2, "confucius"): ("analects", "17.2", AN.format(17)),
    (3, "confucius"): ("analects", "1.2", AN.format(1)),
    (4, "confucius"): ("analects", "1.6", AN.format(1)),
    (5, "confucius"): ("analects", "2.1", AN.format(2)),
    (8, "confucius"): ("analects", "14.23", AN.format(14)),
    (9, "confucius"): ("analects", "12.17, 12.19", AN.format(12)),
    (11, "confucius"): ("analects", "12.1", AN.format(12)),
    (18, "confucius"): ("analects", "2.3", AN.format(2)),
    # Machiavelli
    (1, "machiavelli"): ("prince", "ch. 17", PR.format(17)),
    (2, "machiavelli"): ("discourses", "Book I, ch. 3", None),
    (5, "machiavelli"): ("prince", "ch. 12", PR.format(12)),
    (9, "machiavelli"): ("prince", "ch. 17–18", PR.format(17)),
    # Hobbes
    (1, "hobbes"): ("leviathan", "ch. 13", SE_LEV.format(13)),
    (2, "hobbes"): ("leviathan", "ch. 11", SE_LEV.format(11)),
    (5, "hobbes"): ("leviathan", "ch. 17", SE_LEV.format(17)),
    (6, "hobbes"): ("leviathan", "ch. 17", SE_LEV.format(17)),
    (7, "hobbes"): ("leviathan", "ch. 18", SE_LEV.format(18)),
    (8, "hobbes"): ("leviathan", "ch. 18", SE_LEV.format(18)),
    (11, "hobbes"): ("leviathan", "ch. 18", SE_LEV.format(18)),
    (12, "hobbes"): ("leviathan", "ch. 21", SE_LEV.format(21)),
    (14, "hobbes"): ("leviathan", "ch. 24", SE_LEV.format(24)),
    (18, "hobbes"): ("leviathan", "ch. 30", SE_LEV.format(30)),
    (20, "hobbes"): ("leviathan", "ch. 29", SE_LEV.format(29)),
    # Locke
    (1, "locke"): ("second_treatise", "ch. II, §§6, 13", LOCKE_ST.format(2)),
    (2, "locke"): ("locke_essay", "Book II, ch. I, §2", None),
    (5, "locke"): ("second_treatise", "ch. VIII, §95", LOCKE_ST.format(8)),
    (8, "locke"): ("second_treatise", "ch. XIX, §§222, 240", LOCKE_ST.format(19)),
    (9, "locke"): ("second_treatise", "ch. XI, §§136–137", LOCKE_ST.format(11)),
    (10, "locke"): ("second_treatise", "ch. II, §6", LOCKE_ST.format(2)),
    (14, "locke"): ("second_treatise", "ch. V, §27", LOCKE_ST.format(5)),
    (17, "locke"): ("second_treatise", "ch. II, §4", LOCKE_ST.format(2)),
    (18, "locke"): ("second_treatise", "ch. IX, §124", LOCKE_ST.format(9)),
    # Rousseau
    (1, "rousseau"): ("inequality", "Part II", None),
    (2, "rousseau"): ("emile", "Book I, opening sentence", None),
    (5, "rousseau"): ("social_contract", "Book II, ch. 1–3", SC.format(2)),
    (6, "rousseau"): ("social_contract", "Book III, ch. 15", SC.format(3)),
    (13, "rousseau"): ("social_contract", "Book I, ch. 8", SC.format(1)),
    (14, "rousseau"): ("inequality", "Part II, opening", None),
    (16, "rousseau"): ("emile", "Book V", "https://www.online-literature.com/rousseau/emile/5/"),
    # Montesquieu
    (6, "montesquieu"): ("spirit_laws", "Book XI, ch. 6", None),
    (7, "montesquieu"): ("spirit_laws", "Book XI, ch. 6", None),
    # Ibn Khaldun (Muqaddimah chapters)
    (1, "ibnkhaldun"): ("muqaddimah", "ch. 1, on human civilization in general", None),
    (3, "ibnkhaldun"): ("muqaddimah", "ch. 2, on desert life and group feeling (asabiyya)", None),
    (20, "ibnkhaldun"): ("muqaddimah", "ch. 3, on how dynasties rise and fall", None),
    # Burke (search for the quoted phrase)
    (3, "burke"): ("reflections", "the passage beginning \"We are afraid to put men to live and trade each on his own private stock of reason\"", None),
    (5, "burke"): ("reflections", "the passage on \"an entailed inheritance derived to us from our forefathers\"", None),
    (10, "burke"): ("reflections", "the passage on \"an entailed inheritance derived to us from our forefathers\"", None),
    (8, "burke"): ("reflections", "\"A state without the means of some change is without the means of its conservation\"", None),
    (20, "burke"): ("reflections", "\"A state without the means of some change is without the means of its conservation\"", None),
    # Paine
    (1, "paine"): ("common_sense", "\"Of the Origin and Design of Government\"", None),
    (5, "paine"): ("common_sense", "\"Of the Origin and Design of Government\"", None),
    (6, "paine"): ("common_sense", "\"Of the Origin and Design of Government\"", None),
    (7, "paine"): ("common_sense", "\"Of the Origin and Design of Government\"", None),
    (18, "paine"): ("common_sense", "\"Of the Origin and Design of Government\"", None),
    (8, "paine"): ("common_sense", "\"Thoughts on the Present State of American Affairs\"", None),
    (17, "paine"): ("rights_of_man", "Part I (\"all men are born equal, and with equal natural right\")", None),
    (10, "paine"): ("rights_of_man", "Part I (\"Natural rights are those which appertain to man in right of his existence\")", None),
    (11, "paine"): ("age_of_reason", "Part I, opening section", None),
    (20, "paine"): ("common_sense", "Appendix (\"We have it in our power to begin the world over again\")", None),
    # Wollstonecraft
    (2, "wollstonecraft"): ("vindication", "ch. 2", WV.format(2)),
    (4, "wollstonecraft"): ("vindication", "ch. 4", WV.format(4)),
    (13, "wollstonecraft"): ("vindication", "ch. 9", WV.format(9)),
    (17, "wollstonecraft"): ("vindication", "ch. 9", WV.format(9)),
    (3, "wollstonecraft"): ("vindication", "ch. 12", WV.format(12)),
    (16, "wollstonecraft"): ("vindication", "ch. 12", WV.format(12)),
    (20, "wollstonecraft"): ("vindication", "ch. 12", WV.format(12)),
    # Mill
    (12, "mill"): ("on_liberty", "ch. I (the harm principle)", None),
    (13, "mill"): ("on_liberty", "ch. I (\"Over himself, over his own body and mind, the individual is sovereign\")", None),
    (4, "mill"): ("on_liberty", "ch. II (\"He who knows only his own side of the case, knows little of that\")", None),
    (11, "mill"): ("on_liberty", "ch. II, on freedom of thought and discussion", None),
    (20, "mill"): ("on_liberty", "ch. II, on freedom of thought and discussion", None),
    (6, "mill"): ("rep_gov", "ch. III", None),
    (19, "mill"): ("utilitarianism", "ch. II (the Greatest Happiness Principle)", None),
    (16, "mill"): ("subjection", "ch. I (\"a principle of perfect equality\")", None),
    # Douglass
    (4, "douglass"): ("narrative", "ch. VI (learning to read)", None),
    (13, "douglass"): ("narrative", "ch. VII", None),
    (19, "douglass"): ("narrative", "ch. VII", None),
    (3, "douglass"): ("self_made", "the whole speech", None),
    (10, "douglass"): ("fourth_july", "\"men have a natural right to freedom\"", None),
    (17, "douglass"): ("fourth_july", "the passage asking him to \"prove that we are men\"", None),
    (20, "douglass"): ("fourth_july", "\"it is not light that is needed, but fire\"", None),
    (16, "douglass"): ("north_star", "the paper's motto, \"Right is of no Sex\"", None),
    # Marx
    (3, "marx"): ("manifesto", "ch. 1", MF.format(1)),
    (15, "marx"): ("manifesto", "ch. 1", MF.format(1)),
    (17, "marx"): ("manifesto", "ch. 1", MF.format(1)),
    (18, "marx"): ("manifesto", "ch. 1 (the state as \"a committee for managing the common affairs\" of the owners)", MF.format(1)),
    (19, "marx"): ("manifesto", "ch. 1", MF.format(1)),
    (14, "marx"): ("manifesto", "ch. 2 (\"Abolition of private property\")", MF.format(2)),
    (4, "marx"): ("manifesto", "ch. 2 (the ruling ideas of each age)", MF.format(2)),
    (16, "marx"): ("manifesto", "ch. 2", MF.format(2)),
    (7, "marx"): ("manifesto", "ch. 2 (\"the public power will lose its political character\")", MF.format(2)),
    (13, "marx"): ("manifesto", "ch. 2 (\"the free development of each\")", MF.format(2)),
    (10, "marx"): ("manifesto", "ch. 2 (\"your jurisprudence is but the will of your class made into a law for all\")", MF.format(2)),
    (20, "marx"): ("manifesto", "ch. 4", MF.format(4)),
    # Gandhi
    (4, "gandhi"): ("hind_swaraj", "ch. XVIII, Education", None),
    (8, "gandhi"): ("hind_swaraj", "ch. XVII, Passive Resistance", None),
    (20, "gandhi"): ("hind_swaraj", "ch. XVII, Passive Resistance", None),
    (9, "gandhi"): ("hind_swaraj", "ch. XIII, What Is True Civilization?", None),
    (6, "gandhi"): ("hind_swaraj", "ch. XIV", None),
    (13, "gandhi"): ("hind_swaraj", "ch. XIV (\"It is Swaraj when we learn to rule ourselves\")", None),
    (14, "gandhi"): ("constructive", "§13, Economic Equality (trusteeship)", None),
    (15, "gandhi"): ("constructive", "§13, Economic Equality", None),
    (19, "gandhi"): ("constructive", "§2, Removal of Untouchability", None),
    (7, "gandhi"): ("constructive", "§4, Khadi (self-reliant villages)", None),
    # King
    (8, "king"): ("birmingham", "the passage on nonviolent direct action", None),
    (10, "king"): ("birmingham", "\"A just law is a man-made code that squares with the moral law\"", None),
    (13, "king"): ("birmingham", "\"segregation distorts the soul and damages the personality\"", None),
    (19, "king"): ("birmingham", "\"Injustice anywhere is a threat to justice everywhere\"", None),
    (20, "king"): ("birmingham", "the passage on nonviolent direct action", None),
    (14, "king"): ("where_go", "the passage on a guaranteed income", None),
    (15, "king"): ("where_go", "the passage on a guaranteed income", None),
    (18, "king"): ("where_go", "the passage on restructuring society", None),
    (17, "king"): ("dream", "the whole speech", None),
    # Arendt
    (5, "arendt"): ("human_condition", "ch. 5, Action", None),
    (11, "arendt"): ("human_condition", "ch. 5, Action", None),
    (13, "arendt"): ("human_condition", "ch. 5, Action", None),
    (18, "arendt"): ("human_condition", "ch. 5, Action", None),
    (6, "arendt"): ("on_revolution", "ch. 6, on councils", None),
    (10, "arendt"): ("origins_tot", "ch. 9 (\"the right to have rights\")", None),
    (4, "arendt"): ("thinking", "the whole essay", None),
    # Beauvoir
    (13, "beauvoir"): ("second_sex", "Introduction (woman as \"the Other\")", None),
    (2, "beauvoir"): ("second_sex", "Vol. II, opening of \"Childhood\"", None),
    (16, "beauvoir"): ("second_sex", "\"The Independent Woman\"", None),
    (3, "beauvoir"): ("ambiguity", "the whole essay", None),
    # Rawls
    (10, "rawls"): ("theory_justice", "§3, The Main Idea of the Theory of Justice", None),
    (14, "rawls"): ("theory_justice", "§13, Democratic Equality and the Difference Principle", None),
    (15, "rawls"): ("theory_justice", "§13, Democratic Equality and the Difference Principle", None),
    (18, "rawls"): ("theory_justice", "§13, Democratic Equality and the Difference Principle", None),
    (17, "rawls"): ("theory_justice", "§17, The Tendency to Equality", None),
    (19, "rawls"): ("theory_justice", "§24, The Veil of Ignorance", None),
    # Nozick
    (7, "nozick"): ("asu", "ch. 3, The Minimal State and the Ultraminimal State", None),
    (12, "nozick"): ("asu", "ch. 3, Libertarian Constraints", None),
    (18, "nozick"): ("asu", "ch. 3, The Minimal State and the Ultraminimal State", None),
    (15, "nozick"): ("asu", "ch. 7, The Entitlement Theory", None),
    (19, "nozick"): ("asu", "ch. 7, How Liberty Upsets Patterns", None),
    (14, "nozick"): ("asu", "ch. 7, Locke's Theory of Acquisition", None),
    (3, "nozick"): ("asu", "ch. 7, Natural Assets and Arbitrariness", None),
}

QUOTES = {
    "plato": ("republic", "Book V, 473c–d", REPU(5)),
    "aristotle": ("politics", "Book I, part 2", POLU(1)),
    "confucius": ("analects", "12.17", AN.format(12)),
    "machiavelli": ("prince", "ch. 17", PR.format(17)),
    "hobbes": ("leviathan", "ch. 13", SE_LEV.format(13)),
    "locke": ("second_treatise", "ch. II, §6", LOCKE_ST.format(2)),
    "rousseau": ("social_contract", "Book I, ch. 1", SC.format(1)),
    "montesquieu": ("spirit_laws", "Book XI, ch. 4", None),
    "burke": ("reflections", "search for \"Society is indeed a contract\"", None),
    "paine": ("common_sense", "\"Of the Origin and Design of Government\"", None),
    "wollstonecraft": ("vindication", "ch. 4", WV.format(4)),
    "mill": ("on_liberty", "ch. I", None),
    "douglass": ("narrative", "ch. VI", None),
    "marx": ("manifesto", "ch. 1", MF.format(1)),
    "gandhi": ("hind_swaraj", "ch. XIV", None),
    "king": ("birmingham", "the opening pages", None),
    "arendt": ("human_condition", "ch. 5, Action", None),
    "beauvoir": ("second_sex", "Vol. II, opening of \"Childhood\"", None),
    "rawls": ("theory_justice", "§1, The Role of Justice", None),
    "nozick": ("asu", "ch. 7, Redistribution and Property Rights", None),
}

# Main work for each thinker, used when a question has no pinpoint citation.
MAIN = {"confucius": "analects", "plato": "republic", "aristotle": "politics", "ibnkhaldun": "muqaddimah",
        "machiavelli": "prince", "hobbes": "leviathan", "locke": "second_treatise", "montesquieu": "spirit_laws",
        "rousseau": "social_contract", "burke": "reflections", "paine": "common_sense", "wollstonecraft": "vindication",
        "mill": "on_liberty", "douglass": "narrative", "marx": "manifesto", "gandhi": "hind_swaraj", "arendt": "origins_tot",
        "beauvoir": "second_sex", "rawls": "theory_justice", "king": "birmingham", "nozick": "asu"}

# Works to list for each thinker, in order.
READ = {"confucius": ["analects"], "plato": ["republic", "laws"], "aristotle": ["politics", "ethics"],
        "ibnkhaldun": ["muqaddimah"], "machiavelli": ["prince", "discourses"], "hobbes": ["leviathan"],
        "locke": ["second_treatise", "locke_essay"], "montesquieu": ["spirit_laws"],
        "rousseau": ["social_contract", "inequality", "emile"], "burke": ["reflections"],
        "paine": ["common_sense", "rights_of_man", "age_of_reason"], "wollstonecraft": ["vindication"],
        "mill": ["on_liberty", "subjection", "utilitarianism", "rep_gov"],
        "douglass": ["narrative", "fourth_july", "self_made", "north_star"], "marx": ["manifesto"],
        "gandhi": ["hind_swaraj", "constructive"], "arendt": ["origins_tot", "human_condition", "on_revolution", "thinking"],
        "beauvoir": ["second_sex", "ambiguity"], "rawls": ["theory_justice"], "king": ["birmingham", "where_go", "dream"],
        "nozick": ["asu"]}

W = "https://en.wikipedia.org/wiki/"
SEP = "https://plato.stanford.edu/entries/"
# Where the timeline facts were checked: thinker -> [(label, url)]
LIFE = {
    "confucius": [("Wikipedia: Confucius", W + "Confucius")],
    "plato": [("Wikipedia: Plato", W + "Plato"), ("Wikipedia: Trial of Socrates", W + "Trial_of_Socrates")],
    "aristotle": [("Wikipedia: Aristotle", W + "Aristotle"), ("Wikipedia: Battle of Chaeronea", W + "Battle_of_Chaeronea_(338_BC)")],
    "ibnkhaldun": [("Wikipedia: Ibn Khaldun", W + "Ibn_Khaldun")],
    "machiavelli": [("Wikipedia: Niccolò Machiavelli", W + "Niccol%C3%B2_Machiavelli")],
    "hobbes": [("Wikipedia: Thomas Hobbes", W + "Thomas_Hobbes"), ("Wikipedia: Execution of Charles I", W + "Execution_of_Charles_I")],
    "locke": [("Wikipedia: John Locke", W + "John_Locke"), ("Wikipedia: Bill of Rights 1689", W + "Bill_of_Rights_1689")],
    "montesquieu": [("Wikipedia: Montesquieu", W + "Montesquieu")],
    "rousseau": [("Wikipedia: Jean-Jacques Rousseau", W + "Jean-Jacques_Rousseau")],
    "burke": [("Wikipedia: Edmund Burke", W + "Edmund_Burke")],
    "paine": [("Wikipedia: Thomas Paine", W + "Thomas_Paine")],
    "wollstonecraft": [("Wikipedia: Mary Wollstonecraft", W + "Mary_Wollstonecraft")],
    "mill": [("Wikipedia: John Stuart Mill", W + "John_Stuart_Mill")],
    "douglass": [("Wikipedia: Frederick Douglass", W + "Frederick_Douglass")],
    "marx": [("Wikipedia: Karl Marx", W + "Karl_Marx")],
    "gandhi": [("Wikipedia: Mahatma Gandhi", W + "Mahatma_Gandhi")],
    "arendt": [("Stanford Encyclopedia: Hannah Arendt", SEP + "arendt/"), ("Wikipedia: Hannah Arendt", W + "Hannah_Arendt")],
    "beauvoir": [("Stanford Encyclopedia: Simone de Beauvoir", SEP + "beauvoir/"), ("Wikipedia: Women's suffrage in France", W + "Women%27s_suffrage_in_France")],
    "rawls": [("Stanford Encyclopedia: John Rawls", SEP + "rawls/"), ("Wikipedia: John Rawls", W + "John_Rawls")],
    "king": [("Wikipedia: Martin Luther King Jr.", W + "Martin_Luther_King_Jr.")],
    "nozick": [("Wikipedia: Robert Nozick", W + "Robert_Nozick"), ("Wikipedia: Great Society", W + "Great_Society")],
}
