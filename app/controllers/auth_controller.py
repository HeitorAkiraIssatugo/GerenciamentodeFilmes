from flask import Blueprint, render_template, request, redirect, url_for, session, flash
from app.models.user_model import User
from app.utils import login_required  # Importando o wrapper

auth_bp = Blueprint('auth', __name__, template_folder='../views')

@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    if 'user' in session:
        return redirect(url_for('auth.index'))

    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        user = User.authenticate(username, password)
        if user:
            session['user'] = user.username
            flash('Login realizado com sucesso!', 'success')
            return redirect(url_for('auth.index'))
        else:
            flash('Usuário ou senha inválidos!', 'danger')

    return render_template('login.html')

@auth_bp.route('/index')
@login_required  # Usando o wrapper para proteger esta rota
def index():
    return render_template('index.html', username=session.get('user'))

@auth_bp.route('/logout')
def logout():
    session.pop('user', None)
    flash('Você saiu da sua conta.', 'info')
    return redirect(url_for('auth.login'))