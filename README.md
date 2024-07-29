# LittleLemon Restaurant
(Meta Back-End Developer Capstone Project)

## This is a Django web application for a restaurant named LittleLemon. The application fulfills the following criteria:
- Serves static HTML content using the Django framework
- Connects the backend to a MySQL database
- Implements APIs for menu and table booking
- Set up with user registration and authentication
- Contains unit tests
- The API can be tested with the Insomnia REST client

## Installation and Usage
To use this application, follow these steps:
1. Clone the repository from GitHub
2. Install the required dependencies.
3. Set up a MySQL database and configure the application to use it
4. Run the application using the Django development server.
5. Test the application using the Insomnia REST client or other tools.

## Establishing a MySQL connection
Note: the 'django.db.backends.mysql' engine does not work on ARM based machines. 
Please install mysql-connector-python using pip or pipenv.
Alternatively, if you are using the mysqlclient connector, you can uncomment the 'django.db.backends.mysql' line in **settings.py** and comment out the line below it, in order to establish a database connection.

## Credentials
| Username | Password       | User Type     |
|----------|----------------|---------------|
| admin    | ?admin         | superuser     |
| testuser | ?test123       | standard user |

## Testing
The application contains unit tests that can be run using the Django test runner. To run the tests, use the following command: ```python manage.py test```
The API can also be tested using the Insomnia REST client or other tools.

## API endpoints to test
| Description           | Method | Path                        | Token                                    | Form/JSON payload                                                         |
|-----------------------|--------|-----------------------------|------------------------------------------|---------------------------------------------------------------------------|
| Load static home page | GET    | /restaurant/                |                                          |                                                                           |
| View menu items       | GET    | /restaurant/menu/           |                                          |                                                                           |
| View single menu item | GET    | /restaurant/menu/<<int:pk>> |                                          |                                                                           |
| Add a menu item       | POST   | /restaurant/menu/           | 98c875be86b60a63fd4b7b5cc8061b7ee9bc42d1 | {"id": 4,"title": "Grilled Fish","price": "18.99","inventory": 20 }              |
| Update a menu item    | PUT    | /restaurant/menu/<<int:pk>> | 98c875be86b60a63fd4b7b5cc8061b7ee9bc42d1 | {"id": 3,	"title": "Lemon Dessert",	"price": "4.99",	"inventory": 15} |
| Delete a menu item    | DELETE | /restaurant/menu/<<int:pk>> | 98c875be86b60a63fd4b7b5cc8061b7ee9bc42d1 |                                                                           |
| Obtain authtoken      | POST   | /restaurant/api-token-auth/ |                                          | {"username": "testuser",	"password": "?test123"}                       |
| View table bookings   | GET    | /restaurant/booking/tables  | 98c875be86b60a63fd4b7b5cc8061b7ee9bc42d1 |                                                                           |

