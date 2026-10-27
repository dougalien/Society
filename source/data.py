"""Answer key for the Society game. Run to regenerate data.json and the doc tables (key.md)."""
import json, pathlib
import sources
import lessons

HERE = pathlib.Path(__file__).parent

# id, short code (for share links), name, lived, where, big idea, rundown, quote, challenge question
THINKERS = [
    ("confucius", "con", "Confucius", "551–479 BCE", "China",
     "A good society runs on virtue, duty, and respect, with rulers setting the moral example.",
     "Confucius taught that order starts inside people, not in laws. If rulers are good examples and families honor their duties to each other, society takes care of itself. Rituals, manners, and education build character.",
     "To govern means to rectify. If you lead on the people with correctness, who will dare not to be correct?",
     "Confucius thought respect for parents and elders holds society together. Is there a limit to how much we owe the people above us?"),
    ("plato", "pla", "Plato", "c. 428–348 BCE", "Athens",
     "The wise should rule, and everyone should do the job they are suited for.",
     "In the Republic, Plato imagines a city run by philosopher-kings who are trained for decades to know what is truly good. Each person does the work they are best at, and education shapes everyone for their role. He distrusted democracy, which had put his teacher Socrates to death.",
     "Until philosophers rule as kings, cities will never have rest from their evils.",
     "Plato didn't trust ordinary voters to choose well. Should experts make decisions for the public? Where would you draw the line?"),
    ("aristotle", "ari", "Aristotle", "384–322 BCE", "Greece",
     "Humans are political animals, and the best state mixes rule by one, few, and many around a strong middle class.",
     "Aristotle studied the constitutions of more than 150 Greek cities. He concluded that people only flourish in a community and that the best government blends monarchy, aristocracy, and democracy. A large middle class keeps a city stable, and good laws train citizens in good habits.",
     "Man is by nature a political animal.",
     "Aristotle said a strong middle class makes a society stable. Do you think that's true today? What evidence would you look for?"),
    ("ibnkhaldun", "ibn", "Ibn Khaldun", "1332–1406", "North Africa",
     "Societies rise and fall through asabiyyah, the solidarity that binds a group together.",
     "Ibn Khaldun, often called a founder of sociology, watched dynasties rise and collapse across North Africa. He argued that tight-knit groups with strong solidarity (asabiyyah) take power, then grow comfortable and divided, until a new group replaces them. History moves in cycles shaped by geography, economics, and group loyalty.",
     "",
     "Ibn Khaldun believed every powerful group eventually grows soft and loses power. Can you think of an empire, company, or team that followed this pattern?"),
    ("machiavelli", "mac", "Niccolò Machiavelli", "1469–1527", "Florence",
     "A ruler must do what works to keep power, and it is safer to be feared than loved.",
     "Machiavelli wrote The Prince after watching Italian city-states be conquered and betrayed. He described politics as it really works rather than as it should, and advised rulers to be ruthless when necessary to protect the state. To him, a stable state matters more than a ruler's personal goodness.",
     "It is much safer to be feared than loved.",
     "Machiavelli said results matter more than a leader's personal morals. Can a leader do bad things for a good cause? Give an example."),
    ("hobbes", "hob", "Thomas Hobbes", "1588–1679", "England",
     "Without a strong sovereign, life is \"nasty, brutish, and short.\"",
     "Hobbes lived through the English Civil War, and in Leviathan he argued that without government people would live in a war of all against all. To escape that fear, people agree to hand nearly all power to a sovereign. Even a harsh ruler is better than chaos.",
     "The life of man, solitary, poor, nasty, brutish, and short.",
     "Hobbes said even a harsh government beats no government. Is there any point where you'd rather have chaos than an unjust ruler?"),
    ("locke", "loc", "John Locke", "1632–1704", "England",
     "People have natural rights to life, liberty, and property, and government exists by their consent.",
     "Locke argued that people are born free and equal, with rights that no government gives or can take away. Government is created to protect those rights, and if it betrays that trust, the people may replace it. Jefferson borrowed these ideas for the Declaration of Independence.",
     "Being all equal and independent, no one ought to harm another in his life, health, liberty, or possessions.",
     "Locke said you own what you mix your labor with. Does that idea work for things like land, ideas, or data?"),
    ("montesquieu", "mon", "Montesquieu", "1689–1755", "France",
     "Power must be split into branches that check each other.",
     "In The Spirit of the Laws, Montesquieu argued that liberty survives only when lawmaking, enforcing, and judging are held by separate hands. He also believed laws should fit a country's climate, customs, and history. The U.S. Constitution's three branches come straight from his ideas.",
     "Power should be a check to power.",
     "Montesquieu wanted branches of government to block each other. When does that protect freedom, and when does it just cause gridlock?"),
    ("rousseau", "rou", "Jean-Jacques Rousseau", "1712–1778", "Geneva / France",
     "People are born good and free, and should be ruled by the general will they share.",
     "Rousseau believed humans in nature were peaceful and that private property and competition corrupted them. In The Social Contract, he argued that legitimate laws come from the general will of the whole community, decided by citizens themselves. Freedom means obeying laws you helped make.",
     "Man is born free, and everywhere he is in chains.",
     "Rousseau said society corrupts people who were born good. Do you think people are better or worse because of society? Why?"),
    ("burke", "bur", "Edmund Burke", "1729–1797", "Ireland / Britain",
     "Change slowly, because tradition holds the wisdom of generations.",
     "Burke watched the French Revolution tear down old institutions and turn violent. He argued that customs and institutions carry lessons learned over centuries, and that reformers who sweep them away do great harm. He supported gradual reform, including for the American colonies, but not revolution.",
     "Society is indeed a contract... between those who are living, those who are dead, and those who are to be born.",
     "Burke warned against tearing down traditions too quickly. Name a tradition worth keeping and one worth changing. How do you tell the difference?"),
    ("paine", "pai", "Thomas Paine", "1737–1809", "England / America",
     "Government is a necessary evil, and people have the right to overthrow tyranny and govern themselves.",
     "Paine's pamphlet Common Sense convinced many colonists to break from Britain. He argued that all people have equal natural rights, that kings have no right to rule, and that a republic of elected representatives is best. Later, in Agrarian Justice, he proposed a fund to give every young adult a start in life.",
     "Society in every state is a blessing, but government even in its best state is but a necessary evil.",
     "Paine called government a \"necessary evil.\" What is something government does that you think is necessary? Is it also evil?"),
    ("wollstonecraft", "wol", "Mary Wollstonecraft", "1759–1797", "England",
     "Women are rational beings who deserve the same education and rights as men.",
     "In A Vindication of the Rights of Woman, Wollstonecraft argued that women only seemed less capable because they were denied education. A society that keeps half its people ignorant cannot be truly free or good. She applied Enlightenment ideas about reason and rights to everyone.",
     "I do not wish them to have power over men; but over themselves.",
     "Wollstonecraft said women seemed weaker only because they were denied education. What groups today might be held back by unequal education?"),
    ("mill", "mil", "John Stuart Mill", "1806–1873", "England",
     "Liberty should be limited only to prevent harm to others, and policy should aim at the greatest happiness.",
     "In On Liberty, Mill argued that people should be free to think, speak, and live as they choose unless they harm others. Even wrong opinions help us test the truth. As a utilitarian, he judged laws by whether they increase happiness, and he was an early supporter of women's right to vote.",
     "The only purpose for which power can be rightfully exercised over any member of a civilized community, against his will, is to prevent harm to others.",
     "Mill's harm principle says you can do anything that doesn't harm others. Does online speech that upsets people count as harm?"),
    ("douglass", "dou", "Frederick Douglass", "c. 1818–1895", "United States",
     "No one may own another person, and freedom grows through literacy, voice, and equal rights.",
     "Douglass escaped slavery, taught himself to read, and became one of the most powerful speakers in American history. He argued that the promise of the Declaration of Independence must apply to everyone, and he fought for abolition, Black citizenship, and women's rights. He believed in protest, persuasion, and resistance to injustice.",
     "From that moment, I understood the pathway from slavery to freedom.",
     "Douglass asked, \"What to the slave is the Fourth of July?\" Are there promises in America's founding documents that still haven't been kept for everyone?"),
    ("marx", "mar", "Karl Marx", "1818–1883", "Germany / England",
     "History is class struggle, and workers should end exploitation by abolishing classes.",
     "Marx watched factory workers in industrial England labor long hours for little pay. He argued that owners profit from workers' labor, and that this conflict between classes drives history. He predicted workers would overthrow capitalism and build a society without classes, where the state would no longer be needed.",
     "The history of all hitherto existing society is the history of class struggles.",
     "Marx said your economic class shapes your whole life. How much do you think money and family background decide where people end up?"),
    ("gandhi", "gan", "Mohandas Gandhi", "1869–1948", "India",
     "Change society through nonviolent resistance and self-rule, starting from simple village communities.",
     "Gandhi led India's movement for independence from Britain using satyagraha, nonviolent resistance that refuses to cooperate with injustice. He wanted power spread out to self-governing villages, simple living, and wealth held in trust for the community. His methods inspired civil rights movements around the world.",
     "It is Swaraj when we learn to rule ourselves.",
     "Gandhi believed nonviolence could defeat an empire. Are there situations where nonviolent resistance wouldn't work?"),
    ("arendt", "are", "Hannah Arendt", "1906–1975", "Germany / United States",
     "Freedom lives in people acting and speaking together in public, and totalitarianism destroys it.",
     "Arendt fled Nazi Germany and spent her life studying how totalitarian governments crush people. She argued that real power comes from citizens acting together, and that people lose their rights when they lose membership in a political community. She warned that evil is often done by ordinary people who stop thinking.",
     "Power springs up between men when they act together and vanishes the moment they disperse.",
     "Arendt said evil is often done by ordinary people \"just following orders.\" How can a society train people to think for themselves?"),
    ("beauvoir", "bea", "Simone de Beauvoir", "1908–1986", "France",
     "\"One is not born, but becomes, a woman,\" so freedom means escaping the roles society imposes.",
     "In The Second Sex, Beauvoir argued that society treats men as the norm and women as \"the Other.\" Gender roles are taught, not natural, and they limit everyone's freedom. Real freedom means each person can choose who they become, with the economic independence to do it.",
     "One is not born but becomes a woman.",
     "Beauvoir said gender roles are learned, not natural. Where do you see people learning what's expected of them because of their gender?"),
    ("rawls", "raw", "John Rawls", "1921–2002", "United States",
     "Choose society's rules behind a \"veil of ignorance,\" and allow inequality only if it helps the worst off.",
     "In A Theory of Justice, Rawls asked you to design a society without knowing whether you'd be born rich or poor, healthy or sick. He argued you'd choose equal basic liberties for all and allow inequality only if it improves life for the least advantaged. Fairness, not just freedom, is the test of a just society.",
     "Justice is the first virtue of social institutions.",
     "Try Rawls's veil of ignorance: if you didn't know who you'd be born as, what is one rule you'd want your society to have?"),
    ("king", "kin", "Martin Luther King Jr.", "1929–1968", "United States",
     "Unjust laws must be resisted peacefully, and justice means equal rights and economic fairness for all.",
     "King led the civil rights movement with nonviolent protest, from the Montgomery bus boycott to the March on Washington. In his Letter from Birmingham Jail, he argued that people have a moral duty to disobey unjust laws, openly and peacefully. Later, he campaigned against poverty as part of the same fight for dignity.",
     "Injustice anywhere is a threat to justice everywhere.",
     "King said we have a duty to disobey unjust laws. How do you decide whether a law is unjust? Who gets to decide?"),
    ("nozick", "noz", "Robert Nozick", "1938–2002", "United States",
     "A minimal state protects rights, and taxing people to redistribute wealth is unjust.",
     "In Anarchy, State, and Utopia, Nozick answered Rawls. He argued that if people acquire things fairly and trade freely, the result is just, however unequal it is. Government should be limited to protecting people from force, theft, and fraud.",
     "Taxation of earnings from labor is on a par with forced labor.",
     "Nozick said taxes to help the poor are like forced labor. Rawls disagreed. Who do you side with, and why?"),
]

