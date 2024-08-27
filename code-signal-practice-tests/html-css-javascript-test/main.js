console.log(
  "JavaScript gets executed automatically when the preview re-renders"
);

// add function
let count = 0;
function increment() {
  count++;
  document.getElementsByClassName("counter-value")[0].innerText = count;
}

// note: we could give the element an id and use getElementById instead
