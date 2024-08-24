from .utils.requester import requester
from pymongo import MongoClient
from pymongo.errors import ConfigurationError

class GitHub:
        
    def __init__(self, username:str, mongoUrl:str)->None:
        
        DATABASE_NAME = 'github'
        COLLECTION_NAME = ['repositories', 'user', 'posts']
        try:
            self.client = MongoClient(mongoUrl)
            self.db = self.client[DATABASE_NAME]
            self.collection:dict = {i: self.db[i] for i in COLLECTION_NAME}
        except ConfigurationError:
            print("Failed to connect to MongoDB.")
            exit()
        self.username = username
          
    def user_info(self, userName:str='',fetch_new:bool=False):
        """
            user_info
            ---------
            This method is to search any users github page.

            Args:
                userName (str): Takes the name of the user/repository owner.
            
            Returns:

        """
        userName = self.username if userName=='' else userName
        if fetch_new:
            data = requester(f'https://api.github.com/users/{userName}', raw=False)
        else:
            co = self.collection['user']
            data = co.find_one({'login': userName})
            if data==None:
                data = self.user_info(userName, True)
                co.insert_one(data)
        return data
    
    def getAllRepositoriesByUser(self, username:str='', fetch_new:bool=False):
        """
            getRepositoriesByUser
            ---------------------
            This method is responsible for getting the repositories of any user by there tagName.
            
            Parameters:
            - username str: Take the user name as displayed on the github user profile page.
        """
        username = self.username if username=='' else username
        ret:list = []
        pageNo = 1
        while True:
            data = requester(f'https://api.github.com/users/{username}/repos?page={pageNo}')
            for d in data:
                repo_vals = ["id", "node_id", "name", "full_name", "private", "description", "fork", "url", "created_at", "updated_at", "pushed_at", "git_url", "ssh_url", "clone_url", "svn_url", "homepage", "size", "stargazers_count", "watchers_count", "language", "has_issues", "has_projects", "has_downloads", "has_wiki", "has_pages", "has_discussions", "forks_count", "mirror_url", "archived", "disabled", "open_issues_count", "allow_forking", "is_template", "web_commit_signoff_required", "topics", "visibility", "forks", "open_issues", "watchers", "default_branch", 'owner', 'license']
                d = {k:v for k,v in d.items() if k in repo_vals}
                ret.append(d)            
            if len(data) < 30:
                break 
            else:
                pageNo+=1
        return ret

    def fetchUserRepo(self, userName:str='', repo:str=''):
        pass
