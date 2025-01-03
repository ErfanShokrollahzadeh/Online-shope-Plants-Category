# Plant Shop Django Application

This repository contains a Django application for a Plant Shop. The application includes various modules such as account management, articles, contact, home, products, and site settings.

## Setup Instructions

Follow these steps to set up and run the Django application:

### 1. Clone the repository

```bash
git clone https://github.com/ErfanShokrollahzadeh/Plant-Shop-test-templates-1.git
cd Plant-Shop-test-templates-1
```

### 2. Create and activate a virtual environment

```bash
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```

### 3. Install required packages

```bash
pip install -r requirements.txt
```

### 4. Configure the database settings

Open the `Plant_Shop/settings.py` file and locate the `DATABASES` dictionary. Modify the `ENGINE`, `NAME`, `USER`, `PASSWORD`, `HOST`, and `PORT` keys with the appropriate values for your database. For example, to use PostgreSQL:

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'your_database_name',
        'USER': 'your_database_user',
        'PASSWORD': 'your_database_password',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
```

### 5. Run database migrations

```bash
python manage.py migrate
```

### 6. Create a superuser

```bash
python manage.py createsuperuser
```

### 7. Run the Tailwind CSS build script

```bash
npm install
npm run build-css
```

### 8. Run the Django application

```bash
python manage.py runserver
```

You can now access the application at `http://127.0.0.1:8000/`.

## Entity Relationship Diagrams

### Backend ERD

```mermaid
erDiagram
    User ||--o{ Articles : writes
    User {
        string username
        string email
        string password
        boolean is_active
        boolean is_staff
        datetime date_joined
    }
    
    Articles ||--o{ ArticleCategory : belongs_to
    Articles {
        string title
        string short_description
        text description
        string image
        string slug
        boolean is_active
        datetime created_date
    }
    
    ArticleCategory {
        string title
        string slug
        int parent_id
    }
    
    Product ||--o{ ProductCategory : belongs_to
    Product {
        string name
        string slug
        text description
        decimal price
        string image
        int stock
        boolean is_active
        boolean is_featured
        datetime created_at
    }
    
    ProductCategory {
        string title
        string slug
        boolean is_active
    }
    
    SiteSetting {
        string site_name
        string site_url
        text address
        string logo
        json email
        text copy_right
        string phone
        boolean is_main_setting
    }
    
    ContactUs {
        string name
        string email
        string subject
        text message
        datetime created_date
    }
    
    HeroSection {
        string title
        text subtitle
        string hero_image
    }
    
    PlantBenefit {
        string title
        text description
        string icon_class
        string image
    }
    
    Slider {
        string title
        text subtitle
        string image
        int order
        boolean is_active
        datetime created_at
    }
```

### Frontend Components Structure

```mermaid
graph TD
    A[App] --> B[Layout]
    B --> C[Header/Navigation]
    B --> D[Footer]
    B --> E[Main Content]
    
    E --> F[Home Page]
    F --> G[Hero Section]
    F --> H[Featured Products]
    F --> I[Benefits Section]
    F --> J[Slider]
    
    E --> K[Products Page]
    K --> L[Product List]
    K --> M[Product Filters]
    K --> N[Product Card]
    
    E --> O[Article Page]
    O --> P[Article List]
    O --> Q[Article Detail]
    
    E --> R[Authentication]
    R --> S[Login Form]
    R --> T[Signup Form]
    
    E --> U[Contact Page]
    U --> V[Contact Form]
    
    E --> W[About Page]
    W --> X[Team Section]
    W --> Y[Milestones]
```

