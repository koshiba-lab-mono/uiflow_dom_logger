import { elements } from "chart.js";
import { ContentType } from "./stores/contentStore";
import { wrapDivSvg } from "./utils/utils";
import { clone } from "chart.js/dist/helpers/helpers.core";

const queryName =
  ".blocklyDraggable:not(.blocklydisabled):not(.blocklyInsertionMarker)>.blocklyPath";
const blocklyCanvas = document.querySelector(".blocklyBlockCanvas")!;
let blocks: Element[] = [];

const observer = new MutationObserver(async (mutations) => {
  const tmpBlocks = blocklyCanvas.querySelectorAll(queryName);

  // 組み立て中のブロックに差分が無かったらなにもしない
  if (blocks.length === tmpBlocks.length) {
    return;
  }

  blocks = Array.from(tmpBlocks);
  const sendHtml = Array.from(blocklyCanvas.children)
    .map((blockChunk) => {
      const div = wrapDivSvg(blockChunk);
      return div.outerHTML;
    })
    .join("");

  const content: ContentType = {
    date: Date.now(),
    html: sendHtml,
  };

  chrome.runtime.sendMessage(content, (res) => {});
});

observer.observe(blocklyCanvas, { childList: true });
