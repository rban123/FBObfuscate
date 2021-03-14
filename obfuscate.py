from facepy import GraphAPI
import facebook
import lorem

TOKEN = [line for line in open("token.txt", 'r')][0].split()[1].strip()

graph = GraphAPI(TOKEN)

posts = graph.get('me/posts')

for post in posts['data']:
   print(post)

#print(posts['paging'])
#print(lorem.paragraph()*2)

