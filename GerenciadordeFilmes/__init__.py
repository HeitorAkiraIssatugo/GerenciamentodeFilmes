from flask import Flask, session, redirect, url_for, request

def create_app():
    app = Flask(__name__)
    app.secret_key = 'sua_chave_secreta_super_segura_para_desenvolvimento'

    @app.before_request
    def check_auth():
        public_endpoints = ['auth.login', 'static']
        if request.endpoint not in public_endpoints and 'user' not in session:
            return redirect(url_for('auth.login'))

    @app.route('/')
    def root():
        if 'user' in session:
            return redirect(url_for('auth.index'))
        return redirect(url_for('auth.login'))

    # Correção da importação usando o caminho a partir da pasta app
    from app.controllers.auth_controller import auth_bp
    app.register_blueprint(auth_bp)

    return app