const $header = $('header');
const $btn = $('div#update_header');

$btn.on('click', () => {
  $header.text('New Header!!!');
});
