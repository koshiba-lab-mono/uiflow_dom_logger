import { indexedDBStore } from "./stores/indexedDBStore";
import { ContentType } from "./stores/contentStore";

/**content側からデータを受け取った時，indexedDBに保存するリスナ */
chrome.runtime.onMessage.addListener(async (content: ContentType) => {
  const addedContent = await indexedDBStore.add(content).catch((err) => {
    throw err;
  });
  console.log(`Add: ${addedContent}`);
});