ERAS = [
    ("ancient", "The ancient world", "Thinkers in China and Greece ask what makes a ruler legitimate and a person good."),
    ("medieval", "Empires and city-states", "Dynasties rise and fall, and writers start studying power as it really works."),
    ("revolutions", "The age of revolutions", "Civil wars and revolutions in England, America, and France put the social contract to the test."),
    ("industrial", "The industrial age", "Factories, slavery, and the fight for the vote raise new questions about freedom and equality."),
    ("modern", "The twentieth century", "World wars, totalitarianism, independence movements, and civil rights reshape ideas of justice."),
]

# id: (born, died, era, [(year, event), ...], connections)
HISTORY = {
    "confucius": (-551, -479, "ancient", [
        ("c. 770 BCE on", "The Zhou kings lose control, and China splits into rival states that fight each other."),
        ("c. 500 BCE", "Confucius serves as an official in the state of Lu, then wanders for years looking for a ruler who will take his advice."),
    ], "His students collected his sayings in the Analects. For centuries, China's civil service exams were based on his teachings."),
    "plato": (-428, -348, "ancient", [
        ("404 BCE", "Athens loses the Peloponnesian War to Sparta, and a group of tyrants briefly takes over the city."),
        ("399 BCE", "An Athenian jury sentences his teacher Socrates to death."),
    ], "He was a student of Socrates and the teacher of Aristotle, and he founded the Academy in Athens in the 380s BCE."),
    "aristotle": (-384, -322, "ancient", [
        ("343 BCE", "He becomes tutor to the young prince who will become Alexander the Great."),
        ("338 BCE", "Philip II of Macedon conquers the independent Greek city-states."),
    ], "He studied with Plato for 20 years, then broke with him by studying how real cities worked instead of designing an ideal one."),
    "ibnkhaldun": (1332, 1406, "medieval", [
        ("1347–1351", "The Black Death sweeps through North Africa and kills both of his parents."),
        ("1400–1401", "Trapped inside Damascus while the conqueror Timur (Tamerlane) besieges it, he is lowered over the city wall by rope to negotiate with him."),
    ], "His Muqaddimah (late 1370s) was almost unknown in Europe until the 1800s. Today he is seen as a forerunner of sociology and economics."),
    "machiavelli": (1469, 1527, "medieval", [
        ("1494", "France invades Italy, and the Medici family is driven out of Florence."),
        ("1512–1513", "The Medici return. Machiavelli is fired, jailed, and tortured, then writes The Prince in exile."),
    ], "He drew his lessons from ancient Roman history. Hobbes and later political realists built on his clear-eyed view of power."),
    "hobbes": (1588, 1679, "revolutions", [
        ("1642–1651", "The English Civil War is fought between the king and Parliament."),
        ("1649", "King Charles I is put on trial and executed. Hobbes publishes Leviathan two years later."),
    ], "Locke and Rousseau both answered his social contract with versions that gave people more rights."),
    "locke": (1632, 1704, "revolutions", [
        ("1688", "The Glorious Revolution replaces King James II with William and Mary."),
        ("1689", "The English Bill of Rights limits the power of the monarchy. Locke's Two Treatises of Government appears the same year."),
    ], "He answered Hobbes. Thomas Jefferson drew on his ideas for the Declaration of Independence in 1776."),
    "montesquieu": (1689, 1755, "revolutions", [
        ("1715", "Louis XIV dies after 72 years of absolute rule over France."),
        ("1729–1731", "Montesquieu visits England and admires how power is balanced between king and Parliament."),
    ], "The framers of the U.S. Constitution quoted his Spirit of the Laws (1748) when they designed three separate branches."),
    "rousseau": (1712, 1778, "revolutions", [
        ("1751 on", "Enlightenment writers in Paris publish the Encyclopédie, challenging church and king."),
        ("1762", "He publishes The Social Contract and Emile. Both books are condemned, banned in France and Geneva, and he has to flee."),
    ], "He answered Hobbes and Locke. French revolutionaries in 1789 turned his \"general will\" into a rallying cry."),
    "burke": (1729, 1797, "revolutions", [
        ("1775–1783", "The American Revolution. Burke urged Britain to make peace with the colonies."),
        ("1789–1790", "The French Revolution begins, and Burke attacks it in Reflections on the Revolution in France."),
    ], "His Reflections provoked famous replies from both Wollstonecraft and Paine."),
    "paine": (1737, 1809, "revolutions", [
        ("1776", "Common Sense becomes a bestseller in the American colonies and builds support for independence."),
        ("1791", "Rights of Man defends the French Revolution against Burke's attack."),
    ], "He was a friend of Jefferson and argued directly with Burke. His Agrarian Justice (1797) is an early proposal for a basic income."),
    "wollstonecraft": (1759, 1797, "revolutions", [
        ("1789", "The French Revolution declares the Rights of Man, but not the rights of women."),
        ("1792", "She publishes A Vindication of the Rights of Woman."),
    ], "She also wrote a reply to Burke (1790). Her daughter, Mary Shelley, wrote Frankenstein."),
    "mill": (1806, 1873, "industrial", [
        ("1832", "Britain's Great Reform Act begins slowly expanding the right to vote."),
        ("1867", "As a member of Parliament, Mill proposes changing the word \"man\" to \"person\" in the Reform Bill, which would give women the vote. The proposal fails."),
    ], "He was raised on Jeremy Bentham's utilitarianism. His thinking on women's rights was shaped by Harriet Taylor Mill."),
    "douglass": (1818, 1895, "industrial", [
        ("1838", "He escapes slavery in Maryland and reaches New York."),
        ("1861–1865", "The Civil War ends slavery in the United States. Douglass pushes for Black soldiers to fight for the Union."),
    ], "He spoke at the 1848 Seneca Falls women's rights convention and held the nation to the promises of the Declaration of Independence."),
    "marx": (1818, 1883, "industrial", [
        ("1840s", "Industrial factories spread across England and Germany, with child labor and long, dangerous workdays."),
        ("1848", "Marx and Friedrich Engels publish The Communist Manifesto. Weeks later, revolutions break out across Europe."),
    ], "He built on the philosopher Hegel and on economists like Adam Smith. His ideas shaped the Russian Revolution of 1917."),
    "gandhi": (1869, 1948, "modern", [
        ("1893–1914", "In South Africa, he organizes Indians against racial discrimination."),
        ("1930", "He leads the Salt March against British taxes. India wins independence in 1947."),
    ], "He was inspired by Tolstoy, and he in turn inspired Martin Luther King Jr."),
    "arendt": (1906, 1975, "modern", [
        ("1933", "Hitler takes power. Arendt, who was Jewish, is briefly arrested and then flees Germany."),
        ("1961", "She reports on the trial of Nazi official Adolf Eichmann and writes about \"the banality of evil.\""),
    ], "Her book The Origins of Totalitarianism (1951) compared Nazi Germany and Stalin's Soviet Union."),
    "beauvoir": (1908, 1986, "modern", [
        ("1940–1944", "Germany occupies France during World War II."),
        ("1944", "Women in France win the right to vote. The Second Sex follows in 1949."),
    ], "She was the lifelong partner of Jean-Paul Sartre. The Second Sex helped launch the women's movement of the 1960s."),
    "rawls": (1921, 2002, "modern", [
        ("1943–1945", "He serves as an infantry soldier in the Pacific during World War II."),
        ("1950s–1960s", "The civil rights movement challenges segregation in the United States."),
    ], "He revived the social contract tradition of Locke and Rousseau. Nozick wrote his best-known book as a reply."),
    "king": (1929, 1968, "modern", [
        ("1955–1956", "He leads the Montgomery bus boycott after Rosa Parks is arrested."),
        ("1963", "He writes the Letter from Birmingham Jail and gives the \"I Have a Dream\" speech."),
    ], "He studied Gandhi's nonviolence and Thoreau, and quoted the Declaration of Independence as Douglass had."),
    "nozick": (1938, 2002, "modern", [
        ("1964–1965", "The United States launches the Great Society programs against poverty."),
        ("1974", "He publishes Anarchy, State, and Utopia, three years after Rawls's A Theory of Justice."),
    ], "He was Rawls's colleague at Harvard and drew on Locke's theory of property."),
}

