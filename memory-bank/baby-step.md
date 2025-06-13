# Langkah 1: Setup Dasar Aplikasi Flask dan Struktur Web

**Tujuan:** Membuat struktur file dan folder dasar untuk aplikasi web Flask serta mengimplementasikan server dasar yang dapat diakses melalui browser.

**Petunjuk untuk AI Koding:**

1.  **Buat Struktur Folder dan File:**
    Buat struktur direktori dan file berikut di root proyek:

    ```
    .
    ├── .gitignore
    ├── todo_app/
    │   ├── app.py
    │   ├── models.py
    │   ├── static/
    │   │   ├── css/
    │   │   │   └── style.css
    │   │   └── js/
    │   │       └── main.js
    │   └── templates/
    │       ├── base.html
    │       └── index.html
    └── requirements.txt
    ```

2.  **Isi File `.gitignore`:**
    Masukkan konten standar Python dan web development ke dalam file `.gitignore`:

    ```gitignore
    # Byte-compiled / optimized / DLL files
    __pycache__/
    *.pyc
    *.pyo
    *.pyd

    # Environments
    .env
    .venv
    env/
    venv/
    ENV/
    VENV/

    # Database
    *.db
    *.sqlite
    *.sqlite3
    database.db

    # Flask
    instance/
    .webassets-cache

    # Distribution / packaging
    .Python
    build/
    develop-eggs/
    dist/
    downloads/
    eggs/
    .eggs/
    lib/
    lib64/
    parts/
    sdist/
    var/
    wheels/
    *.egg-info/
    .installed.cfg
    *.egg

    # IDE
    .vscode/
    .idea/
    *.swp
    *.swo
    *~

    # OS
    .DS_Store
    Thumbs.db
    ```

3.  **Isi File `requirements.txt`:**
    Tambahkan dependencies yang diperlukan untuk aplikasi Flask:

    ```
    Flask==2.3.3
    Flask-SQLAlchemy==3.0.5
    Flask-WTF==1.1.1
    WTForms==3.0.1
    SQLAlchemy==2.0.21
    Werkzeug==2.3.7
    ```

4.  **Isi File `todo_app/models.py`:**
    Buat model database untuk tugas menggunakan SQLAlchemy:

    ```python
    from flask_sqlalchemy import SQLAlchemy
    from datetime import datetime

    db = SQLAlchemy()

    class Task(db.Model):
        id = db.Column(db.Integer, primary_key=True)
        description = db.Column(db.String(200), nullable=False)
        completed = db.Column(db.Boolean, default=False, nullable=False)
        created_at = db.Column(db.DateTime, default=datetime.utcnow)
        updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

        def __repr__(self):
            return f'<Task {self.id}: {self.description}>'

        def to_dict(self):
            return {
                'id': self.id,
                'description': self.description,
                'completed': self.completed,
                'created_at': self.created_at.isoformat(),
                'updated_at': self.updated_at.isoformat()
            }
    ```

5.  **Isi File `todo_app/app.py`:**
    Tulis kode Flask berikut untuk aplikasi web utama:

    ```python
    from flask import Flask, render_template, request, jsonify, redirect, url_for
    from models import db, Task
    import os

    def create_app():
        app = Flask(__name__)
        
        # Konfigurasi database
        basedir = os.path.abspath(os.path.dirname(__file__))
        app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{os.path.join(basedir, "database.db")}'
        app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
        app.config['SECRET_KEY'] = 'your-secret-key-here'  # Ganti dengan secret key yang aman
        
        # Inisialisasi database
        db.init_app(app)
        
        # Route utama
        @app.route('/')
        def index():
            tasks = Task.query.order_by(Task.created_at.desc()).all()
            return render_template('index.html', tasks=tasks)
        
        # Route untuk menambah tugas
        @app.route('/add_task', methods=['POST'])
        def add_task():
            description = request.form.get('description')
            if description:
                new_task = Task(description=description)
                db.session.add(new_task)
                db.session.commit()
            return redirect(url_for('index'))
        
        # Route untuk toggle status tugas
        @app.route('/toggle_task/<int:task_id>', methods=['POST'])
        def toggle_task(task_id):
            task = Task.query.get_or_404(task_id)
            task.completed = not task.completed
            db.session.commit()
            return jsonify({'success': True, 'completed': task.completed})
        
        # Route untuk menghapus tugas
        @app.route('/delete_task/<int:task_id>', methods=['POST'])
        def delete_task(task_id):
            task = Task.query.get_or_404(task_id)
            db.session.delete(task)
            db.session.commit()
            return jsonify({'success': True})
        
        # Membuat tabel database
        with app.app_context():
            db.create_all()
        
        return app

    if __name__ == '__main__':
        app = create_app()
        app.run(debug=True, host='0.0.0.0', port=5000)
    ```

6.  **Isi File `todo_app/templates/base.html`:**
    Buat template dasar HTML:

    ```html
    <!DOCTYPE html>
    <html lang="id">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>{% block title %}To-Do List App{% endblock %}</title>
        <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css" rel="stylesheet">
        <link href="{{ url_for('static', filename='css/style.css') }}" rel="stylesheet">
    </head>
    <body>
        <div class="container mt-4">
            {% block content %}{% endblock %}
        </div>
        
        <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/js/bootstrap.bundle.min.js"></script>
        <script src="{{ url_for('static', filename='js/main.js') }}"></script>
    </body>
    </html>
    ```

