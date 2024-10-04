# app.py
from flask import Flask, render_template, request, redirect, url_for
from datetime import datetime

app = Flask(__name__)

# Sample data for Telegram channels/bots
channels = [
    {"name": "Airdrop Channel 1", "url": "https://t.me/airdropchannel1"},
    {"name": "Airdrop Channel 2", "url": "https://t.me/airdropchannel2"},
    {"name": "Airdrop Channel 3", "url": "https://t.me/airdropchannel3"},
]

# Sample posts for carousel
posts = [
    {'image': 'slide1.jpg', 'caption': 'Amazing Airdrop Opportunity!'},
    {'image': 'slide2.jpg', 'caption': 'Join our Telegram Channel!'},
    {'image': 'slide3.jpg', 'caption': 'Exclusive Deals Awaiting You!'},
]

# Dictionary to store check-in status
checkin_status = {}

@app.route('/')
def index():
    today = datetime.now().strftime('%Y-%m-%d')
    return render_template('index.html', channels=channels, today=today, checkin_status=checkin_status, posts=posts)


@app.route('/')
def test():
    today = datetime.now().strftime('%Y-%m-%d')
    return render_template('test.html')

@app.route('/checkin/<channel_name>')
def checkin(channel_name):
    today = datetime.now().strftime('%Y-%m-%d')
    checkin_status[channel_name] = today
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