A = lambda text, strong="", partial="": {"text": text, "strong": strong.split(), "partial": partial.split()}

QUESTIONS = [
    # Human nature and education
    ("Human nature", "Imagine there were no government at all. What would people mostly do?", [
        A("Fight and grab, because everyone is afraid of everyone else", "hobbes machiavelli", "burke ibnkhaldun"),
        A("Mostly get along and respect each other's rights, but argue over disputes", "locke paine", "montesquieu nozick douglass"),
        A("Live simply and peacefully. It's society that makes people greedy", "rousseau", "marx gandhi"),
        A("That can't happen. People only become fully human in a community", "aristotle confucius ibnkhaldun", "plato burke arendt"),
    ]),
    ("Human nature", "What are people like when they are born?", [
        A("Selfish and looking out for themselves", "hobbes machiavelli", "ibnkhaldun"),
        A("A blank slate, shaped by experience and education", "locke wollstonecraft beauvoir", "mill marx ibnkhaldun"),
        A("Naturally good, until society corrupts them", "rousseau", "gandhi paine"),
        A("Able to become good, but only through practice, habit, and guidance", "confucius aristotle", "plato gandhi king"),
    ]),
    ("Human nature", "What shapes who a person becomes the most?", [
        A("Their education", "wollstonecraft plato", "mill confucius douglass king"),
        A("Their economic class and working conditions", "marx", "rousseau"),
        A("Family, tradition, and the customs they grow up in", "burke confucius ibnkhaldun", "aristotle"),
        A("Their own choices and hard work", "nozick douglass beauvoir", "locke arendt gandhi"),
    ]),
    ("Education", "What is the most important thing schools should teach?", [
        A("How to think and reason independently", "wollstonecraft mill arendt", "locke beauvoir paine"),
        A("Good character, respect, and duty to others", "confucius aristotle gandhi", "burke king"),
        A("Reading and knowledge, as the path to freedom", "douglass", "wollstonecraft locke king"),
        A("Preparing each person for their role in society", "plato", "rousseau"),
        A("An understanding of who holds power and why", "marx", "machiavelli beauvoir"),
    ]),
    # Government and authority
    ("Government", "Where does a government get its right to rule?", [
        A("From the consent of the people it governs", "locke paine", "wollstonecraft douglass rawls king gandhi"),
        A("From the wisdom and virtue of its rulers", "plato confucius", "aristotle"),
        A("From its power to keep order and stop chaos", "hobbes machiavelli", "ibnkhaldun"),
        A("From history and traditions built up over generations", "burke", "montesquieu ibnkhaldun"),
        A("From the shared will of the whole community", "rousseau arendt", "marx gandhi"),
    ]),
    ("Government", "Who should make the laws?", [
        A("One strong ruler with final say", "hobbes", "machiavelli ibnkhaldun"),
        A("A small group of the wisest, best-trained people", "plato", "confucius"),
        A("A balanced mix of one leader, a few elites, and the many", "aristotle montesquieu", "burke"),
        A("All the people together, deciding directly", "rousseau arendt gandhi", "marx"),
        A("Representatives elected by the people", "mill paine", "locke wollstonecraft douglass rawls king"),
    ]),
    ("Government", "How should power be arranged?", [
        A("Concentrated in one place, so government can act decisively", "hobbes", "machiavelli"),
        A("Split into branches that check and balance each other", "montesquieu", "locke aristotle arendt paine"),
        A("As limited as possible, only enough to protect rights", "nozick paine", "locke"),
        A("Spread out to small local communities that govern themselves", "gandhi", "arendt rousseau"),
        A("Eventually not needed at all, once classes disappear", "marx", ""),
    ]),
    ("Government", "A government starts abusing its power. What should the people do?", [
        A("Obey anyway, because rebellion is worse than a bad ruler", "hobbes", ""),
        A("Rise up and overthrow it if they have to", "locke paine", "marx wollstonecraft rousseau douglass"),
        A("Refuse to obey through peaceful protest and civil disobedience", "king gandhi", "arendt douglass"),
        A("Push for careful reform that keeps what works", "burke", "montesquieu mill"),
        A("Speak up and urge leaders to act rightly", "confucius", "plato mill"),
    ]),
    ("Government", "What matters most in a leader?", [
        A("Being a good moral example for everyone else", "confucius gandhi", "aristotle plato king"),
        A("Knowledge and wisdom", "plato", "aristotle"),
        A("Getting results and holding on to power, even if it means being feared", "machiavelli", "hobbes ibnkhaldun"),
        A("Being accountable to the people and the law", "locke", "mill montesquieu douglass paine arendt"),
    ]),
    # Rights and freedom
    ("Rights", "Where do people's rights come from?", [
        A("From nature or God. Everyone has them before any government exists", "locke douglass paine king", "wollstonecraft nozick gandhi"),
        A("From agreements people make with each other", "rawls", "hobbes rousseau"),
        A("From belonging to a community and its laws and traditions", "burke arendt", "aristotle montesquieu"),
        A("\"Rights\" mean little until the economy is fair for workers", "marx", ""),
    ]),
    ("Rights", "How much freedom of speech should people have?", [
        A("Almost total. Even wrong ideas help us find the truth", "mill paine arendt", "douglass wollstonecraft king beauvoir"),
        A("Limited whenever speech threatens peace and order", "hobbes", "machiavelli"),
        A("Guided by respect, manners, and tradition", "confucius", "burke gandhi"),
        A("Controlled so it teaches people what is good for the community", "plato", "rousseau"),
    ]),
    ("Freedom", "Should the law stop you from doing something that only hurts yourself?", [
        A("No. If it harms no one else, it's your choice", "mill nozick", "locke beauvoir"),
        A("Yes. Good laws should help people become good", "aristotle plato", "confucius gandhi"),
        A("Sometimes, if it keeps society stable", "hobbes", "burke"),
    ]),
    ("Freedom", "What does it mean to be free?", [
        A("Doing what you want, as long as you don't harm others", "mill", "nozick hobbes"),
        A("Taking part in making the laws you live under", "rousseau arendt", "locke montesquieu paine"),
        A("Not being owned, controlled, or kept down by another person", "douglass wollstonecraft king beauvoir", "gandhi"),
        A("Having the food, time, and resources to develop yourself", "marx", "rawls king"),
    ]),
    # Property, equality, and justice
    ("Property", "What is private property?", [
        A("A natural right. What you make with your own work is yours", "locke nozick", "paine"),
        A("The root of inequality and conflict", "rousseau marx", "plato gandhi"),
        A("Useful, but it should be managed for the good of everyone", "rawls gandhi king", "aristotle mill paine"),
        A("Only safe because a strong government protects it", "hobbes", "burke ibnkhaldun"),
    ]),
    ("Property", "Some people are very rich and others are very poor. Is that okay?", [
        A("Yes, as long as the wealth was earned or traded fairly", "nozick", "locke burke"),
        A("Only if the system also makes life better for the poorest", "rawls king", "mill paine"),
        A("No. The rich get rich by exploiting workers, so the class system must end", "marx", "rousseau beauvoir"),
        A("Extremes are dangerous. A large middle class is best", "aristotle gandhi", "confucius rousseau ibnkhaldun"),
    ]),
    ("Equality", "Should women and men have the same rights and opportunities?", [
        A("Yes: the same education, rights, and place in public life", "wollstonecraft mill douglass beauvoir", "plato hobbes king gandhi arendt"),
        A("No. They have different natural roles", "aristotle rousseau", "confucius burke"),
        A("Inequality between them comes from the economic system and will change with it", "marx", "beauvoir"),
    ]),
    ("Equality", "Are all people equal?", [
        A("Yes. Everyone is born with equal rights", "locke douglass wollstonecraft paine king", "hobbes nozick gandhi beauvoir"),
        A("No. People differ in ability, and society should reflect that", "aristotle plato", "burke"),
        A("Equal in worth, so society should make up for bad luck at birth", "rawls", "mill king"),
        A("Not really, as long as there are rich and poor classes", "marx", "rousseau"),
    ]),
    ("Justice", "What is the main job of government?", [
        A("Keep peace and security", "hobbes", "machiavelli ibnkhaldun"),
        A("Protect life, liberty, and property", "locke nozick paine", "douglass"),
        A("Help citizens live good, virtuous lives", "aristotle confucius", "plato gandhi"),
        A("Make sure things are fair, especially for the worst off", "rawls king", "mill wollstonecraft"),
        A("Give citizens a public space to speak and act together", "arendt", "rousseau aristotle"),
        A("Right now it serves the ruling class, and workers must take it over", "marx", ""),
    ]),
    ("Justice", "A just society is one where...", [
        A("Everyone does the role they are best suited for", "plato", "confucius"),
        A("The rules are ones you'd pick without knowing whether you'd be rich or poor", "rawls", "king"),
        A("Laws produce the greatest happiness for the greatest number", "mill", ""),
        A("People keep what they earn and trade freely", "nozick", "locke paine"),
        A("People of every group are treated with equal dignity", "king gandhi", "douglass beauvoir"),
        A("No one lives off another person's forced labor", "marx douglass", "gandhi"),
    ]),
    ("Change", "How should a society change?", [
        A("Slowly, respecting the wisdom of the past", "burke", "confucius montesquieu"),
        A("Through open debate, speeches, and reform", "mill wollstonecraft douglass", "arendt king"),
        A("Through mass nonviolent protest", "gandhi king", "douglass"),
        A("By revolution, if that's what it takes", "marx paine", "locke rousseau beauvoir"),
        A("As little as possible. Stability matters most", "hobbes", "plato"),
        A("It rises and falls in cycles, whatever people plan", "ibnkhaldun", "machiavelli plato"),
    ]),
]

