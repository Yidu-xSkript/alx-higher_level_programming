const $header = $('header');
const $div = $('DIV#toggle_header');

$div.on('click', () => {
  const thisClass = $header.attr('class');

  if (thisClass === 'green') {
    $header.toggleClass(`${currentClass} red`);
  }

  if (thisClass === 'red') {
    $header.toggleClass(`${currentClass} green`);
  }
});
