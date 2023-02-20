$.ajax({
  url: 'https://swapi-api.hbtn.io/api/films/?format=json',
  dataType: 'json'
}).done((data) => {
  const movies = data.results;

  for (let i = 0; i < movies.length; ++i) {
    const movieTitle = movies[i].title;
    const element = `<li>${movieTitle}`;
    $('ul#list_movies').append(element);
  }
});
