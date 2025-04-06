from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)


songs = [
    {
        "title": "Chillhop Essentials",
        "embed_url": "https://www.youtube.com/embed/HuFYqnbVbzY?si=k0u6Ai6k30iY_2gM",
        "theme": "day"
    },
    {
        "title": "Lo-Fi Rainy Vibes",
        "embed_url": "https://www.youtube.com/embed/P6Segk8cr-c?si=vKzrOPvsPy44JEwL",
        "theme": "rain"
    },
    {
        "title": "Night Time Lo-Fi",
        "embed_url": "https://www.youtube.com/embed/DOQ-5KwritU?si=544JDenw5XKIX_oL",
        "theme": "night"
    },
    {
        "title": "Study Vibes",
        "embed_url": "https://www.youtube.com/embed/jfKfPfyJRdk",
        "theme": "study"
    }
]

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/vibe')
def vibe():
    index = request.args.get('index', default=0, type=int)
    song = songs[index % len(songs)]
    next_index = (index + 1) % len(songs)
    return render_template('vibe.html', song=song, next_index=next_index)


@app.route('/feedback', methods=['GET', 'POST'])
def feedback():
    if request.method == 'POST':
       
        name = request.form.get('name')
        satisfaction = request.form.get('satisfaction')
        comments = request.form.get('comments')
        
        print(f"Name: {name}, Satisfaction: {satisfaction}, Comments: {comments}")
        return redirect(url_for('thankyou', name=name))

    return render_template('feedback.html')

@app.route('/thankyou', methods=['GET'])
def thankyou():
    name = request.args.get('name')

    return render_template('feedback_thank_you.html', name=name)

if __name__ == '__main__':
    app.run(debug=True)
