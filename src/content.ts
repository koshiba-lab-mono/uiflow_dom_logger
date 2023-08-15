const queryName =
  ".blocklyDraggable:not(.blocklydisabled):not(.blocklyInsertionMarker)>.blocklyPath";
const blocklyCanvas = document.querySelector(".blocklyBlockCanvas")!;
let blocks: Element[] = [];

const observer = new MutationObserver((mutations) => {
  const tmpBlocks = blocklyCanvas.querySelectorAll(queryName);

  // 組み立て中のブロックに差分が無かったらなにもしない
  if (blocks.length === tmpBlocks.length) {
    return;
  }

  blocks = Array.from(tmpBlocks);

  const data = {
    date: Date.now(),
    html: blocklyCanvas.outerHTML,
  };

  chrome.runtime.sendMessage(data, (res) => {
    console.log(res);
  });
});

observer.observe(blocklyCanvas, { childList: true });
