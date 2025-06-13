# Tumpukan Teknologi: Aplikasi To-Do List Web-Based

Dokumen ini merinci teknologi yang akan digunakan untuk pengembangan Aplikasi To-Do List Web-Based, sesuai dengan tahapan proyek yang dijelaskan dalam `proposal.md` dan `dokumen-desain-produk.md`.

## Fase 1: MVP (Minimum Viable Product) - Web Application

### Backend Technologies
*   **Bahasa Pemrograman:** Python (versi 3.8+)
    *   **Alasan:** Python adalah bahasa yang serbaguna, mudah dibaca, dan memiliki ekosistem web framework yang matang.
*   **Web Framework:** Flask (versi 2.x)
    *   **Alasan:** Flask adalah micro-framework yang ringan, fleksibel, dan mudah dipelajari. Cocok untuk MVP dengan kemampuan scaling yang baik.
*   **Database:** SQLite (dengan SQLAlchemy ORM)
    *   **Alasan:** SQLite tidak memerlukan setup server database terpisah, mudah untuk development dan testing. SQLAlchemy menyediakan ORM yang powerful.
*   **Template Engine:** Jinja2 (built-in dengan Flask)
    *   **Alasan:** Template engine yang powerful dan terintegrasi dengan Flask.

### Frontend Technologies
*   **HTML5:** Struktur markup modern dengan semantic elements
*   **CSS3:** Styling dengan Flexbox/Grid, animations, dan responsive design
*   **JavaScript (ES6+):** Interaktivitas client-side dan AJAX requests
*   **CSS Framework:** Bootstrap 5 atau Custom CSS
    *   **Alasan:** Bootstrap untuk rapid prototyping atau custom CSS untuk kontrol penuh atas design

### Development Tools
*   **IDE:** Cursor (atau IDE lain dengan integrasi AI & Git)
*   **AI Perencana:** Gemini (atau serupa)
*   **AI Coding Assistant:** Jules (atau serupa, terintegrasi di IDE)
*   **Version Control:** Git & GitHub
*   **Package Manager:** pip dengan requirements.txt
*   **Development Server:** Flask built-in development server

## Fase 2: Enhanced Web Features & Performance

### Backend Enhancements
*   **Database Migration:** Tetap SQLite dengan optimisasi query
*   **Caching:** Flask-Caching untuk response caching
*   **API Development:** Flask-RESTful untuk RESTful API endpoints
*   **Validation:** Flask-WTF untuk form validation dan CSRF protection
*   **Session Management:** Flask-Session untuk user session handling

### Frontend Enhancements
*   **JavaScript Framework:** Vanilla JS dengan modern ES6+ features atau Alpine.js untuk reactivity
*   **CSS Preprocessing:** Sass/SCSS untuk better CSS organization
*   **Build Tools:** Webpack atau Vite untuk asset bundling dan optimization
*   **Progressive Web App (PWA):** Service workers untuk offline capability

## Fase 3: Advanced Web Features & Scalability

### Backend Scaling
*   **Database:** PostgreSQL atau MySQL untuk production scalability
*   **ORM:** SQLAlchemy dengan Alembic untuk database migrations
*   **Authentication:** Flask-Login dan Flask-JWT-Extended untuk user authentication
*   **Authorization:** Role-based access control (RBAC)
*   **Background Tasks:** Celery dengan Redis untuk asynchronous task processing
*   **API Documentation:** Flask-RESTX atau Swagger for API documentation

### Frontend Advanced Features
*   **Frontend Framework:** React.js atau Vue.js untuk complex UI interactions
*   **State Management:** Redux (React) atau Vuex (Vue) untuk application state
*   **Real-time Features:** WebSocket dengan Socket.IO for real-time updates
*   **Testing:** Jest for JavaScript testing, Cypress for E2E testing

## Fase 4: Enterprise & Production Deployment

### Production Infrastructure
*   **Web Server:** Gunicorn atau uWSGI dengan Nginx reverse proxy
*   **Containerization:** Docker dan Docker Compose untuk consistent deployment
*   **Cloud Platform:** 
    *   **Option 1:** Heroku untuk simple deployment
    *   **Option 2:** AWS (EC2, RDS, S3) untuk full control
    *   **Option 3:** DigitalOcean App Platform untuk balanced approach
*   **Database:** PostgreSQL with connection pooling
*   **Monitoring:** 
    *   Application monitoring: Flask-APM atau New Relic
    *   Error tracking: Sentry
    *   Logging: Structured logging with ELK stack

### DevOps & CI/CD
*   **CI/CD Pipeline:** GitHub Actions atau GitLab CI
*   **Testing:** 
    *   Unit tests: pytest
    *   Integration tests: pytest with test database
    *   E2E tests: Selenium or Playwright
*   **Code Quality:** 
    *   Linting: flake8, black for Python; ESLint for JavaScript
    *   Security scanning: bandit for Python security issues
*   **Environment Management:** 
    *   Development: Docker Compose
    *   Staging: Kubernetes or Docker Swarm
    *   Production: Kubernetes with auto-scaling

### Security & Performance
*   **Security:**
    *   HTTPS with SSL certificates (Let's Encrypt)
    *   CSRF protection with Flask-WTF
    *   SQL injection prevention with SQLAlchemy ORM
    *   Rate limiting with Flask-Limiter
*   **Performance:**
    *   CDN for static assets
    *   Database query optimization
    *   Caching strategy (Redis/Memcached)
    *   Load balancing for high availability

## Dependencies Management

### Python Dependencies (requirements.txt)
```
Flask==2.3.3
Flask-SQLAlchemy==3.0.5
Flask-WTF==1.1.1
Flask-Login==0.6.3
WTForms==3.0.1
SQLAlchemy==2.0.21
Werkzeug==2.3.7
```

### Development Dependencies (requirements-dev.txt)
```
pytest==7.4.2
pytest-flask==1.2.0
flake8==6.1.0
black==23.9.1
coverage==7.3.2
```

Dokumen ini akan diperbarui jika ada perubahan atau keputusan teknologi baru selama siklus hidup proyek.
