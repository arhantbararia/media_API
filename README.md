# Media API

Version 1.0

The Media API provides access to reviews and ratings for movies and music. The API is designed to be used with a browsable API client such as Postman and can be accessed using the URL:

`https://arhantbararia.pythonanywhere.com/movie/api/`

The Media API project uses Token authentication to ensure secure access to user data and functionality. Users can obtain an authentication token by logging in through the `/account/api/login/` endpoint. The token can then be used to access other endpoints that require authentication.

`https://arhantbararia.pythonanywhere.com/account/api/...`

or click [here](http://arhantbararia.pythonanywhere.com/movie/api/)

The API provides endpoints for retrieving information about movies and music, including details about the title, release date, director/artist, and user ratings. The API also allows users to submit their own reviews and ratings.

The endpoint reference diagram for the Media API is shown below:
![Media_API_DRF](https://github.com/arhantbararia/media_API/assets/61796574/998ec22c-3bef-4c0c-a89b-18b6e0e3af6b)


To login, logout, and register, use the following endpoints:

- `POST /account/api/login/`: Allows users to log in and obtain an authentication token
- `POST /account/api/logout/`: Allows users to log out and revoke their authentication token
- `POST /account/api/register/`: Allows users to register and create a new account.
