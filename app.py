import json

from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)
app.secret_key = 'your_secret_key'


def load_questions():
    with open('data/questions.json') as f:
        return json.load(f)


questions = load_questions()


@app.route('/')
def index():
    session['current_question'] = 0
    session['user_answers'] = []
    return render_template('index.html')


@app.route('/quiz', methods=['GET', 'POST'])
def quiz():
    if 'current_question' not in session or 'user_answers' not in session:
        return redirect(url_for('index'))

    if request.method == 'POST':
        action = request.form.get('action')
        current_question = session.get('current_question', 0)
        user_answers = session.get('user_answers', [])
        question_type = questions[current_question]['type']

        if question_type == 'single':
            user_answers.append(request.form.get('answer'))
        elif question_type == 'multi':
            user_answers.append(request.form.getlist('answer'))

        session['user_answers'] = user_answers

        if action == 'next':
            session['current_question'] = current_question + 1
            if current_question + 1 >= len(questions):
                return redirect(url_for('result'))
        elif action == 'submit':
            return redirect(url_for('result'))

    current_question = session.get('current_question', 0)
    question = questions[current_question]
    return render_template('quiz.html', question=question, current_question=current_question,
                           total_questions=len(questions))


@app.route('/result')
def result():
    if 'current_question' not in session or 'user_answers' not in session:
        return redirect(url_for('index'))

    user_answers = session.get('user_answers', [])
    score = 0
    total_answered = len(user_answers)
    for i, question in enumerate(questions[:total_answered]):
        if question['type'] == 'single':
            if question['answer'] == user_answers[i]:
                score += 1
        elif question['type'] == 'multi':
            if set(question['answer']) == set(user_answers[i]):
                score += 1

    percentage_score = (score / total_answered) * 100 if total_answered > 0 else 0
    return render_template('result.html', score=percentage_score, user_answers=user_answers, questions=questions,
                           total_answered=total_answered, zip=zip)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
