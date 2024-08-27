function pyramid1() {
  let x = "*";
  let target = 10;
  let total = (target - 1) * 2;
  for (let i = 0; i < target; i++) {
    const pad = total / 2 - i;
    if (i > 0) {
      x += "**";
    }
    console.log(x.padStart(pad + x.length, " "));
  }
}

function pyramid2() {
  let x = "^";
  let target = 10;
  let total = (target - 1) * 2;
  for (let i = 0; i < target; i++) {
    console.log(" ".repeat(total - i) + x.repeat(i * 2 + 1));
  }
}

function pyramid3() {
  let target = 10;
  for (let i = 0; i < target; i++) {
    console.log(" ".repeat(target - i - 1) + "*".repeat(i * 2 + 1));
  }
}

pyramid1();
pyramid2();
pyramid3();