SECTIONS = [
    ("Human nature and education", 0, 4),
    ("Government and authority", 4, 9),
    ("Rights and freedom", 9, 13),
    ("Property, equality, and justice", 13, 20),
]


def build():
    ids = {t[0] for t in THINKERS}
    for _, q, answers in QUESTIONS:
        for a in answers:
            for t in a["strong"] + a["partial"]:
                assert t in ids, (t, q)
            assert not set(a["strong"]) & set(a["partial"]), q
    thinkers = [dict(zip(["id", "code", "name", "lived", "where", "idea", "rundown", "quote", "challenge"], t)) for t in THINKERS]
    assert set(HISTORY) == ids
    for t in thinkers:
        born, died, era, world, link = HISTORY[t["id"]]
        t.update(born=born, died=died, era=era, world=[{"when": w, "what": e} for w, e in world], link=link)
    eras = [dict(zip(["id", "name", "blurb"], e)) for e in ERAS]
    questions = [{"area": area, "q": q, "answers": answers} for area, q, answers in QUESTIONS]

    # Sources (see sources.py). Each thinker gets a citation for every question they have a position on.
    works = {k: dict(zip(["title", "year", "url", "note"], w)) for k, w in sources.WORKS.items()}
    for (n, tid), (w, loc, url) in sources.CITES.items():
        assert tid in ids and 1 <= n <= len(questions) and w in works, (n, tid, w)
    for t in thinkers:
        tid = t["id"]
        on = {i for i, q in enumerate(questions) for a in q["answers"] if tid in a["strong"] + a["partial"]}
        cites = {}
        for i in sorted(on):
            w, loc, url = sources.CITES.get((i + 1, tid), (sources.MAIN[tid], "", None))
            cites[i] = {"work": w, "loc": loc, "url": url or works[w]["url"], "general": (i + 1, tid) not in sources.CITES}
        t["cites"] = cites
        if t["quote"]:
            w, loc, url = sources.QUOTES[tid]
            t["quoteSrc"] = {"work": w, "loc": loc, "url": url or works[w]["url"]}
        t["read"] = sources.READ[tid]
        t["life"] = [{"label": l, "url": u} for l, u in sources.LIFE[tid]]
    # Lesson rounds (see lessons.py)
    les = []
    for L in lessons.LESSONS:
        assert all(t in ids for t in L["pair"]) and all(1 <= n <= len(questions) for n in L["questions"]), L["id"]
        for n in L["questions"]:
            assert all(any(t in a["strong"] + a["partial"] for a in questions[n - 1]["answers"]) for t in L["pair"]), (L["id"], n)
        les.append({**L, "questions": [n - 1 for n in L["questions"]],
                    "warmup": {**L["warmup"], "options": [{"text": t, "who": w} for t, w in L["warmup"]["options"]]},
                    "excerpts": [dict(zip(["who", "text", "src", "url", "adapted"], e)) for e in L["excerpts"]],
                    "apply": [{**a, "options": [dict(zip(["text", "who", "note"], o)) for o in a["options"]]} for a in L["apply"]]})
    (HERE / "data.json").write_text(json.dumps({"thinkers": thinkers, "eras": eras, "questions": questions, "works": works, "lessons": les}, ensure_ascii=False, indent=1))
    n_pin = sum(not c["general"] for t in thinkers for c in t["cites"].values())
    n_all = sum(len(t["cites"]) for t in thinkers)
    print(f"citations: {n_pin} pinpoint of {n_all} thinker positions; the rest point to the thinker's main work")

    names = {t["id"]: t["name"].split()[-1] if t["id"] not in ("ibnkhaldun", "king", "confucius", "plato", "aristotle", "montesquieu") else t["name"] for t in thinkers}
    names["king"] = "King"
    md = []
    for title, lo, hi in SECTIONS:
        md.append(f"## {title} (Q{lo+1}–{hi})\n")
        for i in range(lo, hi):
            q = questions[i]
            md.append(f"**Q{i+1}. {q['q']}**\n")
            md.append("| Answer | Strong match (2) | Partial match (1) |\n| --- | --- | --- |")
            for a in q["answers"]:
                md.append(f"| {a['text']} | {', '.join(names[t] for t in a['strong'])} | {', '.join(names[t] for t in a['partial'])} |")
            md.append("")
        (HERE / f"key_{lo+1}.md").write_text("\n".join(md).strip() + "\n")
        md = []
    # coverage report
    for t in thinkers:
        mx = sum(max([2 if t["id"] in a["strong"] else 1 if t["id"] in a["partial"] else 0 for a in q["answers"]]) for q in questions)
        print(f"{t['name']:24} max {mx}")


if __name__ == "__main__":
    build()
