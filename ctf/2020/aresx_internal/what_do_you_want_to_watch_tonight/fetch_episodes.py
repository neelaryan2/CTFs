import imdb 

ia = imdb.IMDb() 
code = "0203259"

series = ia.get_movie(code) 
ia.update(series, 'episodes') 
episodes = series.data['episodes'] 

for i in episodes.keys(): 
	for j in episodes[i]: 
		title = episodes[i][j]['title'] 
		print(title)
			
