from flask import Flask, render_template, request, redirect
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)

@app.route('/')
def home():
	return render_template('search.html')

@app.route('/search',methods = ['POST', 'GET'])
def search():
	query = request.args.get('q')
	if not query:
		return redirect('/')
	page = request.args.get('page')
	if page:
		new_query = query.replace(' ', '+') + '&start=' + str((int(page)-1)*10)
	else:
		new_query = query.replace(' ', '+')
	html_code = requests.get("https://www.google.com/search?q="+new_query)
	soup = BeautifulSoup(html_code.text, 'html.parser')
	a = soup.find_all('div', class_="ZINbbc xpd O9g5cc uUPGi")
	listOfItem = [i for i in a if i.div.a]
	finalList = [[
					i.find('div', class_="BNeawe vvjwJb AP7Wnd"),
					i.div.a.get('href').split('&')[0][7:],
					i.find('div', class_="BNeawe s3v9rd AP7Wnd"),
				 ] for i in listOfItem]


	return render_template('search_result.html', result = finalList, query=query.replace(' ', '+'))

if __name__ == '__main__':
	app.run(debug=True)