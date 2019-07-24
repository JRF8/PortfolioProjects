//Lines to add eventListeners to the radio buttons
(function() {
  "use strict";

  //GLOBALS
  let title = document.getElementById('form_title'),
    dec_field = document.getElementById('dec_field').childNodes[1],
    bin_field = document.getElementById('bin_field').childNodes[1],
    rbArray = document.getElementById('radio').querySelectorAll('input');

  // set up a couple starting values:
  toggleD2B();
  dec_field.value = '';
  bin_field.value = '';

  // set up event listeners
  rbArray.forEach(rbChecker); // will loop on radio buttons and set up event listeners

  document.onclick = function(event) {
    var node = event.target;
    if (node.name === "dec_value") {
      return;
    } else if (node.name === "bin_value") {
      return;
    } else {
      checkAndCalculate();
    }
  }


  //Function Calls:

  function rbChecker(element, index) {
    element.addEventListener("click", function() {
      dec_field.value = '';
      bin_field.value = '';
      switch (index) {
        case 0:
          toggleD2B();
          break;
        case 1:
          toggleB2D();
          break;
      }
    });
  }

  function toggleD2B() {
    rbArray[0].checked = true;
    rbArray[1].checked = false;
    title.innerHTML = "Decimal To Binary Converter";
    dec_field.disabled = false;
    bin_field.disabled = true;
    bin_field.style.backgroundColor = "darkgray";
    dec_field.style.backgroundColor = "white";
  }

  function toggleB2D() {
    rbArray[0].checked = false;
    rbArray[1].checked = true;
    title.innerHTML = "Binary to Decimal Converter";
    dec_field.disabled = true;
    bin_field.disabled = false;
    bin_field.style.backgroundColor = "white";
    dec_field.style.backgroundColor = "darkgray";
  }

  function checkAndCalculate() {
    if (bin_field.value == '') {
      bin_field.value = parseInt(dec_field.value).toString(2);
    } else if (dec_field.value == '') {
      dec_field.value = parseInt(bin_field.value).toString(10);
    }
  }



})();
