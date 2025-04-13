# Django User Reg აპლიკაცია
Django ვებ აპლიკაცია REST API-ით მომხმარებლის ავტორიზაციისა და პოსტების მართვისთვის.

## შესაძლებლობები
- მომხმარებლის რეგისტრაცია, შესვლა, გამოსვლა.
- პოსტების შექმნა, ნახვა, განახლება, წაშლა (CRUD).

## ინსტალაცია
1. Clone: `git clone https://github.com/vakho-jin/user_reg.git`
2. Setup venv: `python -m venv venv && source venv/bin/activate`
3. Install: `pip install -r requirements.txt`
4. Migrate: `python manage.py makemigrations && python manage.py migrate`
5. Collect static: `python manage.py collectstatic`
6. Run: `python manage.py runserver`

## გამოყენება
- მთავარი: `/`
- რეგისტრაცია: `/register/`
- შესვლა: `/login/`
- პოსტები: `/posts/` (create/delete posts)
- API: `/api/register/`, `/api/login/`, `/api/posts/`