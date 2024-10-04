from flask import Flask, render_template, request, redirect, url_for
from datetime import datetime, timedelta

app = Flask(__name__)

# Track daily check-in data and custom alarms for Telegram mini-apps
users_data = {
    "daily_checkin": False,
    "last_checkin": None,
    "custom_alarms": [],
    "telegram_links": [
        {"name": "App 1", "link": "https://t.me/OfficialBananaBot/banana?startapp=referral=ANUGSJ", "checkin_time": 8, "last_checkin": None},
        {"name": "App 2", "link": "https://t.me/blum/app?startapp=ref_RKodRqpqVS", "checkin_time": 4, "last_checkin": None},
        {"name": "App 3", "link": "https://t.me/your_telegram_app3", "checkin_time": 5, "last_checkin": None},
        {"name": "App 4", "link": "https://t.me/your_telegram_app4", "checkin_time": 6, "last_checkin": None},
        {"name": "App 5", "link": "https://t.me/your_telegram_app5", "checkin_time": 7, "last_checkin": None},
        {"name": "App 6", "link": "https://t.me/your_telegram_app6", "checkin_time": 3, "last_checkin": None},
        {"name": "App 7", "link": "https://t.me/your_telegram_app7", "checkin_time": 4, "last_checkin": None},
        {"name": "App 8", "link": "https://t.me/your_telegram_app8", "checkin_time": 5, "last_checkin": None},
        {"name": "App 9", "link": "https://t.me/your_telegram_app9", "checkin_time": 6, "last_checkin": None},
        {"name": "App 10", "link": "https://t.me/your_telegram_app10", "checkin_time": 7, "last_checkin": None},
    ]
}

# Route for the homepage
@app.route('/')
def index():
    # Check if the time is up for each app to collect rewards
    now = datetime.now()
    for app in users_data['telegram_links']:
        if app['last_checkin']:
            next_checkin_time = app['last_checkin'] + timedelta(hours=app['checkin_time'])
            app['can_checkin'] = now >= next_checkin_time
        else:
            app['can_checkin'] = True  # Can check in if never done before

    return render_template('index.html', users_data=users_data)

# Route to handle check-in for individual Telegram apps with custom check-in times
@app.route('/checkin_app/<int:app_id>', methods=['POST'])
def checkin_app(app_id):
    now = datetime.now()

    if 0 <= app_id < len(users_data["telegram_links"]):
        app = users_data["telegram_links"][app_id]
        if app['last_checkin']:
            next_checkin_time = app['last_checkin'] + timedelta(hours=app['checkin_time'])
            if now >= next_checkin_time:
                app['last_checkin'] = now
        else:
            app['last_checkin'] = now  # First-time check-in

        # Redirect to the Telegram link after check-in
        return redirect(app['link'])

    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
