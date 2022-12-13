import csv

# load the information first
session_dict = {}
with open('presentations.csv', newline='', encoding='utf-8-sig') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        s_code = row['Code']
        # s_name = row['Session']
        p_title = row['Title']
        # p_authors = row['Authors']

        # print(row)

        if s_code is None or s_code == '':
            continue

        if s_code not in session_dict:
            # it's a new session
            session_dict[s_code] = []

        # put this paper into session_dict
        session_dict[s_code].append(
            dict(row)
        )

# output the content
session_codes = [
    'a-1', 'a-2', 'a-3', 'a-4', 'a-5', 'a-6', 'a-7', # analytics
    's-1', 's-2', 's-3', # system
    'h-1', 'h-2', 'h-3', # human factor
    'i-1', 'i-2',        # industry 
    'd-1', 'd-2', 'd-3', # doctoral consortium
    'p-1', 'p-2',        # poster
    't-1', 't-2', 't-3', # tutorials
    'w-1', 'w-2', 'w-3', 'w-4', # workshops
]
# transate the code 
session_id2name = {
    'a': 'Analytics',
    's': 'Systems',
    'h': 'Human Factors',
    'i': 'Industry',
    'd': 'Doctoral Consortium',
    'p': 'Poster and Demo',
    't': 'Tutorial',
    'w': 'Workshop',
}

f = open('TableOfContents22.txt', 'w')

for s_code in session_codes:
    # if not in csv, just skip
    if s_code not in session_dict: continue

    # get the parts
    s_id = s_code[0]
    s_nb = s_code[2]

    # get the session detail name from a record
    s_tt = session_dict[s_code][0]['Session']

    # great! a new session, get its title
    if s_id in 'ahswt':
        session_title = "%s %s - %s" % (
            session_id2name[s_id],
            s_nb,
            s_tt
        )
    else:
        session_title = "%s" % (
            session_id2name[s_id]
        )

    f.write(session_title + '\n')

    # now, let's output the content of this session
    for d in session_dict[s_code]:
        line = "%s, %s" % (
            d['Title'],
            d['Authors']
        )
        f.write('\t' + line + '\n')

    # blanks
    f.write('\n\n')

f.close()
print('* created the toc file!')