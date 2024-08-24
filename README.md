# Github Repository Poster

This is a program is for automatically post github repository/repos on social media automatically.

This is an extention or application of the [Automate-Posting-App](https://github.com/coderooz/automate-posting-app) project.

*Note*: You ca check the posts on my [fb page](https://www.facebook.com/people/Coderooz/61562424744859/)

## Feature

- **Social MediaPosting**
- **Template**: Uses this template to post.

## Social Media Platforms Available

- **Facebook**

## Requirements

- [**Mongodb**](https://www.mongodb.com) : For storing all the data.

- **Libraries**:
    - **python-dotenv** : For handling data from `.env` file.
    - **pymongo** :  For interacting with mongodb.
    - **requests** : For handling requests. 

## How to use

1. **Clone the github repository**
```bash
    git clone https://github.com/coderooz/github-repository-poster.git
    cd github-repository-poster
```

2. **Start a virtual evironment** (*Optional*)

    This is an optional by *recommended* step. 
    
    - Create an `.venv` dir in project folder
    -  Start the virtual environment.
        - **For Windows:**
            ```bash
                .\.venv\Scripts\Acitvate.ps1
            ```

        - **For macOS/Linix:**
            ```bash
                source .venv/bin/acitvate
            ```
    - Check the acivation : There will appear `(venv)` infont of the path in the termnal.

3. **Install required libraries**
    ```bash
        pip3 install -r requirements.txt    
    ```

4. **Create a `.env` file**

    This file will store all the necessary the values and `api_keys`
    ```bash
        MONGO_URI = 'mongodb://localhost:27017/' # mongodb url
        OWNER = 'githib-profile-id' # replace with your github id
        FACEBOOK_ACCESS_TOKEN = 'YOUR-FB-ACCESS-KEY' # replace with your access key
        FB_PAGE_NAME='FB Page Name'
    ```
    *Note:* Do remove the `'` from the .env file that you make.
5. **Run**

    Run a `main.py` for test.
    ```bash
        py main.py
    ```

### Future Improvements

- Multiple Social Medias
- A ui-based user interface

## Contributing
Feel free to fork this repository and contribute by submitting a pull request. For major changes, please open an issue first to discuss what you would like to change.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

## Author

- [**Coderooz**](http://github.com/coderooz) - *Initial work* - Ranit Saha

**Thank You For Visiting this repository of mine.**
