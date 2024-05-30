fetch("https://swapi-api.alx-tools.com/api/films/?format=json")
  .then(response => {
	  return response.json()
  })
  .then(data => {
	  arr = data.results
	  for (x = 0 ; x < arr.length ; x++)
		  $('UL#list_movies').append(`<li>${arr[x].title}</li>`)
		 
  })
