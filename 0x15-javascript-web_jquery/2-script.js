const $header = $('header');
const $div = $('div#red_header');

$div.on('click', function () {
  $header.css('color', '#FF0000');
});
