$.ajax({
  url: 'https://swapi-api.alx-tools.com/api/people/5/?format=json',
  dataType: 'json'
}).done((data) => {
  $('div#character').text(data.name);
});
