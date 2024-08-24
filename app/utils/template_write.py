

def write_template(template:str, data:dict):
    template = template.replace('<title>', data['name'])
    template = template.replace('<desc>', data['description'])
    template = template.replace('<link>', data['svn_url'])
    template = template.replace('<hastags>', ' '.join([f'#{i}' for i in data['topics']]))
    return template