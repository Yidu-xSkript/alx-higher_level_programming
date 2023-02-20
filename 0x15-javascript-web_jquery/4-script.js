const $header = $('header');
const $toggleBtn = $('DIV#toggle_header');

$toggleBtn.on('click', () => {
  const thisClass = $header.attr('class');

  if (thisClass === 'green') {
    $header.toggleClass(`${currentClass} red`);
  }

  if (thisClass === 'red') {
    $header.toggleClass(`${currentClass} green`);
  }
});
