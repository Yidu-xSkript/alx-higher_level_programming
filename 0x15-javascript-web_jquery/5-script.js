const $list = $('ul.my_list');
const $btn = $('div#add_item');

$btn.on('click', () => {
  $list.append('<li>Item</li>');
});
