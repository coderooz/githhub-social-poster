import config as cf
from app import Github, FaceBook
from app.utils.template_write import write_template

github = Github.GitHub(cf.owner, cf.mongo_url) 
facebook = FaceBook.FaceBook(cf.facebook_access_key)

repo_coll = github.collection['repositories']
template = 'Hey guys! Check out my new project.\n\nProject Title: <title>\nProject Desc: <desc>\nLink: <link>\n\n<hastags>'
repos = repo_coll.find({'private':False, 'license.key':'mit','visibility': 'public', 'owner.login':cf.owner}, {'owner': 0, '_id':0, })
for data in repos:
    text:str = write_template(template, data)
    fb_resp:str = facebook.post_text(message=text, page_id=cf.fb_page, link=data['svn_url'])
    update_value = {'posts': {'posted': True, 'fb_post_id': fb_resp, 'instagram_post_id': ''}}
    repo_coll.update_one({'id': data['id']}, {'$set': update_value})
repo_coll.update_many({'posts':{'$exists': False}}, {'$set': {'posts': {'posted': False, 'fb_post_id':'', 'instagram_post_id': ''}}})

    
    
    




