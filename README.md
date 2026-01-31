# DriveX 🚗

A modern car rental platform built with Django featuring owner, renter, and manager dashboards with real-time booking management.

## Features

### For Vehicle Owners
- Add and manage multiple vehicles
- Set custom pricing and availability
- Accept or reject booking requests
- Track rental history and earnings
- Edit vehicle details and photos

### For Renters
- Browse available vehicles by category (Economy, Luxury, Sport)
- View detailed vehicle information
- Book vehicles for specific dates
- Manage active and past bookings
- Cancel bookings
- View booking details including owner information

### For Managers
- Administrative dashboard
- Oversee all platform activities
- Manage users and vehicles
- Monitor bookings and transactions

## Tech Stack

- **Backend**: Django (Python)
- **Frontend**: HTML, CSS, JavaScript
- **Database**: SQLite (development)
- **Authentication**: Django's built-in auth system

## Project Structure

```
DriveX/
├── DriveX/          # Core app (authentication, dashboard)
├── Owner/           # Owner-specific features
├── Renter/          # Renter-specific features
├── Manager/         # Admin/manager features
├── static/          # Static files (CSS, JS, images)
└── config/          # Project settings
```

## Installation

1. Clone the repository:
```bash
git clone https://github.com/Ayush16coder/DriveX.git
cd DriveX
```

2. Create a virtual environment:
```bash
python -m venv venv
venv\Scripts\activate  # On Windows
```

3. Install dependencies:
```bash
pip install django
```

4. Run migrations:
```bash
python manage.py migrate
```

5. Start the development server:
```bash
python manage.py runserver
```

6. Visit `http://localhost:8000` in your browser

## Usage

1. Register as an Owner or Renter
2. Owners can add vehicles from their dashboard
3. Renters can browse and book available vehicles
4. Manage your profile and bookings from the dashboard

## Screenshots

*Coming soon*

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is open source and available under the MIT License.

## Author

**Ayush** - [Ayush16coder](https://github.com/Ayush16coder)
