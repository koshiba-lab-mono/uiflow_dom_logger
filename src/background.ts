import { ContentType } from "./stores/contentStore";
import { indexedDBStore } from "./stores/indexedDBStore";

chrome.runtime.onMessage.addListener(async (content: ContentType) => {
  const addedContent = await indexedDBStore.add(content);
  console.log(addedContent);
});
