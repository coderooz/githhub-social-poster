from .utils.requester import requester
from requests import Response
import logging

class FaceBook:
    def __init__(self, access_token:str) -> None:
        self.access_token = access_token
        self.url = 'https://graph.facebook.com/v20.0/{}'
        self.set_param = {'access_token':self.access_token}
        
        self.me = self.user_info()
        self.pages = {data['name']: {'id': data['id'], 'access_token': data['access_token']} for data in self.get_pages_list()}

    def post_text(self,message: str,  page_id: str='me', link:str=None):
        """
            Posts text to a specified page or personal account.
            
            Parameters:
                page_id (str): The page ID or 'me' for personal account.
                message (str): The message to post.
            
            Returns:
                dict: The API response.
        """
        access_token = self.access_token
        if page_id == 'me':
            page_id = self.me['id']
        elif page_id in self.pages:
            access_token = self.pages[page_id]['access_token']
            page_id = self.pages[page_id]['id']
        else:
            page_info = self.select_page(page_id)
            if page_info:
                page_id = page_info['id']
                access_token = page_info['access_token']
            else:
                print(f"Page '{page_id}' not found.")
                return {'error': 'Page ID or user account not found'}

        return requester(self.url.format(f'{page_id}/feed'), 'post', params={'message': message, 'link': link, 'access_token': access_token})

    def user_info(self)-> (dict|Response):
        url = self.url.format('me')
        params={**self.set_param,'fields': 'id,name,email,gender,birthday,picture'}
        return requester(url, params=params)

    #  post handleing
    def get_posts_list(self, page_name: str, limit: int = 10) -> list:
        """
        Retrieves a list of posts from a specified page or user feed.
        
        Parameters:
            page_name (str): The name of the page or 'me' for user posts.
            limit (int): The number of posts to retrieve. Defaults to 10.
        
        Returns:
            list: A list of posts.
        """
        page_id = ''
        access_token = ''
        if page_name in self.pages:
            page_id = self.pages[page_name]['id']
            access_token = self.pages[page_name]['access_token']
        elif page_name == 'me':
            page_id = self.me['id']
            access_token = self.access_token
        else:
            page_id = self.select_page(page_name)
            access_token = self.pages.get(page_name).get('access_token', '')

        if not page_id or not access_token:
            print(f"Page '{page_name}' not found.")
            return []

        posts = requester(self.url.format(f'{page_id}/posts'), params={'limit': limit, 'access_token':access_token})
        if 'error' in posts:
            logging.error(er:=f"Error fetching posts: {posts['error']}")
            print(er)
            return []
        return posts.get('data', [])
    
    def edit_post(self, post_id: str, message: str, page_name:str):
        """
        Edits an existing post on a page or personal account.
        
        Parameters:
            post_id (str): The ID of the post to edit.
            message (str): The new message content.
        
        Returns:
            dict: The API response.
        """
        if page_name in self.pages:
            access_token = self.pages[page_name]['access_token']
        elif page_name=='me':
            access_token = self.access_token
        else:
            print(f'Page {page_name} not found.')
            return {}
        
        response = requester(self.url.format(post_id), 'post', params={'message': message}, new_access_token=access_token)
        if 'error' in response:
            print(f"Error editing post: {response['error']}")
        return response

    def delete_post(self, post_id: str, page_name:str):
        """
            delete_post
            -----------
            Edits an existing post on a page or personal account.
            
            Parameters:
                post_id (str): The ID of the post to edit.
                message (str): The new message content.
            
            Returns:
                dict: The API response.
        """
        if page_name in self.pages:
            access_token = self.pages[page_name]['access_token']
        elif page_name=='me':
            access_token = self.access_token
        else:
            print(f'Page {page_name} not found.')
            return {}
        
        response = requester(self.url.format(post_id), 'delete', params={'access_token':access_token})
        if 'error' in response:
            print(f"Error editing post: {response['error']}")
        return response
      
    #  pages handleing  
    def get_pages_list(self) -> list:
        """
        Fetches the list of pages that the user has access to.
        
        Returns:
            list: A list of pages.
        """
        response = requester('https://graph.facebook.com/me/accounts', params=self.set_param)
        if 'error' in response:
            print(f"Error fetching pages: {response['error']}")
            return []
        return response.get('data', [])

    def select_page(self, page_name: str) -> dict:
        """
        Selects a page based on the page name.
        
        Parameters:
            page_name (str): The name of the page to select.
        
        Returns:
            dict: The page information including ID and access token, if found.
        """
        pages = self.get_pages_list()
        for page in pages:
            if page['name'] == page_name:
                return {'id': page['id'], 'access_token': page['access_token']}
        print(f"Page '{page_name}' not found.")
        return {}