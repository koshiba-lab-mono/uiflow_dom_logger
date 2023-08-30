import { ContentType } from "../stores/contentStore";

export const wrapDivSvg = (element: Element) => {
  const wrapDiv = document.createElement("div");
  const wrapSvg = document.createElementNS("http://www.w3.org/2000/svg", "svg");
  const rect = element.getBoundingClientRect();
  const { width, height } = rect;
  wrapSvg.setAttribute("width", String(width));
  wrapSvg.setAttribute("height", String(height));
  const cloneElement = element.cloneNode(true) as Element;
  cloneElement.removeAttribute("transform");
  wrapSvg.appendChild(cloneElement);
  wrapDiv.appendChild(wrapSvg);
  return wrapDiv;
};

export const getBlockNum = (content: ContentType) => {
  const tmp = document.createElement("div");
  tmp.innerHTML = content.html;
  const paths = tmp.querySelectorAll(".blocklyPath");
  return paths.length;
};
