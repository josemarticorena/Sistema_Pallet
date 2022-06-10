from shareplum import Site
from shareplum import Office365
from shareplum.site import Version

authcookie = Office365('https://ingenieriausacedu.sharepoint.com', username='3003552890101@ingenieria.usac.edu.gt', password='Corenamarti498').GetCookies()
site = Site('https://ingenieriausacedu.sharepoint.com/sites/EnlacePLC/', authcookie=authcookie)

#site.AddList('Eficiency list', description='Great List!', template_id='Custom List')

new_list = site.List('Eficiency list')
update_data = [{'ID': '1', 'Tiempo_Total_Paro': '60'},
               {'ID': '2', 'Title': 'Another Change'}]
new_list.UpdateListItems(data=update_data, kind='Update')