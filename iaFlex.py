from flask import Flask, render_template, request, redirect, url_for, flash
from TargetJournee import TargetJournee  # Assurez-vous que cette fonction existe et est importée correctement


app = Flask(__name__)

# Variable globale pour stocker les données du formulaire
donneesFormulaireDailyTask = {}
PromptValue = ""

@app.route('/', methods=['GET', 'POST'])
def index():
    prompt = ""
    if request.method == 'POST':
        # Récupérer les données du formulaire et les stocker dans la variable globale
        donneesFormulaireDailyTask['clientName'] = client = request.form['clientName']
        donneesFormulaireDailyTask['langue'] = language = request.form['language']
        donneesFormulaireDailyTask['contexte'] = user_targets = request.form['context']
        donneesFormulaireDailyTask['objectifs'] = targets = request.form['objectives']

        prompt = TargetJournee(client, targets, language, user_targets)     
    
    return render_template('index.html', prompt=prompt)


@app.route('/vote', methods=['GET', 'POST'])
def vote():
    if request.method == 'POST':
        selected_interest = request.form['interesse']
        # flash("Merci pour votre avis!", "success")  # Utilisation de "success" comme catégorie
        print("la valeur choisie est: " + selected_interest)

    return redirect(url_for('index')) 
    
    



@app.route('/login')
def login():

    return render_template('login.html')

if __name__ == '__main__':
    app.run()