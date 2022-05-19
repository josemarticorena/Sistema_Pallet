from shareplum import Site
from shareplum import Office365
from shareplum.site import Version

authcookie = Office365('https://ingenieriausacedu.sharepoint.com', username='3003552890101@ingenieria.usac.edu.gt', password='Corenamarti498').GetCookies()
site = Site('https://ingenieriausacedu.sharepoint.com/sites/EnlacePLC/', authcookie=authcookie)

site.AddList('My New List2', description='Great List!', template_id='Custom List')
