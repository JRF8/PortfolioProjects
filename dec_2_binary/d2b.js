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
      bin_field.value = '';
      return;
    } else if (node.name === "bin_value") {
      dec_field.value = '';
      return;
    } else if (node.name === "twos_comp"){
      return;
    }
    else {
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
        case 2:
          toggleTwosComp();
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

  function toggleTwosComp() {
    var rb = rbArray[2];
    switch (rb.value) {
      case "false":
        rb.checked = true;
        rb.value = true;
        break;
      case "true":
        rb.checked = false;
        rb.value = false;
        break;
    }
  }

  function checkAndCalculate() {
    var d2b;
    if (dec_field.value != '' && dec_field.value != "NaN") {
      d2b = true;
      bin_field.value = parseInt(dec_field.value).toString(2);
      maybeCalcTwosComp(d2b);
    } else if (bin_field.value != '' || bin_field.value != "NaN") {
      d2b = false;
      maybeCalcTwosComp(d2b);
      dec_field.value = parseInt(bin_field.value, 2).toString(10);
    }
  }

  function maybeCalcTwosComp(d2b) {
    var dv = dec_field.value,
      bv = bin_field.value;
    var tc = rbArray[2].checked;
    switch (d2b) {
      case true:
        dv < 0 ? calcTwosComp() : "not negative";
        break;
      case false:
        tc == true ? bv = calcTwosComp() : "tc rb not checked";
        break;
      default:
        "your code doesn't work"
    }
    bin_field.value = bv;
    dec_field.value = dv;
  }

  // logic functions here:
  function calcTwosComp() {
    var binVal = bin_field.value.toString().split("")
    for (var i = binVal.length - 1; i >= 0; i--) {
      binVal[i] == 0 ? binVal[i] = 1 : binVal[i] = 0;
    }
    var carry = 1;
    for (var i = binVal.length - 1; i >= 0; i--) {
      var result = adder(binVal[i], 0, carry);
      binVal[i] = result.v;
      carry = result.c;
    }
    carry === 1 ? binVal[binVal.length] = carry : "";
    return binVal;
  }

  function xor(a, b) {
    var v = 0;
    ((a && b) === 1) ? v = 0: ((a || b) === 0) ? v = 0 : v = 1;
    return v;
  }

  function adder(a, b, c) {
    if ((typeof(c) === "undefined") || (c === 0)) {
      var c = a & b;
      var v = xor(a, b);
    } else if (a && b && c) {
      v = 1, c = 1;
    } else if (xor(a, b) && c === 1) {
      v = 0, c = 1;
    } else {
      v = 1, c = 0;
    }
    return {
      v,
      c
    }
  }




})();
