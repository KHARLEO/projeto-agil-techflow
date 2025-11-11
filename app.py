# app.py
import os
from flask import Flask, render_template, redirect, url_for, flash, request
from models import db, User
from forms import RegisterForm, LoginForm
from flask_login import LoginManager, login_user, logout_user, login_required, current_user

def create_app():
    app = Flask(__name__, instance_relative_config=True)
    app.config['SECRET_KEY'] = 'devkey-change-me'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(app.instance_path, 'app.db')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)

    login_manager = LoginManager()
    login_manager.login_view = 'login'
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))

    @app.route('/')
    def index():
        return render_template('index.html')

    @app.route('/register', methods=['GET', 'POST'])
    def register():
        form = RegisterForm()
        if form.validate_on_submit():
            # check if email or username exists
            if User.query.filter((User.email == form.email.data) | (User.username == form.username.data)).first():
                flash('Email ou username já cadastrado.', 'danger')
                return render_template('register.html', form=form)

            user = User(username=form.username.data, email=form.email.data)
            user.set_password(form.password.data)
            db.session.add(user)
            db.session.commit()
            flash('Conta criada com sucesso! Faça login.', 'success')
            return redirect(url_for('login'))
        return render_template('register.html', form=form)

    @app.route('/login', methods=['GET', 'POST'])
    def login():
        form = LoginForm()
        if form.validate_on_submit():
            user = User.query.filter_by(email=form.email.data).first()
            if user and user.check_password(form.password.data):
                login_user(user)
                flash('Logado com sucesso.', 'success')
                next_page = request.args.get('next')
                return redirect(next_page or url_for('profile'))
            flash('Credenciais inválidas.', 'danger')
        return render_template('login.html', form=form)

    @app.route('/logout')
    @login_required
    def logout():
        logout_user()
        flash('Você saiu.', 'info')
        return redirect(url_for('index'))

    @app.route('/profile')
    @login_required
    def profile():
        return render_template('profile.html', user=current_user)

    # leitura de todos usuarios (admin-simples)
    @app.route('/users')
    @login_required
    def list_users():
        users = User.query.all()
        return render_template('users.html', users=users)

    @app.route('/user/<int:id>/edit', methods=['GET', 'POST'])
    @login_required
    def edit_user(id):
        user = User.query.get_or_404(id)
        # só o proprio usuário pode editar a si mesmo para simplicidade
        if current_user.id != user.id:
            flash('Sem permissão para editar este usuário.', 'danger')
            return redirect(url_for('list_users'))

        # preencher form manualmente (sem WTForms para simplicidade)
        if request.method == 'POST':
            username = request.form.get('username')
            email = request.form.get('email')
            if username:
                user.username = username
            if email:
                user.email = email
            db.session.commit()
            flash('Usuário atualizado.', 'success')
            return redirect(url_for('profile'))

        return render_template('edit_user.html', user=user)

    @app.route('/user/<int:id>/delete', methods=['POST'])
    @login_required
    def delete_user(id):
        user = User.query.get_or_404(id)
        if current_user.id != user.id:
            flash('Sem permissão para deletar este usuário.', 'danger')
            return redirect(url_for('list_users'))
        db.session.delete(user)
        db.session.commit()
        flash('Conta deletada.', 'info')
        return redirect(url_for('index'))
    
    @app.route('/reset-password', methods=['GET','POST'])
    def reset_password():
        if request.method == 'POST':
            email = request.form.get('email')
            user = User.query.filter_by(email=email).first()
            if not user:
                flash('Nenhum usuário com esse email.', 'danger')
                return render_template('reset_password.html')
            # Simulação: em vez de enviar email, mostramos mensagem
            flash(f'Instruções enviadas para {email} (simulado).', 'info')
            return redirect(url_for('login'))
        return render_template('reset_password.html')


    return app

# CLI helper to run flask with python -m flask
from pathlib import Path
if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)


