"""Lesson rounds for the Lessons tab. Each one follows one of Douglas's worksheets.

To add a lesson, copy an entry and change it. Question numbers are the main game's (1-20).
Excerpt "adapted" means the worksheet's wording is modernized; the link goes to the original passage.
"""
from sources import WORKS, SE_LEV, LOCKE_ST, SC, WV

SPIRIT = WORKS["spirit_laws"][2]
EMILE5 = "https://www.online-literature.com/rousseau/emile/5/"
TALLEYRAND = "https://americanliterature.com/author/mary-wollstonecraft/book/a-vindication-of-the-rights-of-woman/letter-to-perigord"

LESSONS = [
    {
        "id": "1.14",
        "title": "Hobbes & Locke: How Should Society Be Governed?",
        "big": "What is the best way to create a better society for all?",
        "pair": ["hobbes", "locke"],
        "warmup": {
            "prompt": "Imagine that your community is creating a new government. Which of these ideas would you support most?",
            "options": [
                ("A strong leader who makes decisions and keeps everyone safe.", "hobbes"),
                ("A government that protects people's rights and listens to their opinions.", "locke"),
                ("A government that balances strong leadership with individual freedom.", "both"),
            ],
            "think": "What is more important for a successful society: keeping people safe or protecting their freedom? Can a government do both?",
        },
        "questions": [1, 2, 5, 7, 8, 10, 18],
        "context": {
            "hobbes": ("Civil war, violence, and the execution of King Charles I (1649)", "A strong government was necessary for peace"),
            "locke": ("The Glorious Revolution (1688) and limits on the monarchy", "Government should protect rights and have limited power"),
        },
        "excerpts": [
            ("hobbes", "And the life of man, solitary, poore, nasty, brutish, and short.", "Leviathan, ch. 13", SE_LEV.format(13), False),
            ("hobbes", "By giving all strength onto this one man, that by terror thereof, he is enabled to establish Peace at home, and defense against their enemies abroad.", "Leviathan, ch. 17", SE_LEV.format(17), True),
            ("locke", "no one ought to harm another in his Life, Health, Liberty, or Possessions", "Second Treatise of Government, ch. II, §6", LOCKE_ST.format(2), False),
            ("locke", "When legislators try to gain or give someone else absolute power over lives, liberties, and property of the people, they abuse the power which the people had put into their hands. It is then the privilege of the people to establish a new legislature to provide for their safety and security.", "Second Treatise of Government, ch. XIX, §222", LOCKE_ST.format(19), True),
        ],
        "apply": [],
        "claim": "Who had a better plan for improving society? Which thinker do you agree with more: Hobbes or Locke? Explain your choice using at least TWO specific ideas from the reading.",
    },
    {
        "id": "1.15",
        "title": "Rousseau & Montesquieu: How Should Society Be Governed?",
        "big": "How should governments protect freedom and prevent the abuse of power?",
        "pair": ["rousseau", "montesquieu"],
        "warmup": {
            "prompt": "Imagine your community is creating a new government. Everyone agrees that freedom is important, but people have different ideas about how to protect it. Which of these ideas would you support most?",
            "options": [
                ("Citizens vote directly on laws and help make decisions for their community.", "rousseau"),
                ("Government power is divided among different branches so no one person or group becomes too powerful.", "montesquieu"),
                ("Citizens have a voice in making laws, and government leaders have limits on their power.", "both"),
            ],
            "think": "What is more important for protecting freedom: giving people a voice in making laws or limiting the power of government leaders? Can a government do both?",
        },
        "questions": [1, 5, 6, 7, 8, 13, 20],
        "context": {
            "rousseau": ("Absolute monarchy and social inequality in France", "People should have a voice in making laws that serve the common good"),
            "montesquieu": ("Absolute monarchy in France under Louis XIV, and a limited monarchy in England where Parliament shared power", "Government power should be divided among different branches so no one person or group becomes too powerful"),
        },
        "excerpts": [
            ("rousseau", "Man is born free; and everywhere he is in chains.", "The Social Contract, Book I, ch. 1", SC.format(1), False),
            ("rousseau", "No man has any natural authority over his fellow men.", "The Social Contract, Book I, ch. 4", SC.format(1), True),
            ("rousseau", "There is often a great deal of difference between the will of all and the general will; the latter considers only the common interest, while the former takes private interest into account.", "The Social Contract, Book II, ch. 3", SC.format(2), False),
            ("montesquieu", "When the legislative and executive powers are united in the same person, or in the same body of magistrates, there can be no liberty; because apprehensions may arise, lest the same monarch or senate should enact tyrannical laws, to execute them in a tyrannical manner.", "The Spirit of the Laws, Book XI, ch. 6", SPIRIT, False),
        ],
        "apply": [
            {
                "title": "Direct vs. representative democracy",
                "scenario": "The Hamilton-Wenham Regional High School student government is considering a change to the school dress code policy. Students must decide whether hats and hoodies should be allowed in classrooms.",
                "options": [
                    ("Option A: Every student votes directly on the dress code change.", "rousseau", "Rousseau would back this. He thought citizens should make laws themselves, and that representatives can't stand in for the general will (The Social Contract, Book III, ch. 15)."),
                    ("Option B: Students elect representatives who gather input and decide for the student body.", "", "Rousseau would object to this. Montesquieu would be more comfortable with it, since he thought most people should choose representatives rather than vote on every law."),
                ],
            },
            {
                "title": "Who should have the power?",
                "scenario": "Under a proposed system, the student council president would create all school policies, enforce them, and decide whether students have violated them and what the punishment is.",
                "options": [
                    ("Keep it. One person deciding everything is faster and more efficient.", "", "Montesquieu would reject this: when the same person makes, enforces, and judges the rules, \"there can be no liberty.\""),
                    ("Split it. A council writes policies, the president enforces them, and a student court judges violations.", "montesquieu", "This is Montesquieu's separation of powers: legislative, executive, and judicial."),
                ],
            },
        ],
        "claim": "Rousseau believed that freedom depended on people having a voice in making laws. Montesquieu believed that freedom depended on limiting government power. Whose plan protects freedom better? Use at least TWO specific ideas from the reading.",
    },
    {
        "id": "2.2",
        "title": "Mary Wollstonecraft and the Rights of Woman",
        "big": "To what extent did Mary Wollstonecraft challenge ideas about the rights of women in 18th century Europe?",
        "pair": ["wollstonecraft", "rousseau"],
        "pairNote": "Wollstonecraft argued directly against Rousseau in chapter 5 of A Vindication of the Rights of Woman, so this round puts the two side by side.",
        "warmup": {
            "prompt": "In 18th century Europe, most girls were taught only to run a home. What should girls' education be?",
            "options": [
                ("The same as boys': reason, knowledge, and the ability to think for yourself.", "wollstonecraft"),
                ("Different from boys', built around pleasing and caring for a husband and family.", "rousseau"),
                ("Some of both, depending on the person.", "both"),
            ],
            "think": "Why might a society decide that girls and boys need different educations? Who benefits from that decision?",
        },
        "questions": [2, 3, 4, 13, 16, 17],
        "context": {
            "wollstonecraft": ("Women shut out of schooling and public life, and Talleyrand's 1791 report to the French National Assembly proposing only a domestic education for girls", "Women have the same reason and natural rights as men and deserve the same education"),
            "rousseau": ("A society he thought was corrupted by wealth, fashion, and inequality", "Boys should be raised for freedom, but a girl's education should be planned around pleasing and serving men (Emile, Book V)"),
        },
        "excerpts": [
            ("wollstonecraft", "...if it be fully proved that reason calls for this respect, and loudly demands JUSTICE for one half of the human race.", "A Vindication of the Rights of Woman, letter to Talleyrand", TALLEYRAND, False),
            ("wollstonecraft", "I do not wish them to have power over men; but over themselves.", "A Vindication of the Rights of Woman, ch. 4", WV.format(4), False),
            ("rousseau", "A woman's education must therefore be planned in relation to man.", "Emile, Book V (Foxley translation)", EMILE5, False),
            ("wollstonecraft", "I shall begin with Rousseau, and give a sketch of the character of women in his own words...", "A Vindication of the Rights of Woman, ch. 5, section 1", WV.format(5), False),
        ],
        "apply": [],
        "claim": "To what extent did Mary Wollstonecraft challenge ideas about the rights of women in 18th century Europe? Use at least TWO specific ideas, and explain which of Rousseau's ideas she was answering.",
    },
]
