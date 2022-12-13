import sys
from flask import Flask
from flask import render_template
from flask_frozen import Freezer
from requests import session

FREEZER_DESTINATION = 'docs'
URL_EASYCHAIR_SUBMISSION = 'https://easychair.org/conferences/?conf=ieeeichi2022'

app = Flask(__name__)
app.config.from_object(__name__)
freezer = Freezer(app)

# predefined session abbr
session_list = [
    'k-1', 'k-2', 'k-3', 'k-4'  # keynote
    'a-1', 'a-2', 'a-3', 'a-4', 'a-5', 'a-6', 'a-7', # analytics
    'h-1', 'h-2', 'h-3', # human factor
    's-1', 's-2', 's-3', # system
    'w-1', 'w-2', 'w-3', 'w-4',     # workshop
    'd-1', 'd-2', 'd-3', 'd-4', # doctoral consortium
    't-1', 't-2', 't-3', # tutorial
    'i-1', 'i-2',        # industry 
    'p-1', 'p-2',        # poster
]

session_codename = {
    'k': 'Keynote',
    'a': 'Analytics Track Session',
    's': 'Systems Track Session',
    'h': 'Human Factors Track Session',
    'i': 'Industry Track Session'
}

@app.route("/")
def index():
    return render_template('index.html')


@app.route("/call_for_sponsors.html")
def call_for_sponsors():
    return render_template('call_for_sponsors.html')


@app.route("/call_for_contributions.html")
def call_for_contributions():
    return render_template('call_for_contributions.html')


@app.route("/call_for_papers.html")
def call_for_papers():
    return render_template('call_for_papers.html')


@app.route("/call_for_posters_and_demos.html")
def call_for_posters_and_demos():
    return render_template('call_for_posters_and_demos.html')


@app.route("/call_for_workshops.html")
def call_for_workshops():
    return render_template('call_for_workshops.html')


@app.route("/call_for_doctorial_consortium.html")
def call_for_doctorial_consortium():
    return render_template('call_for_doctorial_consortium.html')


@app.route("/call_for_industry_track.html")
def call_for_industry_track():
    return render_template('call_for_industry_track.html')


@app.route("/call_for_tutorials.html")
def call_for_tutorials():
    return render_template('call_for_tutorials.html')


@app.route("/attending.html")
def attending():
    return render_template('attending.html')


@app.route("/attendance_grant.html")
def attendance_grant():
    return render_template('attendance_grant.html')


@app.route("/venue_and_logistics.html")
def venue_and_logistics():
    return render_template('venue_and_logistics.html')


@app.route("/workshops.html")
def workshops():
    return render_template('workshops.html')


@app.route("/cme.html")
def cme():
    return render_template('cme.html')


@app.route("/presenter_guidelines.html")
def presenter_guidelines():
    return render_template('presenter_guidelines.html')


@app.route('/conference_materials.html')
def conference_materials():
    return render_template('conference_materials.html')


@app.route('/program_cmeeform.html')
def program_cmeeform():
    # get the details of sessions
    session_dict = get_session_dict()

    dates = [
        'Sunday, June 12',
        'Monday, June 13',
        'Tuesday, June 14'
    ]
    ss = [
        ['k-1', 'a-1', 'a-2', 'a-3', 'k-2', 'a-4', 's-1', 'h-1'],
        ['k-3', 'a-5', 's-2', 'h-2', 'a-6', 'a-7', 'h-3'],
        ['k-4', 'i-1']
    ]

    ds = list(zip(dates, ss))

    return render_template(
        'program_cmeeform.html',
        ds=ds,
        show_calendar=True,
        show_details=False,
        session_dict=session_dict,
        session_codename=session_codename
    )


@app.route('/program_sessionchair.html')
def program_sessionchair():
    # get the details of sessions
    session_dict = get_session_dict()

    dates = [
        'Sunday, June 12',
        'Monday, June 13',
        'Tuesday, June 14'
    ]
    ss = [
        ['a-1', 'a-2', 'a-3', 'a-4', 's-1', 'h-1'],
        ['a-5', 's-2', 'h-2', 'a-6', 'a-7', 'h-3'],
        ['i-1']
    ]

    ds = list(zip(dates, ss))

    return render_template(
        'program_sessionchair.html',
        ds=ds,
        show_calendar=True,
        show_details=False,
        session_dict=session_dict,
        session_codename=session_codename
    )


@app.route("/program.html")
def program():
    # get the details of sessions
    session_dict = get_session_dict()

    return render_template(
        'program.html',
        show_calendar=True,
        show_details=False,
        session_dict=session_dict
    )


@app.route("/program.test.html")
def program_test():
    return program()


@app.route('/program_text.html')
def program_text():
    # get the details of sessions
    session_dict = get_session_dict()

    return render_template(
        'program.html',
        show_calendar=False,
        show_details=True,
        session_dict=session_dict
    )


@app.route("/keynotes.html")
def keynotes():
    return render_template('keynotes.html')


@app.route("/awards.html")
def awards():
    return render_template('awards.html')


@app.route("/committees.html")
def committees():
    return render_template('committees.html')


def get_session_dict():
    '''
    Get session_dict for rendering program
    '''
    import csv
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

    return session_dict


if __name__ == '__main__':
    if len(sys.argv) > 1 and sys.argv[1] == "build":
        freezer.freeze()
        print('* built static version by Flask-Freezer')
    else:
        app.run(host='0.0.0.0', debug=True)