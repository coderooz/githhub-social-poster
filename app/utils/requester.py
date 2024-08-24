import requests
from requests import Response

def requester(url:str, method:str='get', params:dict={}, active_status:int=0, raw:bool=False)->(str|dict|Response):
    """
        requester
        ---------
        This method is responsible for handling all the requests that will be made  in this module.
        
        Parameter:
        - url (str): Takes the url.
        - method (str): Takes the method used for the requests. accepter values are `'get'`, `'post'` & `'delete'`.
        - params (dict): Takes the parameters to be passed during the request.
        - active_status (int): Takes the request status value in which the request will be seen as successfull.
        - raw(bool): for converting requested data into json or text if given `True`.
    """
    if method =='get':
        ret = requests.get(url=url, params=params)
    elif method =='delete':
        ret = requests.delete(url=url, params=params)
    elif method =='post':
        ret = requests.post(url=url, params=params)
    else:
        logging.error("The method value only accepts 'get', 'post' & 'delete'.", exc_info=True)
        # raise ValueError()
    
    if raw==False:
        try:
            ret = ret.json()
        except:
            try:
                ret = ret.text
            except: pass
    return ret
    