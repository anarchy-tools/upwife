// ==UserScript==
// @name         upwife
// @namespace    http://tampermonkey.net/
// @version      0.1
// @description  acquire wife at low expense
// @author       anarchy-tools
// @match        https://tinder.com/app/recs
// @icon         https://www.google.com/s2/favicons?sz=64&domain=tinder.com
// @grant        none
// ==/UserScript==

(async function () {
  "use strict";
  const timeout = async (n) =>
    await new Promise((resolve) => setTimeout(resolve, n));
  const clickFrontBySelector = (selector) => {
    const els = document.querySelectorAll(selector);
    if (els[0]) {
      els[0].click();
      return true;
    } else return false;
  };
  const clickBackByClassName = (className) => {
    const els = document.getElementsByClassName(className);
    if (els.length) {
      els[els.length - 1].click();
      return true;
    } else return false;
  };
  const clickFrontByClassName = (className) => {
    const els = document.getElementsByClassName(className);
    if (els.length) {
      els[0].click();
      return true;
    } else return false;
  };
  const convincinglyRandomIntervalMs = () => Math.floor(Math.random() * 5000) + 2500;
  while (true) {
    try {
      if (!clickFrontBySelector("button[title='Back to Tinder']")) {
        clickBackByClassName("Bgc($c-like-green):a");
        clickFrontByClassName("c1p6lbu0");
      }
    } catch (e) {
      console.error(e);
    }
    await timeout(convincinglyRandomIntervalMs());
  } // Your code here...
})().catch((err) => console.error(err));