7.  **Isi File `todo_app/templates/index.html`:**
    Buat halaman utama aplikasi:

    ```html
    {% extends "base.html" %}

    {% block title %}To-Do List - Kelola Tugas Anda{% endblock %}

    {% block content %}
    <div class="row justify-content-center">
        <div class="col-md-8">
            <h1 class="text-center mb-4">📝 To-Do List App</h1>
            
            <!-- Form untuk menambah tugas -->
            <div class="card mb-4">
                <div class="card-body">
                    <form action="{{ url_for('add_task') }}" method="POST" class="d-flex">
                        <input type="text" name="description" class="form-control me-2" 
                               placeholder="Masukkan tugas baru..." required>
                        <button type="submit" class="btn btn-primary">Tambah</button>
                    </form>
                </div>
            </div>
            
            <!-- Daftar tugas -->
            <div class="card">
                <div class="card-header">
                    <h5 class="mb-0">Daftar Tugas ({{ tasks|length }})</h5>
                </div>
                <div class="card-body">
                    {% if tasks %}
                        <div id="task-list">
                            {% for task in tasks %}
                            <div class="task-item d-flex align-items-center mb-2 p-2 border rounded" data-task-id="{{ task.id }}">
                                <input type="checkbox" class="form-check-input me-3 task-checkbox" 
                                       {% if task.completed %}checked{% endif %}>
                                <span class="task-description flex-grow-1 {% if task.completed %}text-decoration-line-through text-muted{% endif %}">
                                    {{ task.description }}
                                </span>
                                <small class="text-muted me-3">{{ task.created_at.strftime('%d/%m/%Y %H:%M') }}</small>
                                <button class="btn btn-sm btn-outline-danger delete-task">🗑️</button>
                            </div>
                            {% endfor %}
                        </div>
                    {% else %}
                        <div class="text-center text-muted py-4">
                            <p>Belum ada tugas. Tambahkan tugas pertama Anda!</p>
                        </div>
                    {% endif %}
                </div>
            </div>
        </div>
    </div>
    {% endblock %}
    ```

8.  **Isi File `todo_app/static/css/style.css`:**
    Tambahkan styling custom:

    ```css
    body {
        background-color: #f8f9fa;
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    }

    .task-item {
        transition: all 0.3s ease;
        background-color: white;
    }

    .task-item:hover {
        box-shadow: 0 2px 8px rgba(0,0,0,0.1);
        transform: translateY(-1px);
    }

    .task-checkbox {
        transform: scale(1.2);
    }

    .card {
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
        border: none;
    }

    .btn-primary {
        background-color: #007bff;
        border-color: #007bff;
    }

    .btn-primary:hover {
        background-color: #0056b3;
        border-color: #0056b3;
    }

    h1 {
        color: #343a40;
        font-weight: 600;
    }
    ```

9.  **Isi File `todo_app/static/js/main.js`:**
    Tambahkan JavaScript untuk interaktivitas:

    ```javascript
    document.addEventListener('DOMContentLoaded', function() {
        // Handle checkbox toggle
        document.querySelectorAll('.task-checkbox').forEach(checkbox => {
            checkbox.addEventListener('change', function() {
                const taskId = this.closest('.task-item').dataset.taskId;
                const taskDescription = this.closest('.task-item').querySelector('.task-description');
                
                fetch(`/toggle_task/${taskId}`, {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json',
                    }
                })
                .then(response => response.json())
                .then(data => {
                    if (data.success) {
                        if (data.completed) {
                            taskDescription.classList.add('text-decoration-line-through', 'text-muted');
                        } else {
                            taskDescription.classList.remove('text-decoration-line-through', 'text-muted');
                        }
                    }
                })
                .catch(error => {
                    console.error('Error:', error);
                    // Revert checkbox state on error
                    this.checked = !this.checked;
                });
            });
        });
        
        // Handle delete task
        document.querySelectorAll('.delete-task').forEach(button => {
            button.addEventListener('click', function() {
                if (confirm('Apakah Anda yakin ingin menghapus tugas ini?')) {
                    const taskItem = this.closest('.task-item');
                    const taskId = taskItem.dataset.taskId;
                    
                    fetch(`/delete_task/${taskId}`, {
                        method: 'POST',
                        headers: {
                            'Content-Type': 'application/json',
                        }
                    })
                    .then(response => response.json())
                    .then(data => {
                        if (data.success) {
                            taskItem.style.animation = 'fadeOut 0.3s ease';
                            setTimeout(() => {
                                taskItem.remove();
                                // Update task count
                                const taskCount = document.querySelectorAll('.task-item').length;
                                document.querySelector('.card-header h5').textContent = `Daftar Tugas (${taskCount})`;
                            }, 300);
                        }
                    })
                    .catch(error => {
                        console.error('Error:', error);
                        alert('Terjadi kesalahan saat menghapus tugas.');
                    });
                }
            });
        });
    });

    // CSS animation for fade out
    const style = document.createElement('style');
    style.textContent = `
        @keyframes fadeOut {
            from { opacity: 1; transform: translateX(0); }
            to { opacity: 0; transform: translateX(-100%); }
        }
    `;
    document.head.appendChild(style);
    ```

**Verifikasi:**
Setelah kamu selesai, saya harus bisa menjalankan `python todo_app/main.py` dari terminal. Aplikasi harus menampilkan menu, dan jika saya mengetik `3` lalu menekan Enter, aplikasi harus mencetak pesan perpisahan dan berhenti.