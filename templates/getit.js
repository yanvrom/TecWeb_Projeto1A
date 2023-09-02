function getRandomInt(min, max) {
  min = Math.ceil(min);
  max = Math.floor(max);
  return Math.floor(Math.random() * (max - min + 1)) + min;
}

document.addEventListener("DOMContentLoaded", function () {
  // Faz textarea aumentar a altura automaticamente
  // Fonte: https://www.geeksforgeeks.org/how-to-create-auto-resize-textarea-using-javascript-jquery/#:~:text=It%20can%20be%20achieved%20by,height%20of%20an%20element%20automatically.
  let textareas = document.getElementsByClassName("autoresize");
  for (let i = 0; i < textareas.length; i++) {
    let textarea = textareas[i];
    function autoResize() {
      this.style.height = "auto";
      this.style.height = this.scrollHeight + "px";
    }

    textarea.addEventListener("input", autoResize, false);
  }

  // Sorteia classes de cores aleatoriamente para os cards
  let cards = document.getElementsByClassName("card");
  for (let i = 0; i < cards.length; i++) {
    let card = cards[i];
    card.className += ` card-color-${getRandomInt(
      1,
      5
    )} card-rotation-${getRandomInt(1, 11)}`;
  }

  const TOGGLE = document.getElementById("toggle");
  const REFRESH = document.getElementById("refresh");
  let THEME = window.localStorage.getItem("theme");

  if (!THEME) {
    THEME = "light"; // Defina um tema padrão caso não exista no localStorage
    window.localStorage.setItem("theme", THEME);
  }

  if (THEME === "dark") document.body.classList.add("dark");

  TOGGLE.addEventListener("click", () => {
    document.body.classList.toggle("dark");
    if (THEME === "dark") {
      THEME = "light";
      window.localStorage.setItem("theme", "light");
    } else {
      THEME = "dark";
      window.localStorage.setItem("theme", "dark");
    }
  });

  REFRESH.addEventListener("click", () => {
      window.location.reload();
  });
  let count = 1;
  document.getElementById("radio1").checked = true;
});
