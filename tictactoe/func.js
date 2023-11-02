var leftup = document.querySelector("#lg");
var centerup = document.querySelector("#sg");
var rightup = document.querySelector("#pg");
var leftmid = document.querySelector("#ls");
var centermid = document.querySelector("#ss");
var rightmid = document.querySelector("#ps");
var leftdown = document.querySelector("#ld");
var centerdown = document.querySelector("#sd");
var rightdown = document.querySelector("#pd");
var restart = document.querySelector(".button");

leftup.addEventListener("click", function () {
  leftup.textContent = "X";
});
leftup.addEventListener("contextmenu", function () {
  leftup.textContent = "O";
});

centerup.addEventListener("click", function () {
  centerup.textContent = "X";
});
centerup.addEventListener("contextmenu", function () {
  centerup.textContent = "O";
});

rightup.addEventListener("click", function () {
  rightup.textContent = "X";
});
rightup.addEventListener("contextmenu", function () {
  rightup.textContent = "O";
});

leftmid.addEventListener("click", function () {
  leftmid.textContent = "X";
});
leftmid.addEventListener("contextmenu", function () {
  leftmid.textContent = "O";
});

centermid.addEventListener("click", function () {
  centermid.textContent = "X";
});
centermid.addEventListener("contextmenu", function () {
  centermid.textContent = "O";
});

rightmid.addEventListener("click", function () {
  rightmid.textContent = "X";
});
rightmid.addEventListener("contextmenu", function () {
  rightmid.textContent = "O";
});

centerdown.addEventListener("click", function () {
  centerdown.textContent = "X";
});
centerdown.addEventListener("contextmenu", function () {
  centerdown.textContent = "O";
});

leftdown.addEventListener("click", function () {
  leftdown.textContent = "X";
});
leftdown.addEventListener("contextmenu", function () {
  leftdown.textContent = "O";
});

rightdown.addEventListener("click", function () {
  rightdown.textContent = "X";
});
rightdown.addEventListener("contextmenu", function () {
  rightdown.textContent = "O";
});
