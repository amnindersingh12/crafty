# Getting Crafty 🎨

A beautiful, modern e-commerce web application for handmade crafts and DIY projects. Built with Django and inspired by premium Squarespace designs.

![Django](https://img.shields.io/badge/Django-6.0-green.svg)
![Python](https://img.shields.io/badge/Python-3.14-blue.svg)
![License](https://img.shields.io/badge/License-MIT-yellow.svg)

## ✨ Features

### 🎯 Core Functionality
- **Product Catalog** - Browse handmade crafts with beautiful product cards
- **Category Filtering** - Filter products by category (Crochet, Knitting, Sewing, etc.)
- **Shopping Cart** - Session-based cart system with real-time updates
- **Product Detail Pages** - Detailed product views with image/video support
- **Responsive Design** - Mobile-first approach, works on all devices

### 🎨 Design & UX
- **Premium Aesthetics** - Squarespace-inspired design with lavender color palette
- **Smooth Animations** - 650ms transitions with scroll-reveal effects
- **Interactive Elements** - Hover effects, image zoom, and micro-interactions
- **Custom Typography** - Satisfy (display) + Inter (body) font pairing
- **Grain Texture Overlay** - Artistic background with animated mesh gradients

### 🚀 Technical Highlights
- **Django 6.0** - Latest Django framework
- **SQLite Database** - Lightweight database for development
- **Session-based Cart** - No login required for shopping
- **Context Processors** - Global category navigation
- **Custom Management Commands** - Easy sample data loading
- **Static File Handling** - Optimized CSS/JS delivery

## 📸 Screenshots

### Homepage
Beautiful hero section with animated background and featured products.

### Shop Page
2-column responsive grid with category filtering and smooth animations.

### Product Detail
Detailed product view with image zoom and add-to-cart functionality.

## 🛠️ Installation

### Prerequisites
- Python 3.10 or higher
- pip (Python package manager)
- Virtual environment (recommended)

### Quick Start

1. **Clone the repository**
```bash
git clone https://github.com/yourusername/getting-crafty.git
cd getting-crafty
```

2. **Create and activate virtual environment**
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. **Install dependencies**
```bash
pip install -r requirements.txt
```

4. **Run migrations**
```bash
python manage.py migrate
```

5. **Load sample data** (optional)
```bash
python manage.py load_sample_data
```

6. **Create superuser** (optional)
```bash
python manage.py createsuperuser
```

7. **Run development server**
```bash
python manage.py runserver
```

8. **Visit the site**
Open your browser and go to `http://localhost:8000`

## 📁 Project Structure

```
getting-crafty/
├── config/                 # Project configuration
│   ├── settings.py        # Django settings
│   ├── urls.py           # Main URL configuration
│   └── wsgi.py           # WSGI configuration
├── core/                  # Main application
│   ├── management/       # Custom management commands
│   │   └── commands/
│   │       └── load_sample_data.py
│   ├── migrations/       # Database migrations
│   ├── models.py         # Data models (Product, Category, CartItem)
│   ├── views.py          # View functions
│   ├── urls.py           # App URL patterns
│   ├── admin.py          # Admin configuration
│   └── context_processors.py  # Global context data
├── templates/            # HTML templates
│   ├── base.html        # Base template with header/footer
│   ├── home.html        # Homepage
│   ├── shop.html        # Shop page
│   ├── product_detail.html  # Product detail page
│   └── cart.html        # Shopping cart page
├── static/              # Static files
│   ├── css/
│   │   └── styles.css   # Main stylesheet (1300+ lines)
│   └── js/
│       └── main.js      # JavaScript functionality
├── media/               # User-uploaded files
│   ├── products/        # Product images
│   └── videos/          # Product videos
├── db.sqlite3           # SQLite database
├── manage.py            # Django management script
├── requirements.txt     # Python dependencies
└── README.md           # This file
```

## 🎨 Design System

### Color Palette
```css
--lavender-light: #e3dffc;  /* Lighter, airier */
--lavender: #c4bdf4;        /* Soft pastel lavender */
--lavender-dark: #a39be0;   /* Muted depth */
--white: #fdfcfd;           /* Soft paper white */
--black: #2c2a30;           /* Soft charcoal */
--gray-100: #f7f5f9;        /* Very light lavender-tinted gray */
--gray-200: #e8e4ec;        /* Soft separating line color */
--gray-500: #8e8894;        /* Muted text gray */
--gray-700: #59545e;        /* Readable soft dark gray */
```

### Typography
- **Display Font**: Satisfy (cursive, handwritten style)
- **Body Font**: Inter (modern sans-serif)
- **Font Sizes**: Responsive with `clamp()` for fluid scaling

### Animation Timing
- **Duration**: 650ms (matching reference site)
- **Delay**: 1s for scroll reveals
- **Easing**: `cubic-bezier(0.165, 0.84, 0.44, 1)`

## 🔧 Configuration

### Environment Variables
Create a `.env` file in the project root (optional):
```env
SECRET_KEY=your-secret-key-here
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1
```

### Database
The project uses SQLite by default. To use PostgreSQL or MySQL, update `config/settings.py`:
```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'your_db_name',
        'USER': 'your_db_user',
        'PASSWORD': 'your_db_password',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
```

## 📦 Models

### Product
```python
- name: CharField (max 200)
- slug: SlugField (unique)
- description: TextField
- price: DecimalField
- image: ImageField (optional)
- video: FileField (optional)
- category: ForeignKey to Category
- featured: BooleanField
- created_at: DateTimeField
```

### Category
```python
- name: CharField (max 100)
- slug: SlugField (unique)
```

### CartItem
```python
- session_key: CharField (max 40)
- product: ForeignKey to Product
- quantity: PositiveIntegerField
- created_at: DateTimeField
```

## 🚀 Deployment

### Heroku
1. Install Heroku CLI
2. Create `Procfile`:
```
web: gunicorn config.wsgi
```
3. Add `gunicorn` to requirements.txt
4. Deploy:
```bash
heroku create your-app-name
git push heroku main
heroku run python manage.py migrate
```

### Railway
1. Connect your GitHub repository
2. Add environment variables
3. Deploy automatically on push

### DigitalOcean
1. Create a Droplet
2. Install dependencies
3. Configure Nginx + Gunicorn
4. Set up SSL with Let's Encrypt

## 🤝 Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- Design inspiration from [Getting Crafty with Ana](https://www.gettingcraftywithana.com/)
- Django framework and community
- Squarespace for design patterns
- Google Fonts for typography

## 📧 Contact

Your Name - [@yourtwitter](https://twitter.com/yourtwitter)

Project Link: [https://github.com/yourusername/getting-crafty](https://github.com/yourusername/getting-crafty)

---

**Made with ❤️ and Django**
