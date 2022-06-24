function changeTab(x) {
  if (x == 'home') {
    window.document.getElementById("home").style['text-decoration'] = 'underline';
  } else if (x == 'contact') {
    window.document.getElementById("contact").style['text-decoration'] = 'underline';
  }
}

function send() {
  console.log('Good Job')
}

function easterEgg() {
  console.log("It's an easter egg, if you want the answer call me `)")
}